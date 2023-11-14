#
# Eseguire comandi HTTP con Pico
# 2 - sulla pressione di un pulsante spedisce un valore usando POST
#
# maurizio.conti@fablabromagna.org
# 14 novembre 2023
#

import board
import ipaddress
import ssl
import wifi
import socketpool
import microcontroller
import time
import json
import adafruit_requests
import digitalio

# Verifico l'esistenza del file secrets.py
try:
    from secrets import secrets

except ImportError:
    print("Non trovo il file secrets.py con le password del WiFI.")
    raise

# configuro il led a bordo
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# configuro il pulsante
button = digitalio.DigitalInOut(board.GP20)
button.switch_to_input(pull=digitalio.Pull.UP)

# Mi connetto usando SSID e pwd che trovo nel file secrets.py
print( "Mi connetto a " + secrets["ssid"] )
wifi.radio.connect( secrets["ssid"], secrets["password"] )
print("OK. Sono connesso a " + secrets["ssid"])

pool = socketpool.SocketPool( wifi.radio )
context = ssl.create_default_context()
requests = adafruit_requests.Session(pool, context)

# Ci siamo
print( "-" * 40 )

# Adafruit IO data...
url = "https://io.adafruit.com/api/v2/mconti/feeds/test/data"
username = "mconti"
key = "30a62f928b37679fb7512e7c799922159d2f567 8"

# Payload
premuto = {"value": 1}
rilasciato = {"value": 0}

# Headers HTTP
headers = {
    "Content-Type": "application/json",
    "X-AIO-Key": key,
}

while( True ) :
    if( button.value ):
      
        response = requests.get( url )
        risposta = json.loads(response.text)

        if( (risposta[0] is not None) and (risposta[0]["value"] is not None) ):
            # OK, ci siamo
            print( risposta[0]["value"] )
            if( int(risposta[0]["value"]) == 0 ):
                led.value = 0
                payload = {"value": 1}

            else :
                led.value = 1
                payload = {"value": 0}

        # Eseguo un POST
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        risposta = json.loads(response.text)

        if response.status_code == 200:
            print("Dati spediti!")
        else:
            print(f"Errore: {response.status_code}")

        #print(response.text)

        while( button.value ) :
            pass
  
        # Sempre buona cosa deallocare le risorse legate alla connessione
        response.close()

