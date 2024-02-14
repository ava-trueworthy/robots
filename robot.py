import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

from sensor import SENSOR
from motor import MOTOR

class ROBOT:

   def __init__(self):
      self.motors = {}
      self.robotId = p.loadURDF("body.urdf")
      pyrosim.Prepare_To_Simulate(self.robotId)
      self.Prepare_To_Sense()

   def Prepare_To_Sense(self):
      self.sensors = {}
      for linkName in pyrosim.linkNamesToIndices:
         self.sensors[linkName] = SENSOR(linkName)


   def Sense(self, time):
      for sensorInstance in self.sensors:
         self.sensors[sensorInstance].Get_Value(time)
