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
import ctypes

from v4l2codecs import clib

from v4l2codecs.av import util


class EnumCodecID(clib.c_intenum):
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


class EnumFieldOrder(clib.c_intenum):
    class _enum_(enum.IntEnum):
        UNKNOWN = 0
        PROGRESSIVE = enum.auto()
        TT = enum.auto()
        BB = enum.auto()
        TB = enum.auto()
        BT = enum.auto()


class EnumDiscard(clib.c_intenum):
    class _enum_(enum.IntEnum):
        DEFAULT = 0
        NONREF = 8
        BIDIR = 16
        NONINTRA = 24
        NONKEY = 32
        ALL = 48


class EnumAudioServiceType(clib.c_intenum):
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


class EnumPacketSideDataType(clib.c_intenum):
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


class EnumCodecConfig(clib.c_intenum):
    class _enum_(enum.IntEnum):
        PIX_FORMAT = 0
        FRAME_RATE = enum.auto()
        SAMPLE_RATE = enum.auto()
        SAMPLE_FORMAT = enum.auto()
        CHANNEL_LAYOUT = enum.auto()
        COLOR_RANGE = enum.auto()
        COLOR_SPACE = enum.auto()


class EnumPictureStructure(clib.c_intenum):
    class _enum_(enum.IntEnum):
        UNKNOWN = 0
        TOP_FIELD = enum.auto()
        BOTTOM_FIELD = enum.auto()
        FRAME = enum.auto()


class StructProfile(clib.Structure):
    _fields_ = [
        ('profile', clib.c_int),
        ('name', clib.c_char_p),
    ]


class StructCodec(clib.Structure):
    _fields_ = [
        ('name', clib.c_char_p),
        ('long_name', clib.c_char_p),
        ('type', util.EnumMediaType),
        ('id', EnumCodecID),
        ('capabilities', clib.c_int),
        ('max_lowres', clib.c_uint8),
        ('supported_framerates', clib.POINTER(util.StructRational)),
        ('pix_fmts', clib.POINTER(util.EnumPixelFormat)),
        ('supported_samplerates', clib.POINTER(clib.c_int)),
        ('sample_fmts', clib.POINTER(util.EnumSampleFormat)),
        ('priv_class', clib.c_void_p),
        ('profiles', clib.POINTER(StructProfile)),
        ('wrapper_name', clib.c_char_p),
        ('ch_layouts', clib.POINTER(util.StructChannelLayout)),
    ]


class StructRcOverride(clib.Structure):
    _fields_ = [
        ('start_frame', clib.c_int),
        ('end_frame', clib.c_int),
        ('qscale', clib.c_int),
        ('quality_factor', clib.c_float)]


class StructHWAccel(clib.Structure):
    _fields_ = [
        ('name', clib.c_char_p),
        ('type', util.EnumMediaType),
        ('id', EnumCodecID),
        ('pix_fmt', util.EnumPixelFormat),
        ('capabilities', clib.c_int),
    ]


class StructHWConfig(clib.Structure):
    _fields_ = [("pix_fmt", util.EnumPixelFormat),
                ("methods", clib.c_int),
                ("device_type", util.EnumHWDeviceType)]


class StructCodecDescriptor(clib.Structure):
    _fields_ = [
        ('id', EnumCodecID),
        ('type', util.EnumMediaType),
        ('name', clib.c_char_p),
        ('long_name', clib.c_char_p),
        ('props', clib.c_int),
        ('mime_types', clib.POINTER(clib.c_char_p)),
        ('profiles', clib.POINTER(StructProfile)),
    ]


class StructPacketSideData(clib.Structure):
    _fields_ = [
        ('data', clib.POINTER(clib.c_uint8)),
        ('size', clib.c_size_t),
        ('type', EnumPacketSideDataType),
    ]


class StructPacket(clib.Structure):
    _fields_ = [
        ('buf', clib.POINTER(util.StructBufferRef)),
        ('pts', clib.c_int64),
        ('dts', clib.c_int64),
        ('data', clib.POINTER(clib.c_uint8)),
        ('size', clib.c_int),
        ('stream_index', clib.c_int),
        ('flags', clib.c_int),
        ('side_data', clib.POINTER(StructPacketSideData)),
        ('side_data_elems', clib.c_int),
        ('duration', clib.c_int64),
        ('pos', clib.c_int64),
        ('opaque', clib.c_void_p),
        ('opaque_ref', clib.POINTER(util.StructBufferRef)),
        ('time_base', util.StructRational)]


class StructCodecParameters(clib.Structure):
    _fields_ = [
        ('codec_type', util.EnumMediaType),
        ('codec_id', EnumCodecID),
        ('codec_tag', clib.c_uint32),
        ('extradata', clib.POINTER(clib.c_uint8)),
        ('extradata_size', clib.c_int),
        ('coded_side_data', clib.POINTER(StructPacketSideData)),
        ('nb_coded_side_data', clib.c_int),
        ('format', clib.c_int),
        ('bit_rate', clib.c_int64),
        ('bits_per_coded_sample', clib.c_int),
        ('bits_per_raw_sample', clib.c_int),
        ('profile', clib.c_int),
        ('level', clib.c_int),
        ('width', clib.c_int),
        ('height', clib.c_int),
        ('sample_aspect_ratio', util.StructRational),
        ('framerate', util.StructRational),
        ('field_order', EnumFieldOrder),
        ('color_range', util.EnumColorRange),
        ('color_primaries', util.EnumColorPrimaries),
        ('color_trc', util.EnumColorTransferCharacteristic),
        ('color_space', util.EnumColorSpace),
        ('chroma_location', util.EnumChromaLocation),
        ('video_delay', clib.c_int),
        ('ch_layout', util.StructChannelLayout),
        ('sample_rate', clib.c_int),
        ('block_align', clib.c_int),
        ('frame_size', clib.c_int),
        ('initial_padding', clib.c_int),
        ('trailing_padding', clib.c_int),
        ('seek_preroll', clib.c_int)]


class StructContext(clib.Structure):
    pass


StructContext._fields_ = [
    ('av_class', clib.POINTER(util.StructClass)),
    ('log_level_offset', clib.c_int),
    ('codec_type', util.EnumMediaType),
    ('codec', clib.POINTER(StructCodec)),
    ('codec_id', EnumCodecID),
    ('codec_tag', clib.c_uint),
    ('priv_data', clib.c_void_p),
    ('internal', clib.c_void_p),
    ('opaque', clib.c_void_p),
    ('bit_rate', clib.c_int64),
    ('flags', clib.c_int),
    ('flags2', clib.c_int),
    ('extradata', clib.POINTER(clib.c_uint8)),
    ('extradata_size', clib.c_int),
    ('time_base', util.StructRational),
    ('pkt_timebase', util.StructRational),
    ('framerate', util.StructRational),
    ('ticks_per_frame', clib.c_int),
    ('delay', clib.c_int),
    ('width', clib.c_int),
    ('height', clib.c_int),
    ('coded_width', clib.c_int),
    ('coded_height', clib.c_int),
    ('sample_aspect_ratio', util.StructRational),
    ('pix_fmt', util.EnumPixelFormat),
    ('sw_pix_fmt', util.EnumPixelFormat),
    ('color_primaries', util.EnumColorPrimaries),
    ('color_trc', util.EnumColorTransferCharacteristic),
    ('colorspace', util.EnumColorSpace),
    ('color_range', util.EnumColorRange),
    ('chroma_sample_location', util.EnumChromaLocation),
    ('field_order', EnumFieldOrder),
    ('refs', clib.c_int),
    ('has_b_frames', clib.c_int),
    ('slice_flags', clib.c_int),
    ('draw_horiz_band', ctypes.CFUNCTYPE(None,
                                         clib.POINTER(StructContext),
                                         clib.POINTER(util.StructFrame),
                                         clib.c_int * int(8),
                                         clib.c_int,
                                         clib.c_int,
                                         clib.c_int)),
    ('get_format', ctypes.CFUNCTYPE(util.EnumPixelFormat,
                                    clib.POINTER(StructCodec),
                                    clib.POINTER(util.EnumPixelFormat))),
    ('max_b_frames', clib.c_int),
    ('b_quant_factor', clib.c_float),
    ('b_quant_offset', clib.c_float),
    ('i_quant_factor', clib.c_float),
    ('i_quant_offset', clib.c_float),
    ('lumi_masking', clib.c_float),
    ('temporal_cplx_masking', clib.c_float),
    ('spatial_cplx_masking', clib.c_float),
    ('p_masking', clib.c_float),
    ('dark_masking', clib.c_float),
    ('nsse_weight', clib.c_int),
    ('me_cmp', clib.c_int),
    ('me_sub_cmp', clib.c_int),
    ('mb_cmp', clib.c_int),
    ('ildct_cmp', clib.c_int),
    ('dia_size', clib.c_int),
    ('last_predictor_count', clib.c_int),
    ('me_pre_cmp', clib.c_int),
    ('pre_dia_size', clib.c_int),
    ('me_subpel_quality', clib.c_int),
    ('me_range', clib.c_int),
    ('mb_decision', clib.c_int),
    ('intra_matrix', clib.POINTER(clib.c_uint16)),
    ('inter_matrix', clib.POINTER(clib.c_uint16)),
    ('chroma_intra_matrix', clib.POINTER(clib.c_uint16)),
    ('intra_dc_precision', clib.c_int),
    ('mb_lmin', clib.c_int),
    ('mb_lmax', clib.c_int),
    ('bidir_refine', clib.c_int),
    ('keyint_min', clib.c_int),
    ('gop_size', clib.c_int),
    ('mv0_threshold', clib.c_int),
    ('slices', clib.c_int),
    ('sample_rate', clib.c_int),
    ('sample_fmt', util.EnumSampleFormat),
    ('ch_layout', util.StructChannelLayout),
    ('frame_size', clib.c_int),
    ('block_align', clib.c_int),
    ('cutoff', clib.c_int),
    ('audio_service_type', EnumAudioServiceType),
    ('request_sample_fmt', util.EnumSampleFormat),
    ('initial_padding', clib.c_int),
    ('trailing_padding', clib.c_int),
    ('seek_preroll', clib.c_int),
    ('get_buffer2', ctypes.CFUNCTYPE(clib.c_int,
                                     clib.POINTER(StructContext),
                                     clib.POINTER(util.StructFrame),
                                     clib.c_int)),
    ('bit_rate_tolerance', clib.c_int),
    ('global_quality', clib.c_int),
    ('compression_level', clib.c_int),
    ('qcompress', clib.c_float),
    ('qblur', clib.c_float),
    ('qmin', clib.c_int),
    ('qmax', clib.c_int),
    ('max_qdiff', clib.c_int),
    ('rc_buffer_size', clib.c_int),
    ('rc_override_count', clib.c_int),
    ('rc_override', clib.POINTER(StructRcOverride)),
    ('rc_max_rate', clib.c_int64),
    ('rc_min_rate', clib.c_int64),
    ('rc_max_available_vbv_use', clib.c_float),
    ('rc_min_vbv_overflow_use', clib.c_float),
    ('rc_initial_buffer_occupancy', clib.c_int),
    ('trellis', clib.c_int),
    ('stats_out', clib.c_char_p),
    ('stats_in', clib.c_char_p),
    ('workaround_bugs', clib.c_int),
    ('strict_std_compliance', clib.c_int),
    ('error_concealment', clib.c_int),
    ('debug', clib.c_int),
    ('err_recognition', clib.c_int),
    ('hwaccel', clib.POINTER(StructHWAccel)),
    ('hwaccel_context', clib.c_void_p),
    ('hw_frames_ctx', clib.POINTER(util.StructBufferRef)),
    ('hw_device_ctx', clib.POINTER(util.StructBufferRef)),
    ('hwaccel_flags', clib.c_int),
    ('extra_hw_frames', clib.c_int),
    ('error', clib.c_uint64 * int(8)),
    ('dct_algo', clib.c_int),
    ('idct_algo', clib.c_int),
    ('bits_per_coded_sample', clib.c_int),
    ('bits_per_raw_sample', clib.c_int),
    ('thread_count', clib.c_int),
    ('thread_type', clib.c_int),
    ('active_thread_type', clib.c_int),
    ('execute', ctypes.CFUNCTYPE(clib.c_int,
                                 clib.POINTER(StructContext),
                                 ctypes.CFUNCTYPE(clib.c_int,
                                                  clib.POINTER(StructContext),
                                                  clib.c_void_p),
                                 clib.c_void_p,
                                 clib.POINTER(clib.c_int),
                                 clib.c_int,
                                 clib.c_int)),
    ('execute2', ctypes.CFUNCTYPE(clib.c_int,
                                  clib.POINTER(StructContext),
                                  ctypes.CFUNCTYPE(clib.c_int,
                                                   clib.POINTER(StructContext),
                                                   clib.c_void_p,
                                                   clib.c_int,
                                                   clib.c_int),
                                  clib.c_void_p,
                                  clib.POINTER(clib.c_int),
                                  clib.c_int)),
    ('profile', clib.c_int),
    ('level', clib.c_int),
    ('properties', clib.c_uint),
    ('skip_loop_filter', EnumDiscard),
    ('skip_idct', EnumDiscard),
    ('skip_frame', EnumDiscard),
    ('skip_alpha', clib.c_int),
    ('skip_top', clib.c_int),
    ('skip_bottom', clib.c_int),
    ('lowres', clib.c_int),
    ('codec_descriptor', clib.POINTER(StructCodecDescriptor)),
    ('sub_charenc', clib.c_char_p),
    ('sub_charenc_mode', clib.c_int),
    ('subtitle_header_size', clib.c_int),
    ('subtitle_header', clib.POINTER(clib.c_uint8)),
    ('dump_separator', clib.POINTER(clib.c_uint8)),
    ('codec_whitelist', clib.c_char_p),
    ('coded_side_data', clib.POINTER(StructPacketSideData)),
    ('nb_coded_side_data', clib.c_int),
    ('export_side_data', clib.c_int),
    ('max_pixels', clib.c_int64),
    ('apply_cropping', clib.c_int),
    ('discard_damaged_percentage', clib.c_int),
    ('max_samples', clib.c_int64),
    ('get_encode_buffer', ctypes.CFUNCTYPE(clib.c_int,
                                           clib.POINTER(StructContext),
                                           clib.POINTER(StructPacket),
                                           clib.c_int)),
    ('frame_num', clib.c_int64),
    ('side_data_prefer_packet', clib.POINTER(clib.c_int)),
    ('nb_side_data_prefer_packet', clib.c_uint),
    ('decoded_side_data', clib.POINTER(clib.POINTER(util.StructFrameSideData))),
    ('nb_decoded_side_data', clib.c_int)]


class StructParser(clib.Structure):
    pass


class StructParserContext(clib.Structure):
    pass


StructParser._fields_ = [
    ('codec_ids', clib.c_int * int(7)),
    ('priv_data_size', clib.c_int),
    ('parser_init', ctypes.CFUNCTYPE(clib.c_int,
                                     clib.POINTER(StructParserContext))),
    ('parser_parse', ctypes.CFUNCTYPE(clib.c_int,
                                      clib.POINTER(StructParserContext),
                                      clib.POINTER(StructContext),
                                      clib.POINTER(clib.POINTER(clib.c_uint8)),
                                      clib.POINTER(clib.c_int),
                                      clib.POINTER(clib.c_uint8),
                                      clib.c_int)),
    ('parser_close', ctypes.CFUNCTYPE(None,
                                      clib.POINTER(StructParserContext))),
    ('split', ctypes.CFUNCTYPE(clib.c_int,
                               clib.POINTER(StructContext),
                               clib.POINTER(clib.c_uint8),
                               clib.c_int))]


StructParserContext._fields_ = [
    ('priv_data', clib.c_void_p),
    ('parser', clib.POINTER(StructParser)),
    ('frame_offset', clib.c_int64),
    ('cur_offset', clib.c_int64),
    ('next_frame_offset', clib.c_int64),
    ('pict_type', clib.c_int),
    ('repeat_pict', clib.c_int),
    ('pts', clib.c_int64),
    ('dts', clib.c_int64),
    ('last_pts', clib.c_int64),
    ('last_dts', clib.c_int64),
    ('fetch_timestamp', clib.c_int),
    ('cur_frame_start_index', clib.c_int),
    ('cur_frame_offset', clib.c_int64 * int(4)),
    ('cur_frame_pts', clib.c_int64 * int(4)),
    ('cur_frame_dts', clib.c_int64 * int(4)),
    ('flags', clib.c_int),
    ('offset', clib.c_int64),
    ('cur_frame_end', clib.c_int64 * int(4)),
    ('key_frame', clib.c_int),
    ('dts_synclib.c_point', clib.c_int),
    ('dts_ref_dts_delta', clib.c_int),
    ('pts_dts_delta', clib.c_int),
    ('cur_frame_pos', clib.c_int64 * int(4)),
    ('pos', clib.c_int64),
    ('last_pos', clib.c_int64),
    ('duration', clib.c_int),
    ('field_order', EnumFieldOrder),
    ('picture_structure', EnumPictureStructure),
    ('output_picture_number', clib.c_int),
    ('width', clib.c_int),
    ('height', clib.c_int),
    ('coded_width', clib.c_int),
    ('coded_height', clib.c_int),
    ('format', clib.c_int)]


class Codec(clib.Lib):
    _name_ = "avcodec"

    @clib.Lib.Signature("av_codec_iterate", clib.POINTER(clib.c_void_p))
    def codec_iterate(self, opaque):
        return clib.POINTER(StructCodec)

    @clib.Lib.Signature("avcodec_find_decoder", EnumCodecID)
    def find_decoder(self, codecid):
        return clib.POINTER(StructCodec)

    @clib.Lib.Signature("avcodec_find_decoder_by_name", clib.c_char_p)
    def find_decoder_by_name(self, codec_name):
        return clib.POINTER(StructCodec)

    @clib.Lib.Signature("avcodec_find_encoder", EnumCodecID)
    def find_encoder(self, codecid):
        return clib.POINTER(StructCodec)

    @clib.Lib.Signature("avcodec_find_encoder_by_name", clib.c_char_p)
    def find_encoder_by_name(self, name):
        return clib.POINTER(StructCodec)

    @clib.Lib.Signature("av_codec_is_encoder", clib.POINTER(StructCodec))
    def is_encoder(self, codec):
        return clib.c_int

    @clib.Lib.Signature("av_codec_is_decoder", clib.POINTER(StructCodec))
    def is_decoder(self, codec):
        return clib.c_int

    @clib.Lib.Signature("av_codec_get_profile_name", clib.POINTER(StructCodec), clib.c_int)
    def get_profile_name(self, codec, profile):
        return clib.c_int

    @clib.Lib.Signature("avcodec_get_hw_config", clib.POINTER(StructCodec), clib.c_int)
    def get_hw_config(self, codec, index):
        return clib.POINTER(StructHWConfig)

    @clib.Lib.Signature("avcodec_version")
    def version(self):
        return clib.c_uint

    @clib.Lib.Signature("avcodec_configuration")
    def config(self):
        return clib.c_char_p

    @clib.Lib.Signature("avcodec_license")
    def license(self):
        return clib.c_char_p

    @clib.Lib.Signature("avcodec_alloc_context3", clib.POINTER(StructCodec))
    def alloc_context3(self, codec):
        return clib.POINTER(StructContext)

    @clib.Lib.Signature("avcodec_free_context", clib.POINTER(clib.POINTER(StructContext)))
    def free_context(self, context):
        return

    @clib.Lib.Signature("avcodec_get_class")
    def get_class(self):
        return clib.POINTER(util.StructClass)

    @clib.Lib.Signature("avcodec_parameters_from_context", clib.POINTER(StructCodecParameters), clib.POINTER(StructContext))
    def params_from_context(self, par, context):
        return clib.c_int

    @clib.Lib.Signature("avcodec_parameters_to_context", clib.POINTER(StructContext), clib.POINTER(StructCodecParameters))
    def params_to_context(self, context, par):
        return clib.c_int

    @clib.Lib.Signature("avcodec_open2", clib.POINTER(StructContext), clib.POINTER(StructCodec), clib.POINTER(clib.c_void_p))
    def open2(self, context, codec, options):
        return clib.c_int

    @clib.Lib.Signature("avcodec_default_get_buffer2", clib.POINTER(StructContext), clib.POINTER(util.StructFrame), clib.c_int)
    def get_buffer2(self, context, frame, flags):
        return clib.c_int

    @clib.Lib.Signature("avcodec_default_get_encode_buffer", clib.POINTER(StructContext), clib.POINTER(StructPacket), clib.c_int)
    def get_encode_buffer(self, context, packet, flags):
        return clib.c_int

    @clib.Lib.Signature("avcodec_send_packet", clib.POINTER(StructContext), clib.POINTER(StructPacket))
    def send_packet(self, context, packet):
        return clib.c_int

    @clib.Lib.Signature("avcodec_receive_packet", clib.POINTER(StructContext), clib.POINTER(StructPacket))
    def receive_packet(self, context, packet):
        return clib.c_int

    @clib.Lib.Signature("avcodec_send_frame", clib.POINTER(StructContext), clib.POINTER(util.StructFrame))
    def send_frame(self, context, frame):
        return clib.c_int

    @clib.Lib.Signature("avcodec_receive_frame", clib.POINTER(StructContext), clib.POINTER(util.StructFrame))
    def receive_frame(self, context, frame):
        return clib.c_int

    @clib.Lib.Signature("avcodec_get_hw_frames_parameters",
                         clib.POINTER(StructContext), clib.POINTER(util.StructBufferRef),
                         util.EnumPixelFormat, clib.POINTER(clib.POINTER(util.StructBufferRef)))
    def get_hw_frames_parameters(self, context, device_ref, hw_pix_fmt, out_frames_ref):
        return clib.c_int

    @clib.Lib.Signature("avcodec_get_supported_config",
                         clib.POINTER(StructContext), clib.POINTER(StructCodec), EnumCodecConfig,
                         clib.c_int, clib.POINTER(clib.c_void_p),
                         clib.POINTER(clib.c_int))
    def get_supported_config(self, context, codec, config, flags, out_configs, out_num_configs):
        return clib.c_int

    @clib.Lib.Signature("av_packet_alloc")
    def packet_alloc(self):
        return clib.POINTER(StructPacket)

    @clib.Lib.Signature("av_packet_clone", clib.POINTER(StructPacket))
    def packet_clone(self, src):
        return clib.POINTER(StructPacket)

    @clib.Lib.Signature("av_packet_clone", clib.POINTER(clib.POINTER(StructPacket)))
    def packet_free(self, pkt):
        return

    @clib.Lib.Signature("av_new_packet", clib.POINTER(clib.POINTER(StructPacket)), clib.c_int)
    def packet_new(self, pkt, size):
        return clib.c_int

    @clib.Lib.Signature("av_packet_from_data",
                         clib.POINTER(clib.POINTER(StructPacket)),
                         clib.POINTER(clib.c_uint8),
                         clib.c_int)
    def packet_from_data(self, pkt, data, size):
        return clib.c_int

    @clib.Lib.Signature("av_packet_ref", clib.POINTER(StructPacket), clib.POINTER(StructPacket))
    def packet_ref(self, dst, src):
        return clib.c_int

    @clib.Lib.Signature("av_packet_unref", clib.POINTER(StructPacket))
    def packet_unref(self, pkt):
        return

    @clib.Lib.Signature("av_packet_move_ref", clib.POINTER(StructPacket), clib.POINTER(StructPacket))
    def packet_move_ref(self, dst, src):
        return

    @clib.Lib.Signature("av_parser_iterate", clib.POINTER(clib.c_void_p))
    def parser_iterate(self, opaque):
        return clib.POINTER(StructParser)

    @clib.Lib.Signature("av_parser_init", EnumCodecID)
    def parser_init(self, codecid):
        return clib.POINTER(StructParserContext)

    @clib.Lib.Signature("av_parser_parse2",
                         clib.POINTER(StructParserContext),
                         clib.POINTER(StructContext),
                         clib.POINTER(clib.POINTER(clib.c_uint8)),
                         clib.POINTER(clib.c_int),
                         clib.POINTER(clib.c_uint8),
                         clib.c_int,
                         clib.c_int64, clib.c_int64,
                         clib.c_uint64
                         )
    def parser_parse2(self, s, avctx, poutbuf, poutbuf_size, buf, buf_size, pts, dts, pos):
        return clib.c_int

    @clib.Lib.Signature("av_parser_close", clib.POINTER(StructParserContext))
    def parser_close(self, s):
        return

    @clib.Lib.Signature("av_frame_alloc")
    def frame_alloc(self):
        return clib.POINTER(util.StructFrame)

    @clib.Lib.Signature("av_frame_free", clib.POINTER(clib.POINTER(util.StructFrame)))
    def frame_free(self):
        return

    @clib.Lib.Signature("av_frame_clone", clib.POINTER(util.StructFrame))
    def frame_clone(self, src):
        return clib.POINTER(util.StructFrame)

    @clib.Lib.Signature("av_frame_ref", clib.POINTER(clib.POINTER(util.StructFrame)),
                         clib.POINTER(clib.POINTER(util.StructFrame)))
    def frame_ref(self, dst, src):
        return clib.c_int

    @clib.Lib.Signature("av_frame_unref", clib.POINTER(clib.POINTER(util.StructFrame)))
    def frame_unref(self, frame):
        return clib.c_int

    @clib.Lib.Signature("av_frame_move_ref", clib.POINTER(clib.POINTER(util.StructFrame)),
                         clib.POINTER(clib.POINTER(util.StructFrame)))
    def frame_move_ref(self, dst, src):
        return clib.c_int

    @clib.Lib.Signature("av_frame_get_buffer", clib.POINTER(clib.POINTER(util.StructFrame)), clib.c_int)
    def frame_get_buffer(self, frame, align):
        return clib.c_int


"""
log.setlevel(log.DEBUG)
c = Codec()
log.LOGGER.info(c.version())
log.LOGGER.info(c.config().decode())
log.LOGGER.info(c.license().decode())
p = clib.pointer(clib.c_void_p())
while True:
    codec = c.codec_iterate(p)
    if clib.isnullptr(codec):
        break
    log.LOGGER.info(codec.contents.name.decode())
"""
