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
import sys
import ctypes
from v4l2codecs import av
from v4l2codecs import log
from v4l2codecs import clib

CODECID = av.codec.EnumCodecID(av.codec.EnumCodecID._enum_.H264.value)
LOGLEVEL = av.util.EnumLogLevel(av.util.EnumLogLevel._enum_.DEBUG.value)
PATH = sys.argv[1]
CHUNK = 4096

log.LOGGER.setLevel(log.DEBUG)

avcodec = av.codec.Codec()
avutil = av.util.Util()

cb = avutil.functype(avutil.log_default_callback)
avutil.set_log_callback(cb)
avutil.set_log_level(LOGLEVEL)

codec = avcodec.find_decoder(CODECID)
if not clib.ptr_address(codec):
    raise RuntimeError("Can not find codec")

ctx = avcodec.alloc_context3(codec)
if not clib.ptr_address(ctx):
    raise RuntimeError("Can not alloc context")

pkt = avcodec.packet_alloc()
if not clib.ptr_address(pkt):
    raise RuntimeError("Can not alloc packet")

frame = avcodec.frame_alloc()
if not clib.ptr_address(frame):
    raise RuntimeError("Can not alloc frame")

parser = avcodec.parser_init(codec.contents.id)
if not clib.ptr_address(parser):
    raise RuntimeError("Can not alloc parser")

if(avcodec.open2(ctx, codec, None)):
    raise RuntimeError("Can not open codec")

f = open(PATH, "rb")
while True:
    data = f.read(CHUNK)
    if data == b"":
        break
    datalen = len(data)
    data = ctypes.cast(data, ctypes.POINTER(ctypes.c_uint8))
    ret = avcodec.parser_parse2(parser, ctx,
                                ctypes.byref(pkt.contents.data),
                                pkt.contents.size.ref,
                                data, datalen,
                                av.util.NOPTS, av.util.NOPTS,
                                0)
    if(ret < 0):
        raise RuntimeError("Can not parse feed")

f.close()
pass
