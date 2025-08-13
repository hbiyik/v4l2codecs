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

Union = ctypes.Union
sizeof = ctypes.sizeof
cast = ctypes.cast
memmove = ctypes.memmove


class BaseType:
    @property
    def ref(self):
        return ctypes.byref(self)

    def __str__(self):
        for attr in ["address", "value"]:
            val = getattr(self, attr, None)
            if val is not None:
                return str(val)
        if hasattr(self, "_type_"):
            return "nullptr"
        return "mixed"

    def __repr__(self):
        return str(self)


class BasePointer(BaseType):
    @property
    def address(self):
        return ctypes.cast(self, ctypes.c_void_p).value

    @address.setter
    def address(self, addr):
        # change the pointers existing address
        ctypes.memmove(ctypes.byref(self),
                       ctypes.byref(ctypes.c_void_p(addr)),
                       ctypes.sizeof(self))


# wrapper union class so that ctypes will be kept as ctypes when used in Struct
# otherwise they are converted to pythonic types (ie: struct.c_int -> sctruct.int)
class UnionWrapper(Union, BaseType):
    @staticmethod
    def type(ctype):
        def wrapper(cls):
            cls._fields_ = [("value", ctype)]
            return cls
        return wrapper


class c_char_p(ctypes.c_char_p, BasePointer):
    pass


class c_wchar_p(ctypes.c_wchar_p, BasePointer):
    pass


class c_void_p(ctypes.c_void_p, BasePointer):
    pass


class Structure(ctypes.Structure, BaseType):
    pass


@UnionWrapper.type(ctypes.c_short)
class c_short(UnionWrapper):
    pass


@UnionWrapper.type(ctypes.c_ushort)
class c_ushort(UnionWrapper):
    pass


@UnionWrapper.type(ctypes.c_long)
class c_long(UnionWrapper):
    pass


@UnionWrapper.type(ctypes.c_ulong)
class c_ulong(UnionWrapper):
    pass


@UnionWrapper.type(ctypes.c_int)
class c_int(UnionWrapper):
    pass


@UnionWrapper.type(ctypes.c_uint)
class c_uint(UnionWrapper):
    pass


@UnionWrapper.type(ctypes.c_float)
class c_float(UnionWrapper):
    pass


@UnionWrapper.type(ctypes.c_double)
class c_double(UnionWrapper):
    pass


@UnionWrapper.type(ctypes.c_longdouble)
class c_longdouble(UnionWrapper):
    pass


@UnionWrapper.type(ctypes.c_longlong)
class c_longlong(UnionWrapper):
    pass


@UnionWrapper.type(ctypes.c_ulonglong)
class c_ulonglong(UnionWrapper):
    pass


@UnionWrapper.type(ctypes.c_ubyte)
class c_ubyte(UnionWrapper):
    pass


@UnionWrapper.type(ctypes.c_byte)
class c_byte(UnionWrapper):
    pass


@UnionWrapper.type(ctypes.c_bool)
class c_bool(UnionWrapper):
    pass


@UnionWrapper.type(ctypes.c_char)
class c_char(UnionWrapper):
    pass


@UnionWrapper.type(ctypes.c_wchar)
class c_wchar(UnionWrapper):
    pass


c_int8 = c_byte
c_uint8 = c_ubyte


@UnionWrapper.type(ctypes.c_int16)
class c_int16(UnionWrapper):
    pass


@UnionWrapper.type(ctypes.c_int32)
class c_int32(UnionWrapper):
    pass


@UnionWrapper.type(ctypes.c_int64)
class c_int64(UnionWrapper):
    pass


@UnionWrapper.type(ctypes.c_uint16)
class c_uint16(UnionWrapper):
    pass


@UnionWrapper.type(ctypes.c_uint32)
class c_uint32(UnionWrapper):
    pass


@UnionWrapper.type(ctypes.c_uint64)
class c_uint64(UnionWrapper):
    pass


@UnionWrapper.type(ctypes.c_size_t)
class c_size_t(UnionWrapper):
    pass


def POINTER(typ):
    ptyp = ctypes.POINTER(typ)
    ptyp.address = BasePointer.address
    ptyp.ref = BaseType.ref
    ptyp.__str__ = BaseType.__str__
    ptyp.__repr__ = BaseType.__repr__
    return ptyp


# combination of enum module and ctype int
class c_intenum(c_int):
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

    def __eq__(self, value):
        if isinstance(value, c_int):
            return value.value == self.value
        return c_int.__eq__(self, value)
