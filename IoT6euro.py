import ipaddress
import ssl
import wifi
import socketpool
import adafruit_requests
import microcontroller

from secrets import secrets

URL_GOOGLE = "https://script.google.com/macros/s/"
ID_GSHEET = "AKfycbwshOm973RgrSpFbVuArw9HJGmZTyWM27xGobcSX1wBkmh3jaSzt4msaAm2XcBbc36gSw"
TEMP = str(microcontroller.cpu.temperature)
NOME = "Maurizio"

COMANDO = "/exec?temperatura=" + TEMP + "&nome=" + NOME

TEXT_URL = URL_GOOGLE + ID_GSHEET + COMANDO

wifi.radio.connect(secrets["ssid"], secrets["password"])

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())
response = requests.get(TEXT_URL)

print( "Text Response: ", response.text )
print( "-" * 40 )
response.close()

response.close()
