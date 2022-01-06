import RPi.GPIO as gpio
from time import sleep

# setup gpio pins
gpio.setmode(gpio.BOARD)
pins = [7, 8, 11, 26, 40]
for pin in pins:
    gpio.setup(pin, gpio.OUT)


# make a class that has an object for each number (0, 1, 2 etc)
class Count:
    def __init__(self, num):
        self.num = num
        #the right LED is pin 8
        #left is pin 7
        #top is 11
        #mid is 26
        #bot is 40

    def numZero(self):
        # list of all lines of LED used to make zero
        LEDList = [7, 8, 11, 40]

        for LED in LEDList:
            gpio.output(LED, True)  # turn on all LEDs required for zero
        sleep(1)

        for LED in LEDList:
            gpio.output(LED, False)  # turn off all LEDs required for zero
        sleep(0.5)

    def numOne(self):
        # number one only needs one line on either side, either left or right
        gpio.output(8, True)
        sleep(1)
        gpio.output(8, False)
        sleep(0.5)
    def ans(self):
        # list of the functions
        fList = [self.numZero, self.numOne]
        try:
            for f in fList:
                f()
        finally:
            gpio.cleanup()

a = Count(2)
print(a.ans())
