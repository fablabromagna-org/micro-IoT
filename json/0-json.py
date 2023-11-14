
# Utilizzare json in Python 0
# Prime cose da sapere.

# 14 novembre 2023
# maurizio.conti@fablabromagna.org

# Esempi tratti da questo tutorial
# https://oxylabs.io/blog/python-parse-json

import json

# la stringa json... non importa da dove viene.
persona = '{"nome":"Maurizio", "eta":18}'

# con loads la trasformiamo in un dictionary python
# nota: la s di loads sta per "string"
# esiste anche la load per leggere la forma binaria
persona_dict = json.loads(persona)

print(type(persona))
print(type(persona_dict))
print( persona_dict["nome"] )
print( persona_dict["eta"]*3 )

# nota: il tipo ritornato da loads dipende dal contenuto json
# se trova 			Torna un
# object			dict
# array				list
# string			str
# number (integer)	int
# number (real)		float
# true				True
# false				False
# null				None