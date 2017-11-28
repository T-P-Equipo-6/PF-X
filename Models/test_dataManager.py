from unittest import TestCase
from Models.DataManager import DataManager
import sys
sys.tracebacklimit = 0


class TestDataManager(TestCase):
    def setUp(self):
        print(self._testMethodDoc)

    def test_analyze_data(self):
        """--Test Analize Data"""
        msg = "The data is not being correctly analyzed."
        data = DataManager()
        self.assertEqual(data.analyze_data('holi'), None, msg=msg)
