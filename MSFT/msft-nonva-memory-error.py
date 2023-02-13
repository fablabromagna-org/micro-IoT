#
# Client Circuit Python per accedere alle quotazioni di borsa di Microsoft
# maurizio.conti@fablabromagna.org - 20 febbraio 2023

# queste lib sono già dentro al firmware di Circuit Python
import ipaddress
import ssl
import wifi
import socketpool
import microcontroller
import time

# Questa invece si scarica da qui
# 
import adafruit_requests

# Manuale della WebAPI
# https://www.alphavantage.co/documentation/

# Elenco le reti WiFi che trovo con lo scanner
print("WiFi network trovate:")
for network in wifi.radio.start_scanning_networks():
    
    print( "\t%s\t\tRSSI: %d\tChannel: %d" %
        (str(network.ssid, "utf-8"),
        network.rssi,
        network.channel)
    )

# fermo lo scanner WiFi
wifi.radio.stop_scanning_networks()

# Mi connetto usando SSID e pwd che trovo nel file secrets.py
from secrets import secrets
print( "Mi connetto a %s"%secrets["ssid"] )
wifi.radio.connect( secrets["ssid"], secrets["password"] )

print( "Connesso a %s!"%secrets["ssid"])
print("Il mio IP: ", wifi.radio.ipv4_address)
print("Il mio MAC:", [hex(i) for i in wifi.radio.mac_address])

# adafruit_requests serve per eseguire delle connessioni HTTP usando le socket
# La classe prevede anche connessioni HTTPS quindi usa SSL
#
# In sistensi, per fare una chiama HTTP GET, ci serve
# - un socket (oggetto socketpool)
# - un contesto ssl creato con un certificato autogenerato
# - una sessione HTTP/HTTPS 
pool = socketpool.SocketPool( wifi.radio )
context = ssl.create_default_context()
requests = adafruit_requests.Session(pool, context)

# La parte di inizializzazione del client HTTP è finita
# Ora la usiamo
print( "-" * 40 )

# Queste lib servono per la decodifica del JSON
import json
import board

# Qui mi preparo qualche URL utile...
URL_BASE = "https://www.alphavantage.co/query?apikey=demo&function=TIME_SERIES_DAILY_ADJUSTED&symbol=MSFT"

# Non serve a molto, solo per capire che il ciclo
# principale sta ancora girando
NUMERO_DI_GIRO = 0

# per usare il led BUILT_IN uso la lib digitalio
# quindi la devo importare
import digitalio
led = digitalio.DigitalInOut( board.LED )
led.direction = digitalio.Direction.OUTPUT

# ciclo principale
while True:
    
    NUMERO_DI_GIRO += 1
    
    # Esegue la chiamata HTTP con il verbo "GET"
    response = requests.get( URL_BASE )
    risposta = json.loads( response.text )
    print( risposta["Meta Data"] )
    response.close()

    print( "Giro " + str(NUMERO_DI_GIRO) )
    time.sleep(3)