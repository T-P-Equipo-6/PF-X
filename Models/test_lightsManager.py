from unittest import TestCase
from Models.LightsManager import LightsManager
import sys
sys.tracebacklimit = 0


class TestLightsManager(TestCase):
    def setUp(self):
        print(self._testMethodDoc)

    def test_room_status(self):
        """--Test the Lights Status in a Room"""
        msg = "The status was not returned correctly."
        lights = LightsManager()
        self.assertEqual(lights.room_status('BEDROOM'), 'BEDROOM LIGHTS ARE OFF', msg=msg)
        self.assertEqual(lights.room_status('STUDIO'), 'STUDIO LIGHTS ARE OFF', msg=msg)
        self.assertEqual(lights.room_status('KITCHEN'), 'KITCHEN LIGHTS ARE OFF', msg=msg)
        self.assertEqual(lights.room_status('BATHROOM'), 'BATHROOM LIGHTS ARE OFF', msg=msg)

    def test_set_lights(self):
        """--Test the Lights Setting"""
        msg = "The status was not set correctly."
        lights = LightsManager()
        self.assertEqual(lights.room_status('BEDROOM'), 'BEDROOM LIGHTS ARE OFF', msg=msg)
        lights.set_lights('BEDROOM', True)
        self.assertEqual(lights.room_status('BEDROOM'), 'BEDROOM LIGHTS ARE ON', msg=msg)
        self.assertEqual(lights.room_status('STUDIO'), 'STUDIO LIGHTS ARE OFF', msg=msg)
        lights.set_lights('STUDIO', True)
        self.assertEqual(lights.room_status('STUDIO'), 'STUDIO LIGHTS ARE ON', msg=msg)
        self.assertEqual(lights.room_status('KITCHEN'), 'KITCHEN LIGHTS ARE OFF', msg=msg)
        lights.set_lights('KITCHEN', True)
        self.assertEqual(lights.room_status('KITCHEN'), 'KITCHEN LIGHTS ARE ON', msg=msg)
        self.assertEqual(lights.room_status('BATHROOM'), 'BATHROOM LIGHTS ARE OFF', msg=msg)
        lights.set_lights('BATHROOM', True)
        self.assertEqual(lights.room_status('BATHROOM'), 'BATHROOM LIGHTS ARE ON', msg=msg)

    def test_rooms_status(self):
        """--Test the Lights Setting"""
        msg = "The status of all the rooms was not returned correctly."
        lights = LightsManager()
        self.assertEqual(lights.rooms_status(), '\nBEDROOM LIGHTS ARE OFF\nSTUDIO LIGHTS ARE OFF\nKITCHEN LIGHTS ARE OFF\nBATHROOM LIGHTS ARE OFF', msg=msg)

