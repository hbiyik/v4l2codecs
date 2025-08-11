import errno
from .cuse import CuseThread


class Cuse:
    ioctls = {}

    def __init__(self, name, major=None, minor=None, debug=True):
        self.cuse = CuseThread(self, name, major, minor, self.ioctls, debug)

    def ioctl(self, handler, cmd, data):
        return errno.EINVAL

    def open(self, handler):
        return

    def release(self, handler):
        return 0
