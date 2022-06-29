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
green = (0, 153, 0)
# Creating the screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('SUSE Drum Machine')

# Adding custom font
label_font = pygame.font.Font('Snack bowl.otf', 20)

fps = 60
timer = pygame.time.Clock()
beats = 8
instruments = 9
boxes = []
clicked = [[-1 for _ in range(beats)]]


# Drawing the main screen
def draw_grid():
    left_menu = pygame.draw.rect(screen, green, [0, 0, 290, HEIGHT-200], 5)
    bottom_menu = pygame.draw.rect(screen, green, [0, HEIGHT - 200, WIDTH, 200], 5)
    boxes= []
    colors = [gray, white, gray]
    # Putting the names of the instruments on the screen
    hi_hat_text = label_font.render('Hi hat', True, white)
    screen.blit(hi_hat_text, (10, 0))
    snare_text = label_font.render('Snare', True, white)
    screen.blit(snare_text, (10, 70))
    kick_text = label_font.render('Kick', True, white)
    screen.blit(kick_text, (10, 140))
    tom1_text = label_font.render('High Tom', True, white)
    screen.blit(tom1_text, (10, 210))
    tom2_text = label_font.render('Low Tom', True, white)
    screen.blit(tom2_text, (10, 280))
    floor_tom_text = label_font.render('Floor Tom', True, white)
    screen.blit(floor_tom_text, (10, 350))
    crash_1_text = label_font.render('Crash One', True, white)
    screen.blit(crash_1_text, (10, 420))
    crash_2_text = label_font.render('Crash Two', True, white)
    screen.blit(crash_2_text, (10, 490))
    cowbell_text = label_font.render('Blue Oyster', True, white)
    screen.blit(cowbell_text, (10, 560))
    # Painting lines between the names
    for i in range(instruments):
        pygame.draw.line(screen, green, (0, (i * 67) + 67), (290, (i*67) + 67), 5)
    # Painting grid lines for rhythm
    for i in range(beats):
        for j in range(instruments):
            rect = pygame.draw.rect(screen, green, [i * ((WIDTH - 290) // beats) + 295, (j * 67),
                                                  ((WIDTH - 290) // beats), ((HEIGHT - 200)//instruments)], 5)
            boxes.append((rect, (i, j)))
    return boxes

run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    boxes = draw_grid()
    # Checking every keyboard and mouse action
    for event in pygame.event.get():
        # Adding the option to exit the game
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(boxes)):
                if boxes[i][0].colliderect(event.pos):
                    coords = boxes[i][1]
                    clicked[coords[1]][coords[0]]
    pygame.display.flip()
pygame.quit()

