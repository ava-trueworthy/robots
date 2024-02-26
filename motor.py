import numpy
import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:

   def __init__(self, jointName):
      self.jointName = jointName
      self.Prepare_To_Act()

   def Prepare_To_Act(self):
      self.amplitude = c.amplitude
      self.frequency = c.frequency

      if (self.jointName == "Torso_BackLeg"):
         self.frequency = c.frequency*2

      self.offset = c.offset
      self.maxForce = c.maxForce

      self.motorValues = numpy.linspace(0, 2*numpy.pi, num=1000)

      for x in range(1000):
         self.motorValues[x] = self.amplitude * numpy.sin(self.frequency*self.motorValues[x] + self.offset)

   def Set_Value(self, time, robot):
      pyrosim.Set_Motor_For_Joint(bodyIndex=robot,
                                     jointName=self.jointName,
                                     controlMode=p.POSITION_CONTROL,
                                     targetPosition=self.motorValues[time],
                                     maxForce=self.maxForce)

   def Save_Values(self):
      numpy.save("data/" + self.jointName + ".npy", self.motorValues)
