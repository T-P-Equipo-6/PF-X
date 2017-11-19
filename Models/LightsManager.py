class LightsManager:
    def __init__(self):
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
            'True': ' LIGHTS ARE ON',
            'False': ' LIGHTS ARE OFF'
        }

    def set_lights(self, room, status):
        self.rooms[room] = status
        return room + self.status[str(status)]

    def room_status(self, room):
        return room + self.status[str(self.rooms[room])]

    def rooms_status(self):
        message = ''
        for room in self.rooms:
            message = message + '\n' + room + self.status[str(self.rooms[room])]
        return message
