import sys
from simulation import SIMULATION

directOrGUI = sys.argv
print(directOrGUI)

simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness()

