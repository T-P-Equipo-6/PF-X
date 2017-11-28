from unittest import TestCase
from Models.TemperatureManager import TemperatureManager
import sys
sys.tracebacklimit = 0

class TestTemperatureManager(TestCase):
    def setUp(self):
        print(self._testMethodDoc)

    def test_to_celcius(self):
        """--Test the Conversion to Celcius"""
        msg = "The temperature is not being correctly conversed."
        temperature = TemperatureManager()
        self.assertEqual(temperature.to_celsius(100), 48.87585532746823, msg=msg)

    def test_get_temperature(self):
        """--Test the Return of the Actual Temperature"""
        msg = "The temperature is not being correctly returned."
        temperature = TemperatureManager()
        self.assertEqual(temperature.get_temperature(), 'NO TEMPERATURE DATA', msg=msg)