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
import enum

from v4l2codecs import clib

NOPTS = clib.c_int64(0x8000000000000000)


class EnumLogLevel(clib.c_intenum):

    class _enum_(enum.IntEnum):
        QUIET = -8
        PANIC = 0
        FATAL = 8
        ERROR = 16
        WARNING = 24
        INFO = 32
        VERBOSE = 40
        DEBUG = 48
        TRACE = 56


class EnumMediaType(clib.c_intenum):

    class _enum_(enum.IntEnum):
        UNKNOWN = -1  # Usually treated as DATA
        VIDEO = enum.auto()
        AUDIO = enum.auto()
        DATA = enum.auto()  # Opaque data information usually continuous
        SUBTITLE = enum.auto()
        ATTACHMENT = enum.auto()  # Opaque data information usually sparse
        NB = enum.auto()


class EnumPixelFormat(clib.c_intenum):

    class _enum_(enum.IntEnum):
        NONE = -1
        YUV420P = enum.auto()  # planar YUV 4:2:0, 12bpp, (1 Cr & Cb sample per 2x2 Y samples)
        YUYV422 = enum.auto()  # packed YUV 4:2:2, 16bpp, Y0 Cb Y1 Cr
        RGB24 = enum.auto()  # packed RGB 8:8:8, 24bpp, RGBRGB...
        BGR24 = enum.auto()  # packed RGB 8:8:8, 24bpp, BGRBGR...
        YUV422P = enum.auto()  # planar YUV 4:2:2, 16bpp, (1 Cr & Cb sample per 2x1 Y samples)
        YUV444P = enum.auto()  # planar YUV 4:4:4, 24bpp, (1 Cr & Cb sample per 1x1 Y samples)
        YUV410P = enum.auto()  # planar YUV 4:1:0,  9bpp, (1 Cr & Cb sample per 4x4 Y samples)
        YUV411P = enum.auto()  # planar YUV 4:1:1, 12bpp, (1 Cr & Cb sample per 4x1 Y samples)
        GRAY8 = enum.auto()  # Y 8bpp
        MONOWHITE = enum.auto()  # Y 1bpp, 0 is white, 1 is black, in each byte pixels are ordered from the msb to the lsb
        MONOBLACK = enum.auto()  # Y 1bpp, 0 is black, 1 is white, in each byte pixels are ordered from the msb to the lsb
        PAL8 = enum.auto()  # 8 bits with RGB32 palette
        YUVJ420P = enum.auto()  # planar YUV 4:2:0, 12bpp, full scale (JPEG), deprecated in favor of YUV420P and setting color_range
        YUVJ422P = enum.auto()  # planar YUV 4:2:2, 16bpp, full scale (JPEG), deprecated in favor of YUV422P and setting color_range
        YUVJ444P = enum.auto()  # planar YUV 4:4:4, 24bpp, full scale (JPEG), deprecated in favor of YUV444P and setting color_range
        UYVY422 = enum.auto()  # packed YUV 4:2:2, 16bpp, Cb Y0 Cr Y1
        UYYVYY411 = enum.auto()  # packed YUV 4:1:1, 12bpp, Cb Y0 Y1 Cr Y2 Y3
        BGR8 = enum.auto()  # packed RGB 3:3:2,  8bpp, (msb)2B 3G 3R(lsb)
        BGR4 = enum.auto()  # packed RGB 1:2:1 bitstream,  4bpp, (msb)1B 2G 1R(lsb), a byte contains two pixels, the first pixel in the byte is the one composed by the 4 msb bits
        BGR4_BYTE = enum.auto()  # packed RGB 1:2:1,  8bpp, (msb)1B 2G 1R(lsb)
        RGB8 = enum.auto()  # packed RGB 3:3:2,  8bpp, (msb)3R 3G 2B(lsb)
        RGB4 = enum.auto()  # packed RGB 1:2:1 bitstream,  4bpp, (msb)1R 2G 1B(lsb), a byte contains two pixels, the first pixel in the byte is the one composed by the 4 msb bits
        RGB4_BYTE = enum.auto()  # packed RGB 1:2:1,  8bpp, (msb)1R 2G 1B(lsb)
        NV12 = enum.auto()  # planar YUV 4:2:0, 12bpp, 1 plane for Y and 1 plane for the UV components, which are interleaved (first byte U and the following byte V)
        NV21 = enum.auto()  # as above, but U and V bytes are swapped

        ARGB = enum.auto()  # packed ARGB 8:8:8:8, 32bpp, ARGBARGB...
        RGBA = enum.auto()  # packed RGBA 8:8:8:8, 32bpp, RGBARGBA...
        ABGR = enum.auto()  # packed ABGR 8:8:8:8, 32bpp, ABGRABGR...
        BGRA = enum.auto()  # packed BGRA 8:8:8:8, 32bpp, BGRABGRA...

        GRAY16BE = enum.auto()  # Y , 16bpp, big-endian
        GRAY16LE = enum.auto()  # Y , 16bpp, little-endian
        YUV440P = enum.auto()  # planar YUV 4:4:0 (1 Cr & Cb sample per 1x2 Y samples)
        YUVJ440P = enum.auto()  # planar YUV 4:4:0 full scale (JPEG), deprecated in favor of YUV440P and setting color_range
        YUVA420P = enum.auto()  # planar YUV 4:2:0, 20bpp, (1 Cr & Cb sample per 2x2 Y & A samples)
        RGB48BE = enum.auto()  # packed RGB 16:16:16, 48bpp, 16R, 16G, 16B, the 2-byte value for each R/G/B component is stored as big-endian
        RGB48LE = enum.auto()  # packed RGB 16:16:16, 48bpp, 16R, 16G, 16B, the 2-byte value for each R/G/B component is stored as little-endian

        RGB565BE = enum.auto()  # packed RGB 5:6:5, 16bpp, (msb)   5R 6G 5B(lsb), big-endian
        RGB565LE = enum.auto()  # packed RGB 5:6:5, 16bpp, (msb)   5R 6G 5B(lsb), little-endian
        RGB555BE = enum.auto()  # packed RGB 5:5:5, 16bpp, (msb)1X 5R 5G 5B(lsb), big-endian   , X=unused/undefined
        RGB555LE = enum.auto()  # packed RGB 5:5:5, 16bpp, (msb)1X 5R 5G 5B(lsb), little-endian, X=unused/undefined

        BGR565BE = enum.auto()  # packed BGR 5:6:5, 16bpp, (msb)   5B 6G 5R(lsb), big-endian
        BGR565LE = enum.auto()  # packed BGR 5:6:5, 16bpp, (msb)   5B 6G 5R(lsb), little-endian
        BGR555BE = enum.auto()  # packed BGR 5:5:5, 16bpp, (msb)1X 5B 5G 5R(lsb), big-endian   , X=unused/undefined
        BGR555LE = enum.auto()  # packed BGR 5:5:5, 16bpp, (msb)1X 5B 5G 5R(lsb), little-endian, X=unused/undefined
        VAAPI = enum.auto()

        YUV420P16LE = enum.auto()  # planar YUV 4:2:0, 24bpp, (1 Cr & Cb sample per 2x2 Y samples), little-endian
        YUV420P16BE = enum.auto()  # planar YUV 4:2:0, 24bpp, (1 Cr & Cb sample per 2x2 Y samples), big-endian
        YUV422P16LE = enum.auto()  # planar YUV 4:2:2, 32bpp, (1 Cr & Cb sample per 2x1 Y samples), little-endian
        YUV422P16BE = enum.auto()  # planar YUV 4:2:2, 32bpp, (1 Cr & Cb sample per 2x1 Y samples), big-endian
        YUV444P16LE = enum.auto()  # planar YUV 4:4:4, 48bpp, (1 Cr & Cb sample per 1x1 Y samples), little-endian
        YUV444P16BE = enum.auto()  # planar YUV 4:4:4, 48bpp, (1 Cr & Cb sample per 1x1 Y samples), big-endian
        DXVA2_VLD = enum.auto()  # HW decoding through DXVA2, Picture.data[3] contains a LPDIRECT3DSURFACE9 pointer

        RGB444LE = enum.auto()  # packed RGB 4:4:4, 16bpp, (msb)4X 4R 4G 4B(lsb), little-endian, X=unused/undefined
        RGB444BE = enum.auto()  # packed RGB 4:4:4, 16bpp, (msb)4X 4R 4G 4B(lsb), big-endian,    X=unused/undefined
        BGR444LE = enum.auto()  # packed BGR 4:4:4, 16bpp, (msb)4X 4B 4G 4R(lsb), little-endian, X=unused/undefined
        BGR444BE = enum.auto()  # packed BGR 4:4:4, 16bpp, (msb)4X 4B 4G 4R(lsb), big-endian,    X=unused/undefined
        YA8 = enum.auto()  # 8 bits gray, 8 bits alpha

        BGR48BE = enum.auto()  # packed RGB 16:16:16, 48bpp, 16B, 16G, 16R, the 2-byte value for each R/G/B component is stored as big-endian
        BGR48LE = enum.auto()  # packed RGB 16:16:16, 48bpp, 16B, 16G, 16R, the 2-byte value for each R/G/B component is stored as little-endian

        YUV420P9BE = enum.auto()  # planar YUV 4:2:0, 13.5bpp, (1 Cr & Cb sample per 2x2 Y samples), big-endian
        YUV420P9LE = enum.auto()  # planar YUV 4:2:0, 13.5bpp, (1 Cr & Cb sample per 2x2 Y samples), little-endian
        YUV420P10BE = enum.auto()  # planar YUV 4:2:0, 15bpp, (1 Cr & Cb sample per 2x2 Y samples), big-endian
        YUV420P10LE = enum.auto()  # planar YUV 4:2:0, 15bpp, (1 Cr & Cb sample per 2x2 Y samples), little-endian
        YUV422P10BE = enum.auto()  # planar YUV 4:2:2, 20bpp, (1 Cr & Cb sample per 2x1 Y samples), big-endian
        YUV422P10LE = enum.auto()  # planar YUV 4:2:2, 20bpp, (1 Cr & Cb sample per 2x1 Y samples), little-endian
        YUV444P9BE = enum.auto()  # planar YUV 4:4:4, 27bpp, (1 Cr & Cb sample per 1x1 Y samples), big-endian
        YUV444P9LE = enum.auto()  # planar YUV 4:4:4, 27bpp, (1 Cr & Cb sample per 1x1 Y samples), little-endian
        YUV444P10BE = enum.auto()  # planar YUV 4:4:4, 30bpp, (1 Cr & Cb sample per 1x1 Y samples), big-endian
        YUV444P10LE = enum.auto()  # planar YUV 4:4:4, 30bpp, (1 Cr & Cb sample per 1x1 Y samples), little-endian
        YUV422P9BE = enum.auto()  # planar YUV 4:2:2, 18bpp, (1 Cr & Cb sample per 2x1 Y samples), big-endian
        YUV422P9LE = enum.auto()  # planar YUV 4:2:2, 18bpp, (1 Cr & Cb sample per 2x1 Y samples), little-endian
        GBRP = enum.auto()  # planar GBR 4:4:4 24bpp
        GBRP9BE = enum.auto()  # planar GBR 4:4:4 27bpp, big-endian
        GBRP9LE = enum.auto()  # planar GBR 4:4:4 27bpp, little-endian
        GBRP10BE = enum.auto()  # planar GBR 4:4:4 30bpp, big-endian
        GBRP10LE = enum.auto()  # planar GBR 4:4:4 30bpp, little-endian
        GBRP16BE = enum.auto()  # planar GBR 4:4:4 48bpp, big-endian
        GBRP16LE = enum.auto()  # planar GBR 4:4:4 48bpp, little-endian
        YUVA422P = enum.auto()  # planar YUV 4:2:2 24bpp, (1 Cr & Cb sample per 2x1 Y & A samples)
        YUVA444P = enum.auto()  # planar YUV 4:4:4 32bpp, (1 Cr & Cb sample per 1x1 Y & A samples)
        YUVA420P9BE = enum.auto()  # planar YUV 4:2:0 22.5bpp, (1 Cr & Cb sample per 2x2 Y & A samples), big-endian
        YUVA420P9LE = enum.auto()  # planar YUV 4:2:0 22.5bpp, (1 Cr & Cb sample per 2x2 Y & A samples), little-endian
        YUVA422P9BE = enum.auto()  # planar YUV 4:2:2 27bpp, (1 Cr & Cb sample per 2x1 Y & A samples), big-endian
        YUVA422P9LE = enum.auto()  # planar YUV 4:2:2 27bpp, (1 Cr & Cb sample per 2x1 Y & A samples), little-endian
        YUVA444P9BE = enum.auto()  # planar YUV 4:4:4 36bpp, (1 Cr & Cb sample per 1x1 Y & A samples), big-endian
        YUVA444P9LE = enum.auto()  # planar YUV 4:4:4 36bpp, (1 Cr & Cb sample per 1x1 Y & A samples), little-endian
        YUVA420P10BE = enum.auto()  # planar YUV 4:2:0 25bpp, (1 Cr & Cb sample per 2x2 Y & A samples, big-endian)
        YUVA420P10LE = enum.auto()  # planar YUV 4:2:0 25bpp, (1 Cr & Cb sample per 2x2 Y & A samples, little-endian)
        YUVA422P10BE = enum.auto()  # planar YUV 4:2:2 30bpp, (1 Cr & Cb sample per 2x1 Y & A samples, big-endian)
        YUVA422P10LE = enum.auto()  # planar YUV 4:2:2 30bpp, (1 Cr & Cb sample per 2x1 Y & A samples, little-endian)
        YUVA444P10BE = enum.auto()  # planar YUV 4:4:4 40bpp, (1 Cr & Cb sample per 1x1 Y & A samples, big-endian)
        YUVA444P10LE = enum.auto()  # planar YUV 4:4:4 40bpp, (1 Cr & Cb sample per 1x1 Y & A samples, little-endian)
        YUVA420P16BE = enum.auto()  # planar YUV 4:2:0 40bpp, (1 Cr & Cb sample per 2x2 Y & A samples, big-endian)
        YUVA420P16LE = enum.auto()  # planar YUV 4:2:0 40bpp, (1 Cr & Cb sample per 2x2 Y & A samples, little-endian)
        YUVA422P16BE = enum.auto()  # planar YUV 4:2:2 48bpp, (1 Cr & Cb sample per 2x1 Y & A samples, big-endian)
        YUVA422P16LE = enum.auto()  # planar YUV 4:2:2 48bpp, (1 Cr & Cb sample per 2x1 Y & A samples, little-endian)
        YUVA444P16BE = enum.auto()  # planar YUV 4:4:4 64bpp, (1 Cr & Cb sample per 1x1 Y & A samples, big-endian)
        YUVA444P16LE = enum.auto()  # planar YUV 4:4:4 64bpp, (1 Cr & Cb sample per 1x1 Y & A samples, little-endian)

        VDPAU = enum.auto()  # HW acceleration through VDPAU, Picture.data[3] contains a VdpVideoSurface

        XYZ12LE = enum.auto()  # packed XYZ 4:4:4, 36 bpp, (msb) 12X, 12Y, 12Z (lsb), the 2-byte value for each X/Y/Z is stored as little-endian, the 4 lower bits are set to 0
        XYZ12BE = enum.auto()  # packed XYZ 4:4:4, 36 bpp, (msb) 12X, 12Y, 12Z (lsb), the 2-byte value for each X/Y/Z is stored as big-endian, the 4 lower bits are set to 0
        NV16 = enum.auto()  # interleaved chroma YUV 4:2:2, 16bpp, (1 Cr & Cb sample per 2x1 Y samples)
        NV20LE = enum.auto()  # interleaved chroma YUV 4:2:2, 20bpp, (1 Cr & Cb sample per 2x1 Y samples), little-endian
        NV20BE = enum.auto()  # interleaved chroma YUV 4:2:2, 20bpp, (1 Cr & Cb sample per 2x1 Y samples), big-endian

        RGBA64BE = enum.auto()  # packed RGBA 16:16:16:16, 64bpp, 16R, 16G, 16B, 16A, the 2-byte value for each R/G/B/A component is stored as big-endian
        RGBA64LE = enum.auto()  # packed RGBA 16:16:16:16, 64bpp, 16R, 16G, 16B, 16A, the 2-byte value for each R/G/B/A component is stored as little-endian
        BGRA64BE = enum.auto()  # packed RGBA 16:16:16:16, 64bpp, 16B, 16G, 16R, 16A, the 2-byte value for each R/G/B/A component is stored as big-endian
        BGRA64LE = enum.auto()  # packed RGBA 16:16:16:16, 64bpp, 16B, 16G, 16R, 16A, the 2-byte value for each R/G/B/A component is stored as little-endian

        YVYU422 = enum.auto()  # packed YUV 4:2:2, 16bpp, Y0 Cr Y1 Cb

        YA16BE = enum.auto()  # 16 bits gray, 16 bits alpha (big-endian)
        YA16LE = enum.auto()  # 16 bits gray, 16 bits alpha (little-endian)

        GBRAP = enum.auto()  # planar GBRA 4:4:4:4 32bpp
        GBRAP16BE = enum.auto()  # planar GBRA 4:4:4:4 64bpp, big-endian
        GBRAP16LE = enum.auto()  # planar GBRA 4:4:4:4 64bpp, little-endian
        QSV = enum.auto()
        MMAL = enum.auto()

        D3D11VA_VLD = enum.auto()  # HW decoding through Direct3D11 via old API, Picture.data[3] contains a ID3D11VideoDecoderOutputView pointer
        CUDA = enum.auto()

        ORGB = enum.auto()  # packed RGB 8:8:8, 32bpp, XRGBXRGB...   X=unused/undefined
        RGB0 = enum.auto()  # packed RGB 8:8:8, 32bpp, RGBXRGBX...   X=unused/undefined
        OBGR = enum.auto()  # packed BGR 8:8:8, 32bpp, XBGRXBGR...   X=unused/undefined
        BGR0 = enum.auto()  # packed BGR 8:8:8, 32bpp, BGRXBGRX...   X=unused/undefined

        YUV420P12BE = enum.auto()  # planar YUV 4:2:0,18bpp, (1 Cr & Cb sample per 2x2 Y samples), big-endian
        YUV420P12LE = enum.auto()  # planar YUV 4:2:0,18bpp, (1 Cr & Cb sample per 2x2 Y samples), little-endian
        YUV420P14BE = enum.auto()  # planar YUV 4:2:0,21bpp, (1 Cr & Cb sample per 2x2 Y samples), big-endian
        YUV420P14LE = enum.auto()  # planar YUV 4:2:0,21bpp, (1 Cr & Cb sample per 2x2 Y samples), little-endian
        YUV422P12BE = enum.auto()  # planar YUV 4:2:2,24bpp, (1 Cr & Cb sample per 2x1 Y samples), big-endian
        YUV422P12LE = enum.auto()  # planar YUV 4:2:2,24bpp, (1 Cr & Cb sample per 2x1 Y samples), little-endian
        YUV422P14BE = enum.auto()  # planar YUV 4:2:2,28bpp, (1 Cr & Cb sample per 2x1 Y samples), big-endian
        YUV422P14LE = enum.auto()  # planar YUV 4:2:2,28bpp, (1 Cr & Cb sample per 2x1 Y samples), little-endian
        YUV444P12BE = enum.auto()  # planar YUV 4:4:4,36bpp, (1 Cr & Cb sample per 1x1 Y samples), big-endian
        YUV444P12LE = enum.auto()  # planar YUV 4:4:4,36bpp, (1 Cr & Cb sample per 1x1 Y samples), little-endian
        YUV444P14BE = enum.auto()  # planar YUV 4:4:4,42bpp, (1 Cr & Cb sample per 1x1 Y samples), big-endian
        YUV444P14LE = enum.auto()  # planar YUV 4:4:4,42bpp, (1 Cr & Cb sample per 1x1 Y samples), little-endian
        GBRP12BE = enum.auto()  # planar GBR 4:4:4 36bpp, big-endian
        GBRP12LE = enum.auto()  # planar GBR 4:4:4 36bpp, little-endian
        GBRP14BE = enum.auto()  # planar GBR 4:4:4 42bpp, big-endian
        GBRP14LE = enum.auto()  # planar GBR 4:4:4 42bpp, little-endian
        YUVJ411P = enum.auto()  # planar YUV 4:1:1, 12bpp, (1 Cr & Cb sample per 4x1 Y samples) full scale (JPEG), deprecated in favor of YUV411P and setting color_range

        BAYER_BGGR8 = enum.auto()  # bayer, BGBG..(odd line), GRGR..(even line), 8-bit samples
        BAYER_RGGB8 = enum.auto()  # bayer, RGRG..(odd line), GBGB..(even line), 8-bit samples
        BAYER_GBRG8 = enum.auto()  # bayer, GBGB..(odd line), RGRG..(even line), 8-bit samples
        BAYER_GRBG8 = enum.auto()  # bayer, GRGR..(odd line), BGBG..(even line), 8-bit samples
        BAYER_BGGR16LE = enum.auto()  # bayer, BGBG..(odd line), GRGR..(even line), 16-bit samples, little-endian
        BAYER_BGGR16BE = enum.auto()  # bayer, BGBG..(odd line), GRGR..(even line), 16-bit samples, big-endian
        BAYER_RGGB16LE = enum.auto()  # bayer, RGRG..(odd line), GBGB..(even line), 16-bit samples, little-endian
        BAYER_RGGB16BE = enum.auto()  # bayer, RGRG..(odd line), GBGB..(even line), 16-bit samples, big-endian
        BAYER_GBRG16LE = enum.auto()  # bayer, GBGB..(odd line), RGRG..(even line), 16-bit samples, little-endian
        BAYER_GBRG16BE = enum.auto()  # bayer, GBGB..(odd line), RGRG..(even line), 16-bit samples, big-endian
        BAYER_GRBG16LE = enum.auto()  # bayer, GRGR..(odd line), BGBG..(even line), 16-bit samples, little-endian
        BAYER_GRBG16BE = enum.auto()  # bayer, GRGR..(odd line), BGBG..(even line), 16-bit samples, big-endian

        YUV440P10LE = enum.auto()  # planar YUV 4:4:0,20bpp, (1 Cr & Cb sample per 1x2 Y samples), little-endian
        YUV440P10BE = enum.auto()  # planar YUV 4:4:0,20bpp, (1 Cr & Cb sample per 1x2 Y samples), big-endian
        YUV440P12LE = enum.auto()  # planar YUV 4:4:0,24bpp, (1 Cr & Cb sample per 1x2 Y samples), little-endian
        YUV440P12BE = enum.auto()  # planar YUV 4:4:0,24bpp, (1 Cr & Cb sample per 1x2 Y samples), big-endian
        AYUV64LE = enum.auto()  # packed AYUV 4:4:4,64bpp (1 Cr & Cb sample per 1x1 Y & A samples), little-endian
        AYUV64BE = enum.auto()  # packed AYUV 4:4:4,64bpp (1 Cr & Cb sample per 1x1 Y & A samples), big-endian

        VIDEOTOOLBOX = enum.auto()  # hardware decoding through Videotoolbox

        P010LE = enum.auto()  # like NV12, with 10bpp per component, data in the high bits, zeros in the low bits, little-endian
        P010BE = enum.auto()  # like NV12, with 10bpp per component, data in the high bits, zeros in the low bits, big-endian

        GBRAP12BE = enum.auto()  # planar GBR 4:4:4:4 48bpp, big-endian
        GBRAP12LE = enum.auto()  # planar GBR 4:4:4:4 48bpp, little-endian

        GBRAP10BE = enum.auto()  # planar GBR 4:4:4:4 40bpp, big-endian
        GBRAP10LE = enum.auto()  # planar GBR 4:4:4:4 40bpp, little-endian

        MEDIACODEC = enum.auto()  # hardware decoding through MediaCodec

        GRAY12BE = enum.auto()  # Y , 12bpp, big-endian
        GRAY12LE = enum.auto()  # Y , 12bpp, little-endian
        GRAY10BE = enum.auto()  # Y , 10bpp, big-endian
        GRAY10LE = enum.auto()  # Y , 10bpp, little-endian

        P016LE = enum.auto()  # like NV12, with 16bpp per component, little-endian
        P016BE = enum.auto()  # like NV12, with 16bpp per component, big-endian
        D3D11 = enum.auto()

        GRAY9BE = enum.auto()  # Y , 9bpp, big-endian
        GRAY9LE = enum.auto()  # Y , 9bpp, little-endian

        GBRPF32BE = enum.auto()  # IEEE-754 single precision planar GBR 4:4:4,     96bpp, big-endian
        GBRPF32LE = enum.auto()  # IEEE-754 single precision planar GBR 4:4:4,     96bpp, little-endian
        GBRAPF32BE = enum.auto()  # IEEE-754 single precision planar GBRA 4:4:4:4, 128bpp, big-endian
        GBRAPF32LE = enum.auto()  # IEEE-754 single precision planar GBRA 4:4:4:4, 128bpp, little-endian

        DRM_PRIME = enum.auto()
        OPENCL = enum.auto()

        GRAY14BE = enum.auto()  # Y , 14bpp, big-endian
        GRAY14LE = enum.auto()  # Y , 14bpp, little-endian

        GRAYF32BE = enum.auto()  # IEEE-754 single precision Y, 32bpp, big-endian
        GRAYF32LE = enum.auto()  # IEEE-754 single precision Y, 32bpp, little-endian

        YUVA422P12BE = enum.auto()  # planar YUV 4:2:2,24bpp, (1 Cr & Cb sample per 2x1 Y samples), 12b alpha, big-endian
        YUVA422P12LE = enum.auto()  # planar YUV 4:2:2,24bpp, (1 Cr & Cb sample per 2x1 Y samples), 12b alpha, little-endian
        YUVA444P12BE = enum.auto()  # planar YUV 4:4:4,36bpp, (1 Cr & Cb sample per 1x1 Y samples), 12b alpha, big-endian
        YUVA444P12LE = enum.auto()  # planar YUV 4:4:4,36bpp, (1 Cr & Cb sample per 1x1 Y samples), 12b alpha, little-endian

        NV24 = enum.auto()  # planar YUV 4:4:4, 24bpp, 1 plane for Y and 1 plane for the UV components, which are interleaved (first byte U and the following byte V)
        NV42 = enum.auto()  # as above, but U and V bytes are swapped

        VULKAN = enum.auto()

        Y210BE = enum.auto()  # packed YUV 4:2:2 like YUYV422, 20bpp, data in the high bits, big-endian
        Y210LE = enum.auto()  # packed YUV 4:2:2 like YUYV422, 20bpp, data in the high bits, little-endian

        X2RGB10LE = enum.auto()  # packed RGB 10:10:10, 30bpp, (msb)2X 10R 10G 10B(lsb), little-endian, X=unused/undefined
        X2RGB10BE = enum.auto()  # packed RGB 10:10:10, 30bpp, (msb)2X 10R 10G 10B(lsb), big-endian, X=unused/undefined
        X2BGR10LE = enum.auto()  # packed BGR 10:10:10, 30bpp, (msb)2X 10B 10G 10R(lsb), little-endian, X=unused/undefined
        X2BGR10BE = enum.auto()  # packed BGR 10:10:10, 30bpp, (msb)2X 10B 10G 10R(lsb), big-endian, X=unused/undefined

        P210BE = enum.auto()  # interleaved chroma YUV 4:2:2, 20bpp, data in the high bits, big-endian
        P210LE = enum.auto()  # interleaved chroma YUV 4:2:2, 20bpp, data in the high bits, little-endian

        P410BE = enum.auto()  # interleaved chroma YUV 4:4:4, 30bpp, data in the high bits, big-endian
        P410LE = enum.auto()  # interleaved chroma YUV 4:4:4, 30bpp, data in the high bits, little-endian

        P216BE = enum.auto()  # interleaved chroma YUV 4:2:2, 32bpp, big-endian
        P216LE = enum.auto()  # interleaved chroma YUV 4:2:2, 32bpp, little-endian

        P416BE = enum.auto()  # interleaved chroma YUV 4:4:4, 48bpp, big-endian
        P416LE = enum.auto()  # interleaved chroma YUV 4:4:4, 48bpp, little-endian

        VUYA = enum.auto()  # packed VUYA 4:4:4, 32bpp, VUYAVUYA...

        RGBAF16BE = enum.auto()  # IEEE-754 half precision packed RGBA 16:16:16:16, 64bpp, RGBARGBA..., big-endian
        RGBAF16LE = enum.auto()  # IEEE-754 half precision packed RGBA 16:16:16:16, 64bpp, RGBARGBA..., little-endian

        VUYX = enum.auto()  # packed VUYX 4:4:4, 32bpp, Variant of VUYA where alpha channel is left undefined

        P012LE = enum.auto()  # like NV12, with 12bpp per component, data in the high bits, zeros in the low bits, little-endian
        P012BE = enum.auto()  # like NV12, with 12bpp per component, data in the high bits, zeros in the low bits, big-endian

        Y212BE = enum.auto()  # packed YUV 4:2:2 like YUYV422, 24bpp, data in the high bits, zeros in the low bits, big-endian
        Y212LE = enum.auto()  # packed YUV 4:2:2 like YUYV422, 24bpp, data in the high bits, zeros in the low bits, little-endian

        XV30BE = enum.auto()  # packed XVYU 4:4:4, 32bpp, (msb)2X 10V 10Y 10U(lsb), big-endian, variant of Y410 where alpha channel is left undefined
        XV30LE = enum.auto()  # packed XVYU 4:4:4, 32bpp, (msb)2X 10V 10Y 10U(lsb), little-endian, variant of Y410 where alpha channel is left undefined

        XV36BE = enum.auto()  # packed XVYU 4:4:4, 48bpp, data in the high bits, zeros in the low bits, big-endian, variant of Y412 where alpha channel is left undefined
        XV36LE = enum.auto()  # packed XVYU 4:4:4, 48bpp, data in the high bits, zeros in the low bits, little-endian, variant of Y412 where alpha channel is left undefined

        RGBF32BE = enum.auto()  # IEEE-754 single precision packed RGB 32:32:32, 96bpp, RGBRGB..., big-endian
        RGBF32LE = enum.auto()  # IEEE-754 single precision packed RGB 32:32:32, 96bpp, RGBRGB..., little-endian

        RGBAF32BE = enum.auto()  # IEEE-754 single precision packed RGBA 32:32:32:32, 128bpp, RGBARGBA..., big-endian
        RGBAF32LE = enum.auto()  # IEEE-754 single precision packed RGBA 32:32:32:32, 128bpp, RGBARGBA..., little-endian

        P212BE = enum.auto()  # interleaved chroma YUV 4:2:2, 24bpp, data in the high bits, big-endian
        P212LE = enum.auto()  # interleaved chroma YUV 4:2:2, 24bpp, data in the high bits, little-endian

        P412BE = enum.auto()  # interleaved chroma YUV 4:4:4, 36bpp, data in the high bits, big-endian
        P412LE = enum.auto()  # interleaved chroma YUV 4:4:4, 36bpp, data in the high bits, little-endian

        GBRAP14BE = enum.auto()  # planar GBR 4:4:4:4 56bpp, big-endian
        GBRAP14LE = enum.auto()  # planar GBR 4:4:4:4 56bpp, little-endian

        D3D12 = enum.auto()

        NB = enum.auto()  # number of pixel formats, DO NOT USE THIS if you want to link with shared libav* because the number of formats might differ between versions


class EnumSampleFormat(clib.c_intenum):

    class _enum_(enum.IntEnum):
        NONE = -1
        U8 = enum.auto()  # unsigned 8 bits
        S16 = enum.auto()  # signed 16 bits
        S32 = enum.auto()  # signed 32 bits
        FLT = enum.auto()  # float
        DBL = enum.auto()  # double

        U8P = enum.auto()  # unsigned 8 bits, planar
        S16P = enum.auto()  # signed 16 bits, planar
        S32P = enum.auto()  # signed 32 bits, planar
        FLTP = enum.auto()  # float, planar
        DBLP = enum.auto()  # double, planar
        S64 = enum.auto()  # signed 64 bits
        S64P = enum.auto()  # signed 64 bits, planar

        NB = enum.auto()  # Number of sample formats. DO NOT USE if linking dynamically


class EnumChannelOrder(clib.c_intenum):

    class _enum_(enum.IntEnum):
        UNSPEC = 0
        NATIVE = enum.auto()
        CUSTOM = enum.auto()
        AMBISONIC = enum.auto()
        NB = enum.auto()


class EnumChannel(clib.c_intenum):

    class _enum_(enum.IntEnum):
        NONE = -1
        FRONT_LEFT = enum.auto()
        FRONT_RIGHT = enum.auto()
        FRONT_CENTER = enum.auto()
        LOW_FREQUENCY = enum.auto()
        BACK_LEFT = enum.auto()
        BACK_RIGHT = enum.auto()
        FRONT_LEFT_OF_CENTER = enum.auto()
        FRONT_RIGHT_OF_CENTER = enum.auto()
        BACK_CENTER = enum.auto()
        SIDE_LEFT = enum.auto()
        SIDE_RIGHT = enum.auto()
        TOP_CENTER = enum.auto()
        TOP_FRONT_LEFT = enum.auto()
        TOP_FRONT_CENTER = enum.auto()
        TOP_FRONT_RIGHT = enum.auto()
        TOP_BACK_LEFT = enum.auto()
        TOP_BACK_CENTER = enum.auto()
        TOP_BACK_RIGHT = enum.auto()
        STEREO_LEFT = 29
        STEREO_RIGHT = enum.auto()
        WIDE_LEFT = enum.auto()
        WIDE_RIGHT = enum.auto()
        SURROUND_DIRECT_LEFT = enum.auto()
        SURROUND_DIRECT_RIGHT = enum.auto()
        LOW_FREQUENCY_2 = enum.auto()
        TOP_SIDE_LEFT = enum.auto()
        TOP_SIDE_RIGHT = enum.auto()
        BOTTOM_FRONT_CENTER = enum.auto()
        BOTTOM_FRONT_LEFT = enum.auto()
        BOTTOM_FRONT_RIGHT = enum.auto()
        SIDE_SURROUND_LEFT = enum.auto()
        SIDE_SURROUND_RIGHT = enum.auto()
        TOP_SURROUND_LEFT = enum.auto()
        TOP_SURROUND_RIGHT = enum.auto()
        UNUSED = 0x200
        UNKNOWN = 0x300
        AMBISONIC_BASE = 0x400
        AMBISONIC_END = 0x7ff


class EnumOptionType(clib.c_intenum):

    class _enum_(enum.IntEnum):
        FLAGS = 1
        INT = enum.auto()
        INT64 = enum.auto()
        DOUBLE = enum.auto()
        FLOAT = enum.auto()
        STRING = enum.auto()
        RATIONAL = enum.auto()
        BINARY = enum.auto()
        DICT = enum.auto()
        UINT64 = enum.auto()
        CONST = enum.auto()
        IMAGE_SIZE = enum.auto()
        PIXEL_FMT = enum.auto()
        SAMPLE_FMT = enum.auto()
        VIDEO_RATE = enum.auto()
        DURATION = enum.auto()
        COLOR = enum.auto()
        BOOL = enum.auto()
        CHLAYOUT = enum.auto()
        UINT = enum.auto()
        FLAG_ARRAY = (1 << 16)


class EnumClassCategory(clib.c_intenum):

    class _enum_(enum.IntEnum):
        NA = 0
        INPUT = enum.auto()
        OUTPUT = enum.auto()
        MUXER = enum.auto()
        DEMUXER = enum.auto()
        ENCODER = enum.auto()
        DECODER = enum.auto()
        FILTER = enum.auto()
        BITSTREAM_FILTER = enum.auto()
        SWSCALER = enum.auto()
        SWRESAMPLER = enum.auto()
        DEVICE_VIDEO_OUTPUT = 40
        DEVICE_VIDEO_INPUT = enum.auto()
        DEVICE_AUDIO_OUTPUT = enum.auto()
        DEVICE_AUDIO_INPUT = enum.auto()
        DEVICE_OUTPUT = enum.auto()
        DEVICE_INPUT = enum.auto()
        NB = enum.auto()


class EnumFrameSideDataType(clib.c_intenum):

    class _enum_(enum.IntEnum):
        PANSCAN = 0
        A53_CC = enum.auto()
        STEREO3D = enum.auto()
        MATRIXENCODING = enum.auto()
        DOWNMIX_INFO = enum.auto()
        REPLAYGAIN = enum.auto()
        DISPLAYMATRIX = enum.auto()
        AFD = enum.auto()
        MOTION_VECTORS = enum.auto()
        SKIP_SAMPLES = enum.auto()
        AUDIO_SERVICE_TYPE = enum.auto()
        MASTERING_DISPLAY_METADATA = enum.auto()
        SPHERICAL = enum.auto()
        CONTENT_LIGHT_LEVEL = enum.auto()
        ICC_PROFILE = enum.auto()
        S12M_TIMECODE = enum.auto()
        DYNAMIC_HDR_PLUS = enum.auto()
        REGIONS_OF_INTEREST = enum.auto()
        VIDEO_ENC_PARAMS = enum.auto()
        SEI_UNREGISTERED = enum.auto()
        FILM_GRAIN_PARAMS = enum.auto()
        DETECTION_BBOXES = enum.auto()
        DOVI_RPU_BUFFER = enum.auto()
        DOVI_METADATA = enum.auto()
        DYNAMIC_HDR_VIVID = enum.auto()
        AMBIENT_VIEWING_ENVIRONMENT = enum.auto()
        VIDEO_HINT = enum.auto()
        LCEVC = enum.auto()
        VIEW_ID = enum.auto()


class EnumActiveFormatDescription(clib.c_intenum):

    class _enum_(enum.IntEnum):
        SAME = 8
        D_4_3 = 9
        D_16_9 = 10
        D_14_9 = 11
        D_4_3_SP_14_9 = 13
        D_16_9_SP_14_9 = 14
        D_SP_4_3 = 15


class EnumSideDataProps(clib.c_intenum):

    class _enum_(enum.IntEnum):
        GLOBAL = (1 << 0)
        MULTI = (1 << 1)


class EnumColorRange(clib.c_intenum):

    class _enum_(enum.IntEnum):
        UNSPECIFIED = 0
        MPEG = 1
        JPEG = 2
        NB = enum.auto()


class EnumColorPrimaries(clib.c_intenum):

    class _enum_(enum.IntEnum):
        AVCOL_PRI_RESERVED0 = 0
        AVCOL_PRI_BT709 = 1
        AVCOL_PRI_UNSPECIFIED = 2
        AVCOL_PRI_RESERVED = 3
        AVCOL_PRI_BT470M = 4
        AVCOL_PRI_BT470BG = 5
        AVCOL_PRI_SMPTE170M = 6
        AVCOL_PRI_SMPTE240M = 7
        AVCOL_PRI_FILM = 8
        AVCOL_PRI_BT2020 = 9
        AVCOL_PRI_SMPTE428 = 10
        AVCOL_PRI_SMPTE431 = 11
        AVCOL_PRI_SMPTE432 = 12
        AVCOL_PRI_EBU3213 = 22
        AVCOL_PRI_NB = enum.auto()


class EnumColorTransferCharacteristic(clib.c_intenum):

    class _enum_(enum.IntEnum):
        RESERVED0 = 0
        BT709 = 1
        UNSPECIFIED = 2
        RESERVED = 3
        GAMMA22 = 4
        GAMMA28 = 5
        SMPTE170M = 6
        SMPTE240M = 7
        LINEAR = 8
        LOG = 9
        LOG_SQRT = 10
        IEC61966_2_4 = 11
        BT1361_ECG = 12
        IEC61966_2_1 = 13
        BT2020_10 = 14
        BT2020_12 = 15
        SMPTE2084 = 16
        SMPTE428 = 17
        ARIB_STD_B67 = 18
        NB = enum.auto()


class EnumColorSpace(clib.c_intenum):

    class _enum_(enum.IntEnum):
        RGB = 0
        BT709 = 1
        UNSPECIFIED = 2
        RESERVED = 3
        FCC = 4
        BT470BG = 5
        SMPTE170M = 6
        SMPTE240M = 7
        YCGCO = 8
        BT2020_NCL = 9
        BT2020_CL = 10
        SMPTE2085 = 11
        CHROMA_DERIVED_NCL = 12
        CHROMA_DERIVED_CL = 13
        ICTCP = 14
        IPT_C2 = 15
        YCGCO_RE = 16
        YCGCO_RO = 17
        NB = enum.auto()


class EnumChromaLocation(clib.c_intenum):

    class _enum_(enum.IntEnum):
        UNSPECIFIED = 0
        LEFT = 1
        CENTER = 2
        TOPLEFT = 3
        TOP = 4
        BOTTOMLEFT = 5
        BOTTOM = 6
        NB = enum.auto()


class EnumPictureType(clib.c_intenum):

    class _enum_(enum.IntEnum):
        NONE = 0
        II = enum.auto()
        P = enum.auto()
        B = enum.auto()
        S = enum.auto()
        SI = enum.auto()
        SP = enum.auto()
        BI = enum.auto()


class EnumHWDeviceType(clib.c_intenum):

    class _enum_(enum.IntEnum):
        NONE = 0
        VDPAU = enum.auto()
        CUDA = enum.auto()
        VAAPI = enum.auto()
        DXVA2 = enum.auto()
        QSV = enum.auto()
        VIDEOTOOLBOX = enum.auto()
        D3D11VA = enum.auto()
        DRM = enum.auto()
        OPENCL = enum.auto()
        MEDIACODEC = enum.auto()
        VULKAN = enum.auto()
        D3D12VA = enum.auto()


class StructRational(clib.Structure):
    _fields_ = [
        ('num', clib.c_int),
        ('den', clib.c_int), ]


class StructChannelCustom(clib.Structure):
    _fields_ = [
        ('id', EnumChannel),
        ('name', clib.c_char * int(16)),
        ('opaque', clib.c_void_p), ]


class UnionChannel(ctypes.Union):
    _fields_ = [
        ('mask', clib.c_uint64),
        ('map', clib.POINTER(StructChannelCustom)),
    ]


class StructChannelLayout(clib.Structure):
    _fields_ = [
        ('order', EnumChannelOrder),
        ('nb_channels', clib.c_int),
        ('u', UnionChannel),
        ('opaque', clib.c_void_p), ]


class StructOptionArrayDef(clib.Structure):
    _fields_ = [
        ('def', clib.c_char_p),
        ('size_min', clib.c_uint),
        ('size_max', clib.c_uint),
        ('sep', clib.c_char)]


class UnionOption(ctypes.Union):
    _fields_ = [
        ('i64', clib.c_int64),
        ('dbl', clib.c_double),
        ('str', clib.c_char_p),
        ('q', StructRational),
        ('arr', clib.POINTER(StructOptionArrayDef))]


class StructOption(clib.Structure):
    _fields_ = [
        ('name', clib.c_char_p),
        ('help', clib.c_char_p),
        ('offset', clib.c_int),
        ('type', EnumOptionType),
        ('default_val', UnionOption),
        ('min', clib.c_double),
        ('max', clib.c_double),
        ('flags', clib.c_int),
        ('unit', clib.c_char_p)]


class StructOptionRange(clib.Structure):
    _fields_ = [
        ('str', clib.c_char_p),
        ('value_min', clib.c_double),
        ('value_max', clib.c_double),
        ('component_min', clib.c_double),
        ('component_max', clib.c_double),
        ('is_range', clib.c_int)]


class StructOptionRanges(clib.Structure):
    _fields_ = [
        ('range', clib.POINTER(clib.POINTER(StructOptionRange))),
        ('nb_ranges', clib.c_int),
        ('nb_components', clib.c_int),
    ]


class StructClass(clib.Structure):
    pass


StructClass._fields_ = [
    ('class_name', clib.c_char_p),
    ('item_name', ctypes.CFUNCTYPE(clib.c_char_p,
                                   clib.c_void_p)),
    ('option', clib.POINTER(StructOption)),
    ('version', clib.c_int),
    ('log_level_offset_offset', clib.c_int),
    ('parent_log_context_offset', clib.c_int),
    ('category', EnumClassCategory),
    ('get_category', ctypes.CFUNCTYPE(EnumClassCategory,
                                      clib.c_void_p)),
    ('query_ranges', ctypes.CFUNCTYPE(clib.c_int,
                                      clib.POINTER(clib.POINTER(StructOptionRanges)),
                                      clib.c_void_p,
                                      clib.c_char_p,
                                      clib.c_int)),
    ('child_next', ctypes.CFUNCTYPE(clib.POINTER(clib.c_ubyte),
                                    clib.c_void_p,
                                    clib.c_void_p)),
    ('child_class_iterate', ctypes.CFUNCTYPE(clib.POINTER(StructClass),
                                             clib.POINTER(clib.c_void_p))),
]


class StructBufferRef(clib.Structure):
    _fields_ = [
        ('buffer', clib.c_void_p),
        ('data', clib.POINTER(clib.c_uint8)),
        ('size', clib.c_size_t),
    ]


class StructFrameSideData(clib.Structure):
    _fields_ = [
        ('type', EnumFrameSideDataType),
        ('data', clib.POINTER(clib.c_uint8)),
        ('size', clib.c_size_t),
        ('metadata', clib.c_void_p),
        ('buf', clib.POINTER(StructBufferRef))]


class StructFrame(clib.Structure):
    _fields_ = [
        ('data', clib.POINTER(clib.c_uint8) * int(8)),
        ('linesize', clib.c_int * int(8)),
        ('extended_data', clib.POINTER(clib.POINTER(clib.c_uint8))),
        ('width', clib.c_int),
        ('height', clib.c_int),
        ('nb_samples', clib.c_int),
        ('format', clib.c_int),
        ('key_frame', clib.c_int),
        ('pict_type', EnumPictureType),
        ('sample_aspect_ratio', StructRational),
        ('pts', clib.c_int64),
        ('pkt_dts', clib.c_int64),
        ('time_base', StructRational),
        ('quality', clib.c_int),
        ('opaque', clib.POINTER(None)),
        ('repeat_pict', clib.c_int),
        ('interlaced_frame', clib.c_int),
        ('top_field_first', clib.c_int),
        ('palette_has_changed', clib.c_int),
        ('sample_rate', clib.c_int),
        ('buf', clib.POINTER(StructBufferRef) * int(8)),
        ('extended_buf', clib.POINTER(clib.POINTER(StructBufferRef))),
        ('nb_extended_buf', clib.c_int),
        ('side_data', clib.POINTER(clib.POINTER(StructFrameSideData))),
        ('nb_side_data', clib.c_int),
        ('flags', clib.c_int),
        ('color_range', EnumColorRange),
        ('color_primaries', EnumColorPrimaries),
        ('color_trc', EnumColorTransferCharacteristic),
        ('colorspace', EnumColorSpace),
        ('chroma_location', EnumChromaLocation),
        ('best_effort_timestamp', clib.c_int64),
        ('pkt_pos', clib.c_int64),
        ('metadata', clib.c_void_p),
        ('decode_error_flags', clib.c_int),
        ('pkt_size', clib.c_int),
        ('hw_frames_ctx', clib.POINTER(StructBufferRef)),
        ('opaque_ref', clib.POINTER(StructBufferRef)),
        ('crop_top', clib.c_size_t),
        ('crop_bottom', clib.c_size_t),
        ('crop_left', clib.c_size_t),
        ('crop_right', clib.c_size_t),
        ('private_ref', clib.POINTER(StructBufferRef)),
        ('ch_layout', StructChannelLayout),
        ('duration', clib.c_int64)]


class StructBPrint(clib.Structure):
    _fields_ = [
        ('str', clib.c_char_p),
        ('len', clib.c_uint),
        ('size', clib.c_uint),
        ('size_max', clib.c_uint),
        ('reserved_internal_buffer', clib.c_char * int(1)),
    ]


class Util(clib.Lib):
    _name_ = "avutil"

    @clib.Lib.Signature("av_log_get_level")
    def get_log_level(self):
        return clib.c_int

    @clib.Lib.Signature("av_log_set_level", clib.c_int)
    def set_log_level(self, level):
        return

    @clib.Lib.Signature("av_log_set_callback", ctypes.CFUNCTYPE(clib.c_void_p,
                                                                 clib.c_void_p,
                                                                 clib.c_int,
                                                                 clib.c_char_p,
                                                                 clib.c_void_p))
    def set_log_callback(self, callback):
        return

    @clib.Lib.Signature("av_log_default_callback", clib.c_void_p,
                                                    clib.c_int,
                                                    clib.c_char_p,
                                                    clib.c_void_p)
    def log_default_callback(self, ptr, level, fmt, vl):
        return clib.c_void_p

    @clib.Lib.Signature("av_log", clib.c_void_p, clib.c_int, clib.c_char_p)
    def log(self, ctx, level, fmt, *args):
        return

    @clib.Lib.Signature("av_vbprintf", clib.POINTER(StructBPrint), clib.c_char_p)
    def vbprintf(self, buf, fmt, *args):
        return
