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
# import ctypes
import threading
import errno
import traceback

from v4l2codecs import log
from v4l2codecs import clib

CUSE_UNRESTRICTED_IOCTL = 1 << 0
c_off_t = clib.c_longlong


class StructFileInfo(clib.Structure):
    _fields_ = [
        ('flags', clib.c_int),
        ('fh_old', clib.c_ulong),
        ('writepage', clib.c_int),
        ('padding', clib.c_uint),
        ('fh', clib.c_uint64),
        ('lock_owner', clib.c_uint64)]


class StructIoVec(clib.Structure):
    _fields_ = [("base", clib.c_void_p),
                ("size", clib.c_size_t)]


class StructDevInfo(clib.Structure):
    _fields_ = [("major", clib.c_uint),
                ("minor", clib.c_uint),
                ("argc", clib.c_uint),
                ("argv", clib.POINTER(clib.c_char_p)),
                ("flags", clib.c_uint)]


class StructLowlevelOps(clib.Structure):
    class _callbacks_(clib.Lib):
        @clib.Lib.Signature(None, clib.c_void_p, clib.c_void_p)
        def init(self, userdata, conn):
            return

        @clib.Lib.Signature(None, clib.c_void_p)
        def init_done(self, userdata):
            return

        @clib.Lib.Signature(None, clib.c_void_p)
        def destroy(self, userdata):
            return

        @clib.Lib.Signature(None, clib.c_void_p, clib.POINTER(StructFileInfo))
        def open(self, req, fi):
            return

        @clib.Lib.Signature(None,
                            clib.c_void_p,
                            clib.c_size_t,
                            c_off_t,
                            clib.POINTER(StructFileInfo))
        def read(self, req, size, off, fi):
            return

        @clib.Lib.Signature(None,
                            clib.c_void_p,
                            clib.POINTER(clib.c_byte),
                            clib.c_size_t,
                            c_off_t,
                            clib.POINTER(StructFileInfo))
        def write(self, req, buf, size, off, fi):
            return

        @clib.Lib.Signature(None, clib.c_void_p, clib.POINTER(StructFileInfo))
        def flush(self, req, fi):
            return

        @clib.Lib.Signature(None, clib.c_void_p, clib.POINTER(StructFileInfo))
        def release(self, req, fi):
            return

        @clib.Lib.Signature(None, clib.c_void_p, clib.c_int, clib.POINTER(StructFileInfo))
        def fsync(self, req, datasync, fi):
            return

        @clib.Lib.Signature(None,
                            clib.c_void_p,
                            clib.c_int,
                            clib.c_void_p,
                            clib.POINTER(StructFileInfo),
                            clib.c_uint,
                            clib.c_void_p,
                            clib.c_size_t,
                            clib.c_size_t)
        def ioctl(self, req, cmd, arg, fi, flags, in_buf, in_buf_sz, out_buf_sz):
            return

        @clib.Lib.Signature(None, clib.c_void_p, clib.POINTER(StructFileInfo), clib.c_void_p)
        def poll(self, req, fi, ph):
            return

    _fields_ = [
        ('init', _callbacks_.functype(_callbacks_.init)),
        ('init_done', _callbacks_.functype(_callbacks_.init_done)),
        ('destroy', _callbacks_.functype(_callbacks_.destroy)),
        ('open', _callbacks_.functype(_callbacks_.open)),
        ('read', _callbacks_.functype(_callbacks_.read)),
        ('write', _callbacks_.functype(_callbacks_.write)),
        ('flush', _callbacks_.functype(_callbacks_.flush)),
        ('release', _callbacks_.functype(_callbacks_.release)),
        ('fsync', _callbacks_.functype(_callbacks_.fsync)),
        ('ioctl', _callbacks_.functype(_callbacks_.ioctl)),
        ('poll', _callbacks_.functype(_callbacks_.poll))]


class Lib(clib.Lib):
    _name_ = "fuse"

    @clib.Lib.Signature("cuse_lowlevel_main",
                        clib.c_uint,
                        clib.POINTER(clib.c_char_p),
                        clib.POINTER(StructDevInfo),
                        clib.POINTER(StructLowlevelOps),
                        clib.c_void_p)
    def cuse_main(self, argc, argv, ci, clop, userdata):
        return clib.c_int

    @clib.Lib.Signature("cuse_lowlevel_teardown", clib.c_void_p)
    def cuse_teardown(self, se):
        return

    @clib.Lib.Signature("fuse_reply_open", clib.c_void_p, clib.c_void_p)
    def reply_open(self, req, fi):
        return

    @clib.Lib.Signature("fuse_reply_err", clib.c_void_p, clib.c_int)
    def reply_err(self, req, err):
        return

    @clib.Lib.Signature("fuse_reply_none", clib.c_void_p)
    def reply_none(self, req):
        return

    @clib.Lib.Signature("fuse_reply_ioctl",
                        clib.c_void_p,
                        clib.c_int,
                        clib.c_void_p,
                        clib.c_size_t)
    def reply_ioctl(self, req, result, buf, size):
        return

    @clib.Lib.Signature("fuse_reply_ioctl_retry",
                        clib.c_void_p,
                        clib.c_void_p,
                        clib.c_size_t,
                        clib.c_void_p,
                        clib.c_size_t)
    def reply_ioctl_retry(self, req, iniov, incount, outiov, outcount):
        return clib.c_int


class CuseThread(threading.Thread):
    ioctls = {}

    def __init__(self, op, name, major=None, minor=None, ioctls=None, debug=True):
        self.ioctls = ioctls or self.ioctls
        self.op = op
        self.handlers = []
        self._lasthandler = 0
        self.returncode = None
        self.c_lib = Lib()

        # devinfo
        devinfo = [f"DEVNAME={name}".encode()]
        c_devinfo = StructDevInfo(argc=clib.c_uint(len(devinfo)),
                                  argv=(clib.c_char_p * len(devinfo))(*devinfo),
                                  flags=clib.c_uint(CUSE_UNRESTRICTED_IOCTL))
        if major is not None:
            c_devinfo.major = clib.c_int(major)
        if minor is not None:
            c_devinfo.minor = clib.c_int(minor)

        # args
        args = [b"\n", b"-f"]
        if debug:
            args.append(b"-d")
        c_ops = StructLowlevelOps()
        for name, functype in StructLowlevelOps._fields_:
            method = getattr(self, name, None)
            if method:
                setattr(c_ops, name, functype(method))

        threading.Thread.__init__(self, args=(clib.c_uint(len(args)),
                                              (clib.c_char_p * len(args))(*args),
                                               c_devinfo.ref,
                                               c_ops.ref,
                                               None), daemon=True)
        self.start()
        self.join()
        if not self.returncode:
            raise RuntimeError(f"Cuse main returned {self.returncode}")

    def run(self):
        self.returncode = self.c_lib.cuse_main(*self._args)

    def handler(self):
        if self._lasthandler in self.handlers:
            log.LOGGER.error(f"file handler collison {self._lasthandler}")
            return
        handler = self._lasthandler
        self._lasthandler = (self._lasthandler + 1) % 0xFFFFFFFFFFFFFFFF
        return handler

    def open(self, c_req_p, c_fi):
        handler = self.handler()
        c_fi.contents.fh = clib.c_uint64(handler)
        self.safe_callback(self.op.open, handler)
        self.handlers.append(handler)
        self.c_lib.reply_open(c_req_p, c_fi)

    def safe_callback(self, cb, *args, **kwargs):
        try:
            return cb(*args, **kwargs)
        except Exception:
            log.LOGGER.error(traceback.format_exc())
            return errno.EIO

    def ioctl(self, c_req_p, c_cmd, c_arg_p, c_fi, flags, c_in_buf_p, c_in_buf_sz, c_out_buf_sz):
        write = bool((c_cmd.value >> 30) & 1)
        read = bool((c_cmd.value >> 31) & 1)
        if c_cmd.value not in self.ioctls:
            self.c_lib.reply_err(c_req_p, clib.c_int(errno.EINVAL))
            log.LOGGER.warning(f"unhandled ioctl: {c_cmd}")
            return
        datatype = self.ioctls[c_cmd.value]
        in_iov = clib.c_void_p()
        out_iov = clib.c_void_p()
        if write and not c_in_buf_sz.value:
            in_iov = StructIoVec(c_arg_p, clib.c_size_t(clib.sizeof(datatype))).ref
        if read and not c_out_buf_sz.value:
            out_iov = StructIoVec(c_arg_p, clib.c_size_t(clib.sizeof(datatype))).ref
        if in_iov or out_iov:
            self.c_lib.reply_ioctl_retry(c_req_p,
                                         in_iov, clib.c_size_t(int(bool(in_iov))),
                                         out_iov, clib.c_size_t(int(bool(out_iov))),)
            return

        if read or write:
            data = datatype()
            if c_in_buf_p:
                clib.memmove(data.ref, c_in_buf_p, clib.sizeof(datatype))
            ret = clib.c_int(self.safe_callback(self.op.ioctl, c_fi.contents.fh, c_cmd, data))
            if ret.value:
                self.c_lib.reply_err(c_req_p, ret)
            else:
                self.c_lib.reply_ioctl(c_req_p, ret, data.ref, clib.c_size_t(clib.sizeof(data)))
            return
        log.LOGGER.warning(f"wrong ioctl response: {c_cmd}")
        self.c_lib.reply_err(c_req_p, clib.c_int(errno.EINVAL))

    def release(self, c_req_p, c_fi):
        handler = c_fi.contents.fh.value
        if handler not in self.handlers:
            self.c_lib.reply_err(c_req_p, clib.c_int(errno.EBADF))
            return
        self.handlers.remove(handler)
        self.c_lib.reply_err(c_req_p, clib.c_int(0))
