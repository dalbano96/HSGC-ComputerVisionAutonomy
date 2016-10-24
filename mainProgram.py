import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

# Assign pins to motor controller
Motor1A = 13
Motor1B = 15
Motor2A = 18
Motor2B = 22 

# Set pins for output
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)

#GPIO.output(Motor1A, True)
#GPIO.output(Motor1B, True)
#GPIO.output(Motor2A, True)
#GPIO.output(Motor2B, True)

def moveForward():
	print "Moving forward"
	GPIO.output(Motor1A, GPIO.HIGH)
	GPIO.output(Motor1B, GPIO.LOW)
	GPIO.output(Motor2A, GPIO.HIGH)
	GPIO.output(Motor2B, GPIO.LOW)

def moveBackward():
	print "Moving backward"
	GPIO.output(Motor1A, GPIO.LOW)
        GPIO.output(Motor1B, GPIO.HIGH)
        GPIO.output(Motor2A, GPIO.LOW)
        GPIO.output(Motor2B, GPIO.HIGH)

def moveLeft():
	print "Moving left"
	GPIO.output(Motor1A, GPIO.HIGH)
        GPIO.output(Motor1B, GPIO.LOW)
        GPIO.output(Motor2A, GPIO.LOW)
        GPIO.output(Motor2B, GPIO.HIGH)

def moveRight():
	print "Moving right"
	GPIO.output(Motor1A, GPIO.LOW)
        GPIO.output(Motor1B, GPIO.HIGH)
        GPIO.output(Motor2A, GPIO.HIGH)
        GPIO.output(Motor2B, GPIO.LOW)

def stopMovement():
	print "Movement stopped"
	GPIO.output(Motor1A, GPIO.LOW)
        GPIO.output(Motor1B, GPIO.LOW)
        GPIO.output(Motor2A, GPIO.LOW)
        GPIO.output(Motor2B, GPIO.LOW)

moveForward()
sleep(1)
stopMovement()
sleep(1)

moveBackward()
sleep(1)
stopMovement()
sleep(1)

moveLeft()
sleep(1)
stopMovement()
sleep(1)

moveRight()
sleep(1)
stopMovement()
sleep(1)

stopMovement()

print "Stopping motor"
GPIO.cleanup()

