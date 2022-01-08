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
            self.botMid
            ]

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
        # turn LEDs off
        gpio.output(self.topRight, False)
        gpio.output(self.botRight, False)
        sleep(0.5)

    def numTwo(self):
        # list of all pins used for number 2
        ledList = [
            self.topMid,
            self.mid,
            self.botMid,
            self.topRight,
            self.botLeft
            ]

        for led in ledList:
            gpio.output(led, True)      # turn on LEDs to make number 2
        sleep(1)

        for led in ledList:
            gpio.output(led, False)     # turn them off
        sleep(0.5)

    def numThree(self):
        # lits of all pins used for number 3
        ledList = [
            self.topMid,
            self.mid,
            self.botMid,
            self.topRight,
            self.botRight
            ]

        for led in ledList:
            gpio.output(led, True)      # turn LEDs on to make number three
        sleep(1)

        for led in ledList:
            gpio.output(led, False)     # turn LEDs off
        sleep(0.5)

    def numFour(self):
        # list of all pins used for number 4
        ledList = [
            self.topLeft,
            self.topRight,
            self.botRight,
            self.mid
            ]

        for led in ledList:
            gpio.output(led, True)      # turn on LEDs to make number 4
        sleep(1)

        for led in ledList:
            gpio.output(led, False)     # turn off LEDs
        sleep(0.5)

    def numFive(self):
        # list of all pins used for number 5
        ledList = [
            self.topMid,
            self.mid,
            self.botMid,
            self.topLeft,
            self.botRight
            ]

        for led in ledList:
            gpio.output(led, True)      # turn on LEDs to make number 5
        sleep(1)

        for led in ledList:
            gpio.output(led, False)     # turn off LEDs
        sleep(0.5)

    def numSix(self):
        # List of pins used to make number 6
        ledList = [
            self.topMid,
            self.mid,
            self.botMid,
            self.topLeft,
            self.botLeft,
            self.botRight
            ]

        for led in ledList:
            gpio.output(led, True)      # turn on LEDs to make number 6
        sleep(1)

        for led in ledList:
            gpio.output(led, False)     # turn off LEDs
        sleep(0.5)

    def numSeven(self):
        # list of pins used to make number 7
        ledList = [
            self.topMid,
            self.topRight,
            self.botRight
            ]

        for led in ledList:
            gpio.output(led, True)      # turn on LEDs to make number 7
        sleep(1)

        for led in ledList:
            gpio.output(led, False)     # turn off LEDs
        sleep(0.5)

    def numEight(self):
        # 8 uses all pins therefore we can use the list "pins" used in line 6 and turn all of them on and off
        for led in pins:
            gpio.output(led, True)      # turn all LEDs on to make 8
        sleep(1)

        for led in pins:
            gpio.output(led, False)     # tunr all LEDs off
        sleep(0.5)

    def numNine(self):
        # list of pins used to make number 9
        ledList = [
            self.topMid,
            self.mid,
            self.topLeft,
            self.topRight,
            self.botRight
            ]

        for led in ledList:
            gpio.output(led, True)      # turn LEDs on to make number 9
        sleep(1)

        for led in ledList:
            gpio.output(led, False)     # turn LEDs off
        sleep(0.5)

    def results(self):
        # list of the functions
        fList = [
            self.numZero, self.numOne, self.numThree,
            self.numFour, self.numFive, self.numSix,
            self.numSeven, self.numEight, self.numNine
            ]

        try:
            # make a loop to count to their input
            for f in range(0, self.num+1):
                fList[f]()
        finally:
            gpio.cleanup()


# get user input and print the results
num = int(input("What number do you want to count to? (0, 9): "))

# Let the user try again if the input is out of range
while num < 0 or num > 9:
    print("Skriv gärna in ett nummer från 0 till 9: ")
    num = int(input())
    
ans = Count(num)
print(ans.results())
