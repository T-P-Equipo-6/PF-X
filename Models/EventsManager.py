class EventsManager:
    def __init__(self, lights_handler=None, serial_handler=None, twitter_handler=None):
        self.__lights = lights_handler
        self.__serial = serial_handler
        self.__twitter = twitter_handler

    def analyze_event(self,caller=None, user=None, object=None, place=None, action=None, status=None):
        if object == 'LIGHTS':
            self.__lights_event(caller=caller, user=user, place=place, action=action, status=status)

    def __lights_event(self, caller=None, user=None, place=None, action=None, status=None):
        if action == 'SET':
            serial, response = self.__lights.set_lights(room=place, status=status)
            self.__serial(serial)

        if action == 'ROOM_STATUS':
            response = self.__lights.room_status(room=place)

        if action == 'ROOMS_STATUS':
            response = self.__lights.rooms_status()

        if caller == 'TWITTER':
            self.__twitter.send_message(user_id=user, message=response)

