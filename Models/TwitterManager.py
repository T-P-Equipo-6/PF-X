import twitter
import json

from Models.AuthUsers import Users
from Models.TwitterAuth import TwitterAuth


class TwitterManager():
    def __init__(self, lights_manager=None):
        self.__api = twitter.Api(consumer_key=TwitterAuth.keys['consumer_key'],
                                 consumer_secret=TwitterAuth.keys['consumer_secret'],
                                 access_token_key=TwitterAuth.keys['access_token_key'],
                                 access_token_secret=TwitterAuth.keys['access_token_secret'])

        self.__message_id = self.__get_message()['id']

        self.alarm_status = False

        self.door_status = False

        self.__temperature = None

        self.__lights = lights_manager

    def __get_message(self):
        return json.loads(str(self.__api.GetDirectMessages()[0]))

    def send_message(self, user_id, message):
        self.__api.PostDirectMessage(text=message, user_id=user_id)

    def set_temperature(self, temperature_value):
        self.__temperature = temperature_value

    def set_light_status(self, room, status):
        place = self.rooms[room]
        place = status

    def run(self):
        data = self.__get_message()

        if self.__message_id != data['id'] and data['sender']['screen_name'] in Users.auth_users:
            text = data['text'].upper()

            if text == 'HI':
                self.send_message(data['sender']['id'], 'Hi ' + data['sender']['name'])

            elif text == 'ACTIVATE ALARM':
                if not self.alarm_status:
                    self.alarm_status = True
                self.send_message(data['sender']['id'], 'The alarm is activated.')

            elif text == 'DEACTIVATE ALARM':
                if self.alarm_status:
                    self.alarm_status = False
                self.send_message(data['sender']['id'], 'The alarm is deactivated.')

            elif text == 'ALARM STATUS':
                self.send_message(data['sender']['id'], 'Alarm status: ' + str(self.alarm_status))

            elif text == 'OPEN DOOR':
                if not self.door_status:
                    self.door_status = True
                self.send_message(data['sender']['id'], 'The door is open.')

            elif text == 'CLOSE DOOR':
                if self.door_status:
                    self.door_status = False
                self.send_message(data['sender']['id'], 'The door is close.')

            elif text == 'DOOR STATUS':
                self.send_message(data['sender']['id'], 'Door status: ' + str(self.door_status))

            elif text == 'TEMPERATURE':
                self.send_message(data['sender']['id'], str(self.temperature) + 'º C')

            elif text == 'LIGHTS':
                message = str(self.__lights.rooms_status())
                self.send_message(data['sender']['id'], message)

            elif ',' in text:
                try:
                    room = text.split(',')[0]
                    action = text.split(',')[1].strip()
                except KeyError:
                    room = 'Nothing'
                    action = None

                if room in self.__lights.rooms:
                    if action == 'TURN LIGHTS ON':
                        message = self.__lights.set_lights(room, True)
                        self.send_message(data['sender']['id'], message)

                    elif action == 'TURN LIGHTS OFF':
                        message = self.__lights.set_lights(room, False)
                        self.send_message(data['sender']['id'], message)

                    elif action == 'LIGHTS STATUS':
                        message = self.__lights.room_status(room)
                        self.send_message(data['sender']['id'], message)

                    else:
                        self.send_message(data['sender']['id'], action + ' was not recognized')

                else:
                    self.send_message(data['sender']['id', room + ' was not recognized'])

            else:
                self.send_message(data['sender']['id'], 'Command was not recognized.')

            print(text)
            self.__message_id = data['id']
