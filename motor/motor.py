import RPi.GPIO as GPIO
from time import sleep

servoPin = 29

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup (servoPin, GPIO.OUT)
    global servoControl
    servoControl = GPIO.PWM(servoPin, 50)   

def loop():
    setup()
    try:
        while(True):
            servoControl.start(3)
            sleep(1)
            servoControl.start(6)
            sleep(1)
    except KeyboardInterrupt:       
        GPIO.cleanup
    
#Call The Function loop()
if __name__ == '__main__':  
    loop()