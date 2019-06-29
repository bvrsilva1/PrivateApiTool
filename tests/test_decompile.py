import unittest
import pathlib
from helper import DecompileHelper


class TestPrivateApi(unittest.TestCase):

    def setUp(self):

        self.apk_path = '../tests/com.microsoft.office.lync15.apk'
        self.decompiled_path = '../tests/com.microsoft.office.lync15/'
        self.lib_path = '../tests/com.microsoft.office.lync15/lib/'
        self.decompiler = DecompileHelper()

    def test_decompile(self):
        self.decompiler.decompile(self.apk_path)
        self.assertTrue(pathlib.Path(self.lib_path).exists())

    def test_has_decompiled_apk(self):
        self.assertTrue(self.decompiler.decompiled_apk(self.apk_path), self.decompiled_path)