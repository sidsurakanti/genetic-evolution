import pygame
import random
from math import pi


class Brain:
  def __init__(self):
    self.directions = Brain.fill_directions(1000)
    self.step = 0

  def mutate(self):
    MUTATION_RATE = 0.01
    directions = []
    
    for direction in self.directions:
      rand = random.random()
      if rand < MUTATION_RATE:
        rotatedV = direction.rotate_rad(random.uniform(0, 2*pi)).normalize()
        directions.append(rotatedV)
      else:
        directions.append(direction)
      
    self.directions = directions

  @staticmethod
  def fill_directions(len: int = 800):
    vec = pygame.math.Vector2
    directions = []

    for _ in range(len):
      move_i = vec(0, 1)
      rotatedV = move_i.rotate_rad(random.uniform(0, 2*pi)).normalize()
      directions.append(rotatedV)

    return directions
  
brain = Brain()
