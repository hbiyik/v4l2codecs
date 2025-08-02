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

from v4l2codecs import log
from v4l2codecs import clib

from v4l2codecs.av import util


class EnumCodecID(clib.CIntEnum):
    class _enum_(enum.IntEnum):
        NONE = 0
        MPEG1VIDEO = enum.auto()
        MPEG2VIDEO = enum.auto()
        H261 = enum.auto()
        H263 = enum.auto()
        RV10 = enum.auto()
        RV20 = enum.auto()
        MJPEG = enum.auto()
        MJPEGB = enum.auto()
        LJPEG = enum.auto()
        SP5X = enum.auto()
        JPEGLS = enum.auto()
        MPEG4 = enum.auto()
        RAWVIDEO = enum.auto()
        MSMPEG4V1 = enum.auto()
        MSMPEG4V2 = enum.auto()
        MSMPEG4V3 = enum.auto()
        WMV1 = enum.auto()
        WMV2 = enum.auto()
        H263P = enum.auto()
        H263I = enum.auto()
        FLV1 = enum.auto()
        SVQ1 = enum.auto()
        SVQ3 = enum.auto()
        DVVIDEO = enum.auto()
        HUFFYUV = enum.auto()
        CYUV = enum.auto()
        H264 = enum.auto()
        INDEO3 = enum.auto()
        VP3 = enum.auto()
        THEORA = enum.auto()
        ASV1 = enum.auto()
        ASV2 = enum.auto()
        FFV1 = enum.auto()
        X4M = enum.auto()
        VCR1 = enum.auto()
        CLJR = enum.auto()
        MDEC = enum.auto()
        ROQ = enum.auto()
        INTERPLAY_VIDEO = enum.auto()
        XAN_WC3 = enum.auto()
        XAN_WC4 = enum.auto()
        RPZA = enum.auto()
        CINEPAK = enum.auto()
        WS_VQA = enum.auto()
        MSRLE = enum.auto()
        MSVIDEO1 = enum.auto()
        IDCIN = enum.auto()
        BPS8 = enum.auto()
        SMC = enum.auto()
        FLIC = enum.auto()
        TRUEMOTION1 = enum.auto()
        VMDVIDEO = enum.auto()
        MSZH = enum.auto()
        ZLIB = enum.auto()
        QTRLE = enum.auto()
        TSCC = enum.auto()
        ULTI = enum.auto()
        QDRAW = enum.auto()
        VIXL = enum.auto()
        QPEG = enum.auto()
        PNG = enum.auto()
        PPM = enum.auto()
        PBM = enum.auto()
        PGM = enum.auto()
        PGMYUV = enum.auto()
        PAM = enum.auto()
        FFVHUFF = enum.auto()
        RV30 = enum.auto()
        RV40 = enum.auto()
        VC1 = enum.auto()
        WMV3 = enum.auto()
        LOCO = enum.auto()
        WNV1 = enum.auto()
        AASC = enum.auto()
        INDEO2 = enum.auto()
        FRAPS = enum.auto()
        TRUEMOTION2 = enum.auto()
        BMP = enum.auto()
        CSCD = enum.auto()
        MMVIDEO = enum.auto()
        ZMBV = enum.auto()
        AVS = enum.auto()
        SMACKVIDEO = enum.auto()
        NUV = enum.auto()
        KMVC = enum.auto()
        FLASHSV = enum.auto()
        CAVS = enum.auto()
        JPEG2000 = enum.auto()
        VMNC = enum.auto()
        VP5 = enum.auto()
        VP6 = enum.auto()
        VP6F = enum.auto()
        TARGA = enum.auto()
        DSICINVIDEO = enum.auto()
        TIERTEXSEQVIDEO = enum.auto()
        TIFF = enum.auto()
        GIF = enum.auto()
        DXA = enum.auto()
        DNXHD = enum.auto()
        THP = enum.auto()
        SGI = enum.auto()
        C93 = enum.auto()
        BETHSOFTVID = enum.auto()
        PTX = enum.auto()
        TXD = enum.auto()
        VP6A = enum.auto()
        AMV = enum.auto()
        VB = enum.auto()
        PCX = enum.auto()
        SUNRAST = enum.auto()
        INDEO4 = enum.auto()
        INDEO5 = enum.auto()
        MIMIC = enum.auto()
        RL2 = enum.auto()
        ESCAPE124 = enum.auto()
        DIRAC = enum.auto()
        BFI = enum.auto()
        CMV = enum.auto()
        MOTIONPIXELS = enum.auto()
        TGV = enum.auto()
        TGQ = enum.auto()
        TQI = enum.auto()
        AURA = enum.auto()
        AURA2 = enum.auto()
        V210X = enum.auto()
        TMV = enum.auto()
        V210 = enum.auto()
        DPX = enum.auto()
        MAD = enum.auto()
        FRWU = enum.auto()
        FLASHSV2 = enum.auto()
        CDGRAPHICS = enum.auto()
        R210 = enum.auto()
        ANM = enum.auto()
        BINKVIDEO = enum.auto()
        IFF_ILBM = enum.auto()
        KGV1 = enum.auto()
        YOP = enum.auto()
        VP8 = enum.auto()
        PICTOR = enum.auto()
        ANSI = enum.auto()
        A64_MULTI = enum.auto()
        A64_MULTI5 = enum.auto()
        R10K = enum.auto()
        MXPEG = enum.auto()
        LAGARITH = enum.auto()
        PRORES = enum.auto()
        JV = enum.auto()
        DFA = enum.auto()
        WMV3IMAGE = enum.auto()
        VC1IMAGE = enum.auto()
        UTVIDEO = enum.auto()
        BMV_VIDEO = enum.auto()
        VBLE = enum.auto()
        DXTORY = enum.auto()
        V410 = enum.auto()
        XWD = enum.auto()
        CDXL = enum.auto()
        XBM = enum.auto()
        ZEROCODEC = enum.auto()
        MSS1 = enum.auto()
        MSA1 = enum.auto()
        TSCC2 = enum.auto()
        MTS2 = enum.auto()
        CLLC = enum.auto()
        MSS2 = enum.auto()
        VP9 = enum.auto()
        AIC = enum.auto()
        ESCAPE130 = enum.auto()
        G2M = enum.auto()
        WEBP = enum.auto()
        HNM4_VIDEO = enum.auto()
        HEVC = enum.auto()
        FIC = enum.auto()
        ALIAS_PIX = enum.auto()
        BRENDER_PIX = enum.auto()
        PAF_VIDEO = enum.auto()
        EXR = enum.auto()
        VP7 = enum.auto()
        SANM = enum.auto()
        SGIRLE = enum.auto()
        MVC1 = enum.auto()
        MVC2 = enum.auto()
        HQX = enum.auto()
        TDSC = enum.auto()
        HQ_HQA = enum.auto()
        HAP = enum.auto()
        DDS = enum.auto()
        DXV = enum.auto()
        SCREENPRESSO = enum.auto()
        RSCC = enum.auto()
        AVS2 = enum.auto()
        PGX = enum.auto()
        AVS3 = enum.auto()
        MSP2 = enum.auto()
        VVC = enum.auto()
        Y41P = enum.auto()
        AVRP = enum.auto()
        O12V = enum.auto()
        AVUI = enum.auto()
        TARGA_Y216 = enum.auto()
        V308 = enum.auto()
        V408 = enum.auto()
        YUV4 = enum.auto()
        AVRN = enum.auto()
        CPIA = enum.auto()
        XFACE = enum.auto()
        SNOW = enum.auto()
        SMVJPEG = enum.auto()
        APNG = enum.auto()
        DAALA = enum.auto()
        CFHD = enum.auto()
        TRUEMOTION2RT = enum.auto()
        M101 = enum.auto()
        MAGICYUV = enum.auto()
        SHEERVIDEO = enum.auto()
        YLC = enum.auto()
        PSD = enum.auto()
        PIXLET = enum.auto()
        SPEEDHQ = enum.auto()
        FMVC = enum.auto()
        SCPR = enum.auto()
        CLEARVIDEO = enum.auto()
        XPM = enum.auto()
        AV1 = enum.auto()
        BITPACKED = enum.auto()
        MSCC = enum.auto()
        SRGC = enum.auto()
        SVG = enum.auto()
        GDV = enum.auto()
        FITS = enum.auto()
        IMM4 = enum.auto()
        PROSUMER = enum.auto()
        MWSC = enum.auto()
        WCMV = enum.auto()
        RASC = enum.auto()
        HYMT = enum.auto()
        ARBC = enum.auto()
        AGM = enum.auto()
        LSCR = enum.auto()
        VP4 = enum.auto()
        IMM5 = enum.auto()
        MVDV = enum.auto()
        MVHA = enum.auto()
        CDTOONS = enum.auto()
        MV30 = enum.auto()
        NOTCHLC = enum.auto()
        PFM = enum.auto()
        MOBICLIP = enum.auto()
        PHOTOCD = enum.auto()
        IPU = enum.auto()
        ARGO = enum.auto()
        CRI = enum.auto()
        SIMBIOSIS_IMX = enum.auto()
        SGA_VIDEO = enum.auto()
        GEM = enum.auto()
        VBN = enum.auto()
        JPEGXL = enum.auto()
        QOI = enum.auto()
        PHM = enum.auto()
        RADIANCE_HDR = enum.auto()
        WBMP = enum.auto()
        MEDIA100 = enum.auto()
        VQC = enum.auto()
        PDV = enum.auto()
        EVC = enum.auto()
        RTV1 = enum.auto()
        VMIX = enum.auto()
        LEAD = enum.auto()
        FIRST_AUDIO = 0x10000
        PCM_S16LE = 0x10000
        PCM_S16BE = enum.auto()
        PCM_U16LE = enum.auto()
        PCM_U16BE = enum.auto()
        PCM_S8 = enum.auto()
        PCM_U8 = enum.auto()
        PCM_MULAW = enum.auto()
        PCM_ALAW = enum.auto()
        PCM_S32LE = enum.auto()
        PCM_S32BE = enum.auto()
        PCM_U32LE = enum.auto()
        PCM_U32BE = enum.auto()
        PCM_S24LE = enum.auto()
        PCM_S24BE = enum.auto()
        PCM_U24LE = enum.auto()
        PCM_U24BE = enum.auto()
        PCM_S24DAUD = enum.auto()
        PCM_ZORK = enum.auto()
        PCM_S16LE_PLANAR = enum.auto()
        PCM_DVD = enum.auto()
        PCM_F32BE = enum.auto()
        PCM_F32LE = enum.auto()
        PCM_F64BE = enum.auto()
        PCM_F64LE = enum.auto()
        PCM_BLURAY = enum.auto()
        PCM_LXF = enum.auto()
        S302M = enum.auto()
        PCM_S8_PLANAR = enum.auto()
        PCM_S24LE_PLANAR = enum.auto()
        PCM_S32LE_PLANAR = enum.auto()
        PCM_S16BE_PLANAR = enum.auto()
        PCM_S64LE = enum.auto()
        PCM_S64BE = enum.auto()
        PCM_F16LE = enum.auto()
        PCM_F24LE = enum.auto()
        PCM_VIDC = enum.auto()
        PCM_SGA = enum.auto()
        ADPCM_IMA_QT = 0x11000
        ADPCM_IMA_WAV = enum.auto()
        ADPCM_IMA_DK3 = enum.auto()
        ADPCM_IMA_DK4 = enum.auto()
        ADPCM_IMA_WS = enum.auto()
        ADPCM_IMA_SMJPEG = enum.auto()
        ADPCM_MS = enum.auto()
        ADPCM_4XM = enum.auto()
        ADPCM_XA = enum.auto()
        ADPCM_ADX = enum.auto()
        ADPCM_EA = enum.auto()
        ADPCM_G726 = enum.auto()
        ADPCM_CT = enum.auto()
        ADPCM_SWF = enum.auto()
        ADPCM_YAMAHA = enum.auto()
        ADPCM_SBPRO_4 = enum.auto()
        ADPCM_SBPRO_3 = enum.auto()
        ADPCM_SBPRO_2 = enum.auto()
        ADPCM_THP = enum.auto()
        ADPCM_IMA_AMV = enum.auto()
        ADPCM_EA_R1 = enum.auto()
        ADPCM_EA_R3 = enum.auto()
        ADPCM_EA_R2 = enum.auto()
        ADPCM_IMA_EA_SEAD = enum.auto()
        ADPCM_IMA_EA_EACS = enum.auto()
        ADPCM_EA_XAS = enum.auto()
        ADPCM_EA_MAXIS_XA = enum.auto()
        ADPCM_IMA_ISS = enum.auto()
        ADPCM_G722 = enum.auto()
        ADPCM_IMA_APC = enum.auto()
        ADPCM_VIMA = enum.auto()
        ADPCM_AFC = enum.auto()
        ADPCM_IMA_OKI = enum.auto()
        ADPCM_DTK = enum.auto()
        ADPCM_IMA_RAD = enum.auto()
        ADPCM_G726LE = enum.auto()
        ADPCM_THP_LE = enum.auto()
        ADPCM_PSX = enum.auto()
        ADPCM_AICA = enum.auto()
        ADPCM_IMA_DAT4 = enum.auto()
        ADPCM_MTAF = enum.auto()
        ADPCM_AGM = enum.auto()
        ADPCM_ARGO = enum.auto()
        ADPCM_IMA_SSI = enum.auto()
        ADPCM_ZORK = enum.auto()
        ADPCM_IMA_APM = enum.auto()
        ADPCM_IMA_ALP = enum.auto()
        ADPCM_IMA_MTF = enum.auto()
        ADPCM_IMA_CUNNING = enum.auto()
        ADPCM_IMA_MOFLEX = enum.auto()
        ADPCM_IMA_ACORN = enum.auto()
        ADPCM_XMD = enum.auto()
        AMR_NB = 0x12000
        AMR_WB = enum.auto()
        RA_144 = 0x13000
        RA_288 = enum.auto()
        ROQ_DPCM = 0x14000
        INTERPLAY_DPCM = enum.auto()
        XAN_DPCM = enum.auto()
        SOL_DPCM = enum.auto()
        SDX2_DPCM = enum.auto()
        GREMLIN_DPCM = enum.auto()
        DERF_DPCM = enum.auto()
        WADY_DPCM = enum.auto()
        CBD2_DPCM = enum.auto()
        MP2 = 0x15000
        MP3 = enum.auto()
        AAC = enum.auto()
        AC3 = enum.auto()
        DTS = enum.auto()
        VORBIS = enum.auto()
        DVAUDIO = enum.auto()
        WMAV1 = enum.auto()
        WMAV2 = enum.auto()
        MACE3 = enum.auto()
        MACE6 = enum.auto()
        VMDAUDIO = enum.auto()
        FLAC = enum.auto()
        MP3ADU = enum.auto()
        MP3ON4 = enum.auto()
        SHORTEN = enum.auto()
        ALAC = enum.auto()
        WESTWOOD_SND1 = enum.auto()
        GSM = enum.auto()
        QDM2 = enum.auto()
        COOK = enum.auto()
        TRUESPEECH = enum.auto()
        TTA = enum.auto()
        SMACKAUDIO = enum.auto()
        QCELP = enum.auto()
        WAVPACK = enum.auto()
        DSICINAUDIO = enum.auto()
        IMC = enum.auto()
        MUSEPACK7 = enum.auto()
        MLP = enum.auto()
        GSM_MS = enum.auto()
        ATRAC3 = enum.auto()
        APE = enum.auto()
        NELLYMOSER = enum.auto()
        MUSEPACK8 = enum.auto()
        SPEEX = enum.auto()
        WMAVOICE = enum.auto()
        WMAPRO = enum.auto()
        WMALOSSLESS = enum.auto()
        ATRAC3P = enum.auto()
        EAC3 = enum.auto()
        SIPR = enum.auto()
        MP1 = enum.auto()
        TWINVQ = enum.auto()
        TRUEHD = enum.auto()
        MP4ALS = enum.auto()
        ATRAC1 = enum.auto()
        BINKAUDIO_RDFT = enum.auto()
        BINKAUDIO_DCT = enum.auto()
        AAC_LATM = enum.auto()
        QDMC = enum.auto()
        CELT = enum.auto()
        G723_1 = enum.auto()
        G729 = enum.auto()
        SVX8_EXP = enum.auto()
        SVX8_FIB = enum.auto()
        BMV_AUDIO = enum.auto()
        RALF = enum.auto()
        IAC = enum.auto()
        ILBC = enum.auto()
        OPUS = enum.auto()
        COMFORT_NOISE = enum.auto()
        TAK = enum.auto()
        METASOUND = enum.auto()
        PAF_AUDIO = enum.auto()
        ON2AVC = enum.auto()
        DSS_SP = enum.auto()
        CODEC2 = enum.auto()
        FFWAVESYNTH = enum.auto()
        SONIC = enum.auto()
        SONIC_LS = enum.auto()
        EVRC = enum.auto()
        SMV = enum.auto()
        DSD_LSBF = enum.auto()
        DSD_MSBF = enum.auto()
        DSD_LSBF_PLANAR = enum.auto()
        DSD_MSBF_PLANAR = enum.auto()
        GV4 = enum.auto()
        INTERPLAY_ACM = enum.auto()
        XMA1 = enum.auto()
        XMA2 = enum.auto()
        DST = enum.auto()
        ATRAC3AL = enum.auto()
        ATRAC3PAL = enum.auto()
        DOLBY_E = enum.auto()
        APTX = enum.auto()
        APTX_HD = enum.auto()
        SBC = enum.auto()
        ATRAC9 = enum.auto()
        HCOM = enum.auto()
        ACELP_KELVIN = enum.auto()
        MPEGH_3D_AUDIO = enum.auto()
        SIREN = enum.auto()
        HCA = enum.auto()
        FASTAUDIO = enum.auto()
        MSNSIREN = enum.auto()
        DFPWM = enum.auto()
        BONK = enum.auto()
        MISC4 = enum.auto()
        APAC = enum.auto()
        FTR = enum.auto()
        WAVARC = enum.auto()
        RKA = enum.auto()
        AC4 = enum.auto()
        OSQ = enum.auto()
        QOA = enum.auto()
        LC3 = enum.auto()
        FIRST_SUBTITLE = 0x17000
        DVD_SUBTITLE = 0x17000
        DVB_SUBTITLE = enum.auto()
        TEXT = enum.auto()
        XSUB = enum.auto()
        SSA = enum.auto()
        MOV_TEXT = enum.auto()
        HDMV_PGS_SUBTITLE = enum.auto()
        DVB_TELETEXT = enum.auto()
        SRT = enum.auto()
        MICRODVD = enum.auto()
        EIA_608 = enum.auto()
        JACOSUB = enum.auto()
        SAMI = enum.auto()
        REALTEXT = enum.auto()
        STL = enum.auto()
        SUBVIEWER1 = enum.auto()
        SUBVIEWER = enum.auto()
        SUBRIP = enum.auto()
        WEBVTT = enum.auto()
        MPL2 = enum.auto()
        VPLAYER = enum.auto()
        PJS = enum.auto()
        ASS = enum.auto()
        HDMV_TEXT_SUBTITLE = enum.auto()
        TTML = enum.auto()
        ARIB_CAPTION = enum.auto()
        FIRST_UNKNOWN = 0x18000
        TTF = 0x18000
        SCTE_35 = enum.auto()
        EPG = enum.auto()
        BINTEXT = enum.auto()
        XBIN = enum.auto()
        IDF = enum.auto()
        OTF = enum.auto()
        SMPTE_KLV = enum.auto()
        DVD_NAV = enum.auto()
        TIMED_ID3 = enum.auto()
        BIN_DATA = enum.auto()
        SMPTE_2038 = enum.auto()
        LCEVC = enum.auto()
        PROBE = 0x19000
        MPEG2TS = 0x20000
        MPEG4SYSTEMS = 0x20001
        FFMETADATA = 0x21000
        WRAPPED_AVFRAME = 0x21001
        VNULL = enum.auto()
        ANULL = enum.auto()


class EnumFieldOrder(clib.CIntEnum):
    class _enum_(enum.IntEnum):
        UNKNOWN = 0
        PROGRESSIVE = enum.auto()
        TT = enum.auto()
        BB = enum.auto()
        TB = enum.auto()
        BT = enum.auto()


class EnumDiscard(clib.CIntEnum):
    class _enum_(enum.IntEnum):
        DEFAULT = 0
        NONREF = 8
        BIDIR = 16
        NONINTRA = 24
        NONKEY = 32
        ALL = 48


class EnumAudioServiceType(clib.CIntEnum):
    class _enum_(enum.IntEnum):
        MAIN = 0
        EFFECTS = 1
        VISUALLY_IMPAIRED = 2
        HEARING_IMPAIRED = 3
        DIALOGUE = 4
        COMMENTARY = 5
        EMERGENCY = 6
        VOICE_OVER = 7
        KARAOKE = 8
        NB = enum.auto()


class EnumPacketSideDataType(clib.CIntEnum):
    class _enum_(enum.IntEnum):
        PALETTE = 0
        NEW_EXTRADATA = enum.auto()
        PARAM_CHANGE = enum.auto()
        H263_MB_INFO = enum.auto()
        REPLAYGAIN = enum.auto()
        DISPLAYMATRIX = enum.auto()
        STEREO3D = enum.auto()
        AUDIO_SERVICE_TYPE = enum.auto()
        QUALITY_STATS = enum.auto()
        FALLBACK_TRACK = enum.auto()
        CPB_PROPERTIES = enum.auto()
        SKIP_SAMPLES = enum.auto()
        JP_DUALMONO = enum.auto()
        STRINGS_METADATA = enum.auto()
        SUBTITLE_POSITION = enum.auto()
        MATROSKA_BLOCKADDITIONAL = enum.auto()
        WEBVTT_IDENTIFIER = enum.auto()
        WEBVTT_SETTINGS = enum.auto()
        METADATA_UPDATE = enum.auto()
        MPEGTS_STREAM_ID = enum.auto()
        MASTERING_DISPLAY_METADATA = enum.auto()
        SPHERICAL = enum.auto()
        CONTENT_LIGHT_LEVEL = enum.auto()
        A53_CC = enum.auto()
        ENCRYPTION_INIT_INFO = enum.auto()
        ENCRYPTION_INFO = enum.auto()
        AFD = enum.auto()
        PRFT = enum.auto()
        ICC_PROFILE = enum.auto()
        DOVI_CONF = enum.auto()
        S12M_TIMECODE = enum.auto()
        DYNAMIC_HDR10_PLUS = enum.auto()
        IAMF_MIX_GAIN_PARAM = enum.auto()
        IAMF_DEMIXING_INFO_PARAM = enum.auto()
        IAMF_RECON_GAIN_INFO_PARAM = enum.auto()
        AMBIENT_VIEWING_ENVIRONMENT = enum.auto()
        FRAME_CROPPING = enum.auto()
        LCEVC = enum.auto()
        NB = enum.auto()


class EnumCodecConfig(clib.CIntEnum):
    class _enum_(enum.IntEnum):
        PIX_FORMAT = 0
        FRAME_RATE = enum.auto()
        SAMPLE_RATE = enum.auto()
        SAMPLE_FORMAT = enum.auto()
        CHANNEL_LAYOUT = enum.auto()
        COLOR_RANGE = enum.auto()
        COLOR_SPACE = enum.auto()


class EnumPictureStructure(clib.CIntEnum):
    class _enum_(enum.IntEnum):
        UNKNOWN = 0
        TOP_FIELD = enum.auto()
        BOTTOM_FIELD = enum.auto()
        FRAME = enum.auto()


class StructProfile(ctypes.Structure):
    _fields_ = [
        ('profile', ctypes.c_int),
        ('name', ctypes.c_char_p),
    ]


class StructCodec(ctypes.Structure):
    _fields_ = [
        ('name', ctypes.c_char_p),
        ('long_name', ctypes.c_char_p),
        ('type', util.EnumMediaType),
        ('id', EnumCodecID),
        ('capabilities', ctypes.c_int),
        ('max_lowres', ctypes.c_uint8),
        ('supported_framerates', ctypes.POINTER(util.StructRational)),
        ('pix_fmts', ctypes.POINTER(util.EnumPixelFormat)),
        ('supported_samplerates', ctypes.POINTER(ctypes.c_int)),
        ('sample_fmts', ctypes.POINTER(util.EnumSampleFormat)),
        ('priv_class', ctypes.c_void_p),
        ('profiles', ctypes.POINTER(StructProfile)),
        ('wrapper_name', ctypes.c_char_p),
        ('ch_layouts', ctypes.POINTER(util.StructChannelLayout)),
    ]


class StructRcOverride(ctypes.Structure):
    _fields_ = [
        ('start_frame', ctypes.c_int),
        ('end_frame', ctypes.c_int),
        ('qscale', ctypes.c_int),
        ('quality_factor', ctypes.c_float)]


class StructHWAccel(ctypes.Structure):
    _fields_ = [
        ('name', ctypes.c_char_p),
        ('type', util.EnumMediaType),
        ('id', EnumCodecID),
        ('pix_fmt', util.EnumPixelFormat),
        ('capabilities', ctypes.c_int),
    ]


class StructHWConfig(ctypes.Structure):
    _fields_ = [("pix_fmt", util.EnumPixelFormat),
                ("methods", ctypes.c_int),
                ("device_type", util.EnumHWDeviceType)]


class StructCodecDescriptor(ctypes.Structure):
    _fields_ = [
        ('id', EnumCodecID),
        ('type', util.EnumMediaType),
        ('name', ctypes.c_char_p),
        ('long_name', ctypes.c_char_p),
        ('props', ctypes.c_int),
        ('mime_types', ctypes.POINTER(ctypes.c_char_p)),
        ('profiles', ctypes.POINTER(StructProfile)),
    ]


class StructPacketSideData(ctypes.Structure):
    _fields_ = [
        ('data', ctypes.POINTER(ctypes.c_uint8)),
        ('size', ctypes.c_size_t),
        ('type', EnumPacketSideDataType),
    ]


class StructPacket(ctypes.Structure):
    _fields_ = [
        ('buf', ctypes.POINTER(util.StructBufferRef)),
        ('pts', ctypes.c_int64),
        ('dts', ctypes.c_int64),
        ('data', ctypes.POINTER(ctypes.c_uint8)),
        ('size', ctypes.c_int),
        ('stream_index', ctypes.c_int),
        ('flags', ctypes.c_int),
        ('side_data', ctypes.POINTER(StructPacketSideData)),
        ('side_data_elems', ctypes.c_int),
        ('duration', ctypes.c_int64),
        ('pos', ctypes.c_int64),
        ('opaque', ctypes.c_void_p),
        ('opaque_ref', ctypes.POINTER(util.StructBufferRef)),
        ('time_base', util.StructRational)]


class StructCodecParameters(ctypes.Structure):
    _fields_ = [
        ('codec_type', util.EnumMediaType),
        ('codec_id', EnumCodecID),
        ('codec_tag', ctypes.c_uint32),
        ('extradata', ctypes.POINTER(ctypes.c_uint8)),
        ('extradata_size', ctypes.c_int),
        ('coded_side_data', ctypes.POINTER(StructPacketSideData)),
        ('nb_coded_side_data', ctypes.c_int),
        ('format', ctypes.c_int),
        ('bit_rate', ctypes.c_int64),
        ('bits_per_coded_sample', ctypes.c_int),
        ('bits_per_raw_sample', ctypes.c_int),
        ('profile', ctypes.c_int),
        ('level', ctypes.c_int),
        ('width', ctypes.c_int),
        ('height', ctypes.c_int),
        ('sample_aspect_ratio', util.StructRational),
        ('framerate', util.StructRational),
        ('field_order', EnumFieldOrder),
        ('color_range', util.EnumColorRange),
        ('color_primaries', util.EnumColorPrimaries),
        ('color_trc', util.EnumColorTransferCharacteristic),
        ('color_space', util.EnumColorSpace),
        ('chroma_location', util.EnumChromaLocation),
        ('video_delay', ctypes.c_int),
        ('ch_layout', util.StructChannelLayout),
        ('sample_rate', ctypes.c_int),
        ('block_align', ctypes.c_int),
        ('frame_size', ctypes.c_int),
        ('initial_padding', ctypes.c_int),
        ('trailing_padding', ctypes.c_int),
        ('seek_preroll', ctypes.c_int)]


class StructContext(ctypes.Structure):
    pass


StructContext_fields_ = [
    ('av_class', ctypes.POINTER(util.StructClass)),
    ('log_level_offset', ctypes.c_int),
    ('codec_type', util.EnumMediaType),
    ('codec', ctypes.POINTER(StructCodec)),
    ('codec_id', EnumCodecID),
    ('codec_tag', ctypes.c_uint),
    ('priv_data', ctypes.c_void_p),
    ('internal', ctypes.c_void_p),
    ('opaque', ctypes.c_void_p),
    ('bit_rate', ctypes.c_int64),
    ('flags', ctypes.c_int),
    ('flags2', ctypes.c_int),
    ('extradata', ctypes.POINTER(ctypes.c_uint8)),
    ('extradata_size', ctypes.c_int),
    ('time_base', util.StructRational),
    ('pkt_timebase', util.StructRational),
    ('framerate', util.StructRational),
    ('ticks_per_frame', ctypes.c_int),
    ('delay', ctypes.c_int),
    ('width', ctypes.c_int),
    ('height', ctypes.c_int),
    ('coded_width', ctypes.c_int),
    ('coded_height', ctypes.c_int),
    ('sample_aspect_ratio', util.StructRational),
    ('pix_fmt', util.EnumPixelFormat),
    ('sw_pix_fmt', util.EnumPixelFormat),
    ('color_primaries', util.EnumColorPrimaries),
    ('color_trc', util.EnumColorTransferCharacteristic),
    ('colorspace', util.EnumColorSpace),
    ('color_range', util.EnumColorRange),
    ('chroma_sample_location', util.EnumChromaLocation),
    ('field_order', EnumFieldOrder),
    ('refs', ctypes.c_int),
    ('has_b_frames', ctypes.c_int),
    ('slice_flags', ctypes.c_int),
    ('draw_horiz_band', ctypes.CFUNCTYPE(None,
                                         ctypes.POINTER(StructContext),
                                         ctypes.POINTER(util.StructFrame),
                                         ctypes.c_int * int(8),
                                         ctypes.c_int,
                                         ctypes.c_int,
                                         ctypes.c_int)),
    ('get_format', ctypes.CFUNCTYPE(util.EnumPixelFormat,
                                    ctypes.POINTER(StructCodec),
                                    ctypes.POINTER(util.EnumPixelFormat))),
    ('max_b_frames', ctypes.c_int),
    ('b_quant_factor', ctypes.c_float),
    ('b_quant_offset', ctypes.c_float),
    ('i_quant_factor', ctypes.c_float),
    ('i_quant_offset', ctypes.c_float),
    ('lumi_masking', ctypes.c_float),
    ('temporal_cplx_masking', ctypes.c_float),
    ('spatial_cplx_masking', ctypes.c_float),
    ('p_masking', ctypes.c_float),
    ('dark_masking', ctypes.c_float),
    ('nsse_weight', ctypes.c_int),
    ('me_cmp', ctypes.c_int),
    ('me_sub_cmp', ctypes.c_int),
    ('mb_cmp', ctypes.c_int),
    ('ildct_cmp', ctypes.c_int),
    ('dia_size', ctypes.c_int),
    ('last_predictor_count', ctypes.c_int),
    ('me_pre_cmp', ctypes.c_int),
    ('pre_dia_size', ctypes.c_int),
    ('me_subpel_quality', ctypes.c_int),
    ('me_range', ctypes.c_int),
    ('mb_decision', ctypes.c_int),
    ('intra_matrix', ctypes.POINTER(ctypes.c_uint16)),
    ('inter_matrix', ctypes.POINTER(ctypes.c_uint16)),
    ('chroma_intra_matrix', ctypes.POINTER(ctypes.c_uint16)),
    ('intra_dc_precision', ctypes.c_int),
    ('mb_lmin', ctypes.c_int),
    ('mb_lmax', ctypes.c_int),
    ('bidir_refine', ctypes.c_int),
    ('keyint_min', ctypes.c_int),
    ('gop_size', ctypes.c_int),
    ('mv0_threshold', ctypes.c_int),
    ('slices', ctypes.c_int),
    ('sample_rate', ctypes.c_int),
    ('sample_fmt', util.EnumSampleFormat),
    ('ch_layout', util.StructChannelLayout),
    ('frame_size', ctypes.c_int),
    ('block_align', ctypes.c_int),
    ('cutoff', ctypes.c_int),
    ('audio_service_type', EnumAudioServiceType),
    ('request_sample_fmt', util.EnumSampleFormat),
    ('initial_padding', ctypes.c_int),
    ('trailing_padding', ctypes.c_int),
    ('seek_preroll', ctypes.c_int),
    ('get_buffer2', ctypes.CFUNCTYPE(ctypes.c_int,
                                     ctypes.POINTER(StructContext),
                                     ctypes.POINTER(util.StructFrame),
                                     ctypes.c_int)),
    ('bit_rate_tolerance', ctypes.c_int),
    ('global_quality', ctypes.c_int),
    ('compression_level', ctypes.c_int),
    ('qcompress', ctypes.c_float),
    ('qblur', ctypes.c_float),
    ('qmin', ctypes.c_int),
    ('qmax', ctypes.c_int),
    ('max_qdiff', ctypes.c_int),
    ('rc_buffer_size', ctypes.c_int),
    ('rc_override_count', ctypes.c_int),
    ('rc_override', ctypes.POINTER(StructRcOverride)),
    ('rc_max_rate', ctypes.c_int64),
    ('rc_min_rate', ctypes.c_int64),
    ('rc_max_available_vbv_use', ctypes.c_float),
    ('rc_min_vbv_overflow_use', ctypes.c_float),
    ('rc_initial_buffer_occupancy', ctypes.c_int),
    ('trellis', ctypes.c_int),
    ('stats_out', ctypes.c_char_p),
    ('stats_in', ctypes.c_char_p),
    ('workaround_bugs', ctypes.c_int),
    ('strict_std_compliance', ctypes.c_int),
    ('error_concealment', ctypes.c_int),
    ('debug', ctypes.c_int),
    ('err_recognition', ctypes.c_int),
    ('hwaccel', ctypes.POINTER(StructHWAccel)),
    ('hwaccel_context', ctypes.c_void_p),
    ('hw_frames_ctx', ctypes.POINTER(util.StructBufferRef)),
    ('hw_device_ctx', ctypes.POINTER(util.StructBufferRef)),
    ('hwaccel_flags', ctypes.c_int),
    ('extra_hw_frames', ctypes.c_int),
    ('error', ctypes.c_uint64 * int(8)),
    ('dct_algo', ctypes.c_int),
    ('idct_algo', ctypes.c_int),
    ('bits_per_coded_sample', ctypes.c_int),
    ('bits_per_raw_sample', ctypes.c_int),
    ('thread_count', ctypes.c_int),
    ('thread_type', ctypes.c_int),
    ('active_thread_type', ctypes.c_int),
    ('execute', ctypes.CFUNCTYPE(ctypes.c_int,
                                 ctypes.POINTER(StructContext),
                                 ctypes.CFUNCTYPE(ctypes.c_int,
                                                  ctypes.POINTER(StructContext),
                                                  ctypes.c_void_p),
                                 ctypes.c_void_p,
                                 ctypes.POINTER(ctypes.c_int),
                                 ctypes.c_int,
                                 ctypes.c_int)),
    ('execute2', ctypes.CFUNCTYPE(ctypes.c_int,
                                  ctypes.POINTER(StructContext),
                                  ctypes.CFUNCTYPE(ctypes.c_int,
                                                   ctypes.POINTER(StructContext),
                                                   ctypes.c_void_p,
                                                   ctypes.c_int,
                                                   ctypes.c_int),
                                  ctypes.c_void_p,
                                  ctypes.POINTER(ctypes.c_int),
                                  ctypes.c_int)),
    ('profile', ctypes.c_int),
    ('level', ctypes.c_int),
    ('properties', ctypes.c_uint),
    ('skip_loop_filter', EnumDiscard),
    ('skip_idct', EnumDiscard),
    ('skip_frame', EnumDiscard),
    ('skip_alpha', ctypes.c_int),
    ('skip_top', ctypes.c_int),
    ('skip_bottom', ctypes.c_int),
    ('lowres', ctypes.c_int),
    ('codec_descriptor', ctypes.POINTER(StructCodecDescriptor)),
    ('sub_charenc', ctypes.c_char_p),
    ('sub_charenc_mode', ctypes.c_int),
    ('subtitle_header_size', ctypes.c_int),
    ('subtitle_header', ctypes.POINTER(ctypes.c_uint8)),
    ('dump_separator', ctypes.POINTER(ctypes.c_uint8)),
    ('codec_whitelist', ctypes.c_char_p),
    ('coded_side_data', ctypes.POINTER(StructPacketSideData)),
    ('nb_coded_side_data', ctypes.c_int),
    ('export_side_data', ctypes.c_int),
    ('max_pixels', ctypes.c_int64),
    ('apply_cropping', ctypes.c_int),
    ('discard_damaged_percentage', ctypes.c_int),
    ('max_samples', ctypes.c_int64),
    ('get_encode_buffer', ctypes.CFUNCTYPE(ctypes.c_int,
                                           ctypes.POINTER(StructContext),
                                           ctypes.POINTER(StructPacket),
                                           ctypes.c_int)),
    ('frame_num', ctypes.c_int64),
    ('side_data_prefer_packet', ctypes.POINTER(ctypes.c_int)),
    ('nb_side_data_prefer_packet', ctypes.c_uint),
    ('decoded_side_data', ctypes.POINTER(ctypes.POINTER(util.StructFrameSideData))),
    ('nb_decoded_side_data', ctypes.c_int)]


class StructParser(ctypes.Structure):
    pass


class StructParserContext(ctypes.Structure):
    pass


StructParser._fields_ = [
    ('codec_ids', ctypes.c_int * int(7)),
    ('priv_data_size', ctypes.c_int),
    ('parser_init', ctypes.CFUNCTYPE(ctypes.c_int,
                                     ctypes.POINTER(StructParserContext))),
    ('parser_parse', ctypes.CFUNCTYPE(ctypes.c_int,
                                      ctypes.POINTER(StructParserContext),
                                      ctypes.POINTER(StructContext),
                                      ctypes.POINTER(ctypes.POINTER(ctypes.c_uint8)),
                                      ctypes.POINTER(ctypes.c_int),
                                      ctypes.POINTER(ctypes.c_uint8),
                                      ctypes.c_int)),
    ('parser_close', ctypes.CFUNCTYPE(None,
                                      ctypes.POINTER(StructParserContext))),
    ('split', ctypes.CFUNCTYPE(ctypes.c_int,
                               ctypes.POINTER(StructContext),
                               ctypes.POINTER(ctypes.c_uint8),
                               ctypes.c_int))]


StructParserContext._fields_ = [
    ('priv_data', ctypes.c_void_p),
    ('parser', ctypes.POINTER(StructParser)),
    ('frame_offset', ctypes.c_int64),
    ('cur_offset', ctypes.c_int64),
    ('next_frame_offset', ctypes.c_int64),
    ('pict_type', ctypes.c_int),
    ('repeat_pict', ctypes.c_int),
    ('pts', ctypes.c_int64),
    ('dts', ctypes.c_int64),
    ('last_pts', ctypes.c_int64),
    ('last_dts', ctypes.c_int64),
    ('fetch_timestamp', ctypes.c_int),
    ('cur_frame_start_index', ctypes.c_int),
    ('cur_frame_offset', ctypes.c_int64 * int(4)),
    ('cur_frame_pts', ctypes.c_int64 * int(4)),
    ('cur_frame_dts', ctypes.c_int64 * int(4)),
    ('flags', ctypes.c_int),
    ('offset', ctypes.c_int64),
    ('cur_frame_end', ctypes.c_int64 * int(4)),
    ('key_frame', ctypes.c_int),
    ('dts_synctypes.c_point', ctypes.c_int),
    ('dts_ref_dts_delta', ctypes.c_int),
    ('pts_dts_delta', ctypes.c_int),
    ('cur_frame_pos', ctypes.c_int64 * int(4)),
    ('pos', ctypes.c_int64),
    ('last_pos', ctypes.c_int64),
    ('duration', ctypes.c_int),
    ('field_order', EnumFieldOrder),
    ('picture_structure', EnumPictureStructure),
    ('output_picture_number', ctypes.c_int),
    ('width', ctypes.c_int),
    ('height', ctypes.c_int),
    ('coded_width', ctypes.c_int),
    ('coded_height', ctypes.c_int),
    ('format', ctypes.c_int)]


class Codec(clib.CLib):
    _name_ = "avcodec"

    @clib.CLib.Signature("av_codec_iterate", ctypes.POINTER(ctypes.c_void_p))
    def codec_iterate(self, opaque):
        return ctypes.POINTER(StructCodec)

    @clib.CLib.Signature("avcodec_find_decoder", EnumCodecID)
    def find_decoder(self, codecid):
        return ctypes.POINTER(StructCodec)

    @clib.CLib.Signature("avcodec_find_decoder_by_name", ctypes.c_char_p)
    def find_decoder_by_name(self, codec_name):
        return ctypes.POINTER(StructCodec)

    @clib.CLib.Signature("avcodec_find_encoder", EnumCodecID)
    def find_encoder(self, codecid):
        return ctypes.POINTER(StructCodec)

    @clib.CLib.Signature("avcodec_find_encoder_by_name", ctypes.c_char_p)
    def find_encoder_by_name(self, name):
        return ctypes.POINTER(StructCodec)

    @clib.CLib.Signature("av_codec_is_encoder", ctypes.POINTER(StructCodec))
    def is_encoder(self, codec):
        return ctypes.c_int

    @clib.CLib.Signature("av_codec_is_decoder", ctypes.POINTER(StructCodec))
    def is_decoder(self, codec):
        return ctypes.c_int

    @clib.CLib.Signature("av_codec_get_profile_name", ctypes.POINTER(StructCodec), ctypes.c_int)
    def get_profile_name(self, codec, profile):
        return ctypes.c_int

    @clib.CLib.Signature("avcodec_get_hw_config", ctypes.POINTER(StructCodec), ctypes.c_int)
    def get_hw_config(self, codec, index):
        return ctypes.POINTER(StructHWConfig)

    @clib.CLib.Signature("avcodec_version")
    def version(self):
        return ctypes.c_uint

    @clib.CLib.Signature("avcodec_configuration")
    def config(self):
        return ctypes.c_char_p

    @clib.CLib.Signature("avcodec_license")
    def license(self):
        return ctypes.c_char_p

    @clib.CLib.Signature("avcodec_alloc_context3", ctypes.POINTER(StructCodec))
    def alloc_context3(self, codec):
        return ctypes.pointer(StructContext)

    @clib.CLib.Signature("avcodec_free_context", ctypes.POINTER(ctypes.POINTER(StructContext)))
    def free_context(self, context):
        return

    @clib.CLib.Signature("avcodec_get_class")
    def get_class(self):
        return ctypes.POINTER(util.StructClass)

    @clib.CLib.Signature("avcodec_parameters_from_context", ctypes.POINTER(StructCodecParameters), ctypes.POINTER(StructContext))
    def params_from_context(self, par, context):
        return ctypes.c_int

    @clib.CLib.Signature("avcodec_parameters_to_context", ctypes.POINTER(StructContext), ctypes.POINTER(StructCodecParameters))
    def params_to_context(self, context, par):
        return ctypes.c_int

    @clib.CLib.Signature("avcodec_open2", ctypes.POINTER(StructContext), ctypes.POINTER(StructContext), ctypes.POINTER(ctypes.c_void_p))
    def open2(self, context, codec, options):
        return ctypes.c_int

    @clib.CLib.Signature("avcodec_default_get_buffer2", ctypes.POINTER(StructContext), ctypes.POINTER(util.StructFrame), ctypes.c_int)
    def get_buffer2(self, context, frame, flags):
        return ctypes.c_int

    @clib.CLib.Signature("avcodec_default_get_encode_buffer", ctypes.POINTER(StructContext), ctypes.POINTER(StructPacket), ctypes.c_int)
    def get_encode_buffer(self, context, packet, flags):
        return ctypes.c_int

    @clib.CLib.Signature("avcodec_send_packet", ctypes.POINTER(StructContext), ctypes.POINTER(StructPacket))
    def send_packet(self, context, packet):
        return ctypes.c_int

    @clib.CLib.Signature("avcodec_receive_packet", ctypes.POINTER(StructContext), ctypes.POINTER(StructPacket))
    def receive_packet(self, context, packet):
        return ctypes.c_int

    @clib.CLib.Signature("avcodec_send_frame", ctypes.POINTER(StructContext), ctypes.POINTER(util.StructFrame))
    def send_frame(self, context, frame):
        return ctypes.c_int

    @clib.CLib.Signature("avcodec_receive_frame", ctypes.POINTER(StructContext), ctypes.POINTER(util.StructFrame))
    def receive_frame(self, context, frame):
        return ctypes.c_int

    @clib.CLib.Signature("avcodec_get_hw_frames_parameters",
                         ctypes.POINTER(StructContext), ctypes.POINTER(util.StructBufferRef),
                         util.EnumPixelFormat, ctypes.POINTER(ctypes.POINTER(util.StructBufferRef)))
    def get_hw_frames_parameters(self, context, device_ref, hw_pix_fmt, out_frames_ref):
        return ctypes.c_int

    @clib.CLib.Signature("avcodec_get_supported_config",
                         ctypes.POINTER(StructContext), ctypes.POINTER(StructCodec), EnumCodecConfig,
                         ctypes.c_int, ctypes.POINTER(ctypes.c_void_p),
                         ctypes.POINTER(ctypes.c_int))
    def get_supported_config(self, context, codec, config, flags, out_configs, out_num_configs):
        return ctypes.c_int

    @clib.CLib.Signature("av_packet_alloc")
    def packet_alloc(self):
        return ctypes.POINTER(StructPacket)

    @clib.CLib.Signature("av_packet_clone", ctypes.POINTER(StructPacket))
    def packet_clone(self, src):
        return ctypes.POINTER(StructPacket)

    @clib.CLib.Signature("av_packet_clone", ctypes.POINTER(ctypes.POINTER(StructPacket)))
    def packet_free(self, pkt):
        return

    @clib.CLib.Signature("av_new_packet", ctypes.POINTER(ctypes.POINTER(StructPacket)), ctypes.c_int)
    def packet_new(self, pkt, size):
        return ctypes.c_int

    @clib.CLib.Signature("av_packet_from_data",
                         ctypes.POINTER(ctypes.POINTER(StructPacket)),
                         ctypes.POINTER(ctypes.c_uint8),
                         ctypes.c_int)
    def packet_from_data(self, pkt, data, size):
        return ctypes.c_int

    @clib.CLib.Signature("av_packet_ref", ctypes.POINTER(StructPacket), ctypes.POINTER(StructPacket))
    def packet_ref(self, dst, src):
        return ctypes.POINTER(StructPacket)

    @clib.CLib.Signature("av_packet_unref", ctypes.POINTER(StructPacket))
    def packet_unref(self, pkt):
        return ctypes.POINTER(StructPacket)

    @clib.CLib.Signature("av_packet_move_ref", ctypes.POINTER(StructPacket), ctypes.POINTER(StructPacket))
    def packet_move_ref(self, dst, src):
        return ctypes.POINTER(StructPacket)

    @clib.CLib.Signature("av_parser_iterate", ctypes.POINTER(ctypes.c_void_p))
    def parser_iterate(self, opaque):
        return ctypes.POINTER(StructParser)

    @clib.CLib.Signature("av_parser_init", EnumCodecID)
    def parser_init(self, codecid):
        return ctypes.POINTER(StructParserContext)

    @clib.CLib.Signature("av_parser_parse2",
                         ctypes.POINTER(StructParserContext),
                         ctypes.POINTER(StructContext),
                         ctypes.POINTER(ctypes.POINTER(ctypes.c_uint8)), ctypes.c_int,
                         ctypes.POINTER(ctypes.c_uint8), ctypes.c_int,
                         ctypes.c_int64, ctypes.c_int64,
                         ctypes.c_uint64
                         )
    def parser_parse2(self, s, avctx, poutbuf, poutbuf_size, buf, buf_size, pts, dts, pos):
        return ctypes.POINTER(StructParserContext)

    @clib.CLib.Signature("av_parser_close", ctypes.POINTER(StructParserContext))
    def parser_close(self, s):
        return


log.setlevel(log.DEBUG)
c = Codec()
log.LOGGER.info(c.version())
log.LOGGER.info(c.config().decode())
log.LOGGER.info(c.license().decode())
p = ctypes.pointer(ctypes.c_void_p())
while True:
    codec = c.codec_iterate(p)
    if clib.isnullptr(codec):
        break
    log.LOGGER.info(codec.contents.name.decode())
