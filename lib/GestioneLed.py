# Usiamo gli ingressi e le uscite digitali
import board
import digitalio
import time

class Led():
    
    def __init__(self, led, tempo):
        self._acceso = True
        self._led = digitalio.DigitalInOut(led)
        self._led.direction = digitalio.Direction.OUTPUT
        self._led.value = False
    
        self._tempo = tempo
        self._timer = time.monotonic() + self._tempo

    def toggle( self ):
        if( (time.monotonic() - self._timer) > 0.0 ):
            self._timer = time.monotonic() + self._tempo
            if( self._acceso ):
                self._acceso = False
            else :
                self._acceso = True 
            
            self._led.value = self._acceso        
