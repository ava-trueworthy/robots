import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

from sensor import SENSOR
from motor import MOTOR

class ROBOT:

   def __init__(self):
      self.sensors = {}
      self.motors = {}
      self.robotId = p.loadURDF("body.urdf")
      pyrosim.Prepare_To_Simulate(self.robotId)
