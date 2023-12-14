import pygame

width, height = 800, 800
rows, cols = 8, 8
square_size = width//cols

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
DARK_GREY = (100, 100, 100)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'),(44,25))
