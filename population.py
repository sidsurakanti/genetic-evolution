from player import Player
from typing import List

class Population:
    def __init__(self, size: int):
      self.population = Population.generate(size)
      self.size = size

    @staticmethod
    def generate(size: int) -> List[Player]:
      population = []
      for _ in range(size):
        population.append(Player())
      
      return population
    
    # clone N best performing players
    def clone():
      # get 10 best players according to their distance to goal
      pass
