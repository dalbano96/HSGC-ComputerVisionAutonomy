import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor1A = 15
Motor1B = 13
Motor2A = 22
Motor2B = 18

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)

print "Turning motor on"
GPIO.output(Motor1A, GPIO.HIGH)
GPIO.output(Motor2A, GPIO.HIGH)
sleep(3)
GPIO.output(Motor1A, GPIO.LOW)
GPIO.output(Motor2A, GPIO.LOW)

print "Stopping motor"
GPIO.cleanup()

