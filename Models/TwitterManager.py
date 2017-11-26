import twitter
import json

from Models.AuthUsers import Users
from Models.TwitterAuth import TwitterAuth


class TwitterManager():
    def __init__(self, event_handler=None, rooms=None):
        self.__api = twitter.Api(consumer_key=TwitterAuth.keys['consumer_key'],
                                 consumer_secret=TwitterAuth.keys['consumer_secret'],
                                 access_token_key=TwitterAuth.keys['access_token_key'],
                                 access_token_secret=TwitterAuth.keys['access_token_secret'])

        try:
            self.__message_id = self.__get_message()['id']
        except twitter.error.TwitterError:
            self.__message_id = None

        self.alarm_status = False

        self.door_status = False

        self.__temperature = None

        self.__events = event_handler

        self.__rooms = rooms

    def __get_message(self):
        return json.loads(str(self.__api.GetDirectMessages()[0]))

    def send_message(self, user_id, message):
        self.__api.PostDirectMessage(text=message, user_id=user_id)

    def run(self):

        if not self.__message_id:
            try:
                self.__message_id = self.__get_message()['id']
            except twitter.error.TwitterError:
                self.__message_id = None
                print('Twitter temporarily unavailable')
                return

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
                self.__events(caller='TWITTER', user=(data['sender']['id']), event='TEMPERATURE', action='GET')

            elif text == 'LIGHTS':
                self.__events(caller='TWITTER', user=(data['sender']['id']), event='LIGHTS', action='ROOMS_STATUS')

            elif ',' in text:
                try:
                    room = text.split(',')[0]
                    action = text.split(',')[1].strip()
                except KeyError:
                    room = 'Nothing'
                    action = None

                if room in self.__rooms:
                    if action == 'TURN LIGHTS ON':
                        self.__events(caller='TWITTER', user=(data['sender']['id']), event='LIGHTS', place=room,
                                      action='SET', status=True)

                    elif action == 'TURN LIGHTS OFF':
                        self.__events(caller='TWITTER', user=(data['sender']['id']), event='LIGHTS', place=room,
                                      action='SET', status=False)

                    elif action == 'LIGHTS STATUS':
                        self.__events(caller='TWITTER', user=(data['sender']['id']), event='LIGHTS', place=room,
                                      action='ROOM_STATUS')

                    else:
                        self.send_message(data['sender']['id'], action + ' was not recognized')

                else:
                    self.send_message(data['sender']['id'], room + ' was not recognized')

            else:
                self.send_message(data['sender']['id'], 'Command was not recognized.')

            self.__message_id = data['id']
