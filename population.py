from player import Player
from typing import List

class Population:
    def __init__(self, size: int):
      self.population = Population.generate(size)
      self.size = size

    def natural_selection(self):
      # get top players 
      top_performers = sorted([(player, player.fitness([0, 50])) for player in self.population], key=lambda x: x[1], reverse=True)[:10]
      return top_performers
    
    # clone N best performing players
    def clone(self):
      # get 10 best players according to their distance to goal
      pass
      
    @staticmethod
    def generate(size: int) -> List[Player]:
      population = []
      for _ in range(size):
        population.append(Player())
      
      return population
    
