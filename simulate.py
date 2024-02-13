import time
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

amplitudeBackLeg = numpy.pi/8
frequencyBackLeg = 10
phaseOffsetBackLeg = 0

targetAnglesBackLeg = numpy.linspace(0, 2*numpy.pi, num=1000)

for x in range(1000):
   targetAnglesBackLeg[x] = amplitudeBackLeg * numpy.sin(frequencyBackLeg*targetAnglesBackLeg[x] + phaseOffsetBackLeg)

amplitudeFrontLeg = numpy.pi/4
frequencyFrontLeg = 10
phaseOffsetFrontLeg = numpy.pi/4

targetAnglesFrontLeg = numpy.linspace(0, 2*numpy.pi, num=1000)

for x in range(1000):
   targetAnglesFrontLeg[x] = amplitudeFrontLeg * numpy.sin(frequencyFrontLeg*targetAnglesFrontLeg[x] + phaseOffsetFrontLeg)

numpy.save("data/targetAnglesBackLeg.npy", targetAnglesBackLeg)
numpy.save("data/targetAnglesFrontLeg.npy", targetAnglesFrontLeg)

for x in range(1000):
   p.stepSimulation()

   backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
   backLegSensorValues[x] = backLegTouch

   frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
   frontLegSensorValues[x] = frontLegTouch

   pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, 
                               jointName="Torso_BackLeg",
                               controlMode=p.POSITION_CONTROL,
                               targetPosition=targetAnglesBackLeg[x],
                               maxForce=500)

   pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,
                               jointName="Torso_FrontLeg",
                               controlMode=p.POSITION_CONTROL,
                               targetPosition=targetAnglesFrontLeg[x],
                               maxForce=500)

   time.sleep(.001)

numpy.save("data/backLegValues.npy", backLegSensorValues)
numpy.save("data/frontLegValues.npy", frontLegSensorValues)
p.disconnect()
