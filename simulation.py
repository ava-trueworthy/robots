import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time

from world import WORLD
from robot import ROBOT

class SIMULATION:
   
   def __init__(self, directOrGUI):

      if directOrGUI == "DIRECT":

         self.physicsClient = p.connect(p.DIRECT)

      elif directOrGUI == "GUI":

        self.physicsClient = p.connect(p.GUI)

      p.setAdditionalSearchPath(pybullet_data.getDataPath())
      p.setGravity(0,0,-9.8)
      
      self.world = WORLD()
      self.robot = ROBOT()

   def Run(self):

      for x in range(1000):

         p.stepSimulation()

         self.robot.Sense(x)
         self.robot.Think(x)
         self.robot.Act(x)

         time.sleep(.000000001)

   def Get_Fitness(self):

      self.robot.Get_Fitness()

   def __del__(self):

      p.disconnect()
