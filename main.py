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

# Adding custom font
label_font = pygame.font.Font('Snack bowl.otf', 32)

fps = 60
timer = pygame.time.Clock()

run = True
while run:
    timer.tick(fps)
    screen.fill(black)
# Checking every keyboard and mouse action
    for event in pygame.event.get():
# Adding the option to exit the game
        if event.type == pygame.QUIT:
            run = False
