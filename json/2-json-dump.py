
# Utilizzare json in Python 2
# Produrre json

# 14 novembre 2023
# maurizio.conti@fablabromagna.org

# Esempi tratti da questo tutorial
# https://oxylabs.io/blog/python-parse-json

import json

# i vettori in Python si chiamano list e si fanno con le quadre []
linguaggi = ["C/C++", "C#", "JavaScript", "Python", "Verilog", "Rust"]

# i dict in python si fanno con le graffe {}
persona = {
    "nome": "Maurizio Conti",
    "eta": 18,
    "linguaggi": linguaggi
}

strPersona = json.dumps(persona)
print(strPersona)

# sul pico, prima di scrivere serve una abilitazione...
#with open('test-scritto.json', 'w') as f:
#    json.dump(persona, f, indent=4)

