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
from ctypes import util

from v4l2codecs import log


class CIntEnum(ctypes.c_int):
    _enum_ = None

    @property
    def enum(self):
        return self._enum_(self)


class AvMediaType(CIntEnum):
    class _enum_(enum.IntEnum):
        AVMEDIA_TYPE_UNKNOWN = -1 = enum.auto()  # Usually treated as AVMEDIA_TYPE_DATA
        AVMEDIA_TYPE_VIDEO = enum.auto()
        AVMEDIA_TYPE_AUDIO = enum.auto()
        AVMEDIA_TYPE_DATA = enum.auto() = enum.auto()  # Opaque data information usually continuous
        AVMEDIA_TYPE_SUBTITLE = enum.auto()
        AVMEDIA_TYPE_ATTACHMENT = enum.auto() = enum.auto()  # Opaque data information usually sparse
        AVMEDIA_TYPE_NB = enum.auto()


class AVPixelFormat(CIntEnum):
    class _enum_(enum.IntEnum):
        AV_PIX_FMT_NONE = -1
        AV_PIX_FMT_YUV420P = enum.auto()  # planar YUV 4:2:0, 12bpp, (1 Cr & Cb sample per 2x2 Y samples)
        AV_PIX_FMT_YUYV422 = enum.auto()  # packed YUV 4:2:2, 16bpp, Y0 Cb Y1 Cr
        AV_PIX_FMT_RGB24 = enum.auto()  # packed RGB 8:8:8, 24bpp, RGBRGB...
        AV_PIX_FMT_BGR24 = enum.auto()  # packed RGB 8:8:8, 24bpp, BGRBGR...
        AV_PIX_FMT_YUV422P = enum.auto()  # planar YUV 4:2:2, 16bpp, (1 Cr & Cb sample per 2x1 Y samples)
        AV_PIX_FMT_YUV444P = enum.auto()  # planar YUV 4:4:4, 24bpp, (1 Cr & Cb sample per 1x1 Y samples)
        AV_PIX_FMT_YUV410P = enum.auto()  # planar YUV 4:1:0,  9bpp, (1 Cr & Cb sample per 4x4 Y samples)
        AV_PIX_FMT_YUV411P = enum.auto()  # planar YUV 4:1:1, 12bpp, (1 Cr & Cb sample per 4x1 Y samples)
        AV_PIX_FMT_GRAY8 = enum.auto()  # Y 8bpp
        AV_PIX_FMT_MONOWHITE = enum.auto()  # Y 1bpp, 0 is white, 1 is black, in each byte pixels are ordered from the msb to the lsb
        AV_PIX_FMT_MONOBLACK = enum.auto()  # Y 1bpp, 0 is black, 1 is white, in each byte pixels are ordered from the msb to the lsb
        AV_PIX_FMT_PAL8 = enum.auto()  # 8 bits with AV_PIX_FMT_RGB32 palette
        AV_PIX_FMT_YUVJ420P = enum.auto()  # planar YUV 4:2:0, 12bpp, full scale (JPEG), deprecated in favor of AV_PIX_FMT_YUV420P and setting color_range
        AV_PIX_FMT_YUVJ422P = enum.auto()  # planar YUV 4:2:2, 16bpp, full scale (JPEG), deprecated in favor of AV_PIX_FMT_YUV422P and setting color_range
        AV_PIX_FMT_YUVJ444P = enum.auto()  # planar YUV 4:4:4, 24bpp, full scale (JPEG), deprecated in favor of AV_PIX_FMT_YUV444P and setting color_range
        AV_PIX_FMT_UYVY422 = enum.auto()  # packed YUV 4:2:2, 16bpp, Cb Y0 Cr Y1
        AV_PIX_FMT_UYYVYY411 = enum.auto()  # packed YUV 4:1:1, 12bpp, Cb Y0 Y1 Cr Y2 Y3
        AV_PIX_FMT_BGR8 = enum.auto()  # packed RGB 3:3:2,  8bpp, (msb)2B 3G 3R(lsb)
        AV_PIX_FMT_BGR4 = enum.auto()  # packed RGB 1:2:1 bitstream,  4bpp, (msb)1B 2G 1R(lsb), a byte contains two pixels, the first pixel in the byte is the one composed by the 4 msb bits
        AV_PIX_FMT_BGR4_BYTE = enum.auto()  # packed RGB 1:2:1,  8bpp, (msb)1B 2G 1R(lsb)
        AV_PIX_FMT_RGB8 = enum.auto()  # packed RGB 3:3:2,  8bpp, (msb)3R 3G 2B(lsb)
        AV_PIX_FMT_RGB4 = enum.auto()  # packed RGB 1:2:1 bitstream,  4bpp, (msb)1R 2G 1B(lsb), a byte contains two pixels, the first pixel in the byte is the one composed by the 4 msb bits
        AV_PIX_FMT_RGB4_BYTE = enum.auto()  # packed RGB 1:2:1,  8bpp, (msb)1R 2G 1B(lsb)
        AV_PIX_FMT_NV12 = enum.auto()  # planar YUV 4:2:0, 12bpp, 1 plane for Y and 1 plane for the UV components, which are interleaved (first byte U and the following byte V)
        AV_PIX_FMT_NV21 = enum.auto()  # as above, but U and V bytes are swapped

        AV_PIX_FMT_ARGB = enum.auto()  # packed ARGB 8:8:8:8, 32bpp, ARGBARGB...
        AV_PIX_FMT_RGBA = enum.auto()  # packed RGBA 8:8:8:8, 32bpp, RGBARGBA...
        AV_PIX_FMT_ABGR = enum.auto()  # packed ABGR 8:8:8:8, 32bpp, ABGRABGR...
        AV_PIX_FMT_BGRA = enum.auto()  # packed BGRA 8:8:8:8, 32bpp, BGRABGRA...

        AV_PIX_FMT_GRAY16BE = enum.auto()  # Y , 16bpp, big-endian
        AV_PIX_FMT_GRAY16LE = enum.auto()  # Y , 16bpp, little-endian
        AV_PIX_FMT_YUV440P = enum.auto()  # planar YUV 4:4:0 (1 Cr & Cb sample per 1x2 Y samples)
        AV_PIX_FMT_YUVJ440P = enum.auto()  # planar YUV 4:4:0 full scale (JPEG), deprecated in favor of AV_PIX_FMT_YUV440P and setting color_range
        AV_PIX_FMT_YUVA420P = enum.auto()  # planar YUV 4:2:0, 20bpp, (1 Cr & Cb sample per 2x2 Y & A samples)
        AV_PIX_FMT_RGB48BE = enum.auto()  # packed RGB 16:16:16, 48bpp, 16R, 16G, 16B, the 2-byte value for each R/G/B component is stored as big-endian
        AV_PIX_FMT_RGB48LE = enum.auto()  # packed RGB 16:16:16, 48bpp, 16R, 16G, 16B, the 2-byte value for each R/G/B component is stored as little-endian

        AV_PIX_FMT_RGB565BE = enum.auto()  # packed RGB 5:6:5, 16bpp, (msb)   5R 6G 5B(lsb), big-endian
        AV_PIX_FMT_RGB565LE = enum.auto()  # packed RGB 5:6:5, 16bpp, (msb)   5R 6G 5B(lsb), little-endian
        AV_PIX_FMT_RGB555BE = enum.auto()  # packed RGB 5:5:5, 16bpp, (msb)1X 5R 5G 5B(lsb), big-endian   , X=unused/undefined
        AV_PIX_FMT_RGB555LE = enum.auto()  # packed RGB 5:5:5, 16bpp, (msb)1X 5R 5G 5B(lsb), little-endian, X=unused/undefined

        AV_PIX_FMT_BGR565BE = enum.auto()  # packed BGR 5:6:5, 16bpp, (msb)   5B 6G 5R(lsb), big-endian
        AV_PIX_FMT_BGR565LE = enum.auto()  # packed BGR 5:6:5, 16bpp, (msb)   5B 6G 5R(lsb), little-endian
        AV_PIX_FMT_BGR555BE = enum.auto()  # packed BGR 5:5:5, 16bpp, (msb)1X 5B 5G 5R(lsb), big-endian   , X=unused/undefined
        AV_PIX_FMT_BGR555LE = enum.auto()  # packed BGR 5:5:5, 16bpp, (msb)1X 5B 5G 5R(lsb), little-endian, X=unused/undefined
        AV_PIX_FMT_VAAPI = enum.auto()

        AV_PIX_FMT_YUV420P16LE = enum.auto()  # planar YUV 4:2:0, 24bpp, (1 Cr & Cb sample per 2x2 Y samples), little-endian
        AV_PIX_FMT_YUV420P16BE = enum.auto()  # planar YUV 4:2:0, 24bpp, (1 Cr & Cb sample per 2x2 Y samples), big-endian
        AV_PIX_FMT_YUV422P16LE = enum.auto()  # planar YUV 4:2:2, 32bpp, (1 Cr & Cb sample per 2x1 Y samples), little-endian
        AV_PIX_FMT_YUV422P16BE = enum.auto()  # planar YUV 4:2:2, 32bpp, (1 Cr & Cb sample per 2x1 Y samples), big-endian
        AV_PIX_FMT_YUV444P16LE = enum.auto()  # planar YUV 4:4:4, 48bpp, (1 Cr & Cb sample per 1x1 Y samples), little-endian
        AV_PIX_FMT_YUV444P16BE = enum.auto()  # planar YUV 4:4:4, 48bpp, (1 Cr & Cb sample per 1x1 Y samples), big-endian
        AV_PIX_FMT_DXVA2_VLD = enum.auto()  # HW decoding through DXVA2, Picture.data[3] contains a LPDIRECT3DSURFACE9 pointer

        AV_PIX_FMT_RGB444LE = enum.auto()  # packed RGB 4:4:4, 16bpp, (msb)4X 4R 4G 4B(lsb), little-endian, X=unused/undefined
        AV_PIX_FMT_RGB444BE = enum.auto()  # packed RGB 4:4:4, 16bpp, (msb)4X 4R 4G 4B(lsb), big-endian,    X=unused/undefined
        AV_PIX_FMT_BGR444LE = enum.auto()  # packed BGR 4:4:4, 16bpp, (msb)4X 4B 4G 4R(lsb), little-endian, X=unused/undefined
        AV_PIX_FMT_BGR444BE = enum.auto()  # packed BGR 4:4:4, 16bpp, (msb)4X 4B 4G 4R(lsb), big-endian,    X=unused/undefined
        AV_PIX_FMT_YA8 = enum.auto()  # 8 bits gray, 8 bits alpha

        AV_PIX_FMT_BGR48BE = enum.auto()  # packed RGB 16:16:16, 48bpp, 16B, 16G, 16R, the 2-byte value for each R/G/B component is stored as big-endian
        AV_PIX_FMT_BGR48LE = enum.auto()  # packed RGB 16:16:16, 48bpp, 16B, 16G, 16R, the 2-byte value for each R/G/B component is stored as little-endian

        AV_PIX_FMT_YUV420P9BE = enum.auto()  # planar YUV 4:2:0, 13.5bpp, (1 Cr & Cb sample per 2x2 Y samples), big-endian
        AV_PIX_FMT_YUV420P9LE = enum.auto()  # planar YUV 4:2:0, 13.5bpp, (1 Cr & Cb sample per 2x2 Y samples), little-endian
        AV_PIX_FMT_YUV420P10BE = enum.auto()  # planar YUV 4:2:0, 15bpp, (1 Cr & Cb sample per 2x2 Y samples), big-endian
        AV_PIX_FMT_YUV420P10LE = enum.auto()  # planar YUV 4:2:0, 15bpp, (1 Cr & Cb sample per 2x2 Y samples), little-endian
        AV_PIX_FMT_YUV422P10BE = enum.auto()  # planar YUV 4:2:2, 20bpp, (1 Cr & Cb sample per 2x1 Y samples), big-endian
        AV_PIX_FMT_YUV422P10LE = enum.auto()  # planar YUV 4:2:2, 20bpp, (1 Cr & Cb sample per 2x1 Y samples), little-endian
        AV_PIX_FMT_YUV444P9BE = enum.auto()  # planar YUV 4:4:4, 27bpp, (1 Cr & Cb sample per 1x1 Y samples), big-endian
        AV_PIX_FMT_YUV444P9LE = enum.auto()  # planar YUV 4:4:4, 27bpp, (1 Cr & Cb sample per 1x1 Y samples), little-endian
        AV_PIX_FMT_YUV444P10BE = enum.auto()  # planar YUV 4:4:4, 30bpp, (1 Cr & Cb sample per 1x1 Y samples), big-endian
        AV_PIX_FMT_YUV444P10LE = enum.auto()  # planar YUV 4:4:4, 30bpp, (1 Cr & Cb sample per 1x1 Y samples), little-endian
        AV_PIX_FMT_YUV422P9BE = enum.auto()  # planar YUV 4:2:2, 18bpp, (1 Cr & Cb sample per 2x1 Y samples), big-endian
        AV_PIX_FMT_YUV422P9LE = enum.auto()  # planar YUV 4:2:2, 18bpp, (1 Cr & Cb sample per 2x1 Y samples), little-endian
        AV_PIX_FMT_GBRP = enum.auto()  # planar GBR 4:4:4 24bpp
        AV_PIX_FMT_GBRP9BE = enum.auto()  # planar GBR 4:4:4 27bpp, big-endian
        AV_PIX_FMT_GBRP9LE = enum.auto()  # planar GBR 4:4:4 27bpp, little-endian
        AV_PIX_FMT_GBRP10BE = enum.auto()  # planar GBR 4:4:4 30bpp, big-endian
        AV_PIX_FMT_GBRP10LE = enum.auto()  # planar GBR 4:4:4 30bpp, little-endian
        AV_PIX_FMT_GBRP16BE = enum.auto()  # planar GBR 4:4:4 48bpp, big-endian
        AV_PIX_FMT_GBRP16LE = enum.auto()  # planar GBR 4:4:4 48bpp, little-endian
        AV_PIX_FMT_YUVA422P = enum.auto()  # planar YUV 4:2:2 24bpp, (1 Cr & Cb sample per 2x1 Y & A samples)
        AV_PIX_FMT_YUVA444P = enum.auto()  # planar YUV 4:4:4 32bpp, (1 Cr & Cb sample per 1x1 Y & A samples)
        AV_PIX_FMT_YUVA420P9BE = enum.auto()  # planar YUV 4:2:0 22.5bpp, (1 Cr & Cb sample per 2x2 Y & A samples), big-endian
        AV_PIX_FMT_YUVA420P9LE = enum.auto()  # planar YUV 4:2:0 22.5bpp, (1 Cr & Cb sample per 2x2 Y & A samples), little-endian
        AV_PIX_FMT_YUVA422P9BE = enum.auto()  # planar YUV 4:2:2 27bpp, (1 Cr & Cb sample per 2x1 Y & A samples), big-endian
        AV_PIX_FMT_YUVA422P9LE = enum.auto()  # planar YUV 4:2:2 27bpp, (1 Cr & Cb sample per 2x1 Y & A samples), little-endian
        AV_PIX_FMT_YUVA444P9BE = enum.auto()  # planar YUV 4:4:4 36bpp, (1 Cr & Cb sample per 1x1 Y & A samples), big-endian
        AV_PIX_FMT_YUVA444P9LE = enum.auto()  # planar YUV 4:4:4 36bpp, (1 Cr & Cb sample per 1x1 Y & A samples), little-endian
        AV_PIX_FMT_YUVA420P10BE = enum.auto()  # planar YUV 4:2:0 25bpp, (1 Cr & Cb sample per 2x2 Y & A samples, big-endian)
        AV_PIX_FMT_YUVA420P10LE = enum.auto()  # planar YUV 4:2:0 25bpp, (1 Cr & Cb sample per 2x2 Y & A samples, little-endian)
        AV_PIX_FMT_YUVA422P10BE = enum.auto()  # planar YUV 4:2:2 30bpp, (1 Cr & Cb sample per 2x1 Y & A samples, big-endian)
        AV_PIX_FMT_YUVA422P10LE = enum.auto()  # planar YUV 4:2:2 30bpp, (1 Cr & Cb sample per 2x1 Y & A samples, little-endian)
        AV_PIX_FMT_YUVA444P10BE = enum.auto()  # planar YUV 4:4:4 40bpp, (1 Cr & Cb sample per 1x1 Y & A samples, big-endian)
        AV_PIX_FMT_YUVA444P10LE = enum.auto()  # planar YUV 4:4:4 40bpp, (1 Cr & Cb sample per 1x1 Y & A samples, little-endian)
        AV_PIX_FMT_YUVA420P16BE = enum.auto()  # planar YUV 4:2:0 40bpp, (1 Cr & Cb sample per 2x2 Y & A samples, big-endian)
        AV_PIX_FMT_YUVA420P16LE = enum.auto()  # planar YUV 4:2:0 40bpp, (1 Cr & Cb sample per 2x2 Y & A samples, little-endian)
        AV_PIX_FMT_YUVA422P16BE = enum.auto()  # planar YUV 4:2:2 48bpp, (1 Cr & Cb sample per 2x1 Y & A samples, big-endian)
        AV_PIX_FMT_YUVA422P16LE = enum.auto()  # planar YUV 4:2:2 48bpp, (1 Cr & Cb sample per 2x1 Y & A samples, little-endian)
        AV_PIX_FMT_YUVA444P16BE = enum.auto()  # planar YUV 4:4:4 64bpp, (1 Cr & Cb sample per 1x1 Y & A samples, big-endian)
        AV_PIX_FMT_YUVA444P16LE = enum.auto()  # planar YUV 4:4:4 64bpp, (1 Cr & Cb sample per 1x1 Y & A samples, little-endian)

        AV_PIX_FMT_VDPAU = enum.auto()  # HW acceleration through VDPAU, Picture.data[3] contains a VdpVideoSurface

        AV_PIX_FMT_XYZ12LE = enum.auto()  # packed XYZ 4:4:4, 36 bpp, (msb) 12X, 12Y, 12Z (lsb), the 2-byte value for each X/Y/Z is stored as little-endian, the 4 lower bits are set to 0
        AV_PIX_FMT_XYZ12BE = enum.auto()  # packed XYZ 4:4:4, 36 bpp, (msb) 12X, 12Y, 12Z (lsb), the 2-byte value for each X/Y/Z is stored as big-endian, the 4 lower bits are set to 0
        AV_PIX_FMT_NV16 = enum.auto()  # interleaved chroma YUV 4:2:2, 16bpp, (1 Cr & Cb sample per 2x1 Y samples)
        AV_PIX_FMT_NV20LE = enum.auto()  # interleaved chroma YUV 4:2:2, 20bpp, (1 Cr & Cb sample per 2x1 Y samples), little-endian
        AV_PIX_FMT_NV20BE = enum.auto()  # interleaved chroma YUV 4:2:2, 20bpp, (1 Cr & Cb sample per 2x1 Y samples), big-endian

        AV_PIX_FMT_RGBA64BE = enum.auto()  # packed RGBA 16:16:16:16, 64bpp, 16R, 16G, 16B, 16A, the 2-byte value for each R/G/B/A component is stored as big-endian
        AV_PIX_FMT_RGBA64LE = enum.auto()  # packed RGBA 16:16:16:16, 64bpp, 16R, 16G, 16B, 16A, the 2-byte value for each R/G/B/A component is stored as little-endian
        AV_PIX_FMT_BGRA64BE = enum.auto()  # packed RGBA 16:16:16:16, 64bpp, 16B, 16G, 16R, 16A, the 2-byte value for each R/G/B/A component is stored as big-endian
        AV_PIX_FMT_BGRA64LE = enum.auto()  # packed RGBA 16:16:16:16, 64bpp, 16B, 16G, 16R, 16A, the 2-byte value for each R/G/B/A component is stored as little-endian

        AV_PIX_FMT_YVYU422 = enum.auto()  # packed YUV 4:2:2, 16bpp, Y0 Cr Y1 Cb

        AV_PIX_FMT_YA16BE = enum.auto()  # 16 bits gray, 16 bits alpha (big-endian)
        AV_PIX_FMT_YA16LE = enum.auto()  # 16 bits gray, 16 bits alpha (little-endian)

        AV_PIX_FMT_GBRAP = enum.auto()  # planar GBRA 4:4:4:4 32bpp
        AV_PIX_FMT_GBRAP16BE = enum.auto()  # planar GBRA 4:4:4:4 64bpp, big-endian
        AV_PIX_FMT_GBRAP16LE = enum.auto()  # planar GBRA 4:4:4:4 64bpp, little-endian
        AV_PIX_FMT_QSV = enum.auto()
        AV_PIX_FMT_MMAL = enum.auto()

        AV_PIX_FMT_D3D11VA_VLD = enum.auto()  # HW decoding through Direct3D11 via old API, Picture.data[3] contains a ID3D11VideoDecoderOutputView pointer
        AV_PIX_FMT_CUDA = enum.auto()

        AV_PIX_FMT_0RGB = enum.auto()  # packed RGB 8:8:8, 32bpp, XRGBXRGB...   X=unused/undefined
        AV_PIX_FMT_RGB0 = enum.auto()  # packed RGB 8:8:8, 32bpp, RGBXRGBX...   X=unused/undefined
        AV_PIX_FMT_0BGR = enum.auto()  # packed BGR 8:8:8, 32bpp, XBGRXBGR...   X=unused/undefined
        AV_PIX_FMT_BGR0 = enum.auto()  # packed BGR 8:8:8, 32bpp, BGRXBGRX...   X=unused/undefined

        AV_PIX_FMT_YUV420P12BE = enum.auto()  # planar YUV 4:2:0,18bpp, (1 Cr & Cb sample per 2x2 Y samples), big-endian
        AV_PIX_FMT_YUV420P12LE = enum.auto()  # planar YUV 4:2:0,18bpp, (1 Cr & Cb sample per 2x2 Y samples), little-endian
        AV_PIX_FMT_YUV420P14BE = enum.auto()  # planar YUV 4:2:0,21bpp, (1 Cr & Cb sample per 2x2 Y samples), big-endian
        AV_PIX_FMT_YUV420P14LE = enum.auto()  # planar YUV 4:2:0,21bpp, (1 Cr & Cb sample per 2x2 Y samples), little-endian
        AV_PIX_FMT_YUV422P12BE = enum.auto()  # planar YUV 4:2:2,24bpp, (1 Cr & Cb sample per 2x1 Y samples), big-endian
        AV_PIX_FMT_YUV422P12LE = enum.auto()  # planar YUV 4:2:2,24bpp, (1 Cr & Cb sample per 2x1 Y samples), little-endian
        AV_PIX_FMT_YUV422P14BE = enum.auto()  # planar YUV 4:2:2,28bpp, (1 Cr & Cb sample per 2x1 Y samples), big-endian
        AV_PIX_FMT_YUV422P14LE = enum.auto()  # planar YUV 4:2:2,28bpp, (1 Cr & Cb sample per 2x1 Y samples), little-endian
        AV_PIX_FMT_YUV444P12BE = enum.auto()  # planar YUV 4:4:4,36bpp, (1 Cr & Cb sample per 1x1 Y samples), big-endian
        AV_PIX_FMT_YUV444P12LE = enum.auto()  # planar YUV 4:4:4,36bpp, (1 Cr & Cb sample per 1x1 Y samples), little-endian
        AV_PIX_FMT_YUV444P14BE = enum.auto()  # planar YUV 4:4:4,42bpp, (1 Cr & Cb sample per 1x1 Y samples), big-endian
        AV_PIX_FMT_YUV444P14LE = enum.auto()  # planar YUV 4:4:4,42bpp, (1 Cr & Cb sample per 1x1 Y samples), little-endian
        AV_PIX_FMT_GBRP12BE = enum.auto()  # planar GBR 4:4:4 36bpp, big-endian
        AV_PIX_FMT_GBRP12LE = enum.auto()  # planar GBR 4:4:4 36bpp, little-endian
        AV_PIX_FMT_GBRP14BE = enum.auto()  # planar GBR 4:4:4 42bpp, big-endian
        AV_PIX_FMT_GBRP14LE = enum.auto()  # planar GBR 4:4:4 42bpp, little-endian
        AV_PIX_FMT_YUVJ411P = enum.auto()  # planar YUV 4:1:1, 12bpp, (1 Cr & Cb sample per 4x1 Y samples) full scale (JPEG), deprecated in favor of AV_PIX_FMT_YUV411P and setting color_range

        AV_PIX_FMT_BAYER_BGGR8 = enum.auto()  # bayer, BGBG..(odd line), GRGR..(even line), 8-bit samples
        AV_PIX_FMT_BAYER_RGGB8 = enum.auto()  # bayer, RGRG..(odd line), GBGB..(even line), 8-bit samples
        AV_PIX_FMT_BAYER_GBRG8 = enum.auto()  # bayer, GBGB..(odd line), RGRG..(even line), 8-bit samples
        AV_PIX_FMT_BAYER_GRBG8 = enum.auto()  # bayer, GRGR..(odd line), BGBG..(even line), 8-bit samples
        AV_PIX_FMT_BAYER_BGGR16LE = enum.auto()  # bayer, BGBG..(odd line), GRGR..(even line), 16-bit samples, little-endian
        AV_PIX_FMT_BAYER_BGGR16BE = enum.auto()  # bayer, BGBG..(odd line), GRGR..(even line), 16-bit samples, big-endian
        AV_PIX_FMT_BAYER_RGGB16LE = enum.auto()  # bayer, RGRG..(odd line), GBGB..(even line), 16-bit samples, little-endian
        AV_PIX_FMT_BAYER_RGGB16BE = enum.auto()  # bayer, RGRG..(odd line), GBGB..(even line), 16-bit samples, big-endian
        AV_PIX_FMT_BAYER_GBRG16LE = enum.auto()  # bayer, GBGB..(odd line), RGRG..(even line), 16-bit samples, little-endian
        AV_PIX_FMT_BAYER_GBRG16BE = enum.auto()  # bayer, GBGB..(odd line), RGRG..(even line), 16-bit samples, big-endian
        AV_PIX_FMT_BAYER_GRBG16LE = enum.auto()  # bayer, GRGR..(odd line), BGBG..(even line), 16-bit samples, little-endian
        AV_PIX_FMT_BAYER_GRBG16BE = enum.auto()  # bayer, GRGR..(odd line), BGBG..(even line), 16-bit samples, big-endian

        AV_PIX_FMT_YUV440P10LE = enum.auto()  # planar YUV 4:4:0,20bpp, (1 Cr & Cb sample per 1x2 Y samples), little-endian
        AV_PIX_FMT_YUV440P10BE = enum.auto()  # planar YUV 4:4:0,20bpp, (1 Cr & Cb sample per 1x2 Y samples), big-endian
        AV_PIX_FMT_YUV440P12LE = enum.auto()  # planar YUV 4:4:0,24bpp, (1 Cr & Cb sample per 1x2 Y samples), little-endian
        AV_PIX_FMT_YUV440P12BE = enum.auto()  # planar YUV 4:4:0,24bpp, (1 Cr & Cb sample per 1x2 Y samples), big-endian
        AV_PIX_FMT_AYUV64LE = enum.auto()  # packed AYUV 4:4:4,64bpp (1 Cr & Cb sample per 1x1 Y & A samples), little-endian
        AV_PIX_FMT_AYUV64BE = enum.auto()  # packed AYUV 4:4:4,64bpp (1 Cr & Cb sample per 1x1 Y & A samples), big-endian

        AV_PIX_FMT_VIDEOTOOLBOX = enum.auto()  # hardware decoding through Videotoolbox

        AV_PIX_FMT_P010LE = enum.auto()  # like NV12, with 10bpp per component, data in the high bits, zeros in the low bits, little-endian
        AV_PIX_FMT_P010BE = enum.auto()  # like NV12, with 10bpp per component, data in the high bits, zeros in the low bits, big-endian

        AV_PIX_FMT_GBRAP12BE = enum.auto()  # planar GBR 4:4:4:4 48bpp, big-endian
        AV_PIX_FMT_GBRAP12LE = enum.auto()  # planar GBR 4:4:4:4 48bpp, little-endian

        AV_PIX_FMT_GBRAP10BE = enum.auto()  # planar GBR 4:4:4:4 40bpp, big-endian
        AV_PIX_FMT_GBRAP10LE = enum.auto()  # planar GBR 4:4:4:4 40bpp, little-endian

        AV_PIX_FMT_MEDIACODEC = enum.auto()  # hardware decoding through MediaCodec

        AV_PIX_FMT_GRAY12BE = enum.auto()  # Y , 12bpp, big-endian
        AV_PIX_FMT_GRAY12LE = enum.auto()  # Y , 12bpp, little-endian
        AV_PIX_FMT_GRAY10BE = enum.auto()  # Y , 10bpp, big-endian
        AV_PIX_FMT_GRAY10LE = enum.auto()  # Y , 10bpp, little-endian

        AV_PIX_FMT_P016LE = enum.auto()  # like NV12, with 16bpp per component, little-endian
        AV_PIX_FMT_P016BE = enum.auto()  # like NV12, with 16bpp per component, big-endian
        AV_PIX_FMT_D3D11 = enum.auto()

        AV_PIX_FMT_GRAY9BE = enum.auto()  # Y , 9bpp, big-endian
        AV_PIX_FMT_GRAY9LE = enum.auto()  # Y , 9bpp, little-endian

        AV_PIX_FMT_GBRPF32BE = enum.auto()  # IEEE-754 single precision planar GBR 4:4:4,     96bpp, big-endian
        AV_PIX_FMT_GBRPF32LE = enum.auto()  # IEEE-754 single precision planar GBR 4:4:4,     96bpp, little-endian
        AV_PIX_FMT_GBRAPF32BE = enum.auto()  # IEEE-754 single precision planar GBRA 4:4:4:4, 128bpp, big-endian
        AV_PIX_FMT_GBRAPF32LE = enum.auto()  # IEEE-754 single precision planar GBRA 4:4:4:4, 128bpp, little-endian

        AV_PIX_FMT_DRM_PRIME = enum.auto()
        AV_PIX_FMT_OPENCL = enum.auto()

        AV_PIX_FMT_GRAY14BE = enum.auto()  # Y , 14bpp, big-endian
        AV_PIX_FMT_GRAY14LE = enum.auto()  # Y , 14bpp, little-endian

        AV_PIX_FMT_GRAYF32BE = enum.auto()  # IEEE-754 single precision Y, 32bpp, big-endian
        AV_PIX_FMT_GRAYF32LE = enum.auto()  # IEEE-754 single precision Y, 32bpp, little-endian

        AV_PIX_FMT_YUVA422P12BE = enum.auto()  # planar YUV 4:2:2,24bpp, (1 Cr & Cb sample per 2x1 Y samples), 12b alpha, big-endian
        AV_PIX_FMT_YUVA422P12LE = enum.auto()  # planar YUV 4:2:2,24bpp, (1 Cr & Cb sample per 2x1 Y samples), 12b alpha, little-endian
        AV_PIX_FMT_YUVA444P12BE = enum.auto()  # planar YUV 4:4:4,36bpp, (1 Cr & Cb sample per 1x1 Y samples), 12b alpha, big-endian
        AV_PIX_FMT_YUVA444P12LE = enum.auto()  # planar YUV 4:4:4,36bpp, (1 Cr & Cb sample per 1x1 Y samples), 12b alpha, little-endian

        AV_PIX_FMT_NV24 = enum.auto()  # planar YUV 4:4:4, 24bpp, 1 plane for Y and 1 plane for the UV components, which are interleaved (first byte U and the following byte V)
        AV_PIX_FMT_NV42 = enum.auto()  # as above, but U and V bytes are swapped

        AV_PIX_FMT_VULKAN = enum.auto()

        AV_PIX_FMT_Y210BE = enum.auto()  # packed YUV 4:2:2 like YUYV422, 20bpp, data in the high bits, big-endian
        AV_PIX_FMT_Y210LE = enum.auto()  # packed YUV 4:2:2 like YUYV422, 20bpp, data in the high bits, little-endian

        AV_PIX_FMT_X2RGB10LE = enum.auto()  # packed RGB 10:10:10, 30bpp, (msb)2X 10R 10G 10B(lsb), little-endian, X=unused/undefined
        AV_PIX_FMT_X2RGB10BE = enum.auto()  # packed RGB 10:10:10, 30bpp, (msb)2X 10R 10G 10B(lsb), big-endian, X=unused/undefined
        AV_PIX_FMT_X2BGR10LE = enum.auto()  # packed BGR 10:10:10, 30bpp, (msb)2X 10B 10G 10R(lsb), little-endian, X=unused/undefined
        AV_PIX_FMT_X2BGR10BE = enum.auto()  # packed BGR 10:10:10, 30bpp, (msb)2X 10B 10G 10R(lsb), big-endian, X=unused/undefined

        AV_PIX_FMT_P210BE = enum.auto()  # interleaved chroma YUV 4:2:2, 20bpp, data in the high bits, big-endian
        AV_PIX_FMT_P210LE = enum.auto()  # interleaved chroma YUV 4:2:2, 20bpp, data in the high bits, little-endian

        AV_PIX_FMT_P410BE = enum.auto()  # interleaved chroma YUV 4:4:4, 30bpp, data in the high bits, big-endian
        AV_PIX_FMT_P410LE = enum.auto()  # interleaved chroma YUV 4:4:4, 30bpp, data in the high bits, little-endian

        AV_PIX_FMT_P216BE = enum.auto()  # interleaved chroma YUV 4:2:2, 32bpp, big-endian
        AV_PIX_FMT_P216LE = enum.auto()  # interleaved chroma YUV 4:2:2, 32bpp, little-endian

        AV_PIX_FMT_P416BE = enum.auto()  # interleaved chroma YUV 4:4:4, 48bpp, big-endian
        AV_PIX_FMT_P416LE = enum.auto()  # interleaved chroma YUV 4:4:4, 48bpp, little-endian

        AV_PIX_FMT_VUYA = enum.auto()  # packed VUYA 4:4:4, 32bpp, VUYAVUYA...

        AV_PIX_FMT_RGBAF16BE = enum.auto()  # IEEE-754 half precision packed RGBA 16:16:16:16, 64bpp, RGBARGBA..., big-endian
        AV_PIX_FMT_RGBAF16LE = enum.auto()  # IEEE-754 half precision packed RGBA 16:16:16:16, 64bpp, RGBARGBA..., little-endian

        AV_PIX_FMT_VUYX = enum.auto()  # packed VUYX 4:4:4, 32bpp, Variant of VUYA where alpha channel is left undefined

        AV_PIX_FMT_P012LE = enum.auto()  # like NV12, with 12bpp per component, data in the high bits, zeros in the low bits, little-endian
        AV_PIX_FMT_P012BE = enum.auto()  # like NV12, with 12bpp per component, data in the high bits, zeros in the low bits, big-endian

        AV_PIX_FMT_Y212BE = enum.auto()  # packed YUV 4:2:2 like YUYV422, 24bpp, data in the high bits, zeros in the low bits, big-endian
        AV_PIX_FMT_Y212LE = enum.auto()  # packed YUV 4:2:2 like YUYV422, 24bpp, data in the high bits, zeros in the low bits, little-endian

        AV_PIX_FMT_XV30BE = enum.auto()  # packed XVYU 4:4:4, 32bpp, (msb)2X 10V 10Y 10U(lsb), big-endian, variant of Y410 where alpha channel is left undefined
        AV_PIX_FMT_XV30LE = enum.auto()  # packed XVYU 4:4:4, 32bpp, (msb)2X 10V 10Y 10U(lsb), little-endian, variant of Y410 where alpha channel is left undefined

        AV_PIX_FMT_XV36BE = enum.auto()  # packed XVYU 4:4:4, 48bpp, data in the high bits, zeros in the low bits, big-endian, variant of Y412 where alpha channel is left undefined
        AV_PIX_FMT_XV36LE = enum.auto()  # packed XVYU 4:4:4, 48bpp, data in the high bits, zeros in the low bits, little-endian, variant of Y412 where alpha channel is left undefined

        AV_PIX_FMT_RGBF32BE = enum.auto()  # IEEE-754 single precision packed RGB 32:32:32, 96bpp, RGBRGB..., big-endian
        AV_PIX_FMT_RGBF32LE = enum.auto()  # IEEE-754 single precision packed RGB 32:32:32, 96bpp, RGBRGB..., little-endian

        AV_PIX_FMT_RGBAF32BE = enum.auto()  # IEEE-754 single precision packed RGBA 32:32:32:32, 128bpp, RGBARGBA..., big-endian
        AV_PIX_FMT_RGBAF32LE = enum.auto()  # IEEE-754 single precision packed RGBA 32:32:32:32, 128bpp, RGBARGBA..., little-endian

        AV_PIX_FMT_P212BE = enum.auto()  # interleaved chroma YUV 4:2:2, 24bpp, data in the high bits, big-endian
        AV_PIX_FMT_P212LE = enum.auto()  # interleaved chroma YUV 4:2:2, 24bpp, data in the high bits, little-endian

        AV_PIX_FMT_P412BE = enum.auto()  # interleaved chroma YUV 4:4:4, 36bpp, data in the high bits, big-endian
        AV_PIX_FMT_P412LE = enum.auto()  # interleaved chroma YUV 4:4:4, 36bpp, data in the high bits, little-endian

        AV_PIX_FMT_GBRAP14BE = enum.auto()  # planar GBR 4:4:4:4 56bpp, big-endian
        AV_PIX_FMT_GBRAP14LE = enum.auto()  # planar GBR 4:4:4:4 56bpp, little-endian

        AV_PIX_FMT_D3D12 = enum.auto()

        AV_PIX_FMT_NB = enum.auto()  # number of pixel formats, DO NOT USE THIS if you want to link with shared libav* because the number of formats might differ between versions


class AVRational(ctypes.Structure):
    _fields_ = [
        ('num', ctypes.c_int),
        ('den', ctypes.c_int),]


class struct_AVCodec(ctypes.Structure):
    _fields_ = [
        ('name', ctypes.c_char_p),
        ('long_name', ctypes.POINTER(ctypes.c_char)),
        ('type', AvMediaType),
        ('id', ctypes.c_int),
        ('capabilities', ctypes.c_int),
        ('max_lowres', ctypes.c_uint8),
        ('supported_framerates', ctypes.POINTER(AVRational)),
        ('pix_fmts', ctypes.POINTER(enum_AVPixelFormat)),
        ('supported_samplerates', ctypes.POINTER(ctypes.c_int)),
        ('sample_fmts', ctypes.POINTER(enum_AVSampleFormat)),
        ('priv_class', ctypes.POINTER(AVClass)),
        ('profiles', ctypes.POINTER(AVProfile)),
        ('wrapper_name', ctypes.c_char_p),
        ('ch_layouts', ctypes.POINTER(AVChannelLayout)),
    ]

class CWrapper:
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


class Codec(CWrapper):
    _name_ = "avcodec"
    _functions_ = (("avcodec_find_decoder", (ctypes.c_int,)),)


log.setlevel(log.DEBUG)
c = Codec()
pass
