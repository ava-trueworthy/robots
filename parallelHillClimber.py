import copy
import constants as c
from solution import SOLUTION

class PARALLEL_HILL_CLIMBER:

   def __init__(self):

      self.parents = {}
      self.nextAvailableID = 0
      
      for i in range(c.populationSize):

         self.parents[i] = SOLUTION(self.nextAvailableID)
         self.nextAvailableID += 1
      
   def Evolve(self):

      for parent in self.parents:

         self.parents[parent].Evaluate("GUI")
         """
         for currentGeneration in range(c.numberOfGenerations):

            self.Evolve_For_One_Generation()
         """

   def Evolve_For_One_Generation(self):

      self.Spawn()
      self.Mutate()
      self.child.Evaluate("DIRECT")
      self.Print()
      self.Select()

   def Spawn(self):

      self.child = copy.deepcopy(self.parent)
      self.child.Set_ID(self.nextAvailableID)
      self.nextAvailableID += 1

   def Mutate(self):

      self.child.Mutate()

   def Select(self):

      if self.parent.fitness < self.child.fitness:

         self.parent = self.child

   def Print(self):

      print()
      print(str(self.parent.fitness) + "  " + str(self.child.fitness))
      print()

   def Show_Best(self):

      self.parent.Evaluate("GUI")

