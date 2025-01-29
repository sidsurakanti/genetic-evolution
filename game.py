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
population = Population(1000)
generations = [population]

### STEPS OF EVOLUTION
# NAUTRAL SELECTION
# REPRODUCTION OF TOP PERFORMERS
# SMALL GENETIC MUTATION
# RINSE AND REPEAT FOR HELLA GENERATIONS

while running: 
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      running = False
  
  screen.fill("black")

  pygame.draw.rect(screen, 'green', pygame.Rect(0, 50, WIDTH, 20))
  
  curr_gen = generations[-1]

  if curr_gen.isGenerationDone():
    print("generation finished")
    new_gen = curr_gen.clone()
    generations.append(new_gen)
    # print(new_gen.population)
    # create new generation

  for player in curr_gen.population:
    screen.blit(player.surface, player.pos)
    player.move()


  pygame.display.flip()
  clock.tick(60)

pygame.quit()

  