import pygame
from brain import Brain

class Player():
  dt = 1/60
  width = 20
  height = 20
  size = width, height

  def __init__(self): 
    self.surface = pygame.Surface(self.size)
    self.surface.fill("blue")

    self.brain = Brain()

    self.pos = pygame.math.Vector2(400/2, 800-50)
    self.acc = pygame.math.Vector2(0, 0)
    self.vel = pygame.math.Vector2(0, 0)

    self.dead = False
    self.passed = True

  def move(self):
    # update position
    if self.dead: return

    if (self.brain.step < len(self.brain.directions)):  
      self.acc = self.brain.directions[self.brain.step] * self.dt
      self.vel += self.acc
      self.pos += self.vel 
    else:
      self.dead = True

    # stop updating if player reaches bounds
    if self.pos[0] + self.width > 400 or self.pos[1] + self.height > 800 or self.pos[0] < 0:
      self.dead = True
      return
    # stop updating if player passes 
    elif self.pos[0] < 0:
      self.passed = True

    self.brain.step += 1
  
