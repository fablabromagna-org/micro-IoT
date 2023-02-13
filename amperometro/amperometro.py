
import time
import board
import busio

#
# La adafruit_ina219 la trovi qui
# https://github.com/adafruit/Adafruit_CircuitPython_INA219
#
# Serve anche Adafruit_CircuitPython_Register, che si trova qui
# https://github.com/adafruit/Adafruit_CircuitPython_Register
#
# Copiare la cartella completa con tutti i file nella propria cartella lib
from adafruit_ina219 import ADCResolution, BusVoltageRange, INA219


# Qui alcuni dettagli per capire come collegare I2C del rasp Pico
# https://docs.google.com/presentation/d/1sK1kn_NXdJw3I0VPeUFKF_hjDPEu8TyoAwHSTRCq6cs/edit#slide=id.gdde244374a_0_0
i2c_bus = ( busio.I2C( board.GP9, board.GP8 ) )
ina219 = INA219(i2c_bus)
print("ina219 test")

# optional : change configuration to use 32 samples averaging for both bus voltage and shunt voltage
ina219.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S
ina219.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S
# optional : change voltage range to 16V
ina219.bus_voltage_range = BusVoltageRange.RANGE_16V

# measure and display loop
while True:
    # display some of the advanced field (just to test)
    print("Config register:")
    print("  bus_voltage_range:    0x%1X" % ina219.bus_voltage_range)
    print("  gain:                 0x%1X" % ina219.gain)
    print("  bus_adc_resolution:   0x%1X" % ina219.bus_adc_resolution)
    print("  shunt_adc_resolution: 0x%1X" % ina219.shunt_adc_resolution)
    print("  mode:                 0x%1X" % ina219.mode)
    print("")
    bus_voltage = ina219.bus_voltage  # voltage on V- (load side)
    shunt_voltage = ina219.shunt_voltage  # voltage between V+ and V- across the shunt
    current = ina219.current  # current in mA
    power = ina219.power  # power in watts

    # INA219 measure bus voltage on the load side. So PSU voltage = bus_voltage + shunt_voltage
    print("Voltage (VIN+) : {:6.3f}   V".format(bus_voltage + shunt_voltage))
    print("Voltage (VIN-) : {:6.3f}   V".format(bus_voltage))
    print("Shunt Voltage  : {:8.5f} V".format(shunt_voltage))
    print("Shunt Current  : {:7.4f}  A".format(current / 1000))
    print("Power Calc.    : {:8.5f} W".format(bus_voltage * (current / 1000)))
    print("Power Register : {:6.3f}   W".format(power))
    print("")

    # Check internal calculations haven't overflowed (doesn't detect ADC overflows)
    if ina219.overflow:
        print("Internal Math Overflow Detected!")
        print("")

    time.sleep(2)
