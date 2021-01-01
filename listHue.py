#!/usr/bin/python
from phue import Bridge
import random

b = Bridge('192.168.1.23') # Enter bridge IP here.

#If running for the first time, press button on bridge and run with b.connect() uncommented
#b.connect()


lights = b.get_light_objects('id')


for light in lights:
    print("id=%d name=%s" %(light, b.get_light(light, 'name')))
