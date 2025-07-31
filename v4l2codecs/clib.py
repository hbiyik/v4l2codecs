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
from ctypes import util

from v4l2codecs import log


def isnullptr(ptr):
    return ctypes.cast(ptr, ctypes.c_void_p).value is None


class CIntEnum(ctypes.c_int):
    _enum_ = None

    @property
    def enum(self):
        try:
            return self._enum_(self.value)
        except ValueError:
            return

    def __str__(self):
        e = self.enum
        return str(self.value) if e is None else e.name

    def __repr__(self):
        return f"{str(self)}({self.value})"


class CLib:
    _functions_ = []
    _name_ = None

    def __init__(self, name=None):
        name = name or self._name_
        self._name = util.find_library(name)
        if not self._name:
            raise RuntimeError(f"{name} library can not be found")
        log.LOGGER.debug(f"loading library {self._name}")
        self._lib = ctypes.CDLL(self._name)
        for declaration in self._functions_:
            self._wrap_function(*declaration)

    def _wrap_function(self, name, args, rettype=None):
        if getattr(self, name, None):
            raise RuntimeError(f"function {name} has already been prototyped")
        ptr = getattr(self._lib, name, None)
        if not ptr:
            raise RuntimeError(f"function {name} is not exported from {self._name}")
        setattr(ptr, "argtypes", args)
        setattr(ptr, "restype", rettype)
        setattr(self, name, ptr)
        log.LOGGER.debug(f"function {name} is wrapped from {self._name}")
