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
import logging

LOGLEVEL = logging.DEBUG
MOUNTPATH = "test"
APP = "v4l2codecs"
VERSION_MAJOR = 3
VERSION_MINOR = 0
VERSION_PATCH = 1
VERSION = f"{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATCH}"
VERSION_INT = VERSION_MAJOR << 16 | VERSION_MINOR << 8 | VERSION_PATCH
V4L2_DEV_MAJOR = 81
