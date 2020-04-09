import smbus

address = 0x48
bus = smbus.SMBus(1)
out = []
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
    while True:
        print(readA0(), readA1(), readA2(), readA3())
    