# Amperometro 
# Raspberry Pi Pico Version
#

import time
import board, busio
from adafruit_st7735r import ST7735R
import terminalio
import displayio
from gauge import Gauge #get the library here: https://github.com/benevpi/Circuit-Python-Gauge
from adafruit_display_text.label import Label
from adafruit_ina219 import ADCResolution, BusVoltageRange, INA219

# Configuro il sensore di corrente INA2019
i2c_bus = ( busio.I2C( board.GP9, board.GP8 ) )
ina219 = INA219(i2c_bus)

# optional : change configuration to use 32 samples averaging for both bus voltage and shunt voltage
ina219.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S
ina219.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S
# optional : change voltage range to 16V
ina219.bus_voltage_range = BusVoltageRange.RANGE_16V


# Configuro il display
clk_pin=board.GP2
sda_pin=board.GP3      #mosi
reset_pin=board.GP4 
cs_pin=board.GP5
A0_pin=board.GP16

# Inizializzo il display
displayio.release_displays()
spi = busio.SPI( clock=clk_pin, MOSI=sda_pin )

# E' una SPI a cinque  fili...
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

gauge = Gauge( 0, 200, 64, 80, value_label="mA: ", arc_colour=0xFF0000, colour=0xFFFF00, outline_colour=0xFFFF00)
gauge.x = 0
gauge.y = 0

gauge2 = Gauge( 0, 1000, 64, 80, value_label="mW: ", arc_colour=0xFF0000, colour=0xFFFF00, outline_colour=0xFFFF00)
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

    # leggo V, A, P
    bus_voltage = ina219.bus_voltage  # voltage on V- (load side)
    shunt_voltage = ina219.shunt_voltage  # voltage between V+ and V- across the shunt
    current = ina219.current  # current in mA
    power = ina219.power  # power in watts

    l1.text = str("V")
    gauge.update( current )
    gauge2.update( power*1000 )
    
    print("Voltage (VIN+) : {:6.3f}   V".format(bus_voltage + shunt_voltage))
    print("Voltage (VIN-) : {:6.3f}   V".format(bus_voltage))
    print("Shunt Voltage  : {:8.5f} V".format(shunt_voltage))
    print("Shunt Current  : {:7.4f}  A".format(current / 1000))
    print("Power Calc.    : {:8.5f} W".format(bus_voltage * (current / 1000)))
    print("Power Register : {:6.3f}   W".format(power))
    print("")

    time.sleep(1)
