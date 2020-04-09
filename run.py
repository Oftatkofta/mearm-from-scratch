import smbus
import RPi.GPIO as GPIO
import time

address = 0x48
bus = smbus.SMBus(1)
out = []

GPIO.setmode(GPIO.BCM)

basePin = 4
leftPin = 15
rightPin = 17
gripPin = 10

pins = [basePin, leftPin, rightPin, gripPin]

for pin in pins:
    GPIO.setup(pin,GPIO.OUT)
    
base = GPI.PWM(basePin, 50)
left = GPI.PWM(leftPin, 50)
right = GPI.PWM(rightPin, 50)
grip = GPI.PWM(griPin, 50)

def readA0():
    bus.write_byte(address, 0x40)
    bus.read_byte(address)
    
    return bus.read_byte(address)

def readA1():
    bus.write_byte(address, 0x41)
    bus.read_byte(address)
    
    return bus.read_byte(address)

def readA2():
    bus.write_byte(address, 0x42)
    bus.read_byte(address)
    
    return bus.read_byte(address)

def readA3():
    bus.write_byte(address, 0x43)
    bus.read_byte(address)
    
    return bus.read_byte(address)

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()

if __name__ == "__main__":
    while True:
        print(readA0(), readA1(), readA2(), readA3())
    