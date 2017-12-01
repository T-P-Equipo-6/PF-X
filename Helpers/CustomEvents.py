from enum import Enum


class Events(Enum):
    ALARM = 'ALARM'
    LIGHTS = 'LIGHTS'
    DOOR = 'DOOR'
    TEMPERATURE = 'TEMPERATURE'


class Actions(Enum):
    SET = 'SET'
    GET = 'GET'