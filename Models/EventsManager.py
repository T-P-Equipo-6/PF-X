from twitter import error
from Helpers.CustomEvents import Events, Actions
from Helpers.CustomCallers import Callers


class EventsManager:
    def __init__(self, lights_handler=None, serial_handler=None, twitter_handler=None, buttons_update=None,
                 temperature_handler=None, voice_handler=None, alarm_handler=None, door_handler=None, alarm_button_update=None,
                 door_button_update=None):

        self.__lights = lights_handler
        self.__serial = serial_handler
        self.__twitter = twitter_handler
        self.__buttons_update = buttons_update
        self.__temperature = temperature_handler
        self.__voice = voice_handler
        self.__alarm = alarm_handler
        self.__door = door_handler
        self.__alarm_update = alarm_button_update
        self.__door_update = door_button_update

    def analyze_event(self, caller=None, user=None, event=None, place=None, action=None, status=None):
        if event == Events.LIGHTS.value:
            self.__lights_event(caller=caller, user=user, place=place, action=action, status=status)

        if event == Events.TEMPERATURE.value:
            self.__temperature_event(caller=caller, user=user, place=place, action=action, status=status)

        if event == Events.ALARM.value:
            self.__alarm_event(caller=caller, user=user, place=place, action=action, status=status)

        if event == Events.DOOR.value:
            self.__door_event(caller=caller, user=user, action=action, status=status)

    def __door_event(self, caller=None, user=None, action=None, status=None):

        if action == Actions.SET.value:
            actual_door_status = self.__door.get_door_status()
            if actual_door_status and status:
                return
            if not actual_door_status and not status:
                return

            if status:
                self.__serial('DOORFRONTOPEN')
                self.__door_update(True)
                self.__door.set_door_status(True)

            else:
                self.__serial('DOORFRONTCLOSE')
                self.__door_update(False)
                self.__door.set_door_status(False)

            response = self.__door.get_door_response()
            if caller == Callers.TWITTER.value:
                self.__twitter.send_message(user_id=user, message=response)

            if caller == Callers.VOICE.value:
                self.__voice.say(message=response)

        if action == Actions.GET.value:
            response = self.__door.get_door_response()
            if caller == Callers.TWITTER.value:
                self.__twitter.send_message(user_id=user, message=response)

            if caller == Callers.VOICE.value:
                self.__voice.say(message=response)

    def __lights_event(self, caller=None, user=None, place=None, action=None, status=None):
        response = ''

        if action == Actions.SET.value:
            serial, response = self.__lights.set_lights(room=place, status=status)
            self.__serial(serial)

        if action == 'ROOM_STATUS':
            response = self.__lights.room_status(room=place)

        if action == 'ROOMS_STATUS':
            response = self.__lights.rooms_status()

        if caller == Callers.TWITTER.value:
            self.__buttons_update()
            self.__twitter.send_message(user_id=user, message=response)

        if caller == Callers.VOICE.value:
            self.__buttons_update()
            self.__voice.say(message=response)

    def __temperature_event(self, caller=None, user=None, place=None, action=None, status=None):

        if action == 'FAN':
            if status:
                self.__serial('FANHOUSEON')
                self.__voice.say('The fans were activated.')

            elif not status:
                self.__serial('FANHOUSEOFF')
                self.__voice.say('The fans were deactivated.')

        if action == Actions.GET.value:
            response = self.__temperature.get_temperature()

            if caller == Callers.TWITTER.value:
                self.__twitter.send_message(user_id=user, message=response)

            if caller == Callers.VOICE.value:
                self.__voice.say(message=response)

    def __alarm_event(self, caller=None, user=None, place=None, action=None, status=None):

        if action == Actions.SET.value:
            if status:
                self.__serial('ALARMON')
                self.__alarm.set_alarm(True)
                self.__lights.turn_off_lights()
                self.__voice.say('The alarm has been activated, taking security measures.')
                self.__buttons_update()
                self.__alarm_update(True)

                try:
                    self.__twitter.send_alarm_message(message='The alarm has been activated \n Please take security measures.')
                except error.TwitterError:
                    self.__voice.say('Unable to send Twitter message')

                if caller == Callers.TWITTER.value:
                    self.__alarm_update(True)

                if caller == Callers.VOICE.value:
                    self.__alarm_update(True)

            if not status:
                self.__serial('ALARMOFF')
                self.__alarm.set_alarm(False)
                response = 'The alarm has been deactivated'

                if caller == Callers.TWITTER.value:
                    self.__alarm_update(False)
                    self.__twitter.send_message(user_id=user, message=response)

                if caller == Callers.VOICE.value:
                    self.__alarm_update(False)
                    self.__voice.say(message=response)

        if action == Actions.GET.value:
            response = self.__alarm.alarm_status()

            if caller == Callers.TWITTER.value:
                self.__twitter.send_message(user_id=user, message=response)

            if caller == Callers.VOICE.value:
                self.__voice.say(message=response)







