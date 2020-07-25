# import any of the required libraries for the sensor

# include the networktablesinstance
from networktables import NetworkTablesInstance

# create the class
# see https://www.programiz.com/python-programming/class for a tutorial
class SensorTemplate:
    "Put a description of your class here in quotes"

    # setup network tables
    ntinst = NetworkTablesInstance.getDefault()
    ntinst.startClient("put ip address of the server here")
    # change "sensor" to be the name of your sensor
    table = ntinst.getTable("sensor")
    # change the following to match the information you want to store for your sensor
    sensor_value = table.getEntry("sensor_value")
    sensor_value_2 = table.getEntry("sensor_value_2")
    # add as many entries as you need

    # create the constructor to initialize the class
    # you can specify as many parameters as needed, with or without defaults
    # see https://www.programiz.com/python-programming/function-argument for a tutorial
    def __init__(self, value1=0, value2=0):
        self.sensor_value = value1
        self.sensor_value_2 = value2

    def reset(self):
        # TODO: add you reset logic here
        print("sensor reset")

    def get_sensor_value(self):
        return sensor_value

    def get_sensor_value_2(self):
        return sensor_value_2

    while True:
        # TODO: add your sensor logic here

        # store the values in the network table
        sensor_value.setValue(sensor_value)
        sensor_value_2.setValue(sensor_value_2)
