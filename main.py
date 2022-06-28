import pygame
from pygame import mixer
pygame.init()

# Setting up the screen
WIDTH = 1400
HEIGHT = 800

# Defining RGB colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

# Creating the screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('SUSE Drum Machine')

