
import ipaddress
import ssl
import wifi
import socketpool
import adafruit_requests

for network in wifi.radio.start_scanning_networks():
    print(network, network.ssid, network.channel)
wifi.radio.stop_scanning_networks()

# URLs to fetch from
#TEXT_URL = "https://script.google.com/a/macros/ittsrimini.edu.it/s/AKfycbynXBrhC329kigevlrGH8XPKMjBdA_yP1F8m6bR51EO5rQ1evUpz8tjPPLUtozz4cKcXg/exec?temperatura=21.2"
TEXT_URL = "https://script.google.com/macros/s/AKfycbwkgK96UqbcgXljbcDItEazQRp5whC2-IrXuPreZP7F7ppgNrJfBLLXfLDnAapFQz5Ehg/exec?temperatura=21.2"
# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

print("Connecting to %s"%secrets["ssid"])
wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Connected to %s!"%secrets["ssid"])
print("My IP address is", wifi.radio.ipv4_address)

ipv4 = ipaddress.ip_address("8.8.4.4")
print("Ping google.com: %f ms" % (wifi.radio.ping(ipv4)*1000))

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

print("Fetching text from", TEXT_URL)

print("-" * 40)

try:
    response = requests.get(TEXT_URL)
    print(response)
except OSError:
    print("Errore di connessione... controlla url.")

print("-" * 40)

    