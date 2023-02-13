import time
import board
import GestioneLed

led1 = GestioneLed.Led( board.LED, 0.1 )
led2 = GestioneLed.Led( board.GP20, 0.5 )

while True:
    led1.toggle()
    led2.toggle()

