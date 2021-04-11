from machine import Pin
from time import sleep

# GPIO pin constants
rsPin = Pin(3, Pin.OUT)
rwPin = Pin(4, Pin.OUT)
ePin = Pin(5, Pin.OUT)

data0Pin = Pin(8, Pin.OUT)
data1Pin = Pin(9, Pin.OUT)
data2Pin = Pin(10, Pin.OUT)
data3Pin = Pin(11, Pin.OUT)
data4Pin = Pin(12, Pin.OUT)
data5Pin = Pin(13, Pin.OUT)
data6Pin = Pin(14, Pin.OUT)
data7Pin = Pin(15, Pin.OUT)

def initDisplay():
    """Initializes the 1602 LCD Display module."""
    sendInstruction(0b00111000)
    sendInstruction(0b00001110)
    sendInstruction(0b00000110)


def send():
    """Sends data or an instruction to the display."""
    ePin(1)
    ePin(0)


def sendInstruction(bits):
    """Sends the instruction to the display."""
    ePin(0)
    rsPin(0)
    rwPin(0)
    setDataPins(bits)

    send()


def setDataPins(bits):
    """Sets the data pins to the given value."""
    data7Pin(bits & 0b10000000)
    data6Pin(bits & 0b01000000)
    data5Pin(bits & 0b00100000)
    data4Pin(bits & 0b00010000)
    data3Pin(bits & 0b00001000)
    data2Pin(bits & 0b00000100)
    data1Pin(bits & 0b00000010)
    data0Pin(bits & 0b00000001)


def writeCharacter(char):
    """Writes the given character to the display."""
    bits = ord(char)
    ePin(0)
    rsPin(1)
    rwPin(0)
    setDataPins(bits)

    send()


initDisplay()
writeCharacter('H')
writeCharacter('e')
writeCharacter('l')
writeCharacter('l')
writeCharacter('o')
writeCharacter(',')
writeCharacter(' ')
writeCharacter('w')
writeCharacter('o')
writeCharacter('r')
writeCharacter('l')
writeCharacter('d')
writeCharacter('!')
