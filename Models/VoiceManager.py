from Models.VoiceAuth import VoiceAuth
from Helpers.CustomEvents import Events, Actions
from Helpers.CustomCallers import Callers
import speech_recognition as sr
import pyttsx3


class VoiceCommands:
    def __init__(self, event_handler=None, rooms=None):
        self.engine = pyttsx3.init()
        self.engine.startLoop(False)
        self.engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
        self.r = sr.Recognizer()

        self.key = VoiceAuth.key

        self.__events = event_handler
        self.__rooms = rooms

        self.actions = ['turn', 'activate', 'deactivate', 'status', 'open', 'close']

        self.objects = {
            'lights',
            'alarm',
            'door',
            'temperature'
        }

        self.status = ['on', 'off']

    def run(self):

            audio = self.listen()
            self.say('Processing...')
            try:
                data = self.recognize_audio(audio)
            except TypeError:
                data = None

            if not data:
                self.say("Sorry, I didn't understand you")

            try:
                action = data['entities']['action'][0]['value']
            except KeyError:
                action = 'None'

            try:
                object = data['entities']['object'][0]['value']
            except KeyError:
                object = 'None'

            try:
                status = data['entities']['status'][0]['value']
            except KeyError:
                status = 'None'

            try:
                place = data['entities']['place'][0]['value']
            except KeyError:
                place = 'None'

            if action in self.actions:

                if action == 'activate' and object == 'alarm':
                    self.__events(caller=Callers.VOICE.value, event=Events.ALARM.value, action=Actions.SET.value, status=True)

                elif action == 'deactivate' and object == 'alarm':
                    self.__events(caller=Callers.VOICE.value, event=Events.ALARM.value, action=Actions.SET.value, status=False)

                elif action == 'open' and object == 'door':
                    self.__events(caller=Callers.VOICE.value, event=Events.DOOR.value, action=Actions.SET.value, status=True)

                elif action == 'close' and object == 'door':
                    self.__events(caller=Callers.VOICE.value, event=Events.DOOR.value, action=Actions.SET.value, status=False)

                elif action == 'status' and object in self.objects:
                    self.validate_status(object, place)

                elif action == 'turn' and object == 'lights' and status in self.status and place.upper() in self.__rooms:
                    self.validate_turn(status=status, place=place.upper())

                else:
                    self.say("I was unable to fullfill the command.")

            else:
                self.say("Sorry, I didn't understand any command.")

    def listen(self):
        with sr.Microphone() as source:
            return self.r.listen(source)

    def say(self, message):
        self.engine.say(message)
        self.engine.iterate()

    def recognize_audio(self, audio):
        try:
            return self.r.recognize_wit(audio, key=self.key, show_all=True)
        except sr.UnknownValueError:
            print("Wit.ai was unable to understand audio")
            return None
        except sr.RequestError as e:
            print("Could not request results from Wit.ai service; {0}".format(e))
            return None

    def validate_status(self, object, place):
        if object == 'lights':
            if place is not None:
                self.__events(caller=Callers.VOICE.value, event=Events.LIGHTS.value, place=place.upper(), action='ROOM_STATUS')
            else:
                self.say('From which room you want to know?')
                audio = self.listen()
                data = self.recognize_audio(audio)

                try:
                    room = data['entities']['place'][0]['value']
                except KeyError:
                    room = None
                if room in self.__rooms:
                    self.__events(caller=Callers.VOICE.value, event=Events.LIGHTS.value, place=room.upper(), action='ROOM_STATUS')
                else:
                    self.say("Sorry, I didn't understand that room")

        if object == 'temperature':
            self.__events(caller=Callers.VOICE.value, event=Events.TEMPERATURE.value, action=Actions.GET.value)

        if object == 'door':
            self.__events(caller=Callers.VOICE.value, event=Events.DOOR.value, action=Actions.GET.value)

    def validate_turn(self, status, place):
        if status == 'on':
            self.__events(caller=Callers.VOICE.value, event=Events.LIGHTS.value, place=place, action=Actions.SET.value, status=True)
        if status == 'off':
            self.__events(caller=Callers.VOICE.value, event=Events.LIGHTS.value, place=place, action=Actions.SET.value, status=False)


if __name__ == "__main__":
    app = VoiceCommands()
    app.run()
