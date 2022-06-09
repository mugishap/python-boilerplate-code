import RPi.GPIO as GPIO
from time import sleep

LEDPin = 7

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup (LEDPin, GPIO.OUT)

def loop():
    setup()

    try:
        while(True):
            GPIO.output(LEDPin,1)
            sleep(0.5)
            GPIO.output(LEDPin,0)
            sleep(0.5)

    except KeyboardInterrupt:
        GPIO.cleanup

#Call The Function loop()
if __name__ == '__main__':
   loop()