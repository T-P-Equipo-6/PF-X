from unittest import TestCase
from Models.AlarmManager import AlarmManager
import sys
sys.tracebacklimit = 0


class TestAlarmManager(TestCase):
    def setUp(self):
        print(self._testMethodDoc)

    def test_alarm_status(self):
        """--Test Alarm Status"""
        msg = "The alarm is not being correctly set."
        alarm = AlarmManager()
        self.assertEqual(alarm.alarm_status, False, msg=msg)
        self.assertEqual(alarm.set_alarm(True), None, msg=msg)
        self.assertEqual(alarm.alarm_status, True, msg=msg)

