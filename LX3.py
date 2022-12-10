from ThreeSpaceAPI import *
import serial
import time
from time import sleep
from exampleComClasses import USB_ExampleClass


# Create communication object instance.
com = USB_ExampleClass.UsbCom("COM3")

# Create sensor instance. This will call the open function of the communication object.
sensor = ThreeSpaceSensor(com)

# Create initial time stamp
initTS = time.time()
timestamp = initTS
accelOutFile = open('linear.txt', 'w', buffering=1)
tsOutFile = open('timestamp.txt', 'w', buffering=1)
countOutFile = open('count.txt', 'w', buffering=1)
# allOutFile = open('all.txt', 'w')
count = 0

while True:
    count += 1
    print(count)
    # Get reading from sensor, returns as tuple.
    reading = sensor.getCorrectedLinearAccelerationInGlobalSpace()
    # reading = sensor.getRawAccelerometerVector()
    # totalRead = sensor.getAllCorrectedComponentSensorData()
    timestamp = time.perf_counter()
    reading = str(reading)+'\n'
    timestamp = str(timestamp)+'\n'
    accelOutFile.write(reading)
    tsOutFile.write(timestamp)
    countOutFile.write(str(count)+'\n')
    # totalRead = str(totalRead) + '\n'
    # allOutFile.write(totalRead)
    # time.sleep(0.002)
    # if count == 200:
    #     break

# close communication object and join any spawned threads
sensor.cleanup()







