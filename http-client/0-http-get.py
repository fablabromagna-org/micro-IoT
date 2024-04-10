#
# Eseguire comandi HTTP con Pico
# 0 - Esegue una chiamata GET sul sito io.adafruit.com
#
# maurizio.conti@fablabromagna.org
# 14 novembre 2023
# 10 aprile 2024

# queste lib sono già dentro al firmware di Circuit Python
import board
import ipaddress
import ssl
import wifi
import socketpool
import microcontroller
import time
import digitalio

# Questa invece si scarica da qui
# https://learn.adafruit.com/pages/20891/elements/3077480/download?type=zip
import adafruit_requests

# Verifico l'esistenza del file secrets.py
try:
    from secrets import secrets

except ImportError:
    print("Non trovo il file secrets.py con le password del WiFI.")
    raise

# Mi connetto usando SSID e pwd che trovo nel file secrets.py
print( "Mi connetto a " + secrets["ssid"] )
wifi.radio.connect( secrets["ssid"], secrets["password"] )
print("OK. Sono connesso a " + secrets["ssid"])

#######################################################
# ZONA in cui preparo il codice per la connessione
# Per fare una chiamata HTTP GET, servono tre cose:

# 1) un oggetto socket(di tipo socketpool)
pool = socketpool.SocketPool( wifi.radio )

# 2) un oggetto ssl (il certificato è dentro al core di CP)
context = ssl.create_default_context()

# 3) un oggetto in grado di eseguire chiamate HTTP/HTTPS 
requests = adafruit_requests.Session(pool, context)

# Fine ZONA in cui preparo il codice per la connessione
#######################################################

# Ci siamo
print( "-" * 40 )

# URLdei dati relativi al feed adafruit (compreso last data ad esempio)
#URL = "https://io.adafruit.com/api/v2/mconti/feeds/test"

# URL della history
URL = "https://io.adafruit.com/api/v2/mconti/feeds/test/data"

# Esegue la chiamata HTTP con il verbo "GET"
response = requests.get( URL )

# dentro a response.text c'è una stringa JSON
print( "Text Response: ", response.text )

import json
risposta = json.loads(response.text)

if( len(risposta) > 0 ):
    # Verifichiamo che ci siano dati e procediamo
    if( (risposta[0] is not None) and (risposta[0]["value"] is not None) ):
        # OK, ci siamo
        print( risposta[0]["value"] )

        # configuro il led a bordo
        led = digitalio.DigitalInOut(board.LED)
        led.direction = digitalio.Direction.OUTPUT

        led.value = int(risposta[0]["value"])
    
# Sempre buona cosa deallocare le risorse legate alla connessione
response.close()

#
# /api/v2/mconti/feeds/test/data

