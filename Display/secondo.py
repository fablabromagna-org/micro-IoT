import time
import board

# Usiamo gli ingressi e le uscite digitali
from digitalio import DigitalInOut, Direction, Pull

# Switch setup
switch = DigitalInOut(board.GP5)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

# Display 7 segmenti
import TM1637
sevenSeg_CLK = board.GP20
sevenSeg_DIO = board.GP21
sevenSeg = TM1637.TM1637(sevenSeg_CLK, sevenSeg_DIO)
sevenSeg.write([0b00111001, 0b00111111, 0b00111111, 0b00111000])
time.sleep(2)

contatore=0
while True:
    if switch.value == True:
        contatore = contatore + 1   
        sevenSeg.number(contatore)
        #time.sleep(0.7)
        while switch.value == True:
            pass
        time.sleep(0.04)