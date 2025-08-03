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


# wrapper union class so that ctypes will be kept as ctypes when used in Struct
# otherwise they are converted to pythonic types (ie: struct.c_int -> sctruct.int)
class UnionWrapper(ctypes.Union):
    _base_type_ = None

    @staticmethod
    def type(ctype):
        def wrapper(cls):
            cls._base_type_ = ctype
            cls._fields_ = [("value", ctype)]
            return cls
        return wrapper

    @property
    def ref(self):
        return ctypes.cast(ctypes.byref(self), ctypes.POINTER(self._base_type_))


@UnionWrapper.type(ctypes.c_int)
class c_int(UnionWrapper):
    pass


@UnionWrapper.type(ctypes.c_uint)
class c_uint(UnionWrapper):
    pass


def ptr_address(ptr):
    return ctypes.cast(ptr, ctypes.c_void_p).value


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


class Lib:
    _name_ = None

    @staticmethod
    def Signature(functionname, *cargs):
        def decorator(function):
            def wrapper(self, *args):
                cfunction = self._functions.get(functionname)
                if not cfunction:
                    cfunction = self._wrap_function(functionname, cargs, function(self, *cargs))
                    self._functions[functionname] = cfunction
                return cfunction(*args)

            wrapper.functionname = functionname
            wrapper.cargs = cargs
            return wrapper
        return decorator

    def __init__(self, name=None):
        name = name or self._name_
        self._name = util.find_library(name)
        self._functions = {}
        if not self._name:
            raise RuntimeError(f"{name} library can not be found")
        log.LOGGER.debug(f"loading library {self._name}")
        self._lib = ctypes.CDLL(self._name)

    def functype(self, callback):
        cargs = callback.__closure__[0].cell_contents
        retval = callback.__closure__[1].cell_contents(self, *cargs)
        if not hasattr(retval, "_type_") or not isinstance(retval._type_, str) or not retval._type_ != "P":
            retval = ctypes.c_void_p
        functionname = callback.__closure__[2].cell_contents
        ptr = self._wrap_function(functionname, cargs, retval)
        return ctypes.CFUNCTYPE(retval, *cargs)(ptr)

    def _wrap_function(self, name, args, rettype=None):
        if self._functions.get(name):
            raise RuntimeError(f"function {name} has already been prototyped")
        ptr = getattr(self._lib, name, None)
        if not ptr:
            raise RuntimeError(f"function {name} is not exported from {self._name}")
        rettype = rettype or ctypes.c_void_p
        setattr(ptr, "argtypes", args)
        setattr(ptr, "restype", rettype)
        log.LOGGER.debug(f"function {name} is wrapped from {self._name}")
        return ptr


class Clib(Lib):
    _name_ = "c"
