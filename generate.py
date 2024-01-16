import pyrosim.pyrosim as pyrosim
length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5

pyrosim.Start_SDF("boxes.sdf")

for i in range(5):
   z = 0.5
   y = 0
   length = 1
   width = 1
   height = 1
   for j in range (5):
      z = 0.5
      length = 1
      width = 1
      height = 1
      for k in range(10):
         pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])
         z = z + (height)
         length = length * 0.9
         width = width * 0.9
         height = height * 0.9
      y = y + 1
   x = x + 1

pyrosim.End()
