import time
import board
import digitalio

from audiomp3 import MP3Decoder

try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        pass  # not always supported by every board!

button1 = digitalio.DigitalInOut(board.GP20)
button1.switch_to_input(pull=digitalio.Pull.UP)

# configuro il led a bordo
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# from https://pixabay.com/it/sound-effects/
mp3files = ["claps.mp3"]

# You have to specify some mp3 file when creating the decoder
mp3 = open(mp3files[0], "rb")
decoder = MP3Decoder(mp3)
audio = AudioOut(board.GP18)

while True:
    if button1.value:
        decoder.file = open(mp3files[0], "rb")
        audio.play(decoder)

        led.value=1
        print("playing", mp3files[0])

        while audio.playing:
            pass
 
        led.value=0
        print("finito")
