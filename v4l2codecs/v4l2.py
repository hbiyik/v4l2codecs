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

import enum
from v4l2codecs import ioctl
from v4l2codecs import clib


def fourcc(a, b, c, d):
    return ord(a) | (ord(b) << 8) | (ord(c) << 16) | (ord(d) << 24)


def fourcc_be(a, b, c, d):
    return (fourcc(a, b, c, d)) | (1 << 31)


class EnumCapability(clib.c_uintenum):
    class _enum_(enum.IntEnum):
        VIDEO_CAPTURE = 0x00000001  # Is a video capture device
        VIDEO_OUTPUT = 0x00000002  # Is a video output device
        VIDEO_OVERLAY = 0x00000004  # Can do video overlay
        VBI_CAPTURE = 0x00000010  # Is a raw VBI capture device
        VBI_OUTPUT = 0x00000020  # Is a raw VBI output device
        SLICED_VBI_CAPTURE = 0x00000040  # Is a sliced VBI capture device
        SLICED_VBI_OUTPUT = 0x00000080  # Is a sliced VBI output device
        RDS_CAPTURE = 0x00000100  # RDS data capture
        VIDEO_OUTPUT_OVERLAY = 0x00000200  # Can do video output overlay
        HW_FREQ_SEEK = 0x00000400  # Can do hardware frequency seek
        RDS_OUTPUT = 0x00000800  # Is an RDS encoder
        VIDEO_CAPTURE_MPLANE = 0x1000
        VIDEO_OUTPUT_MPLANE = 0x2000
        VIDEO_M2M_MPLANE = 0x4000
        VIDEO_M2M = 0x8000
        TUNER = 0x00010000  # has a tuner
        AUDIO = 0x00020000  # has audio support
        RADIO = 0x00040000  # is a radio device
        MODULATOR = 0x00080000  # has a modulator
        SDR_CAPTURE = 0x00100000  # Is a SDR capture device
        EXT_PIX_FORMAT = 0x00200000  # Supports the extended pixel format
        SDR_OUTPUT = 0x00400000  # Is a SDR output device
        META_CAPTURE = 0x00800000  # Is a metadata capture device
        READWRITE = 0x01000000  # read/write systemcalls
        STREAMING = 0x04000000  # streaming I/O ioctls
        META_OUTPUT = 0x08000000  # Is a metadata output device
        TOUCH = 0x10000000  # Is a touch device
        IO_MC = 0x20000000  # Is input/output controlled by the media controller
        DEVICE_CAPS = 0x80000000  # sets device capabilities field
        TIMEPERFRAME = 0x1000  # timeperframe field is supported
        ASYNCIO = 0x2000000


class EnumPixelFormat(clib.c_uintenum):
    class _enum_(enum.IntEnum):
        RGB332 = fourcc("R", "G", "B", "1")  # 8  RGB-3-3-2
        RGB444 = fourcc("R", "4", "4", "4")  # 16  xxxxrrrr ggggbbbb
        ARGB444 = fourcc("A", "R", "1", "2")  # 16  aaaarrrr ggggbbbb
        XRGB444 = fourcc("X", "R", "1", "2")  # 16  xxxxrrrr ggggbbbb
        RGBA444 = fourcc("R", "A", "1", "2")  # 16  rrrrgggg bbbbaaaa
        RGBX444 = fourcc("R", "X", "1", "2")  # 16  rrrrgggg bbbbxxxx
        ABGR444 = fourcc("A", "B", "1", "2")  # 16  aaaabbbb ggggrrrr
        XBGR444 = fourcc("X", "B", "1", "2")  # 16  xxxxbbbb ggggrrrr
        BGRA444 = fourcc("G", "A", "1", "2")  # 16  bbbbgggg rrrraaaa
        BGRX444 = fourcc("B", "X", "1", "2")  # 16  bbbbgggg rrrrxxxx
        RGB555 = fourcc("R", "G", "B", "O")  # 16  RGB-5-5-5
        ARGB555 = fourcc("A", "R", "1", "5")  # 16  ARGB-1-5-5-5
        XRGB555 = fourcc("X", "R", "1", "5")  # 16  XRGB-1-5-5-5
        RGBA555 = fourcc("R", "A", "1", "5")  # 16  RGBA-5-5-5-1
        RGBX555 = fourcc("R", "X", "1", "5")  # 16  RGBX-5-5-5-1
        ABGR555 = fourcc("A", "B", "1", "5")  # 16  ABGR-1-5-5-5
        XBGR555 = fourcc("X", "B", "1", "5")  # 16  XBGR-1-5-5-5
        BGRA555 = fourcc("B", "A", "1", "5")  # 16  BGRA-5-5-5-1
        BGRX555 = fourcc("B", "X", "1", "5")  # 16  BGRX-5-5-5-1
        RGB565 = fourcc("R", "G", "B", "P")  # 16  RGB-5-6-5
        RGB555X = fourcc("R", "G", "B", "Q")  # 16  RGB-5-5-5 BE
        ARGB555X = fourcc_be("A", "R", "1", "5")  # 16  ARGB-5-5-5 BE
        XRGB555X = fourcc_be("X", "R", "1", "5")  # 16  XRGB-5-5-5 BE
        RGB565X = fourcc("R", "G", "B", "R")  # 16  RGB-5-6-5 BE
        BGR666 = fourcc("B", "G", "R", "H")  # 18  BGR-6-6-6
        BGR24 = fourcc("B", "G", "R", "3")  # 24  BGR-8-8-8
        RGB24 = fourcc("R", "G", "B", "3")  # 24  RGB-8-8-8
        BGR32 = fourcc("B", "G", "R", "4")  # 32  BGR-8-8-8-8
        ABGR32 = fourcc("A", "R", "2", "4")  # 32  BGRA-8-8-8-8
        XBGR32 = fourcc("X", "R", "2", "4")  # 32  BGRX-8-8-8-8
        BGRA32 = fourcc("R", "A", "2", "4")  # 32  ABGR-8-8-8-8
        BGRX32 = fourcc("R", "X", "2", "4")  # 32  XBGR-8-8-8-8
        RGB32 = fourcc("R", "G", "B", "4")  # 32  RGB-8-8-8-8
        RGBA32 = fourcc("A", "B", "2", "4")  # 32  RGBA-8-8-8-8
        RGBX32 = fourcc("X", "B", "2", "4")  # 32  RGBX-8-8-8-8
        ARGB32 = fourcc("B", "A", "2", "4")  # 32  ARGB-8-8-8-8
        XRGB32 = fourcc("B", "X", "2", "4")  # 32  XRGB-8-8-8-8
        RGBX1010102 = fourcc("R", "X", "3", "0")  # 32  RGBX-10-10-10-2
        RGBA1010102 = fourcc("R", "A", "3", "0")  # 32  RGBA-10-10-10-2
        ARGB2101010 = fourcc("A", "R", "3", "0")  # 32  ARGB-2-10-10-10
        BGR48_12 = fourcc("B", "3", "1", "2")  # 48  BGR 12-bit per component
        ABGR64_12 = fourcc("B", "4", "1", "2")  # 64  BGRA 12-bit per component
        GREY = fourcc("G", "R", "E", "Y")  # 8  Greyscale
        Y4 = fourcc("Y", "0", "4", " ")  # 4  Greyscale
        Y6 = fourcc("Y", "0", "6", " ")  # 6  Greyscale
        Y10 = fourcc("Y", "1", "0", " ")  # 10  Greyscale
        Y12 = fourcc("Y", "1", "2", " ")  # 12  Greyscale
        Y012 = fourcc("Y", "0", "1", "2")  # 12  Greyscale
        Y14 = fourcc("Y", "1", "4", " ")  # 14  Greyscale
        Y16 = fourcc("Y", "1", "6", " ")  # 16  Greyscale
        Y16_BE = fourcc_be("Y", "1", "6", " ")  # 16  Greyscale BE
        Y10BPACK = fourcc("Y", "1", "0", "B")  # 10  Greyscale bit-packed
        Y10P = fourcc("Y", "1", "0", "P")  # 10  Greyscale, MIPI RAW10 packed
        IPU3_Y10 = fourcc("i", "p", "3", "y")  # IPU3 packed 10-bit greyscale
        Y12P = fourcc("Y", "1", "2", "P")  # 12  Greyscale, MIPI RAW12 packed
        Y14P = fourcc("Y", "1", "4", "P")  # 14  Greyscale, MIPI RAW14 packed
        PAL8 = fourcc("P", "A", "L", "8")  # 8  8-bit palette
        UV8 = fourcc("U", "V", "8", " ")  # 8  UV 4:4
        YUYV = fourcc("Y", "U", "Y", "V")  # 16  YUV 4:2:2
        YYUV = fourcc("Y", "Y", "U", "V")  # 16  YUV 4:2:2
        YVYU = fourcc("Y", "V", "Y", "U")  # 16 YVU 4:2:2
        UYVY = fourcc("U", "Y", "V", "Y")  # 16  YUV 4:2:2
        VYUY = fourcc("V", "Y", "U", "Y")  # 16  YUV 4:2:2
        Y41P = fourcc("Y", "4", "1", "P")  # 12  YUV 4:1:1
        YUV444 = fourcc("Y", "4", "4", "4")  # 16  xxxxyyyy uuuuvvvv
        YUV555 = fourcc("Y", "U", "V", "O")  # 16  YUV-5-5-5
        YUV565 = fourcc("Y", "U", "V", "P")  # 16  YUV-5-6-5
        YUV24 = fourcc("Y", "U", "V", "3")  # 24  YUV-8-8-8
        YUV32 = fourcc("Y", "U", "V", "4")  # 32  YUV-8-8-8-8
        AYUV32 = fourcc("A", "Y", "U", "V")  # 32  AYUV-8-8-8-8
        XYUV32 = fourcc("X", "Y", "U", "V")  # 32  XYUV-8-8-8-8
        VUYA32 = fourcc("V", "U", "Y", "A")  # 32  VUYA-8-8-8-8
        VUYX32 = fourcc("V", "U", "Y", "X")  # 32  VUYX-8-8-8-8
        YUVA32 = fourcc("Y", "U", "V", "A")  # 32  YUVA-8-8-8-8
        YUVX32 = fourcc("Y", "U", "V", "X")  # 32  YUVX-8-8-8-8
        M420 = fourcc("M", "4", "2", "0")  # 12  YUV 4:2:0 2 lines y, 1 line uvclib.c_interleaved
        YUV48_12 = fourcc("Y", "3", "1", "2")  # 48  YUV 4:4:4 12-bit per component
        Y210 = fourcc("Y", "2", "1", "0")  # 32  YUYV 4:2:2
        Y212 = fourcc("Y", "2", "1", "2")  # 32  YUYV 4:2:2
        Y216 = fourcc("Y", "2", "1", "6")  # 32  YUYV 4:2:2
        NV12 = fourcc("N", "V", "1", "2")  # 12  Y/CbCr 4:2:0
        NV21 = fourcc("N", "V", "2", "1")  # 12  Y/CrCb 4:2:0
        NV16 = fourcc("N", "V", "1", "6")  # 16  Y/CbCr 4:2:2
        NV61 = fourcc("N", "V", "6", "1")  # 16  Y/CrCb 4:2:2
        NV24 = fourcc("N", "V", "2", "4")  # 24  Y/CbCr 4:4:4
        NV42 = fourcc("N", "V", "4", "2")  # 24  Y/CrCb 4:4:4
        P010 = fourcc("P", "0", "1", "0")  # 24  Y/CbCr 4:2:0 10-bit per component
        P012 = fourcc("P", "0", "1", "2")  # 24  Y/CbCr 4:2:0 12-bit per component
        NV12M = fourcc("N", "M", "1", "2")  # 12  Y/CbCr 4:2:0
        NV21M = fourcc("N", "M", "2", "1")  # 21  Y/CrCb 4:2:0
        NV16M = fourcc("N", "M", "1", "6")  # 16  Y/CbCr 4:2:2
        NV61M = fourcc("N", "M", "6", "1")  # 16  Y/CrCb 4:2:2
        P012M = fourcc("P", "M", "1", "2")  # 24  Y/CbCr 4:2:0 12-bit per component
        YUV410 = fourcc("Y", "U", "V", "9")  # 9  YUV 4:1:0
        YVU410 = fourcc("Y", "V", "U", "9")  # 9  YVU 4:1:0
        YUV411P = fourcc("4", "1", "1", "P")  # 12  YVU411 planar
        YUV420 = fourcc("Y", "U", "1", "2")  # 12  YUV 4:2:0
        YVU420 = fourcc("Y", "V", "1", "2")  # 12  YVU 4:2:0
        YUV422P = fourcc("4", "2", "2", "P")  # 16  YVU422 planar
        YUV420M = fourcc("Y", "M", "1", "2")  # 12  YUV420 planar
        YVU420M = fourcc("Y", "M", "2", "1")  # 12  YVU420 planar
        YUV422M = fourcc("Y", "M", "1", "6")  # 16  YUV422 planar
        YVU422M = fourcc("Y", "M", "6", "1")  # 16  YVU422 planar
        YUV444M = fourcc("Y", "M", "2", "4")  # 24  YUV444 planar
        YVU444M = fourcc("Y", "M", "4", "2")  # 24  YVU444 planar
        NV12_4L4 = fourcc("V", "T", "1", "2")  # 12  Y/CbCr 4:2:0  4x4 tiles
        NV12_16L16 = fourcc("H", "M", "1", "2")  # 12  Y/CbCr 4:2:0 16x16 tiles
        NV12_32L32 = fourcc("S", "T", "1", "2")  # 12  Y/CbCr 4:2:0 32x32 tiles
        NV15_4L4 = fourcc("V", "T", "1", "5")  # 15 Y/CbCr 4:2:0 10-bit 4x4 tiles
        P010_4L4 = fourcc("T", "0", "1", "0")  # 12  Y/CbCr 4:2:0 10-bit 4x4 macroblocks
        NV12_8L128 = fourcc("A", "T", "1", "2")  # Y/CbCr 4:2:0 8x128 tiles
        NV12_10BE_8L128 = fourcc_be("A", "X", "1", "2")  # Y/CbCr 4:2:0 10-bit 8x128 tiles
        NV12MT = fourcc("T", "M", "1", "2")  # 12  Y/CbCr 4:2:0 64x32 tiles
        NV12MT_16X16 = fourcc("V", "M", "1", "2")  # 12  Y/CbCr 4:2:0 16x16 tiles
        NV12M_8L128 = fourcc("N", "A", "1", "2")  # Y/CbCr 4:2:0 8x128 tiles
        NV12M_10BE_8L128 = fourcc_be("N", "T", "1", "2")  # Y/CbCr 4:2:0 10-bit 8x128 tiles
        SBGGR8 = fourcc("B", "A", "8", "1")  # 8  BGBG.. GRGR..
        SGBRG8 = fourcc("G", "B", "R", "G")  # 8  GBGB.. RGRG..
        SGRBG8 = fourcc("G", "R", "B", "G")  # 8  GRGR.. BGBG..
        SRGGB8 = fourcc("R", "G", "G", "B")  # 8  RGRG.. GBGB..
        SBGGR10 = fourcc("B", "G", "1", "0")  # 10  BGBG.. GRGR..
        SGBRG10 = fourcc("G", "B", "1", "0")  # 10  GBGB.. RGRG..
        SGRBG10 = fourcc("B", "A", "1", "0")  # 10  GRGR.. BGBG..
        SRGGB10 = fourcc("R", "G", "1", "0")  # 10  RGRG.. GBGB..
        SBGGR10P = fourcc("p", "B", "A", "A")
        SGBRG10P = fourcc("p", "G", "A", "A")
        SGRBG10P = fourcc("p", "g", "A", "A")
        SRGGB10P = fourcc("p", "R", "A", "A")
        SBGGR10ALAW8 = fourcc("a", "B", "A", "8")
        SGBRG10ALAW8 = fourcc("a", "G", "A", "8")
        SGRBG10ALAW8 = fourcc("a", "g", "A", "8")
        SRGGB10ALAW8 = fourcc("a", "R", "A", "8")
        SBGGR10DPCM8 = fourcc("b", "B", "A", "8")
        SGBRG10DPCM8 = fourcc("b", "G", "A", "8")
        SGRBG10DPCM8 = fourcc("B", "D", "1", "0")
        SRGGB10DPCM8 = fourcc("b", "R", "A", "8")
        SBGGR12 = fourcc("B", "G", "1", "2")  # 12  BGBG.. GRGR..
        SGBRG12 = fourcc("G", "B", "1", "2")  # 12  GBGB.. RGRG..
        SGRBG12 = fourcc("B", "A", "1", "2")  # 12  GRGR.. BGBG..
        SRGGB12 = fourcc("R", "G", "1", "2")  # 12  RGRG.. GBGB..
        SBGGR12P = fourcc("p", "B", "C", "C")
        SGBRG12P = fourcc("p", "G", "C", "C")
        SGRBG12P = fourcc("p", "g", "C", "C")
        SRGGB12P = fourcc("p", "R", "C", "C")
        SBGGR14 = fourcc("B", "G", "1", "4")  # 14  BGBG.. GRGR..
        SGBRG14 = fourcc("G", "B", "1", "4")  # 14  GBGB.. RGRG..
        SGRBG14 = fourcc("G", "R", "1", "4")  # 14  GRGR.. BGBG..
        SRGGB14 = fourcc("R", "G", "1", "4")  # 14  RGRG.. GBGB..
        SBGGR14P = fourcc("p", "B", "E", "E")
        SGBRG14P = fourcc("p", "G", "E", "E")
        SGRBG14P = fourcc("p", "g", "E", "E")
        SRGGB14P = fourcc("p", "R", "E", "E")
        SBGGR16 = fourcc("B", "Y", "R", "2")  # 16  BGBG.. GRGR..
        SGBRG16 = fourcc("G", "B", "1", "6")  # 16  GBGB.. RGRG..
        SGRBG16 = fourcc("G", "R", "1", "6")  # 16  GRGR.. BGBG..
        SRGGB16 = fourcc("R", "G", "1", "6")  # 16  RGRG.. GBGB..
        HSV24 = fourcc("H", "S", "V", "3")
        HSV32 = fourcc("H", "S", "V", "4")
        MJPEG = fourcc("M", "J", "P", "G")  # Motion-JPEG
        JPEG = fourcc("J", "P", "E", "G")  # JFIF JPEG
        DV = fourcc("d", "v", "s", "d")  # 1394
        MPEG = fourcc("M", "P", "E", "G")  # MPEG-1/2/4 Multiplexed
        H264 = fourcc("H", "2", "6", "4")  # H264 with start codes
        H264_NO_SC = fourcc("A", "V", "C", "1")  # H264 without start codes
        H264_MVC = fourcc("M", "2", "6", "4")  # H264 MVC
        H263 = fourcc("H", "2", "6", "3")  # H263
        MPEG1 = fourcc("M", "P", "G", "1")  # MPEG-1 ES
        MPEG2 = fourcc("M", "P", "G", "2")  # MPEG-2 ES
        MPEG2_SLICE = fourcc("M", "G", "2", "S")  # MPEG-2 parsed slice data
        MPEG4 = fourcc("M", "P", "G", "4")  # MPEG-4 part 2 ES
        XVID = fourcc("X", "V", "I", "D")  # Xvid
        VC1_ANNEX_G = fourcc("V", "C", "1", "G")  # SMPTE 421M Annex G compliant stream
        VC1_ANNEX_L = fourcc("V", "C", "1", "L")  # SMPTE 421M Annex L compliant stream
        VP8 = fourcc("V", "P", "8", "0")  # VP8
        VP8_FRAME = fourcc("V", "P", "8", "F")  # VP8 parsed frame
        VP9 = fourcc("V", "P", "9", "0")  # VP9
        VP9_FRAME = fourcc("V", "P", "9", "F")  # VP9 parsed frame
        HEVC = fourcc("H", "E", "V", "C")  # HEVC aka H.265
        FWHT = fourcc("F", "W", "H", "T")  # Fast Walsh Hadamard Transform (vicodec)
        FWHT_STATELESS = fourcc("S", "F", "W", "H")  # Stateless FWHT (vicodec)
        H264_SLICE = fourcc("S", "2", "6", "4")  # H264 parsed slices
        HEVC_SLICE = fourcc("S", "2", "6", "5")  # HEVC parsed slices
        AV1_FRAME = fourcc("A", "V", "1", "F")  # AV1 parsed frame
        SPK = fourcc("S", "P", "K", "0")  # Sorenson Spark
        RV30 = fourcc("R", "V", "3", "0")  # RealVideo 8
        RV40 = fourcc("R", "V", "4", "0")  # RealVideo 9 & 10
        CPIA1 = fourcc("C", "P", "I", "A")  # cpia1 YUV
        WNVA = fourcc("W", "N", "V", "A")  # Winnov hw compress
        SN9C10X = fourcc("S", "9", "1", "0")  # SN9C10x compression
        SN9C20X_I420 = fourcc("S", "9", "2", "0")  # SN9C20x YUV 4:2:0
        PWC1 = fourcc("P", "W", "C", "1")  # pwc older webcam
        PWC2 = fourcc("P", "W", "C", "2")  # pwc newer webcam
        ET61X251 = fourcc("E", "6", "2", "5")  # ET61X251 compression
        SPCA501 = fourcc("S", "5", "0", "1")  # YUYV per line
        SPCA505 = fourcc("S", "5", "0", "5")  # YYUV per line
        SPCA508 = fourcc("S", "5", "0", "8")  # YUVY per line
        SPCA561 = fourcc("S", "5", "6", "1")  # compressed GBRG bayer
        PAC207 = fourcc("P", "2", "0", "7")  # compressed BGGR bayer
        MR97310A = fourcc("M", "3", "1", "0")  # compressed BGGR bayer
        JL2005BCD = fourcc("J", "L", "2", "0")  # compressed RGGB bayer
        SN9C2028 = fourcc("S", "O", "N", "X")  # compressed GBRG bayer
        SQ905C = fourcc("9", "0", "5", "C")  # compressed RGGB bayer
        PJPG = fourcc("P", "J", "P", "G")  # Pixart 73xx JPEG
        OV511 = fourcc("O", "5", "1", "1")  # ov511 JPEG
        OV518 = fourcc("O", "5", "1", "8")  # ov518 JPEG
        STV0680 = fourcc("S", "6", "8", "0")  # stv0680 bayer
        TM6000 = fourcc("T", "M", "6", "0")  # tm5600/tm60x0
        CIT_YYVYUY = fourcc("C", "I", "T", "V")  # one line of Y then 1 line of VYUY
        KONICA420 = fourcc("K", "O", "N", "I")  # YUV420 planar in blocks of 256 pixels
        JPGL = fourcc("J", "P", "G", "L")  # JPEG-Lite
        SE401 = fourcc("S", "4", "0", "1")  # se401 janggu compressed rgb
        S5C_UYVY_JPG = fourcc("S", "5", "C", "I")  # S5C73M3clib.c_interleaved UYVY/JPEG
        Y8I = fourcc("Y", "8", "I", " ")  # Greyscale 8-bit L/Rclib.c_interleaved
        Y12I = fourcc("Y", "1", "2", "I")  # Greyscale 12-bit L/Rclib.c_interleaved
        Z16 = fourcc("Z", "1", "6", " ")  # Depth data 16-bit
        MT21C = fourcc("M", "T", "2", "1")  # Mediatek compressed block mode
        MM21 = fourcc("M", "M", "2", "1")  # Mediatek 8-bit block mode, two non-contiguous planes
        MT2110T = fourcc("M", "T", "2", "T")  # Mediatek 10-bit block tile mode
        MT2110R = fourcc("M", "T", "2", "R")  # Mediatek 10-bit block raster mode
        INZI = fourcc("I", "N", "Z", "I")  # Intel Planar Greyscale 10-bit and Depth 16-bit
        CNF4 = fourcc("C", "N", "F", "4")  # Intel 4-bit packed depth confidence information
        HI240 = fourcc("H", "I", "2", "4")  # BTTV 8-bit dithered RGB
        QC08C = fourcc("Q", "0", "8", "C")  # Qualcomm 8-bit compressed
        QC10C = fourcc("Q", "1", "0", "C")  # Qualcomm 10-bit compressed
        AJPG = fourcc("A", "J", "P", "G")  # Aspeed JPEG
        HEXTILE = fourcc("H", "X", "T", "L")  # Hextile compressed
        IPU3_SBGGR10 = fourcc("i", "p", "3", "b")  # IPU3 packed 10-bit BGGR bayer
        IPU3_SGBRG10 = fourcc("i", "p", "3", "g")  # IPU3 packed 10-bit GBRG bayer
        IPU3_SGRBG10 = fourcc("i", "p", "3", "G")  # IPU3 packed 10-bit GRBG bayer
        IPU3_SRGGB10 = fourcc("i", "p", "3", "r")  # IPU3 packed 10-bit RGGB bayer
        PRIV_MAGIC = 0xFEEDCAFE
        HM12 = NV12_16L16
        SUNXI_TILED_NV12 = NV12_32L32


class FlagPixelFormat(clib.c_uintenum):
    class _enum_(enum.IntFlag):
        PREMUL_ALPHA = 0x1
        SET_CSC = 0x2


class FlagVbi(clib.c_uintenum):
    class _enum_(enum.IntFlag):
        UNSYNC = 1 << 0
        INTERLACED = 1 << 1
        ITU_525_F1_START = 1
        ITU_525_F2_START = 264
        ITU_625_F1_START = 1
        ITU_625_F2_START = 314


class EnumYcbcrEncoding(clib.c_uintenum):
    class _enum_(enum.IntEnum):
        DEFAULT = 0
        _601 = 1
        _709 = 2
        XV601 = 3
        XV709 = 4
        SYCC = 5
        BT2020 = 6
        BT2020_CONST_LUM = 7
        SMPTE240M = 8


class EnumHsvEncoding(clib.c_uintenum):
    class _enum_(enum.IntEnum):
        _180 = 128
        _256 = 129


class EnumQuantization(clib.c_uintenum):
    class _enum_(enum.IntEnum):
        DEFAULT = 0
        FULL_RANGE = 1
        LIM_RANGE = 2


class EnumXferFunc(clib.c_uintenum):
    class _enum_(enum.IntEnum):
        DEFAULT = 0
        _709 = 1
        SRGB = 2
        OPRGB = 3
        SMPTE240M = 4
        NONE = 5
        DCI_P3 = 6
        SMPTE2084 = 7


class EnumField(clib.c_uintenum):
    class _enum_(enum.IntEnum):
        ANY = 0
        NONE = 1
        TOP = 2
        BOTTOM = 3
        INTERLACED = 4
        SEQ_TB = 5
        SEQ_BT = 6
        ALTERNATE = 7
        INTERLACED_TB = 8
        INTERLACED_BT = 9


class EnumColorSpace(clib.c_uintenum):
    class _enum_(enum.IntEnum):
        DEFAULT = 0
        SMPTE170M = 1
        SMPTE240M = 2
        REC709 = 3
        BT878 = 4
        _470_SYSTEM_M = 5
        _470_SYSTEM_BG = 6
        JPEG = 7
        SRGB = 8
        OPRGB = 9
        BT2020 = 10
        RAW = 11
        DCI_P3 = 12


class StructCapability(clib.Structure):
    _fields_ = [
        ("driver", clib.c_char * 16),
        ("card", clib.c_char * 32),
        ("bus_info", clib.c_char * 32),
        ("version", clib.c_uint),
        ("capabilities", EnumCapability),
        ("device_caps", EnumCapability),
        ("reserved", clib.c_uint * 3),
    ]


class StructFmtdesc(clib.Structure):
    _fields_ = [
        ("index", clib.c_uint),
        ("type", clib.c_uint),
        ("flags", clib.c_uint),
        ("description", clib.c_char * 32),
        ("pixelformat", EnumPixelFormat),
        ("mbus_code", clib.c_uint),
        ("reserved", clib.c_uint * 3),
    ]


class StructPixFormat(clib.Structure):
    class M1(clib.Union):
        _fields_ = [("ycbcr_enc", EnumYcbcrEncoding),
                    ("hsv_enc", EnumHsvEncoding)]
    _anonymous_ = ("m1",)
    _fields_ = [
        ("width", clib.c_uint),
        ("height", clib.c_uint),
        ("pixelformat", EnumPixelFormat),
        ("field", EnumField),
        ("bytesperline", clib.c_uint),
        ("sizeimage", clib.c_uint),
        ("colorspace", EnumColorSpace),
        ("priv", clib.c_uint),
        ("flags", FlagPixelFormat),
        ("m1", M1),
        ("quantization", EnumQuantization),
        ("xfer_func", EnumXferFunc),
    ]


class StructPlanePixFormat(clib.Structure):
    _pack_ = True
    _fields_ = [("sizeimage", clib.c_uint),
                ("bytesperline", clib.c_uint),
                ("reserved", clib.c_uint16 * 6)]


class StructPixFormatMplane(clib.Structure):
    _pack_ = True

    class M1(clib.Union):
        _pack_ = True
        _fields_ = [("ycbcr_enc", EnumYcbcrEncoding),
                    ("hsv_enc", EnumHsvEncoding)]

    _anonymous_ = ("m1",)
    _fields_ = [
        ("width", clib.c_uint),
        ("height", clib.c_uint),
        ("pixelformat", EnumPixelFormat),
        ("field", EnumField),
        ("colorspace", EnumColorSpace),
        ("plane_fmt", StructPlanePixFormat * 8),
        ("num_planes", clib.c_uint8),
        ("flags", FlagPixelFormat),
        ("m1", M1),
        ("quantization", EnumQuantization),
        ("xfer_func", EnumXferFunc),
        ("reserved", clib.c_char * 7),
    ]


class StructRect(clib.Structure):
    _fields_ = [("left", clib.c_int),
                ("top", clib.c_int),
                ("width", clib.c_uint),
                ("height", clib.c_uint)]


class StructClip(clib.Structure):
    pass


StructClip._fields_ = [("c", StructRect),
                       ("next", clib.POINTER(StructClip))]


class StructWindow(clib.Structure):
    _fields_ = [
        ("w", StructRect),
        ("field", EnumField),
        ("chromakey", clib.c_uint),
        ("clips", clib.POINTER(StructClip)),
        ("clipcount", clib.c_uint),
        ("bitmap", clib.POINTER(None)),
        ("global_alpha", clib.c_uint8),
    ]


class StructVbiFormat(clib.Structure):
    _fields_ = [
        ("sampling_rate", clib.c_uint),
        ("offset", clib.c_uint),
        ("samples_per_line", clib.c_uint),
        ("sample_format", EnumPixelFormat),
        ("start", clib.c_int * 2),
        ("count", clib.c_uint * 2),
        ("flags", FlagVbi),
        ("reserved", clib.c_uint * 2),
    ]


class StructSlicedVbiFormat(clib.Structure):
    _fields_ = [
        ("service_set", clib.c_uint16),
        ("service_lines", clib.c_uint16 * 24 * 2),
        ("io_size", clib.c_uint),
        ("reserved", clib.c_uint * 2),
    ]


class StructSdrFormat(clib.Structure):
    _pack_ = True
    _fields_ = [("pixelformat", EnumPixelFormat),
                ("buffersize", clib.c_uint),
                ("reserved", clib.c_char * 24)]


class StructMetaFormat(clib.Structure):
    _pack_ = True
    _fields_ = [
        ("dataformat", EnumPixelFormat),
        ("buffersize", clib.c_uint),
        ("width", clib.c_uint),
        ("height", clib.c_uint),
        ("bytesperline", clib.c_uint),
    ]


class StructFormat(clib.Structure):
    class M1(clib.Union):
        pass

    M1._fields_ = [
        ("pix", StructPixFormat),
        ("pix_mp", StructPixFormatMplane),
        ("win", StructWindow),
        ("vbi", StructVbiFormat),
        ("sliced", StructSlicedVbiFormat),
        ("sdr", StructSdrFormat),
        ("meta", StructMetaFormat),
        ("raw_data", clib.c_char * 200),
    ]


class IOC(enum.IntEnum):
    QUERYCAP = ioctl.IOR("V", 0, StructCapability)
    ENUM_FMT = ioctl.IOWR("V", 2, StructFmtdesc)
    G_FMT = ioctl.IOWR("V", 4, StructFormat)
    S_FMT = ioctl.IOWR("V", 5, StructFormat)
    REQBUFS = ioctl.IOWR("V", 8, v4l2_requestbuffers)
    QUERYBUF = ioctl.IOWR("V", 9, v4l2_buffer)
    G_FBUF = ioctl.IOR("V", 10, v4l2_framebuffer)
    S_FBUF = ioctl.IOW("V", 11, v4l2_framebuffer)
    OVERLAY = ioctl.IOW("V", 14, clib.c_int)
    QBUF = ioctl.IOWR("V", 15, v4l2_buffer)
    EXPBUF = ioctl.IOWR("V", 16, v4l2_exportbuffer)
    DQBUF = ioctl.IOWR("V", 17, v4l2_buffer)
    STREAMON = ioctl.IOW("V", 18, clib.c_int)
    STREAMOFF = ioctl.IOW("V", 19, clib.c_int)
    G_PARM = ioctl.IOWR("V", 21, v4l2_streamparm)
    S_PARM = ioctl.IOWR("V", 22, v4l2_streamparm)
    G_STD = ioctl.IOR("V", 23, v4l2_std_id)
    S_STD = ioctl.IOW("V", 24, v4l2_std_id)
    ENUMSTD = ioctl.IOWR("V", 25, v4l2_standard)
    ENUMINPUT = ioctl.IOWR("V", 26, v4l2_input)
    G_CTRL = ioctl.IOWR("V", 27, v4l2_control)
    S_CTRL = ioctl.IOWR("V", 28, v4l2_control)
    G_TUNER = ioctl.IOWR("V", 29, v4l2_tuner)
    S_TUNER = ioctl.IOW("V", 30, v4l2_tuner)
    G_AUDIO = ioctl.IOR("V", 33, v4l2_audio)
    S_AUDIO = ioctl.IOW("V", 34, v4l2_audio)
    QUERYCTRL = ioctl.IOWR("V", 36, v4l2_queryctrl)
    QUERYMENU = ioctl.IOWR("V", 37, v4l2_querymenu)
    G_INPUT = ioctl.IOR("V", 38, clib.c_int)
    S_INPUT = ioctl.IOWR("V", 39, clib.c_int)
    G_EDID = ioctl.IOWR("V", 40, v4l2_edid)
    S_EDID = ioctl.IOWR("V", 41, v4l2_edid)
    G_OUTPUT = ioctl.IOR("V", 46, clib.c_int)
    S_OUTPUT = ioctl.IOWR("V", 47, clib.c_int)
    ENUMOUTPUT = ioctl.IOWR("V", 48, v4l2_output)
    G_AUDOUT = ioctl.IOR("V", 49, v4l2_audioout)
    S_AUDOUT = ioctl.IOW("V", 50, v4l2_audioout)
    G_MODULATOR = ioctl.IOWR("V", 54, v4l2_modulator)
    S_MODULATOR = ioctl.IOW("V", 55, v4l2_modulator)
    G_FREQUENCY = ioctl.IOWR("V", 56, v4l2_frequency)
    S_FREQUENCY = ioctl.IOW("V", 57, v4l2_frequency)
    CROPCAP = ioctl.IOWR("V", 58, v4l2_cropcap)
    G_CROP = ioctl.IOWR("V", 59, v4l2_crop)
    S_CROP = ioctl.IOW("V", 60, v4l2_crop)
    G_JPEGCOMP = ioctl.IOR("V", 61, v4l2_jpegcompression)
    S_JPEGCOMP = ioctl.IOW("V", 62, v4l2_jpegcompression)
    QUERYSTD = ioctl.IOR("V", 63, v4l2_std_id)
    TRY_FMT = ioctl.IOWR("V", 64, StructFormat)
    ENUMAUDIO = ioctl.IOWR("V", 65, v4l2_audio)
    ENUMAUDOUT = ioctl.IOWR("V", 66, v4l2_audioout)
    G_PRIORITY = ioctl.IOR("V", 67, clib.c_uint32)  # enum v4l2_priority
    S_PRIORITY = ioctl.IOW("V", 68, clib.c_uint32)  # enum v4l2_priority
    G_SLICED_VBI_CAP = ioctl.IOWR("V", 69, v4l2_sliced_vbi_cap)
    LOG_STATUS = ioctl.IO("V", 70)
    G_EXT_CTRLS = ioctl.IOWR("V", 71, v4l2_ext_controls)
    S_EXT_CTRLS = ioctl.IOWR("V", 72, v4l2_ext_controls)
    TRY_EXT_CTRLS = ioctl.IOWR("V", 73, v4l2_ext_controls)
    ENUM_FRAMESIZES = ioctl.IOWR("V", 74, v4l2_frmsizeenum)
    ENUM_FRAMEINTERVALS = ioctl.IOWR("V", 75, v4l2_frmivalenum)
    G_ENC_INDEX = ioctl.IOR("V", 76, v4l2_enc_idx)
    ENCODER_CMD = ioctl.IOWR("V", 77, v4l2_encoder_cmd)
    TRY_ENCODER_CMD = ioctl.IOWR("V", 78, v4l2_encoder_cmd)
    DBG_S_REGISTER = ioctl.IOW("V", 79, v4l2_dbg_register)
    DBG_G_REGISTER = ioctl.IOWR("V", 80, v4l2_dbg_register)
    S_HW_FREQ_SEEK = ioctl.IOW("V", 82, v4l2_hw_freq_seek)
    S_DV_TIMINGS = ioctl.IOWR("V", 87, v4l2_dv_timings)
    G_DV_TIMINGS = ioctl.IOWR("V", 88, v4l2_dv_timings)
    DQEVENT = ioctl.IOR("V", 89, v4l2_event)
    SUBSCRIBE_EVENT = ioctl.IOW("V", 90, v4l2_event_subscription)
    UNSUBSCRIBE_EVENT = ioctl.IOW("V", 91, v4l2_event_subscription)
    CREATE_BUFS = ioctl.IOWR("V", 92, v4l2_create_buffers)
    PREPARE_BUF = ioctl.IOWR("V", 93, v4l2_buffer)
    G_SELECTION = ioctl.IOWR("V", 94, v4l2_selection)
    S_SELECTION = ioctl.IOWR("V", 95, v4l2_selection)
    DECODER_CMD = ioctl.IOWR("V", 96, v4l2_decoder_cmd)
    TRY_DECODER_CMD = ioctl.IOWR("V", 97, v4l2_decoder_cmd)
    ENUM_DV_TIMINGS = ioctl.IOWR("V", 98, v4l2_enum_dv_timings)
    QUERY_DV_TIMINGS = ioctl.IOR("V", 99, v4l2_dv_timings)
    DV_TIMINGS_CAP = ioctl.IOWR("V", 100, v4l2_dv_timings_cap)
    ENUM_FREQ_BANDS = ioctl.IOWR("V", 101, v4l2_frequency_band)
    DBG_G_CHIP_INFO = ioctl.IOWR("V", 102, v4l2_dbg_chip_info)
    QUERY_EXT_CTRL = ioctl.IOWR("V", 103, v4l2_query_ext_ctrl)
    REMOVE_BUFS = ioctl.IOWR("V", 104, v4l2_remove_buffers)
    SUBDEV_QUERYCAP = ioctl.IOR("V", 0, v4l2_subdev_capability)
    SUBDEV_G_FMT = ioctl.IOWR("V", 4, v4l2_subdev_format)
    SUBDEV_S_FMT = ioctl.IOWR("V", 5, v4l2_subdev_format)
    SUBDEV_G_FRAME_INTERVAL = ioctl.IOWR("V", 21, v4l2_subdev_frame_interval)
    SUBDEV_S_FRAME_INTERVAL = ioctl.IOWR("V", 22, v4l2_subdev_frame_interval)
    SUBDEV_ENUM_MBUS_CODE = ioctl.IOWR("V", 2, v4l2_subdev_mbus_code_enum)
    SUBDEV_ENUM_FRAME_SIZE = ioctl.IOWR("V", 74, v4l2_subdev_frame_size_enum)
    SUBDEV_ENUM_FRAME_INTERVAL = ioctl.IOWR("V", 75, v4l2_subdev_frame_interval_enum)
    SUBDEV_G_CROP = ioctl.IOWR("V", 59, v4l2_subdev_crop)
    SUBDEV_S_CROP = ioctl.IOWR("V", 60, v4l2_subdev_crop)
    SUBDEV_G_SELECTION = ioctl.IOWR("V", 61, v4l2_subdev_selection)
    SUBDEV_S_SELECTION = ioctl.IOWR("V", 62, v4l2_subdev_selection)
    SUBDEV_G_ROUTING = ioctl.IOWR("V", 38, v4l2_subdev_routing)
    SUBDEV_S_ROUTING = ioctl.IOWR("V", 39, v4l2_subdev_routing)
    SUBDEV_G_CLIENT_CAP = ioctl.IOR("V", 101, v4l2_subdev_client_capability)
    SUBDEV_S_CLIENT_CAP = ioctl.IOWR("V", 102, v4l2_subdev_client_capability)
    SUBDEV_G_STD = ioctl.IOR("V", 23, v4l2_std_id)
    SUBDEV_S_STD = ioctl.IOW("V", 24, v4l2_std_id)
    SUBDEV_ENUMSTD = ioctl.IOWR("V", 25, v4l2_standard)
    SUBDEV_G_EDID = ioctl.IOWR("V", 40, v4l2_edid)
    SUBDEV_S_EDID = ioctl.IOWR("V", 41, v4l2_edid)
    SUBDEV_QUERYSTD = ioctl.IOR("V", 63, v4l2_std_id)
    SUBDEV_S_DV_TIMINGS = ioctl.IOWR("V", 87, v4l2_dv_timings)
    SUBDEV_G_DV_TIMINGS = ioctl.IOWR("V", 88, v4l2_dv_timings)
    SUBDEV_ENUM_DV_TIMINGS = ioctl.IOWR("V", 98, v4l2_enum_dv_timings)
    SUBDEV_QUERY_DV_TIMINGS = ioctl.IOR("V", 99, v4l2_dv_timings)
    SUBDEV_DV_TIMINGS_CAP = ioctl.IOWR("V", 100, v4l2_dv_timings_cap)
