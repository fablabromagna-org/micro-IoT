#
# Semplice tastiera MIDI con due pulsanti per testare OBS
# maurizio.conti@fablabromagna.org
# 12 dicembre 2023
#

import board
import time
import busio
import random
from simpleio import map_range
from digitalio import DigitalInOut, Direction, Pull


#MIDI
import usb_midi
import adafruit_midi
from adafruit_midi.note_on          import NoteOn
from adafruit_midi.note_off         import NoteOff
from adafruit_midi.control_change   import ControlChange
    
#
# Si parte
#
print("USB MIDI controller by FabLab Romagna 2023" )
       

# Configuro il pulsante 1
btn1 = DigitalInOut(board.GP1)
btn1.direction = Direction.INPUT

# Configuro il pulsante 5
btn5 = DigitalInOut(board.GP5)
btn5.direction = Direction.INPUT

# Configuro il led a bordo
led25 = DigitalInOut(board.GP25)
led25.direction = Direction.OUTPUT

#  MIDI setup as MIDI out and in device
midi = adafruit_midi.MIDI(
    midi_in=usb_midi.ports[0],
    in_channel=0,
    midi_out=usb_midi.ports[1],
    out_channel=0
)

while True:
    if btn1.value:
        print("btn1" )
        midi.send(NoteOn(60))
        while btn1.value:
            pass
        midi.send(NoteOff(60))

    if btn5.value:
        print("btn5" )
        midi.send(NoteOn(61))
        while btn5.value:
            pass
        midi.send(NoteOff(61))

    time.sleep(0.1)

