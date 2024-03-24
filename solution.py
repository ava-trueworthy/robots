import constants as c
import numpy as np
import os
import pyrosim.pyrosim as pyrosim
import random
import time

class SOLUTION:

   def __init__(self, myID):

      self.myID = myID
      self.weights = np.array([[np.random.rand(), np.random.rand()],
                      [np.random.rand(), np.random.rand()],
                      [np.random.rand(), np.random.rand()]])
      
      self.weights = self.weights * 2 - 1

   def Start_Simulation(self, directOrGUI):

      self.Create_World()
      self.Generate_Body()
      self.Generate_Brain()

      os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")

   def Wait_For_Simulation_To_End(self):

      while not os.path.exists("fitness" + str(self.myID) + ".txt"):

         time.sleep(0.01)

      fitnessFile = open("fitness" + str(self.myID) + ".txt", "r")
      self.fitness = float(fitnessFile.read())
      fitnessFile.close()
      
      os.system("rm fitness" + str(self.myID) + ".txt")

   def Mutate(self):

      randomRow = random.randint(0,2)
      randomColumn = random.randint(0,1)
      self.weights[randomRow][randomColumn] = random.random() * 2 - 1

   def Create_World(self):

      length = 1
      width = 1
      height = 1

      pyrosim.Start_SDF("world.sdf")

      pyrosim.Send_Cube(name="Box", pos=[-2, -2, 0.5], size=[length, width, height])

      pyrosim.End()

   def Generate_Body(self):

      pyrosim.Start_URDF("body.urdf")

      pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[1,1,1])

      pyrosim.Send_Joint(name = "Torso_BackLeg", parent = "Torso", child = "BackLeg", type = "revolute", position = [1,0,1])
      pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[1,1,1])

      pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2,0,1])
      pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[1,1,1])

      pyrosim.End()

   def Generate_Brain(self):

      pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

      pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
      pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
      pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

      pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
      pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

      for currentRow in range(c.numSensorNeurons):

         for currentColumn in range(c.numMotorNeurons):

            pyrosim.Send_Synapse(sourceNeuronName=str(currentRow), targetNeuronName=str(currentColumn+c.numSensorNeurons), weight=self.weights[currentRow][currentColumn])

      pyrosim.End()
      
   def Set_ID(self, myID):

      self.myID = myID


