class EventsManager:
    def __init__(self, lights_handler=None, serial_handler=None, twitter_handler=None, buttons_update=None,
                 temperature_handler=None, voice_handler=None):
        self.__lights = lights_handler
        self.__serial = serial_handler
        self.__twitter = twitter_handler
        self.__buttons_update = buttons_update
        self.__temperature = temperature_handler
        self.__voice = voice_handler

    def analyze_event(self,caller=None, user=None, event=None, place=None, action=None, status=None):
        if event == 'LIGHTS':
            self.__lights_event(caller=caller, user=user, place=place, action=action, status=status)

        if event == 'TEMPERATURE':
            self.__temperature_event(caller=caller, user=user, place=place, action=action, status=status)

        if event == 'ALARM':
            self.__alarm_event(caller=caller, user=user, place=place, action=action, status=status)

    def __lights_event(self, caller=None, user=None, place=None, action=None, status=None):
        response = ''

        if action == 'SET':
            serial, response = self.__lights.set_lights(room=place, status=status)
            self.__serial(serial)

        if action == 'ROOM_STATUS':
            response = self.__lights.room_status(room=place)

        if action == 'ROOMS_STATUS':
            response = self.__lights.rooms_status()

        if caller == 'TWITTER':
            self.__buttons_update()
            self.__twitter.send_message(user_id=user, message=response)

        if caller == 'VOICE':
            self.__buttons_update()
            self.__voice.say(message=response)

    def __temperature_event(self, caller=None, user=None, place=None, action=None, status=None):

        if action == 'FAN':
            if status:
                self.__serial('FANHOUSEON')

            elif not status:
                self.__serial('FANHOUSEOFF')

        if action == 'GET':
            response = self.__temperature.get_temperature()

            if caller == 'TWITTER':
                self.__twitter.send_message(user_id=user, message=response)

            if caller == 'VOICE':
                self.__voice.say(message=response)


    def __alarm_event(self, caller=None, user=None, place=None, action=None, status=None):

        if action == 'ACTIVATE':
            self.__twitter.send_alarm_message(message='The alarm has been activated \n Taking security measures.')




