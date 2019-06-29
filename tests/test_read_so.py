import unittest
from helper import ReadLibraryHelper


class TestReadSo(unittest.TestCase):

    def setUp(self):
        self.path = '../tests/com.microsoft.office.lync15/lib/armeabi/librtcqcomhwcodec.so'
        self.reader = ReadLibraryHelper()

    def test_read_so(self):
        result = self.reader.read_library_so(self.path)
        self.assertEqual(result, ['libutils.so', 'libstagefright.so', 'libmedia.so', 'libbinder.so', 'liblog.so', 'libstdc++.so', 'libm.so', 'libc.so', 'libdl.so'])