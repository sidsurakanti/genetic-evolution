import pygame
from player import Player
from population import Population

SIZE = WIDTH, HEIGHT = 400, 800

pygame.init()
pygame.display.set_caption("Genetic Evolution")

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
running = True

player = Player()
population = Population(20)
goal = pygame.draw.circle(pygame.Surface((20, 20)), 'white', (0, 0), 4)

while running: 
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      running = False
  
  screen.fill("black")

  for player in population.population:
    screen.blit(player.surface, player.pos)
    player.move()


  pygame.display.flip()
  clock.tick(60)

pygame.quit()

  