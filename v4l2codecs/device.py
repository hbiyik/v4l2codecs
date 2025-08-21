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
import os
import errno

from v4l2codecs.fuse import Cuse
from v4l2codecs import log
from v4l2codecs import defs
from v4l2codecs import v4l2
from v4l2codecs import clib


class Device(Cuse):
    ioctls = {v4l2.IOC.QUERYCAP: v4l2.StructCapability,
              v4l2.IOC.ENUM_FMT: v4l2.StructFmtDesc,
              v4l2.IOC.TRY_FMT: v4l2.StructFormat,
              v4l2.IOC.S_FMT: v4l2.StructFormat,
              v4l2.IOC.G_FMT: v4l2.StructFormat,
              v4l2.IOC.REQBUFS: v4l2.StructRequestBuffers,
              v4l2.IOC.QUERYBUF: v4l2.StructBuffer}

    formats = [(v4l2.EnumBufferType.VIDEO_CAPTURE,
                v4l2.EnumPixelFormat(v4l2.EnumPixelFormat._enum_.NV12),
                v4l2.FlagFormat(0)),
               (v4l2.EnumBufferType.VIDEO_OUTPUT,
                v4l2.EnumPixelFormat(v4l2.EnumPixelFormat._enum_.H264),
                v4l2.FlagFormat(v4l2.FlagFormat._enum_.COMPRESSED))]

    def __init__(self):
        self.name = "mpp"
        self.decoder = True
        self.encoder = False
        self.devname = "video0-ffmpeg-dec"
        self.formats_selected = []
        super().__init__(self.devname)

    def find_v4l2_index(self):
        indexes = []
        for fname in os.listdir("/dev"):
            if fname.startswith("video"):
                index = fname.replace("video", "").strip()
                if index.isdigit():
                    indexes.append(int(index))
        for i in range(64):
            if i not in indexes:
                return i

    def find_v4l2_device(self):
        chardevs = {}
        for fname in os.listdir("/sys/dev/char"):
            major, minor = [x.strip() for x in fname.split(":")]
            if not major.isdigit() or not minor.isdigit():
                continue
            major = int(major)
            minor = int(minor)
            if major not in chardevs:
                chardevs[major] = []
            if minor not in chardevs[major]:
                chardevs[major].append(minor)
        # dynamic assingment range
        for major in range(384, 512):
            for minor in range(256):
                if major not in chardevs or minor not in chardevs[major]:
                    return major, minor

    def getformat(self, formats, typ=None, fmt=None, flags=None):
        for f_type, f_format, f_flags in formats:
            if (typ is None or f_type == typ) and \
                    (fmt is None or f_format == fmt) and \
                    (flags is None or f_flags == flags):
                return f_type, f_format, f_flags

    def ioctl_querycap(self, data):
        clib.arrset(data.driver, f"ffmpeg-{self.name}".encode())
        clib.arrset(data.card, f"/dev/{self.devname}".encode())
        clib.arrset(data.bus_info, f"platform:{self.devname}".encode())
        data.version.value = defs.VERSION_INT
        data.capabilities.value = v4l2.FlagCapability.VIDEO_CAPTURE | \
                                  v4l2.FlagCapability.VIDEO_M2M | \
                                  v4l2.FlagCapability.EXT_PIX_FORMAT | \
                                  v4l2.FlagCapability.DEVICE_CAPS | \
                                  v4l2.FlagCapability.RDS_CAPTURE | \
                                  v4l2.FlagCapability.STREAMING
        data.device_caps.value = v4l2.FlagCapability.VIDEO_CAPTURE | \
                                 v4l2.FlagCapability.VIDEO_M2M | \
                                 v4l2.FlagCapability.RDS_CAPTURE | \
                                 v4l2.FlagCapability.STREAMING
        return 0

    def ioctl_enum_fmt(self, fmtdesc):
        if not fmtdesc.index.value < len(self.formats):
            return errno.EINVAL
        fmtdesc.type.value, fmtdesc.pixelformat, fmtdesc.flags = self.formats[fmtdesc.index.value]
        return 0

    def ioctl_g_fmt(self, data):
        fmt = self.getformat(self.formats_selected, typ=data.type)
        if fmt:
            _typ, fmt, flags = fmt
            data.fmt.pix.pixelformat = fmt
            data.fmt.pix.flags = flags
            return 0
        return errno.EINVAL

    def ioctl_s_fmt(self, data):
        fmt = self.getformat(self.formats, typ=data.type, fmt=data.fmt.pix.pixelformat.value)
        if fmt:
            # TODO: set formats by type rather than appending
            # TODO: check dims
            self.formats_selected.append(fmt)
            return 0
        return errno.EINVAL

    def ioctl_try_fmt(self, data):
        fmt = self.getformat(self.formats, typ=data.type, fmt=data.fmt.pix.pixelformat.value)
        if fmt:
            return 0
        return errno.EINVAL

    def ioctl_reqbufs(self, data):
        return 0

    def ioctl_querybuf(self, data):
        return 0

    def ioctl(self, handler, cmd, data):
        try:
            ioctl_cmd = v4l2.IOC(cmd.value)
        except ValueError:
            log.LOGGER.warning(f"unknown ioctl {cmd}")
            return errno.EINVAL
        callback = getattr(self, f"ioctl_{ioctl_cmd.name.lower()}", None)
        if not callback:
            log.LOGGER.warning(f"unhandled ioctl {ioctl_cmd.name}")
            return errno.EINVAL
        ret = callback(data)
        log.LOGGER.debug(f"Handled ioctl {ioctl_cmd.name}")
        return ret
