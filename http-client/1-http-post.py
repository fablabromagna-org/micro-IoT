#
# Eseguire comandi HTTP con Pico
# 1 - Esegue una chiamata POST sul sito io.adafruit.com
#
# maurizio.conti@fablabromagna.org
# 14 novembre 2023
#
###############################################
#
# Con VSCode si può utilizzare un file .http per testare la connessione HTTP
#GET https://io.adafruit.com/api/v2/mconti/feeds/test/data HTTP/1.1

###
#POST https://io.adafruit.com/api/v2/mconti/feeds/test/data HTTP/1.1
#X-AIO-KEY: 30a62f928b37679fb7512e7c799922159d2f567 8
#content-type: application/json
#
#{"value": "20"}

###############################################

# queste lib sono già dentro al firmware di Circuit Python
import ipaddress
import ssl
import wifi
import socketpool
import microcontroller
import time
import json

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

# Adafruit IO data...
url = "https://io.adafruit.com/api/v2/mconti/feeds/test/data"
username = "mconti"
key = "30a62f928b37679fb7512e7c799922159d2f567 8"

# Payload
data = {"value": 42}

# Headers HTTP
headers = {
    "Content-Type": "application/json",
    "X-AIO-Key": key,
}

# Eseguo un POST
response = requests.post(url, data=json.dumps(data), headers=headers)

# dentro a response.text c'è una stringa JSON
print( "Text Response: ", response.text )

import json
risposta = json.loads(response.text)

# Check the response
if response.status_code == 200:
    print("Dati spediti!")
else:
    print(f"Errore: {response.status_code}")

print(response.text)
    
# Sempre buona cosa deallocare le risorse legate alla connessione
response.close()

