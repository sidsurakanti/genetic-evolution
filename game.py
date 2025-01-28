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
population = Population(500)

while running: 
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      running = False
  
  screen.fill("black")

  pygame.draw.rect(screen, 'green', pygame.Rect(0, 50, WIDTH, 20))

  for player in population.population:
    screen.blit(player.surface, player.pos)
    if player.brain.step == 1000:
      # create new generation after natural selection    
      pass  

    player.move()


  pygame.display.flip()
  clock.tick(60)

pygame.quit()

  