class DoorManager:
    def __init__(self):
        self.door_status = False

    def set_door_status(self, status):
        self.door_status = status

    def get_door_status(self):
        return self.door_status

    def get_door_response(self):
        if self.door_status:
            return 'THE DOOR IS OPEN'
        else:
            return 'THE DOOR IS CLOSE'
