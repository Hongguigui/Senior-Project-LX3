import bluetooth    # requires PyBluez 0.30
                    # can be installed by running `pip install git+https://github.com/pybluez/pybluez#egg=Pybluez` in cmd prompt

class BluetoothComClass:
    def __init__(self, name=None, addr=None):
        self.sock = None
        self.name = name
        self.addr = addr
        
    def open(self):
        name = None
        # address was not provided (name will be used to find it)
        if self.addr is None:
            # name was not provided either
            if self.name is None:
                nearby_devices = bluetooth.discover_devices()
                for addr in nearby_devices:
                    # chance of not finding the device, so we'll try a few times
                    for j in range(3):
                        name = bluetooth.lookup_name(addr)
                        if name is not None:
                            break
                    # use first sensor we find
                    if name is not None and "yostlabs" in name.lower():
                        self.name = name
                        self.addr = addr
                        break
            # name was provided
            else:
                nearby_devices = bluetooth.discover_devices()
                for addr in nearby_devices:
                    # chance of not finding the device, so we'll try a few times
                    for j in range(3):
                        name = bluetooth.lookup_name(addr)
                        if name is not None:
                            break
                    if self.name == name:
                        self.addr = addr
                        break
        # if address is still None, the device was not found
        if self.addr is None:
            print("Could not find 3 Space device")
        # address was given or discovered
        else:
            # name was not provided (name is not necessary at this point, but could be useful for debugging)
            if self.name is None:
                # chance of not finding the device, so we'll try a few times
                for j in range(3):
                    self.name = bluetooth.lookup_name(self.addr)
                    if self.name is not None:
                        break
                if self.name == None:
                    print("Name of device at address", self.addr, "not found")
            print("3 Space device found")
            # attempt to connect to device
            try:
                self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                self.sock.connect((self.addr, 1))
                print("Successfully connected to", self.name, "at address", self.addr)
            except:
                print("Failed to connect to", self.name, "at address", self.addr)
            
    def close(self):
        self.sock.close()
        
    def write(self, data, length):
        self.sock.send(bytes(data))
        
    def read(self, numToRead):
        return self.sock.recv(numToRead)