
import digitalio


class GestioneLed:
    
    def init(self, led):
        self.led=digitalio.DigitalInOut(led)
        self.led.direction = digitalio.Direction.OUTPUT

        self.acceso = True
        self.led.value = self.acceso
    
    def toggle():
        if( self.acceso ):
            self.acceso = false
        else:
            self.acceso=True 

        self.led.value = self.acceso
     