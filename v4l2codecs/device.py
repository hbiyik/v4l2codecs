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
import ctypes

from linuxpy.video import raw as v4l2

from v4l2codecs import cuse
from v4l2codecs import log
from v4l2codecs import defs


class Device(cuse.Cuse):
    ioctls = {v4l2.IOC.QUERYCAP: v4l2.v4l2_capability,
              v4l2.IOC.ENUM_FMT: v4l2.v4l2_fmtdesc}

    def __init__(self):
        self.name = "mpp"
        self.decoder = True
        self.encoder = False
        self.devname = "video0-ffmpeg-dec"
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

    def ioctl_read(self, handler, cmd, data):
        if cmd == v4l2.IOC.QUERYCAP:
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
        if cmd == v4l2.IOC.ENUM_FMT:
            return 0
