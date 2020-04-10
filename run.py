import smbus
import RPi.GPIO as GPIO
import time

address = 0x48
bus = smbus.SMBus(1)
level = 100
increment = 10
PWMfreq = 60

GPIO.setmode(GPIO.BCM)

basePin = 4
leftPin = 15
rightPin = 17
gripPin = 10

pins = [basePin, leftPin, rightPin, gripPin]

for pin in pins:
    GPIO.setup(pin,GPIO.OUT)
    
base = GPIO.PWM(basePin, PWMfreq)
left = GPIO.PWM(leftPin, PWMfreq)
right = GPIO.PWM(rightPin, PWMfreq)
grip = GPIO.PWM(gripPin, PWMfreq)

servos = [base, left, right, grip]

for servo in servos:
    servo.start(level/2)

def scale(read, maxval):
    
    return (read/255)*maxval


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
        
            #level += increment
            #if (level > 100) or (level < 0):
            
             #   increment = increment * -1
             #   level += increment
            
            
            
            print(readA0(), readA1(), readA2(), readA3(), level)
            
            base.ChangeDutyCycle(scale(readA0(), level))
            left.ChangeDutyCycle(scale(readA1(), level))
            right.ChangeDutyCycle(scale(readA2(), level))
            grip.ChangeDutyCycle(scale(readA3(), level))
            
            time.sleep(0.2)
    
    except (KeyboardInterrupt, SystemExit):
        print("exit & cleanup")
        base.stop()
        left.stop()
        right.stop()
        grip.stop()
        GPIO.cleanup()