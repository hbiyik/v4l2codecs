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
import errno
import logging
from v4l2codecs import clib
from v4l2codecs import av
from v4l2codecs import log
import ctypes


CODECID = av.codec.EnumCodecID(av.codec.EnumCodecID._enum_.H264.value)
LOGLEVEL = av.util.EnumLogLevel(av.util.EnumLogLevel._enum_.TRACE.value)
PATH = sys.argv[1]
CHUNK = 4096


avutil = av.util.Util()
libc = clib.Clib()


def loghandler(ptr, level, fmt, vl):
    ctx = clib.POINTER(av.util.StructClass).from_address(ptr.address)
    vl = clib.c_void_p(vl.address)
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
    level = levels.get(level.value, logging.DEBUG)
    msg = b"\0" * len(fmt.value) * 2
    libc._lib.vsnprintf(clib.c_char_p(msg), len(msg), fmt, vl)
    msg = msg.split(b"\n")[0]
    record = log.LOGGER.makeRecord(log.LOGGER.name,
                                   level,
                                   "ffmpeg",
                                   0,
                                   msg.decode(),
                                   [], [],
                                   func=ctx.contents.class_name.value.decode())
    log.LOGGER.handle(record)
    pass


cb = ctypes.CFUNCTYPE(clib.c_void_p,
                      clib.c_void_p,
                      clib.c_int,
                      clib.c_char_p,
                      clib.c_void_p)(loghandler)
log.LOGGER.setLevel(log.DEBUG)
avutil.set_log_level(LOGLEVEL)
avutil.set_log_callback(cb)

avcodec = av.codec.Codec()
codec = avcodec.find_decoder(CODECID)
if not codec.address:
    raise RuntimeError("Can not find codec")

ctx = avcodec.alloc_context3(codec)
if not ctx.address:
    raise RuntimeError("Can not alloc context")

pkt = avcodec.packet_alloc()
if not pkt.address:
    raise RuntimeError("Can not alloc packet")

frame = avcodec.frame_alloc()
if not frame.address:
    raise RuntimeError("Can not alloc frame")

parser = avcodec.parser_init(codec.contents.id)
if not parser.address:
    raise RuntimeError("Can not alloc parser")

if(avcodec.open2(ctx, codec, None).value):
    raise RuntimeError("Can not open codec")

f = open(PATH, "rb")
while True:
    data = f.read(CHUNK)
    if data == b"":
        break
    readlen = len(data)
    while readlen > 0:
        data = ctypes.cast(data, clib.POINTER(clib.c_uint8))
        parselen = avcodec.parser_parse2(parser, ctx,
                                         pkt.contents.data.ref,
                                         pkt.contents.size.ref,
                                         data, clib.c_int(readlen),
                                         av.util.NOPTS, av.util.NOPTS,
                                         clib.c_uint64(0))
        data.address += parselen.value
        readlen -= parselen.value
        if pkt.contents.size.value:
            ret = avcodec.send_packet(ctx, pkt)
            if ret.value < 0:
                raise RuntimeError(f"Error Sending packet {ret.value}")
            ret = clib.c_int(0)
            while not ret.value:
                ret = avcodec.receive_frame(ctx, frame)
                if ret.value < 0:
                    if ret.value == -errno.EAGAIN:
                        break
                    else:
                        raise RuntimeError(f"Error receiving frame {ret.value}")
                # log.LOGGER.info(f"Decoded frame {ctx.contents.frame_num.value}")
        if parselen.value < 0:
            raise RuntimeError("Can not parse feed")

f.close()
pass
