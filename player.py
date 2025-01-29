import pygame
from brain import Brain
from math import sqrt, dist

class Player():
  dt = 1/60
  width = 20
  height = 20
  size = width, height

  def __init__(self): 
    self.surface = pygame.Surface(self.size)
    self.surface.fill("white")

    self.brain = Brain()

    self.pos = pygame.math.Vector2(400/2, 800-50)
    self.acc = pygame.math.Vector2(0, 0)
    self.vel = pygame.math.Vector2(0, 0)

    self.dead = False
    self.passed = False

  # update position
  def move(self):
    if self.dead or self.passed: return
    self.brain.step += 1

    if (self.brain.step < len(self.brain.directions)):  
      self.acc = self.brain.directions[self.brain.step] * self.dt
      self.vel += self.acc
      self.pos += self.vel 
    else:
      self.dead = True
      print("dead no directions")
      return

    # stop updating on the next round if player reaches bounds
    if self.pos[0] + self.width > 400 or self.pos[1] + self.height > 800 or self.pos[0] < 0:
      self.dead = True
      print("dead from boundaries")
      return
    # same if player passes
    elif self.pos[1] < 0:
      self.passed = True
      print("player passed")
      return

  
  def fitness(self):
    goal = (200, 50)
    pos = self.pos

    if self.passed:
      return 1000/(self.brain.step*self.brain.step)
    elif self.dead:
      return 1/dist(goal, pos)*3

    return 1/dist(goal, pos)*2

  def clone(self):
    new_player = Player()
    new_player.brain.directions = self.brain.directions
    return new_player
  
  def __repr__(self):
    return f"PLAYER. POS {self.pos}, DEAD: {self.dead}\n"
