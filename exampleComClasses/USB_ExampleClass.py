import serial
import serial.tools.list_ports

class UsbCom:
    def __init__(self, portName=None):
        self.baud = 115200
        self.sensor = None
        self.portName = portName
    def open(self):
        if self.portName is None:
            self.portName = input("Enter sensor COM port name (<Enter> to autodetectport):").strip()

            if self.portName == "":
                ports = serial.tools.list_ports.comports()
                self.portName = None
                for port in ports:
                    # 9334 is the vendor id of 3 Space products
                    if port.vid is not None and port.vid == 9334:
                        self.portName = port.device
                        print("sensor discovered on port:", self.portName)
                        try:
                            self.sensor = serial.Serial(self.portName, 115200, timeout=0.03)
                            return
                        except:
                            print("Error opening port:",self.portName)

                if self.portName == None:
                    print("sensor not discovered.")
                    exit(0)
        self.sensor = serial.Serial(self.portName, 115200, timeout=0.03)

    def close(self):
        self.sensor.close()

    def write(self, data, length):
        self.sensor.write(data)

    def read(self, numToRead):
        return self.sensor.read(numToRead)

