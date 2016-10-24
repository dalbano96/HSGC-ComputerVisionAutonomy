
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

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
	GPIO.output(Motor1A, HIGH)
	GPIO.output(Motor1B, LOW)
	GPIO.output(Motor2A, HIGH)
	GPIO.output(Motor2B, LOW)
	return

def moveBackward():
	print "Moving backward"
	GPIO.output(Motor1A, LOW)
        GPIO.output(Motor1B, HIGH)
        GPIO.output(Motor2A, LOW)
        GPIO.output(Motor2B, HIGH)
	return

def moveLeft():
	print "Moving left"
	GPIO.output(Motor1A, HIGH)
        GPIO.output(Motor1B, LOW)
        GPIO.output(Motor2A, LOW)
        GPIO.output(Motor2B, HIGH)
	return

def moveRight():
	print "Moving right"
	GPIO.output(Motor1A, LOW)
        GPIO.output(Motor1B, HIGH)
        GPIO.output(Motor2A, HIGH)
        GPIO.output(Motor2B, LOW)
	return

def stopMovement():
	print "Movement stopped"
	GPIO.output(Motor1A, LOW)
        GPIO.output(Motor1B, LOW)
        GPIO.output(Motor2A, LOW)
        GPIO.output(Motor2B, LOW)
	return

def getChar():
	inputChar = raw_input("Enter character: ")
	while (inputChar != 'q'): 
		if inputChar == 'w':
			moveForward()		
		if inputChar == 's':
			moveBackward()
		if inputChar == 'a':
			moveLeft()
		if inputChar == 'd':
			moveRight()
		inputChar = raw_input("Enter character: ")
	return

getChar()

print "Stopping motor"
GPIO.cleanup()

