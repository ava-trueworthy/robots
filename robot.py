import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

from sensor import SENSOR
from motor import MOTOR

class ROBOT:

   def __init__(self):

      self.robotId = p.loadURDF("body.urdf")
      pyrosim.Prepare_To_Simulate(self.robotId)
      self.Prepare_To_Sense()
      self.Prepare_To_Act()
      self.nn = NEURAL_NETWORK("brain.nndf")

   def Prepare_To_Sense(self):

      self.sensors = {}

      for linkName in pyrosim.linkNamesToIndices:

         self.sensors[linkName] = SENSOR(linkName)

   def Prepare_To_Act(self):

      self.motors = {}

      for jointName in pyrosim.jointNamesToIndices:

         self.motors[jointName] = MOTOR(jointName)

   def Sense(self, time):

      for sensorInstance in self.sensors:

         self.sensors[sensorInstance].Get_Value(time)

   def Think(self, time):

      self.nn.Update()
      """
      self.nn.Print()
      """

   def Act(self, time):

      for neuronName in self.nn.Get_Neuron_Names():

         if self.nn.Is_Motor_Neuron(neuronName):

            jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
            desiredAngle = self.nn.Get_Value_Of(neuronName)
            self.motors[jointName].Set_Value(desiredAngle, self.robotId)

   def Get_Fitness(self):

      self.stateOfLinkZero = p.getLinkState(self.robotId, 0)
      self.positionOfLinkZero = self.stateOfLinkZero[0]
      self.xCoordinateOfLinkZero = self.positionOfLinkZero[0]

      fitnessFile = open("fitness.txt", "w")
      fitnessFile.write(str(self.xCoordinateOfLinkZero))
      fitnessFile.close()
