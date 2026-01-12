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
import fcntl
import enum
import mmap

from v4l2codecs import log
from v4l2codecs import ioctl
from v4l2codecs import clib


devices = ["/dev/dma_heap/system-uncached",
           "/dev/dma_heap/system-uncached-dma32",
           "/dev/dma_heap/system",
           "/dev/dma_heap/system-dma32",
           "/dev/dma_heap/cma-uncached",
           "/dev/dma_heap/cma-uncached-dma32",
           "/dev/dma_heap/cma",
           ]


class dma_heap_allocation_data(clib.Structure):
    _fields_ = [
        ('len', clib.c_uint64),
        ('fd', clib.c_uint32),
        ('fd_flags', clib.c_uint32),
        ('heap_flags', clib.c_uint64),
    ]


class IOC(enum.IntEnum):
    ALLOC = ioctl.IOWR("H", 0, dma_heap_allocation_data)


class Allocator():
    def __init__(self, *paths):
        self.dma_fds = {}
        self.paths = paths
        self.fd = None
        self.path = None
        self.open()

    def open(self):
        for path in self.paths or devices:
            if not os.path.exists(path):
                continue
            self.fd = os.open(path, os.O_RDWR | os.O_CLOEXEC)
            self.path = path
            log.LOGGER.debug(f"Opened DMA device {self.path}")
            break

    def alloc(self, size):
        data = dma_heap_allocation_data(len=clib.c_uint64(size),
                                        fd_flags=clib.c_uint32(os.O_RDWR | os.O_CLOEXEC))
        fcntl.ioctl(self.fd, IOC.ALLOC, data)
        self.dma_fds[data.fd.value] = data, None
        log.LOGGER.debug(f"Allocated {data.len} bytes with fd {data.fd} on {self.path}")
        return data.fd.value

    def unalloc(self, fd):
        if fd in self.dma_fds:
            self.unmap(fd)
            data, _mapped = self.dma_fds.pop(fd)
            os.close(data.fd.value)
            log.LOGGER.debug(f"Unallocated {data.len.value} bytes with fd {data.fd.value} on {self.path}")

    def map(self, fd):
        if fd not in self.dma_fds:
            raise OSError(f"No dma fd {fd}")
        data, mapped = self.dma_fds[fd]
        if not mapped:
            mapped = self.mmap = mmap.mmap(data.fd.value,
                                           data.len.value,
                                           mmap.MAP_SHARED,
                                           mmap.PROT_READ | mmap.PROT_WRITE,
                                           0)
            self.dma_fds[data.fd.value] = data, mapped
            log.LOGGER.debug(f"Mapped {data.len.value} bytes with fd {data.fd.value} on {self.path} to address 0x{mapped.ref:x}")
        return mapped

    def unmap(self, fd):
        if fd not in self.dma_fds:
            raise OSError(f"No dma fd {fd}")
        data, mapped = self.dma_fds[fd]
        if mapped:
            mapped.close()
            self.dma_fds[data.fd.value] = data, None
            log.LOGGER.debug(f"Unmapped {data.len.value} bytes with fd {data.fd.value} on {self.path} from address 0x{mapped.ref:x}")

    def close(self):
        for fd in list(self.dma_fds):
            self.unalloc(fd)
        if self.fd is not None:
            os.close(self.fd)
        self.fd = None
