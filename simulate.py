import time
import pybullet as p
physicsClient = p.connect(p.GUI)
p.loadSDF("box.sdf")
for x in range(1000):
   p.stepSimulation()
   time.sleep(.001)
   print(x)
p.disconnect()
