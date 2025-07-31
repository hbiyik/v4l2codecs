"""
 Copyright (C) 2025 boogie

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import ctypes
import threading
import errno
import traceback

from refuse import low

from v4l2codecs import log
from v4l2codecs import clib

CUSE_UNRESTRICTED_IOCTL = 1 << 0


class IoVec(ctypes.Structure):
    _fields_ = [("base", ctypes.c_void_p),
                ("size", ctypes.c_size_t)]


class DevInfo(ctypes.Structure):
    _fields_ = [("major", ctypes.c_uint),
                ("minor", ctypes.c_uint),
                ("argc", ctypes.c_uint),
                ("argv", ctypes.POINTER(ctypes.c_char_p)),
                ("flags", ctypes.c_uint)]


class LowlevelOps(ctypes.Structure):
    _fields_ = [
        ('init', ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)),

        ('init_done', ctypes.CFUNCTYPE(None, ctypes.c_void_p)),

        ('destroy', ctypes.CFUNCTYPE(None, ctypes.c_void_p)),

        ('open', ctypes.CFUNCTYPE(None, low.fuse_req_t, low.fuse_file_info_p)),

        ('read', ctypes.CFUNCTYPE(
            None, low.fuse_req_t, ctypes.c_size_t, low.c_off_t,
            low.fuse_file_info_p)),

        ('write', ctypes.CFUNCTYPE(
            None, low.fuse_req_t, low.c_bytes_p, ctypes.c_size_t,
            low.c_off_t, low.fuse_file_info_p)),

        ('flush', ctypes.CFUNCTYPE(
            None, low.fuse_req_t, low.fuse_file_info_p)),

        ('release', ctypes.CFUNCTYPE(
            None, low.fuse_req_t, low.fuse_file_info_p)),

        ('fsync', ctypes.CFUNCTYPE(
            None, low.fuse_req_t, ctypes.c_int, low.fuse_file_info_p)),

        ('ioctl', ctypes.CFUNCTYPE(
            None, low.fuse_req_t, ctypes.c_int, ctypes.c_void_p, low.fuse_file_info_p,
            ctypes.c_uint, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t)),

        ('poll', ctypes.CFUNCTYPE(
            None, low.fuse_req_t, low.fuse_file_info_p, ctypes.c_void_p)),
    ]


class CCuse(threading.Thread):
    ioctls = {}

    class Lib(clib.CLib):
        _name_ = "fuse"
        _functions_ = (("cuse_lowlevel_main", (ctypes.c_uint,
                                               ctypes.POINTER(ctypes.c_char_p),
                                               ctypes.POINTER(DevInfo),
                                               ctypes.POINTER(LowlevelOps),
                                               ctypes.c_void_p), ctypes.c_int),
                       ("cuse_lowlevel_teardown", (ctypes.c_void_p,)),
                       ("fuse_reply_open", (low.fuse_req_t, ctypes.c_void_p)),
                       ("fuse_reply_err", (low.fuse_req_t, ctypes.c_int)),
                       ("fuse_reply_none", (low.fuse_req_t,)),
                       ("fuse_reply_ioctl", (low.fuse_req_t,
                                             ctypes.c_int,
                                             ctypes.c_void_p,
                                             ctypes.c_size_t), ctypes.c_int),
                       ("fuse_reply_ioctl_retry",(low.fuse_req_t,
                                                  ctypes.c_void_p,
                                                  ctypes.c_size_t,
                                                  ctypes.c_void_p,
                                                  ctypes.c_size_t), ctypes.c_int),
                       )

    def __init__(self, op, name, major=None, minor=None, ioctls=None, debug=True):
        self.ioctls = ioctls or self.ioctls
        self.op = op
        self.handlers = []
        self._lasthandler = 0
        self.returncode = None
        self.c_lib = self.Lib()

        # devinfo
        devinfo = [f"DEVNAME={name}".encode()]
        c_devinfo = DevInfo(argc=len(devinfo),
                            argv=(ctypes.c_char_p * len(devinfo))(*devinfo),
                            flags=CUSE_UNRESTRICTED_IOCTL)
        if major is not None:
            c_devinfo.major = major
        if minor is not None:
            c_devinfo.minor = minor

        # args
        args = [b"\n", b"-f"]
        if debug:
            args.append(b"-d")
        c_ops = LowlevelOps()
        for name, prototype in LowlevelOps._fields_:
            method = getattr(self, name, None)
            if method:
                setattr(c_ops, name, prototype(method))

        threading.Thread.__init__(self, args=(len(args),
                                              (ctypes.c_char_p * len(args))(*args),
                                              ctypes.byref(c_devinfo),
                                              ctypes.byref(c_ops),
                                              None), daemon=True)
        self.start()
        self.join()
        if not self.returncode:
            raise RuntimeError(f"Cuse main returned {self.returncode}")

    def run(self):
        self.returncode = self.c_lib.cuse_lowlevel_main(*self._args)

    def handler(self):
        if self._lasthandler in self.handlers:
            log.LOGGER.error(f"file handler collison {self._lasthandler}")
            return
        handler = self._lasthandler
        self._lasthandler = (self._lasthandler + 1) % 0xFFFFFFFFFFFFFFFF
        return handler

    def open(self, c_req_p, c_fi):
        handler = self.handler()
        c_fi.contents.fh = handler
        self.safe_callback(self.op.open, handler)
        self.handlers.append(handler)
        self.c_lib.fuse_reply_open(c_req_p, c_fi)

    def safe_callback(self, cb, *args, **kwargs):
        try:
            return cb(*args, **kwargs)
        except Exception:
            log.LOGGER.error(traceback.format_exc())
            return errno.EIO

    def ioctl(self, c_req_p, c_cmd, c_arg_p, c_fi, flags, c_in_buf_p, c_in_buf_sz, c_out_buf_sz):
        write = bool((c_cmd >> 30) & 1)
        read = bool((c_cmd >> 31) & 1)
        if c_cmd not in self.ioctls:
            self.c_lib.fuse_reply_err(c_req_p, errno.EINVAL)
            log.LOGGER.warning(f"unhandled ioctl: {c_cmd}")
            return
        datatype = self.ioctls[c_cmd]
        in_iov = ctypes.c_void_p()
        out_iov = ctypes.c_void_p()
        if write and not c_in_buf_sz:
            in_iov = ctypes.byref(IoVec(c_arg_p, ctypes.sizeof(datatype)))
        if read and not c_out_buf_sz:
            out_iov = ctypes.byref(IoVec(c_arg_p, ctypes.sizeof(datatype)))
        if in_iov or out_iov:
            self.c_lib.fuse_reply_ioctl_retry(c_req_p,
                                              in_iov, int(bool(in_iov)),
                                              out_iov, int(bool(out_iov)),)
            return

        if read or write:
            data = datatype()
            if c_in_buf_p:
                ctypes.memmove(ctypes.byref(data), c_in_buf_p, ctypes.sizeof(datatype))
            ret = self.safe_callback(self.op.ioctl_read, c_fi.contents.fh, c_cmd, data)
            if ret:
                self.c_lib.fuse_reply_err(c_req_p, ret)
            else:
                self.c_lib.fuse_reply_ioctl(c_req_p, ret, ctypes.byref(data), ctypes.sizeof(data))
            return
        log.LOGGER.warning(f"wrong ioctl response: {c_cmd}")
        self.c_lib.fuse_reply_err(c_req_p, errno.EINVAL)

    def release(self, c_req_p, c_fi):
        handler = c_fi.contents.fh
        if handler not in self.handlers:
            self.c_lib.fuse_reply_err(c_req_p, errno.EBADF)
            return
        self.handlers.remove(handler)
        self.c_lib.fuse_reply_err(c_req_p, 0)
