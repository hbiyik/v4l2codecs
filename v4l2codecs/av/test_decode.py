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


CODECID = av.codec.EnumCodecID(av.codec.EnumCodecID._enum_.H264.value)
LOGLEVEL = av.util.EnumLogLevel(av.util.EnumLogLevel._enum_.TRACE.value)
VT_VIDEO = av.util.EnumMediaType(av.util.EnumMediaType._enum_.VIDEO)
HWTYPE = av.util.EnumHWDeviceType(av.util.EnumHWDeviceType._enum_.VDPAU)
FMT_NONE = av.util.EnumPixelFormat(av.util.EnumPixelFormat._enum_.NONE)
FMT_SELECT = av.util.EnumPixelFormat(av.util.EnumPixelFormat._enum_.VDPAU)
PATH = sys.argv[1]
CHUNK = 4096


avutil = av.util.Lib()
avformat = av.format.Lib()
avcodec = av.codec.Lib()
libc = clib.Clib()


def loghandler(ptr, level, fmt, vl):
    name = "ffmpeg"
    if ptr.address:
        dec_ctx = clib.POINTER(av.util.StructClass).from_address(ptr.address)
        name = dec_ctx.contents.class_name.value.decode()
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
                                   func=name)
    log.LOGGER.handle(record)


def get_format(s, fmts):
    while True:
        if fmts.contents == FMT_SELECT:
            return FMT_SELECT.value
        if fmts.contents == FMT_NONE:
            break
        fmts.address += clib.sizeof(fmts.contents)
    return FMT_NONE.value


log.LOGGER.setLevel(log.DEBUG)
avutil.set_log_level(LOGLEVEL)
cb = avutil.functype(avutil.log_default_callback)(loghandler)
avutil.set_log_callback(cb)

in_ctx = clib.POINTER(av.format.StructContext)()
dec_ctx = clib.POINTER(av.codec.StructContext)()
dev_ctx = clib.POINTER(av.util.StructBufferRef)()
frame = clib.POINTER(av.util.StructFrame)()

dec = clib.POINTER(av.codec.StructCodec)()
hwconfig = clib.POINTER(av.codec.StructHWConfig)()


if avformat.open_input(in_ctx.ref, PATH.encode(), None, None).value:
    raise RuntimeError("Can not open file")

if avformat.find_stream_info(in_ctx, None).value < 0:
    raise RuntimeError("Can not find streams")

video_stream = avformat.find_best_stream(in_ctx, VT_VIDEO,
                                         clib.c_int(-1),
                                         clib.c_int(-1),
                                         dec.ref,
                                         clib.c_int(0))

if video_stream.value < 0:
    raise RuntimeError("Can not find video stream")

index = clib.c_int(0)
while True:
    hwconfig = avcodec.get_hw_config(dec, index)
    if hwconfig.contents.device_type == HWTYPE:
        break
    if not hwconfig.address:
        raise RuntimeError(f"Can not find hwaccel {HWTYPE}")
    index.value += 1

dec_ctx = avcodec.alloc_context(dec)
if not dec_ctx.address:
    raise RuntimeError("Can not alloc context")

if (avcodec.params_to_context(dec_ctx, in_ctx.contents.streams[video_stream.value].contents.codecpar).value < 0):
    raise RuntimeError("Can not copy dec parameters")

dec_ctx.contents.get_format = av.codec.Lib.functype(av.codec.Lib.get_format)(get_format)

if avutil.hwdevice_ctx_create(dev_ctx.ref, HWTYPE, None, None, clib.c_int(0)).value:
    raise RuntimeError(f"Can not create {HWTYPE}")

dec_ctx.contents.hw_device_ctx = avutil.buffer_ref(dev_ctx)

if(avcodec.open(dec_ctx, dec, None).value):
    raise RuntimeError("Can not open dec")

pkt = avcodec.packet_alloc()
if not pkt.address:
    raise RuntimeError("Can not alloc packet")

newpacket = True
eof = False
while True:
    if newpacket and avformat.read_frame(in_ctx, pkt).value < 0:
        log.LOGGER.info("file finished")
        break

    if not video_stream.value == pkt.contents.stream_index.value:
        continue

    ret = avcodec.send_packet(dec_ctx, pkt)
    if ret.value == -errno.EAGAIN:
        newpacket = False
    elif ret.value < 0:
        raise RuntimeError(f"Error Sending packet {ret.value}")
    else:
        avcodec.packet_unref(pkt)
        newpacket = True

    if not frame.address:
        frame = avcodec.frame_alloc()
        if not frame.address:
            raise RuntimeError("Can not alloc frame")

    ret = avcodec.receive_frame(dec_ctx, frame)
    if ret.value == -errno.EAGAIN:
        continue
    elif ret.value < 0:
        raise RuntimeError(f"Error receiving frame {ret.value}")
    else:
        avcodec.frame_free(frame.ref)
        log.LOGGER.info(f"Decoded frame {dec_ctx.contents.frame_num.value}")

# clean stuff
pass
