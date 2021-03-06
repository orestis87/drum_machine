import pygame
from pygame import mixer
pygame.init()
pygame.mixer.init()
# Setting up the screen
WIDTH = 1400
HEIGHT = 800

# Defining RGB colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
dark_gray = (50, 50, 50, 0)
green = (0, 153, 0)
gold = (212, 175, 55)
blue = (0, 255, 255)
# Creating the screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('SUSE Drum Machine')

# Adding custom font
label_font = pygame.font.Font('Snack bowl.otf', 20)
medium_font = pygame.font.Font('Snack bowl.otf', 25)
fps = 60
timer = pygame.time.Clock()
beats = 8
instruments = 9
boxes = []
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
bpm = 240
playing = True
active_length = 0
active_beat = 0
beat_changed = True

# Load sounds
pygame.mixer.init(44100, -16,2,2048)
hi_hat = mixer.Sound('Samples\Hats\closed_hi-hat.wav')
snare = mixer.Sound('Samples\snare\Snrambnt2.wav')
kick = mixer.Sound('Samples\Kicks\AFCC kick 2.wav')
tom1 = mixer.Sound('Samples\Tom\\10tom.wav')
tom2 = mixer.Sound('Samples\Tom\\14tom.wav')
floor_tom = mixer.Sound('Samples\Tom\\16tom.wav')
crash_1 = mixer.Sound('Samples\Crash\cym10splsh.wav')
crash_2 = mixer.Sound('Samples\Crash\cymhicrsh.wav')
cowbell = mixer.Sound('Samples\Cowbell\low_cowbell.wav')
pygame.mixer.set_num_channels(instruments * 3)

def play_notes():
    for i in range(len(clicked)):
        if clicked[i][active_beat] == 1:
            if i == 0:
                hi_hat.play()
            if i == 1:
                snare.play()
            if i == 2:
                kick.play()
            if i == 3:
                tom1.play()
            if i == 4:
                tom2.play()
            if i == 5:
                floor_tom.play()
            if i == 6:
                crash_1.play()
            if i == 7:
                crash_2.play()
            if i == 8:
                cowbell.play()


# Drawing the main screen
def draw_grid(clicks, beat):
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
            if clicks[j][i] == -1:
                color = gray
            else:
                color = green
            rect = pygame.draw.rect(screen, color, [i * ((WIDTH - 290) // beats) + 300, (j * 67) + 5,
                                                  ((WIDTH - 290) // beats) - 10, ((HEIGHT - 200)//instruments) - 10], 0)
            pygame.draw.rect(screen, green, [i * ((WIDTH - 290) // beats) + 295, (j * 67),
                                             ((WIDTH - 290) // beats), ((HEIGHT - 200)//instruments)], 5)
            pygame.draw.rect(screen, black, [i * ((WIDTH - 290) // beats) + 295, (j * 67),
                                                    ((WIDTH - 290) // beats), ((HEIGHT - 200)//instruments)], 2)
            boxes.append((rect, (i, j)))

        active = pygame.draw.rect(screen, blue, [beat * ((WIDTH - 290)//beats) + 295, 0, ((WIDTH - 295)//beats), instruments * 67], 5)
    return boxes

run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    boxes = draw_grid(clicked, active_beat)
    # Buttons
    play_pause = pygame.draw.rect(screen, gray, [50, HEIGHT - 150, 200, 100], 5)
    play_text = label_font.render('Play/Pause', True, white)
    screen.blit(play_text, (70, HEIGHT - 130))
    if playing:
        play_text2 = medium_font.render('Playing', True, green)
    else:
        play_text2 = medium_font.render ('Paused', True, green)
    screen.blit(play_text2, (70, HEIGHT - 100))
    if beat_changed:
        play_notes()
        beat_changed = False

    # Checking every keyboard and mouse action
    for event in pygame.event.get():
        # Adding the option to exit the game
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(boxes)):
                if boxes[i][0].collidepoint(event.pos):
                    coords = boxes[i][1]
                    clicked[coords[1]][coords[0]] *= -1
        if event.type == pygame.MOUSEBUTTONUP:
            if play_pause.collidepoint(event.pos):
                if playing:
                    playing = False
                elif not playing:
                    playing = True


    beat_length = fps * 60 // bpm

    if playing:
        if active_length < beat_length:
            active_length +=1
        else:
            active_length = 0
            if active_beat < beats - 1:
                active_beat += 1
                beat_changed = True
            else:
                active_beat = 0
                beat_changed = True

    pygame.display.flip()
pygame.quit()

