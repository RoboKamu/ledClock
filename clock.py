import RPi.GPIO as gpio
from time import sleep

# setup gpio pins
gpio.setmode(gpio.BOARD)
pins = [7, 8, 11, 12, 23, 38, 40]
for pin in pins:
    gpio.setup(pin, gpio.OUT)


# make a class that has an object for each number (0, 1, 2 etc)
class Count:
    def __init__(self, num):
        self.num = num
        # set global variable names for all pins for ease of use
        self.botRight = 8
        self.topRight = 12
        self.botLeft = 7
        self.topLeft = 23
        self.topMid = 11
        self.mid = 38
        self.botMid = 40

    def numZero(self):
        # list of all lines of LED used to make zero
        ledList = [
            self.botLeft,
            self.botRight,
            self.topMid,
            self.topRight,
            self.topLeft,
            self.botMid]

        for led in ledList:
            gpio.output(led, True)  # turn on all LEDs required for zero
        sleep(1)

        for led in ledList:
            gpio.output(led, False)  # turn off all LEDs required for zero
        sleep(0.5)

    def numOne(self):
        # number one only needs one line on either side, either left or right, only 2 pins needed
        gpio.output(self.topRight, True)
        gpio.output(self.botRight, True)
        sleep(1)

        gpio.output(self.topRight, False)
        gpio.output(self.botRight, False)
        sleep(0.5)

    def numThree(self):
        # lits of all pins used for number 3
        ledList = [
            self.topMid,
            self.mid,
            self.botMid,
            self.topRight,
            self.botRight]

        for led in ledList:
            gpio.output(led, True)
        sleep(1)

        for led in ledList:
            gpio.output(led, False)
        sleep(0.5)

    def numFour(self):
        # list of all pins used for number 4
        ledList = []

    def ans(self):
        # list of the functions
        fList = [self.numZero, self.numOne]
        try:
            for f in range(0, self.num):
                fList[f]()
        finally:
            gpio.cleanup()


a = Count(4)
print(a.ans())
