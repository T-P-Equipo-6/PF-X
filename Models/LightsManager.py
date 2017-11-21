class LightsManager:
    def __init__(self, house_handler=None):
        self.__house = house_handler
        self.__bedroom_light = False
        self.__studio_light = False
        self.__kitchen_light = False
        self.__livingroom_light = False

        self.rooms = {
            'BEDROOM': self.__bedroom_light,
            'STUDIO': self.__studio_light,
            'KITCHEN': self.__kitchen_light,
            'LIVINGROOM': self.__livingroom_light
        }

        self.status = {
            'True': 'ON',
            'False': 'OFF'
        }

        self.phrase = ' LIGHTS ARE '

    def set_lights(self, room, status):
        self.rooms[room] = status
        condition = self.status[str(status)]
        self.__house('LIGHTS', room, condition)
        return room + self.phrase + condition

    def room_status(self, room):
        return room + self.phrase + self.status[str(self.rooms[room])]

    def rooms_status(self):
        message = ''
        for room in self.rooms:
            message = message + '\n' + room + self.phrase + self.status[str(self.rooms[room])]
        return message
