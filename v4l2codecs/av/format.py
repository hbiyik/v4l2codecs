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

from v4l2codecs import clib
from v4l2codecs.av import util
from v4l2codecs.av import codec


class EnumIODataMarkerType(clib.c_intenum):
    class _enum_:
        AVIO_DATA_MARKER_HEADER = 0
        AVIO_DATA_MARKER_SYNC_POINT = enum.auto()
        AVIO_DATA_MARKER_BOUNDARY_POINT = enum.auto()
        AVIO_DATA_MARKER_UNKNOWN = enum.auto()
        AVIO_DATA_MARKER_TRAILER = enum.auto()
        AVIO_DATA_MARKER_FLUSH_POINT = enum.auto()


class EnumDurationEstimationMethod(clib.c_intenum):
    class _enum_:
        PTS = 0
        STREAM = enum.auto()
        BITRATE = enum.auto()


class EnumStreamGroupParamsType(clib.c_intenum):
    class _enum_:
        NONE = 0
        IAMF_AUDIO_ELEMENT = enum.auto()
        IAMF_MIX_PRESENTATION = enum.auto()
        TILE_GRID = enum.auto()
        LCEVC = enum.auto()


class StructStream(clib.Structure):
    _fields_ = [
        ('av_class', clib.POINTER(util.StructClass)),
        ('index', clib.c_int),
        ('id', clib.c_int),
        ('codecpar', clib.POINTER(codec.StructCodecParameters)),
        ('priv_data', clib.c_void_p),
        ('time_base', util.StructRational),
        ('start_time', clib.c_int64),
        ('duration', clib.c_int64),
        ('nb_frames', clib.c_int64),
        ('disposition', clib.c_int),
        ('discard', codec.EnumDiscard),
        ('sample_aspect_ratio', util.StructRational),
        ('metadata', clib.c_void_p),
        ('avg_frame_rate', util.StructRational),
        ('attached_pic', codec.StructPacket),
        ('side_data', clib.c_void_p),
        ('nb_side_data', clib.c_int),
        ('event_flags', clib.c_int),
        ('r_frame_rate', util.StructRational),
        ('pts_wrap_bits', clib.c_int),
    ]


class StructIAMFAudioElement(clib.Structure):
    pass


class StructIAMFMixPresentation(clib.Structure):
    pass


class StructStreamGroupTileGrid(clib.Structure):
    class _union_offsets_(clib.Union):
        _fields_ = [
            ('idx', clib.c_uint),
            ('horizontal', clib.c_int),
            ('vertical', clib.c_int),]

    _fields_ = [
        ('av_class', clib.POINTER(util.StructClass)),
        ('nb_tiles', clib.c_uint),
        ('coded_width', clib.c_int),
        ('coded_height', clib.c_int),
        ('offsets', clib.POINTER(_union_offsets_)),
        ('background', clib.c_uint8 * int(4)),
        ('horizontal_offset', clib.c_int),
        ('vertical_offset', clib.c_int),
        ('width', clib.c_int),
        ('height', clib.c_int)]


class StructStreamGroupLCEVC(clib.Structure):
    _fields_ = [
        ('av_class', clib.POINTER(util.StructClass)),
        ('lcevc_index', clib.c_uint),
        ('width', clib.c_int),
        ('height', clib.c_int),
    ]


class StructStreamGroup(clib.Structure):
    class _union_params_(clib.Union):
        _fields_ = [
            ('iamf_audio_element', clib.POINTER(StructIAMFAudioElement)),
            ('iamf_mix_presentation', clib.POINTER(StructIAMFMixPresentation)),
            ('tile_grid', clib.POINTER(StructStreamGroupTileGrid)),
            ('lcevc', clib.POINTER(StructStreamGroupLCEVC))]

    _fields_ = [
        ('av_class', clib.POINTER(util.StructClass)),
        ('priv_data', clib.c_void_p),
        ('index', clib.c_uint),
        ('id', clib.c_int64),
        ('type', EnumStreamGroupParamsType),
        ('params', _union_params_),
        ('metadata', clib.c_void_p),
        ('nb_streams', clib.c_uint),
        ('streams', clib.POINTER(clib.POINTER(StructStream))),
        ('disposition', clib.c_int),
    ]


class StructIOContext(clib.Structure):
    class _callbacks_(clib.Lib):
        @clib.Lib.Signature("read_packet", clib.c_void_p, clib.POINTER(clib.c_uint8), clib.c_int)
        def read_packet(self, opaque, buf, buf_size):
            return clib.c_int

        @clib.Lib.Signature("write_packet", clib.c_void_p, clib.POINTER(clib.c_uint8), clib.c_int)
        def write_packet(self, opaque, buf, buf_size):
            return clib.c_int

        @clib.Lib.Signature("seek", clib.c_void_p, clib.c_int64, clib.c_int)
        def seek(self, opaque, buf, buf_size):
            return clib.c_int64

        @clib.Lib.Signature("update_checksum", clib.c_ulong, clib.POINTER(clib.c_uint8), clib.c_uint)
        def update_checksum(self, checksum, buf, size):
            return clib.c_ulong

        @clib.Lib.Signature("read_pause", clib.c_void_p, clib.c_int)
        def read_pause(self, opaque, pause):
            return clib.c_int

        @clib.Lib.Signature("read_seek", clib.c_void_p, clib.c_int, clib.c_int64, clib.c_int)
        def read_seek(self, opaque, streamindex, timestamp, flags):
            return clib.c_int64

        @clib.Lib.Signature("write_data_type", clib.c_void_p, clib.POINTER(clib.c_uint8), clib.c_int, EnumIODataMarkerType, clib.c_int64)
        def write_data_type(self, opaque, buf, buf_size, typ, time):
            return clib.c_int

    _fields_ = [
        ('av_class', clib.POINTER(codec.StructContext)),
        ('buffer', clib.POINTER(clib.c_ubyte)),
        ('buffer_size', clib.c_int),
        ('buf_ptr', clib.POINTER(clib.c_ubyte)),
        ('buf_end', clib.POINTER(clib.c_ubyte)),
        ('opaque', clib.c_void_p),
        ('read_packet', _callbacks_.functype(_callbacks_.read_packet)),
        ('write_packet', _callbacks_.functype(_callbacks_.write_packet)),
        ('seek', _callbacks_.functype(_callbacks_.seek)),
        ('pos', clib.c_int64),
        ('eof_reached', clib.c_int),
        ('error', clib.c_int),
        ('write_flag', clib.c_int),
        ('max_packet_size', clib.c_int),
        ('min_packet_size', clib.c_int),
        ('checksum', clib.c_ulong),
        ('checksum_ptr', clib.POINTER(clib.c_ubyte)),
        ('update_checksum', _callbacks_.functype(_callbacks_.update_checksum)),
        ('read_pause', _callbacks_.functype(_callbacks_.read_pause)),
        ('read_seek', _callbacks_.functype(_callbacks_.read_seek)),
        ('seekable', clib.c_int),
        ('direct', clib.c_int),
        ('protocol_whitelist', clib.c_char_p),
        ('protocol_blacklist', clib.c_char_p),
        ('write_data_type',_callbacks_.functype(_callbacks_.write_data_type)),
        ('ignore_boundary_point', clib.c_int),
        ('buf_ptr_max', clib.POINTER(clib.c_ubyte)),
        ('bytes_read', clib.c_int64),
        ('bytes_written', clib.c_int64),
    ]


class StructOutputFormat(clib.Structure):
    _fields_ = [
        ('name', clib.c_char_p),
        ('long_name', clib.c_char_p),
        ('mime_type', clib.c_char_p),
        ('extensions', clib.c_char_p),
        ('audio_codec', codec.EnumCodecID),
        ('video_codec', codec.EnumCodecID),
        ('subtitle_codec', codec.EnumCodecID),
        ('flags', clib.c_int),
        ('codec_tag', clib.POINTER(clib.c_void_p)),
        ('priv_class', clib.POINTER(util.StructClass)),
    ]


class StructInputFormat(clib.Structure):
    _fields_ = [
        ('name', clib.c_char_p),
        ('long_name', clib.c_char_p),
        ('flags', clib.c_int),
        ('extensions', clib.c_char_p),
        ('codec_tag', clib.POINTER(clib.c_void_p)),
        ('priv_class', clib.POINTER(util.StructClass)),
        ('mime_type', clib.c_char_p)]


class StructChapter(clib.Structure):
    _fields_ = [
        ('id', clib.c_int64),
        ('time_base', util.StructRational),
        ('start', clib.c_int64),
        ('end', clib.c_int64),
        ('metadata', clib.c_void_p),
    ]


class StructProgram(clib.Structure):
    _fields_ = [
        ('id', clib.c_int),
        ('flags', clib.c_int),
        ('discard', codec.EnumDiscard),
        ('stream_index', clib.POINTER(clib.c_uint)),
        ('nb_stream_indexes', clib.c_uint),
        ('metadata', clib.c_void_p),
        ('program_num', clib.c_int),
        ('pmt_pid', clib.c_int),
        ('pcr_pid', clib.c_int),
        ('pmt_version', clib.c_int),
        ('start_time', clib.c_int64),
        ('end_time', clib.c_int64),
        ('pts_wrap_reference', clib.c_int64),
        ('pts_wrap_behavior', clib.c_int),
    ]


class StructIOInterruptCB(clib.Structure):
    class _callbacks_(clib.Lib):
        @clib.Lib.Signature("callback", clib.c_void_p)
        def callback(self, opaque):
            return clib.c_int

    _fields_ = [
        ('callback', _callbacks_.functype(_callbacks_.callback)),
        ('opaque', clib.c_void_p),
    ]


class StructContext(clib.Structure):
    pass


class _StructContext_callbacks_(clib.Lib):
    @clib.Lib.Signature("io_open",
                        clib.POINTER(StructContext),
                        clib.POINTER(clib.POINTER(StructIOContext)),
                        clib.c_char_p, clib.c_int,
                        clib.POINTER(clib.c_void_p))
    def io_open(self, s, pb, url, flags, options):
        return clib.c_int

    @clib.Lib.Signature("io_close2", clib.POINTER(StructContext), clib.POINTER(StructIOContext))
    def io_close2(self, s, pb):
        return clib.c_int

    @clib.Lib.Signature("control_message", clib.POINTER(StructContext), clib.c_int, clib.c_void_p, clib.c_size_t)
    def control_message(self, s, typ, data, data_size):
        return clib.c_int


StructContext._callbacks_ = _StructContext_callbacks_
StructContext._fields_ = [
    ('av_class', clib.POINTER(util.StructClass)),
    ('iformat', clib.POINTER(StructInputFormat)),
    ('oformat', clib.POINTER(StructOutputFormat)),
    ('priv_data', clib.c_void_p),
    ('pb', clib.POINTER(StructIOContext)),
    ('ctx_flags', clib.c_int),
    ('nb_streams', clib.c_uint),
    ('streams', clib.POINTER(clib.POINTER(StructStream))),
    ('nb_stream_groups', clib.c_uint),
    ('stream_groups', clib.POINTER(clib.POINTER(StructStreamGroup))),
    ('nb_chapters', clib.c_uint),
    ('chapters', clib.POINTER(clib.POINTER(StructChapter))),
    ('url', clib.c_char_p),
    ('start_time', clib.c_int64),
    ('duration', clib.c_int64),
    ('bit_rate', clib.c_int64),
    ('packet_size', clib.c_uint),
    ('max_delay', clib.c_int),
    ('flags', clib.c_int),
    ('probesize', clib.c_int64),
    ('max_analyze_duration', clib.c_int64),
    ('key', clib.POINTER(clib.c_uint8)),
    ('keylen', clib.c_int),
    ('nb_programs', clib.c_uint),
    ('programs', clib.POINTER(clib.POINTER(StructProgram))),
    ('video_codec_id', codec.EnumCodecID),
    ('audio_codec_id', codec.EnumCodecID),
    ('subtitle_codec_id', codec.EnumCodecID),
    ('data_codec_id', codec.EnumCodecID),
    ('metadata', clib.c_void_p),
    ('start_time_realtime', clib.c_int64),
    ('fps_probe_size', clib.c_int),
    ('error_recognition', clib.c_int),
    ('interrupt_callback', StructIOInterruptCB),
    ('debug', clib.c_int),
    ('max_streams', clib.c_int),
    ('max_index_size', clib.c_uint),
    ('max_picture_buffer', clib.c_uint),
    ('max_interleave_delta', clib.c_int64),
    ('max_ts_probe', clib.c_int),
    ('max_chunk_duration', clib.c_int),
    ('max_chunk_size', clib.c_int),
    ('max_probe_packets', clib.c_int),
    ('strict_std_compliance', clib.c_int),
    ('event_flags', clib.c_int),
    ('avoid_negative_ts', clib.c_int),
    ('audio_preload', clib.c_int),
    ('use_wallclock_as_timestamps', clib.c_int),
    ('skip_estimate_duration_from_pts', clib.c_int),
    ('avio_flags', clib.c_int),
    ('duration_estimation_method', EnumDurationEstimationMethod),
    ('skip_initial_bytes', clib.c_int64),
    ('correct_ts_overflow', clib.c_uint),
    ('seek2any', clib.c_int),
    ('flush_packets', clib.c_int),
    ('probe_score', clib.c_int),
    ('format_probesize', clib.c_int),
    ('codec_whitelist', clib.c_char_p),
    ('format_whitelist', clib.c_char_p),
    ('protocol_whitelist', clib.c_char_p),
    ('protocol_blacklist', clib.c_char_p),
    ('io_repositioned', clib.c_int),
    ('video_codec', clib.POINTER(codec.StructCodec)),
    ('audio_codec', clib.POINTER(codec.StructCodec)),
    ('subtitle_codec', clib.POINTER(codec.StructCodec)),
    ('data_codec', clib.POINTER(codec.StructCodec)),
    ('metadata_header_padding', clib.c_int),
    ('opaque', clib.c_void_p),
    ('control_message_cb', StructContext._callbacks_.functype(StructContext._callbacks_.control_message)),
    ('output_ts_offset', clib.c_int64),
    ('dump_separator', clib.POINTER(clib.c_uint8)),
    ('io_open', StructContext._callbacks_.functype(StructContext._callbacks_.io_open)),
    ('io_close2', StructContext._callbacks_.functype(StructContext._callbacks_.io_close2)),
    ('duration_probesize', clib.c_int64)]
