from simulation import SIMULATION
"""
import constants as c
import numpy
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random
import time

for x in range(1000):
   p.stepSimulation()

   backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
   c.backLegSensorValues[x] = backLegTouch

   frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
   c.frontLegSensorValues[x] = frontLegTouch

   pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, 
                               jointName="Torso_BackLeg",
                               controlMode=p.POSITION_CONTROL,
                               targetPosition=c.targetAnglesBackLeg[x],
                               maxForce=c.maxForceBackLeg)

   pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,
                               jointName="Torso_FrontLeg",
                               controlMode=p.POSITION_CONTROL,
                               targetPosition=c.targetAnglesFrontLeg[x],
                               maxForce=c.maxForceFrontLeg)

   time.sleep(.001)

p.disconnect()
"""
simulation = SIMULATION()
