import smbus
import RPi.GPIO as GPIO
import time

address = 0x48
bus = smbus.SMBus(1)
level = 2.5
increment = 0.5

GPIO.setmode(GPIO.BCM)

basePin = 4
leftPin = 15
rightPin = 17
gripPin = 10

pins = [basePin, leftPin, rightPin, gripPin]

for pin in pins:
    GPIO.setup(pin,GPIO.OUT)
    
base = GPIO.PWM(basePin, 50)
left = GPIO.PWM(leftPin, 50)
right = GPIO.PWM(rightPin, 50)
grip = GPIO.PWM(gripPin, 50)

servos = [base, left, right, grip]

for servo in servos:
    servo.start(level)


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


if __name__ == "__main__":
    try:
        while True:
            
            if (level >= 5.0):
            
                increment = increment * -1
            
            level += 0.1
            
            print(readA0(), readA1(), readA2(), readA3(), level)
            for servo in servos:
                servo.ChangeDutyCycle(level)
            
            time.sleep(0.5)
    
    except (KeyboardInterrupt, SystemExit):
        base.stop()
        left.stop()
        right.stop()
        grip.stop()
        GPIO.cleanup()