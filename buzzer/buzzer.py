import RPi.GPIO as GPIO
from time import sleep

BuzzerPin = 7

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(BuzzerPin, GPIO.OUT,initial=0)

def loop():
    setup()

    try:
        while(True):
            GPIO.output(BuzzerPin, 1)
            sleep(0.5)
            GPIO.output(BuzzerPin, 0)
            sleep(0.5)

    except KeyboardInterrupt:
        GPIO.cleanup()

# call The function loop()
if __name__ == '__main__':
    loop()
