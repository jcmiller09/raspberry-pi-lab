import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
chan_list = [18, 22, 24]
GPIO.setup(chan_list, GPIO.OUT, initial=GPIO.HIGH)
time.sleep(3)
GPIO.output(chan_list, GPIO.LOW)
GPIO.cleanup()


