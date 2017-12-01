import twitter
import json

from Models.AuthUsers import Users
from Models.TwitterAuth import TwitterAuth
from Helpers.CustomEvents import Events, Actions
from Helpers.CustomCallers import Callers


class TwitterManager:
    def __init__(self, event_handler=None, rooms=None):
        self.__api = twitter.Api(consumer_key=TwitterAuth.keys['consumer_key'],
                                 consumer_secret=TwitterAuth.keys['consumer_secret'],
                                 access_token_key=TwitterAuth.keys['access_token_key'],
                                 access_token_secret=TwitterAuth.keys['access_token_secret'])

        try:
            self.__message_id = self.__get_message()['id']
        except twitter.error.TwitterError:
            self.__message_id = None

        self.__temperature = None

        self.__events = event_handler

        self.__rooms = rooms

    def __get_message(self):
        return json.loads(str(self.__api.GetDirectMessages()[0]))

    def send_message(self, user_id, message):
        self.__api.PostDirectMessage(text=message, user_id=user_id)

    def send_alarm_message(self, message):
        for user in Users.auth_users:
            self.__api.PostDirectMessage(text=message, user_id=Users.auth_users[user]['user_id'])

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
                self.__events(caller=Callers.TWITTER.value, user=(data['sender']['id']), event=Events.ALARM.value, action=Actions.SET.value, status=True)

            elif text == 'DEACTIVATE ALARM':
                self.__events(caller=Callers.TWITTER.value, user=(data['sender']['id']), event=Events.ALARM.value, action=Actions.SET.value, status=False)

            elif text == 'ALARM STATUS':
                self.__events(caller=Callers.TWITTER.value, user=(data['sender']['id']), event=Events.ALARM.value, action=Actions.GET.value)

            elif text == 'OPEN DOOR':
                self.__events(caller=Callers.TWITTER.value, user=(data['sender']['id']), event=Events.DOOR.value, action=Actions.SET.value, status=True)

            elif text == 'CLOSE DOOR':
                self.__events(caller=Callers.TWITTER.value, user=(data['sender']['id']), event=Events.DOOR.value, action=Actions.SET.value, status=False)

            elif text == 'DOOR STATUS':
                self.__events(caller=Callers.TWITTER.value, user=(data['sender']['id']), event=Events.DOOR.value, action=Actions.GET.value)

            elif text == Events.TEMPERATURE.value:
                self.__events(caller=Callers.TWITTER.value, user=(data['sender']['id']), event=Events.TEMPERATURE.value, action=Actions.GET.value)

            elif text == Events.LIGHTS.value:
                self.__events(caller=Callers.TWITTER.value, user=(data['sender']['id']), event=Events.LIGHTS.value, action='ROOMS_STATUS')

            elif ',' in text:
                try:
                    room = text.split(',')[0]
                    action = text.split(',')[1].strip()
                except KeyError:
                    room = 'Nothing'
                    action = None

                if room in self.__rooms:
                    if action == 'TURN LIGHTS ON':
                        self.__events(caller=Callers.TWITTER.value, user=(data['sender']['id']), event=Events.LIGHTS.value, place=room,
                                      action=Actions.SET.value, status=True)

                    elif action == 'TURN LIGHTS OFF':
                        self.__events(caller=Callers.TWITTER.value, user=(data['sender']['id']), event=Events.LIGHTS.value, place=room,
                                      action=Actions.SET.value, status=False)

                    elif action == 'LIGHTS STATUS':
                        self.__events(caller=Callers.TWITTER.value, user=(data['sender']['id']), event=Events.LIGHTS.value, place=room,
                                      action='ROOM_STATUS')

                    else:
                        self.send_message(data['sender']['id'], action + ' was not recognized')

                else:
                    self.send_message(data['sender']['id'], room + ' was not recognized')

            else:
                self.send_message(data['sender']['id'], 'Command was not recognized.')

            self.__message_id = data['id']
