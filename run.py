import smbus

address = 0x48
bus = smbus.SMBus(1)

def readA0():
    bus.write_byte(address, 0x40)
    bus.read_byte(address, 0x40)
    
    return bus.read_byte(address, 0x40)

if __name__ == "__main__":
    print(readA0())
    