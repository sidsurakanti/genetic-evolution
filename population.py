from player import Player
from typing import List
import random

class Population:
    def __init__(self, size: int, population = None):
      self.population = population if population else Population.generate(size) 
      self.size = size
      self.generation = 0

    # clone N best performing players
    def clone(self):
      # get 10 best players according to their distance to goal
      new_gen = Population(self.size)
      get_babies = self.natural_selection()
      new_gen.population = get_babies
      return new_gen

    def natural_selection(self):
      # get new generation based on a random selection of top players
      fitnessValues = [player.fitness() for player in self.population]
      fitnessSum = int(sum(fitnessValues))
      new_babies = []

      for _ in range(self.size):
        baby = self.get_fit_parent(fitnessValues, fitnessSum)
        baby.brain.mutate()
        new_babies.append(baby)
      
      return new_babies

    def get_fit_parent(self, fitnessValues, fitnessSum):
      runningSum = 0
      rand = random.uniform(0, fitnessSum)

      for player, fitness in zip(self.population, fitnessValues):
        runningSum += fitness
        if runningSum > rand:
          return player.clone()
      

    def isGenerationDone(self):
      for player in self.population:
        if not (player.dead or player.passed):
          return False

      return True


    @staticmethod
    def generate(size: int) -> List[Player]:
      population = []
      for _ in range(size):
        population.append(Player())
      
      return population
    

