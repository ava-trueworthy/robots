import numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:

   def __init__(self, linkName):
      self.linkName = linkName
      self.Prepare_To_Sense()

   def Prepare_To_Sense(self):
      self.values = numpy.zeros(1000)

   def Get_Value(self, time):
      value = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
      self.values[time] = value

   def Save_Values(self):
      numpy.save("data/" + self.linkName + ".npy", self.values)
