import unittest
from database import Database


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database()
        self.database = self.db.build_database()

    def test_size_database(self):
        self.assertEqual(len(self.database), 5)

    def test_api24_has_libOpenMAXAL(self):
        self.assertTrue('libOpenMAXAL.so' in self.database['android-24'])

    def test_api24_doesnt_have_libneuralnetworks(self):
        self.assertTrue('libneuralnetworks.so' not in self.database['android-24'])

    def test_api29_has_libneuralnetworks(self):
        self.assertTrue('libneuralnetworks.so' in self.database['android-29'])