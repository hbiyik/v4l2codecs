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

from v4l2codecs import cuse
from v4l2codecs import log
from v4l2codecs import defs
from v4l2codecs import v4l2


class Device(cuse.Cuse):
    ioctls = {v4l2.IOC.QUERYCAP: v4l2.v4l2_capability,
              v4l2.IOC.ENUM_FMT: v4l2.v4l2_fmtdesc,
              v4l2.IOC.TRY_FMT: v4l2.v4l2_format,
              v4l2.IOC.S_FMT: v4l2.v4l2_format,
              v4l2.IOC.G_FMT: v4l2.v4l2_format,
              v4l2.IOC.REQBUFS: v4l2.v4l2_requestbuffers}

    def __init__(self):
        self.name = "mpp"
        self.decoder = True
        self.encoder = False
        self.devname = "video0-ffmpeg-dec"
        v4l2.v4l2_fmtdesc()
        self.all_formats = [(v4l2.BufType.VIDEO_CAPTURE, v4l2.PixelFormat.NV12, 0),
                            (v4l2.BufType.VIDEO_OUTPUT, v4l2.PixelFormat.H264, v4l2.ImageFormatFlag.COMPRESSED)]
        self.act_formats = []
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
        # dynamic addingment range
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
        data.driver = f"ffmpeg-{self.name}".encode()
        data.card = f"/dev/{self.devname}".encode()
        data.bus_info = f"platform:{self.devname}".encode()
        data.version = defs.VERSION_INT
        data.capabilities = v4l2.Capability.VIDEO_CAPTURE | \
                            v4l2.Capability.VIDEO_M2M | \
                            v4l2.Capability.EXT_PIX_FORMAT | \
                            v4l2.Capability.DEVICE_CAPS | \
                            v4l2.Capability.RDS_CAPTURE | \
                            v4l2.Capability.STREAMING
        data.device_caps = v4l2.Capability.VIDEO_CAPTURE | \
                           v4l2.Capability.VIDEO_M2M | \
                           v4l2.Capability.RDS_CAPTURE | \
                           v4l2.Capability.STREAMING
        return 0

    def ioctl_enum_fmt(self, data):
        if not data.index < len(self.all_formats):
            return errno.EINVAL
        data.type, data.pixelformat, data.flags = self.all_formats[data.index]
        return 0

    def ioctl_g_fmt(self, data):
        fmt = self.getformat(self.act_formats, typ=data.type)
        if fmt:
            _typ, fmt, flags = fmt
            data.fmt.pix.pixelformat = fmt
            data.fmt.pix.flags = flags
            return 0
        return errno.EINVAL

    def ioctl_s_fmt(self, data):
        fmt = self.getformat(self.all_formats, typ=data.type, fmt=data.fmt.pix.pixelformat.value)
        if fmt:
            self.act_formats.append(fmt)
            return 0
        return errno.EINVAL

    def ioctl_try_fmt(self, data):
        fmt = self.getformat(self.all_formats, typ=data.type, fmt=data.fmt.pix.pixelformat.value)
        if fmt:
            return 0
        return errno.EINVAL

    def ioctl_reqbufs(self, data):
        pass

    def ioctl_read(self, handler, cmd, data):
        try:
            ioctl_cmd = v4l2.IOC(cmd)
        except ValueError:
            log.LOGGER.warning(f"unknown ioctl {cmd}")
            return errno.EINVAL
        callback = getattr(self, f"ioctl_{ioctl_cmd.name.lower()}", None)
        if not callback:
            log.LOGGER.warning(f"unhandled ioctl {ioctl_cmd.name}")
            return errno.EINVAL
        return callback(data)
