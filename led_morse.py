import board
import time
import digitalio

def punto():
    led.value = 1
    time.sleep(0.1)
    led.value = 0
    time.sleep(0.1)
    
def trattino():
    led.value = 1
    time.sleep(0.5)
    led.value = 0
    time.sleep(0.1)

led= digitalio.DigitalInOut(board.GP18)
led.direction= digitalio.Direction.OUTPUT
lettera=str(input("Inserisci una lettera"))
dimensione = len(lettera)

for x in range (dimensione):
    if lettera[x] == ' ':
        time.sleep(1)
        
    if lettera[x] == 'a' or lettera[x] == 'A':
        punto()
        trattino()

    if lettera[x] == 'b' or lettera[x] == 'B':
        trattino()
        for x in range (3):
            punto()
        
    if lettera[x] == 'c' or lettera[x] == 'C':
        for x in range (2):
            trattino()
            punto()

    if lettera[x] == 'd' or lettera[x] == 'D':
        trattino()
        for x in range (2):
            punto()

    if lettera[x] == 'e' or lettera[x] == 'E':
        punto()

    if lettera[x] == 'f' or lettera[x] == 'F':
        for x in range (2):
            punto()
        trattino()
        punto()

    if lettera[x] == 'g' or lettera[x] == 'G':
        for x in range (2):
            trattino()
        punto()

    if lettera[x] == 'h' or lettera[x] == 'H':
        for x in range (4):
            punto()

    if lettera[x] == 'i' or lettera[x] == 'I':
        for x in range (2):
            punto()

    if lettera[x] == 'j' or lettera[x] == 'J':
        punto()
        for x in range (3):
            trattino()

    if lettera[x] == 'k' or lettera[x] == 'K':
        trattino()
        punto()
        trattino()
            
    if lettera[x] == 'L' or lettera[x] == 'l':
        punto()
        trattino()
        for x in range (2):
            punto()

    if lettera[x] == 'M' or lettera[x] == 'm':
        for x in range (2):
            trattino()
        
    if lettera[x] == 'N' or lettera[x] == 'n':
        trattino()
        punto()

    if lettera[x] == 'O' or lettera[x] == 'o':
        for x in range (3):
            trattino()

    if lettera[x] == 'P' or lettera[x] == 'p':
        punto()
        for x in range (2):
            trattino()
        punto()

    if lettera[x] == 'Q' or lettera[x] == 'q':
        for x in range (2):
            trattino()
        punto()
        trattino()

    if lettera[x] == 'R' or lettera[x] == 'r':
        punto()
        trattino()
        punto()

    if lettera[x] == 'S' or lettera[x] == 's':
        for x in range (3):
            punto()
            
    if lettera[x] == 'T' or lettera[x] == 't':
            trattino()
            
    if lettera[x] == 'U' or lettera[x] == 'u':
        for x in range (2):
            punto()
        trattino()
        
    if lettera[x] == 'V' or lettera[x] == 'v':
        for x in range (3):
            punto()
        trattino()

    if lettera[x] == 'W' or lettera[x] == 'w':
        punto()
        for x in range (2):
            trattino()

    if lettera[x] == 'X' or lettera[x] == 'x':
        trattino()
        for x in range (2):
            punto()
        trattino()

    if lettera[x] == 'Y' or lettera[x] == 'y':
        trattino()
        for x in range (2):
            punto()
        trattino()

    if lettera[x] == 'Z' or lettera[x] == 'z':
        for x in range (2):
            trattino()
        for x in range (2):
            punto()
