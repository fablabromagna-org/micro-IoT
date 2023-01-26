import ipaddress
import ssl
import wifi
import socketpool
import adafruit_requests
import microcontroller
import time

# Lo sheet Google che espone il metodo doGet() sulla rete in modo anonimo
# https://docs.google.com/spreadsheets/d/1LkNOM1B16-zjvHQdMEo2EpseA1GPHAQpP4YLxw8zfcc/edit#gid=0

# ID dello script (ad ogni deploy fatto dentro l'editor AppScript, questo codice cambia)
ID_GSHEET = "AKfycbwshOm973RgrSpFbVuArw9HJGmZTyWM27xGobcSX1wBkmh3jaSzt4msaAm2XcBbc36gSw"
ID_GSHEET = "AKfycby-AJf9agC3O9LXCewBOHpEE7PHwFZrIYmASQGwj6IDRk10YB9ul5hIar_tNt4qRNSJwA"
ID_GSHEET = "AKfycbweLEA1vrXL_jiXB-ErDOR1v9QzI-QU5q_tx4jzBDX8bq9CP9hy5lJOwP0SdC8L9gJigA"


# la temperatura interna del Pico, in formato stringa
temperatura = str(microcontroller.cpu.temperature)
# il nome del chiamante (così da riconoscerlo...)
nome = "Maurizio"

# prima parte dell'URL da chiamare (sempre uguale)
URL_GOOGLE = "https://script.google.com/macros/s/"

# assembliamo la parte che forma il comando
COMANDO = "/exec?temperatura=" + temperatura + "&nome=" + nome

# mettiamo tutto insieme
TEXT_URL = URL_GOOGLE + ID_GSHEET + COMANDO

# le password per il wifi le teniamo nel file secrets.py
# che includiamo con il comando import
from secrets import secrets

print( "Connecting to %s"%secrets["ssid"] )
wifi.radio.connect( secrets["ssid"], secrets["password"] )
print( "Connected to %s!"%secrets["ssid"])
print("My IP address is", wifi.radio.ipv4_address)

pool = socketpool.SocketPool( wifi.radio )
context = ssl.create_default_context()
requests = adafruit_requests.Session(pool, context)
print( "-" * 40 )

import json
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    response = requests.get(TEXT_URL)
    print( "Text Response: ", response.text )

    statoLed = (json.loads(response.text))
    print( statoLed[0] )
    led.value = statoLed[0]
    time.sleep(1.5)

response.close()
