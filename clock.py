import RPi.GPIO as gpio
from time import sleep

#setup gpio pins 
gpio.setmode(gpio.BOARD)
pins = [7, 8, 11, 26, 40]
for pin in pins:
	gpio.setup(pin, gpio.OUT)

#make a class that has an object for each number (0, 1, 2 etc)
class Count:
	def __init__(self, num):
		self.num = num
		self.countList = []
		self.leftLED = 7
		self.rightLED = 8
		self.topLED = 11
		self.midLED = 26
		self.botLED = 40
		
	def numZero():
		#list of all lines of LED used to make zero
		LEDList = [leftLED, rightLED, topLED, botLED]
		
		for LED in LEDList:
			gpio.output(LED, True)		#turn on all LEDs required for zero 
		
		sleep(1)	
		
		for LED in LEDlist:
			gpio.output(LED, False)		#turn off all LEDs required for zero
		
	def numOne():
		#number one only needs one line on either side, either left or right
		gpio.output(rightLED, True)
		sleep(1)
		gpio.output(rightLED, False)
		
	def ans():
		#list of the functions 
		fList = [numZero, numOne]
		try:
			for f in range(0, num):
				fList[f]()
		finally:
			gpio.cleanup()
