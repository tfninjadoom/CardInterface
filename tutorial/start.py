import pygame
from pygame.locals import *

pygame.init()
display = pygame.display.set_mode((700,500))

#Game loop begins
while True:
      # Code
      # More Code


      for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
      
      pygame.display.update()