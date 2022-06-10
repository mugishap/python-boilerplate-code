import RPi.GPIO as GPIO
from time import sleep, time

trigPin = 18
echoPin = 22

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup (trigPin, GPIO.OUT)
    GPIO.setup (echoPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def loop():
    setup()

    try:
        while(True):
            GPIO.output(trigPin, 0)
            sleep(0.000002)
            GPIO.output(trigPin, 1)
            sleep(0.00001)
            GPIO.output(trigPin, 0) 
            duration = pulseIn(echoPin, 0)
            distance = (duration / 2) / 29.1
            if(distance >= 100 or distance <= 0):
                print("Out of range")
            else:
                print("%.2f cm"% distance)
            sleep(0.1)

    except KeyboardInterrupt:       
        GPIO.cleanup

def pulseIn(inputPin, state):
        global pulse_start
        swap = {0: 1, 1:0}

        while GPIO.input(inputPin)==state:
            pulse_start = time()
        while GPIO.input(inputPin)==swap[state]:
            pulse_end = time()

        return (pulse_end - pulse_start)*1000000

#Call The Function loop()
if __name__ == '__main__':  
    loop()  