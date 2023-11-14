
# Utilizzare json in Python 1
# Decodificare un file completo

# 14 novembre 2023
# maurizio.conti@fablabromagna.org

# Esempi tratti da questo tutorial
# https://oxylabs.io/blog/python-parse-json

import json

# Come in Python normale,
# possiamo usare il file handle ritornato da open
# come parametro per la load (stavolta senza la s!!)
data = json.load(open('testo.json'))

# per chiudere il file correttamente meglio usare with
with open('testo.json') as f:
  data = json.load(f)

print( type(data) )

# visto che è un dict, possiamo farci dare le chiavi
print( data.keys() )

# e i valori
print( data.values() )        # tutti
print( data['linguaggi'][3] ) # solo quelli che ci servono
