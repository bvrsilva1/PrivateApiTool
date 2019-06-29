import unittest
from engine import Checker


class TestPrivateApi(unittest.TestCase):

    def setUp(self):
        path = '../tests/com.microsoft.office.lync15.apk'
        self.library_path = ['../tests/com.microsoft.office.lync15/lib/armeabi']
        self.architecture = '../tests/com.microsoft.office.lync15/lib/armeabi'
        self.checker = Checker().build('private_api')
        self.checker.path = path

    def test_get_architectures(self):
        self.assertEqual(self.checker.get_architectures(), ['../tests/com.microsoft.office.lync15/lib/armeabi'])

    def test_get_libraries(self):
        libraries = self.checker.get_libraries(self.library_path[0])
        self.assertEqual(len(libraries), 4)
