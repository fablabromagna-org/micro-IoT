#############################
# driver per i vari sensori intelligenti
#############################
import time
import board
import busio
import terminalio

import displayio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

displayio.release_displays()

i2c = busio.I2C( scl=board.GP21, sda=board.GP20 )
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

#sht30 = adafruit_sht31d.SHT31D(i2c, address=0x44)

while True:
    #print("\nTemperature: {:.2f} C".format(sht30.temperature))
    #print("Humidity: {:.2f} %".format(sht30.relative_humidity))
    #print("Pressure: {:.2f} hPa".format(bmp280.pressure))
    #print("Altitude = {:.2f} meters".format(bmp280.altitude))

    # Make the display context
    text_group = displayio.Group()

    # Draw a label
    text = "ENVIRONMENT SENSOR"
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=0, y=4)
    text_group.append(text_area)

    #text = "Temp (C):   {:.2f}".format(sht30.temperature)
    text = "Temp (C):   {:.2f}".format(30.1)
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=0, y=17)
    text_group.append(text_area)

    #text = "Humi (%):   {:.2f}".format(sht30.relative_humidity)
    text = "Humi (%):   {:.2f}".format(66)
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=0, y=30)
    text_group.append(text_area)

    #text = "Pres (hPa): {:.2f}".format(bmp280.pressure)
    text = "Pres (hPa): {:.2f}".format(1020)
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=0, y=43)
    text_group.append(text_area)

    #text = "Alti (m):   {:.2f}".format(bmp280.altitude)
    text = "Alti (m):   {:.2f}".format(87)
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=0, y=56)
    text_group.append(text_area)

    display.show(text_group)

    time.sleep(2)