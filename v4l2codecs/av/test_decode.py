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
import logging
from v4l2codecs import av
from v4l2codecs import log
from v4l2codecs import clib

CODECID = av.codec.EnumCodecID(av.codec.EnumCodecID._enum_.H264.value)
LOGLEVEL = av.util.EnumLogLevel(av.util.EnumLogLevel._enum_.TRACE.value)
PATH = sys.argv[1]
CHUNK = 4096


avutil = av.util.Util()


def loghandler(ptr, level, fmt, vl):
    ctx = ctypes.POINTER(av.util.StructClass).from_address(ptr)
    vl = ctypes.c_void_p(vl)
    libc = clib.Clib()
    levels = {av.util.EnumLogLevel._enum_.QUIET: logging.NOTSET,
              av.util.EnumLogLevel._enum_.PANIC: logging.CRITICAL,
              av.util.EnumLogLevel._enum_.FATAL: logging.FATAL,
              av.util.EnumLogLevel._enum_.ERROR: logging.ERROR,
              av.util.EnumLogLevel._enum_.WARNING: logging.WARNING,
              av.util.EnumLogLevel._enum_.INFO: logging.INFO,
              av.util.EnumLogLevel._enum_.VERBOSE: logging.DEBUG,
              av.util.EnumLogLevel._enum_.DEBUG: logging.DEBUG,
              av.util.EnumLogLevel._enum_.TRACE: logging.DEBUG,
              }
    level = levels.get(level, logging.DEBUG)
    msg = b"0" * len(fmt) * 2
    libc._lib.vsnprintf(msg, len(msg), fmt, vl)
    record = log.LOGGER.makeRecord(log.LOGGER.name,
                                   level,
                                   "ffmpeg",
                                   0,
                                   msg.decode(),
                                   [], [],
                                   func=ctx.contents.class_name.decode())
    log.LOGGER.handle(record)
    pass


cb = ctypes.CFUNCTYPE(ctypes.c_void_p,
                      ctypes.c_void_p,
                      ctypes.c_int,
                      ctypes.c_char_p,
                      ctypes.c_void_p)(loghandler)
log.LOGGER.setLevel(log.DEBUG)
avutil.set_log_level(LOGLEVEL)
avutil.set_log_callback(cb)

avcodec = av.codec.Codec()
codec = avcodec.find_decoder(CODECID)
if not clib.ptr_address(codec):
    raise RuntimeError("Can not find codec")

ctx = avcodec.alloc_context3(codec)
if not clib.ptr_address(ctx):
    raise RuntimeError("Can not alloc context")

avutil.log(ctx, LOGLEVEL, b"test")

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
