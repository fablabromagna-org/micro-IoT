#Raspberry Pi Pico Version

import board, busio
from adafruit_st7735r import ST7735R
import terminalio
import displayio
from gauge import Gauge #get the library here: https://github.com/benevpi/Circuit-Python-Gauge
from adafruit_display_text.label import Label

clk_pin=board.GP2
sda_pin=board.GP3      #mosi
reset_pin=board.GP4 
cs_pin=board.GP5
A0_pin=board.GP16

# Release any resources currently in use for the displays
displayio.release_displays()
spi = busio.SPI( clock=clk_pin, MOSI=sda_pin )

# servono cinque  fili...
# clk e sda sono su SPI, gli altri tre spare
display_bus = displayio.FourWire(
    spi,
    command=A0_pin,
    reset=reset_pin,
    chip_select=cs_pin
)

display = ST7735R(display_bus, width=160, height=128, rotation=90, bgr=True)

l1 = Label(terminalio.FONT, text="0.0", color=0xFFFFFF)
l1.x = 100
l1.y = 100

gauge = Gauge( 0, 100, 64, 80, value_label="x:", arc_colour=0xFF0000, colour=0xFFFF00, outline_colour=0xFFFF00)
gauge.x = 0
gauge.y = 0

gauge2 = Gauge( 0, 100, 64, 80, value_label="y:", arc_colour=0xFF0000, colour=0xFFFF00, outline_colour=0xFFFF00)
gauge2.x = 64
gauge2.y = 0

group = displayio.Group( scale=1 )

group.append(gauge)
group.append(gauge2)
group.append( l1 )

display.show(group)
display.auto_refresh = True

x = 0
y = 100

while True:
    
    while x < 100:
        x += 2
        y -= 2
        gauge.update(x)
        gauge2.update(y)
        l1.text = str(int(x))
        
    while x > 0:
        x -= 2
        y += 2
        gauge.update(x)
        gauge2.update(y)
        l1.text = str(int(x))
        
    while x < 100:
        x += 5
        y -= 5
        gauge.update(x)
        gauge2.update(y)
        l1.text = str(int(x))
        
    while x > 0:
        x -= 5
        y += 5
        gauge.update(x)
        gauge2.update(y)
        l1.text = str(int(x))
