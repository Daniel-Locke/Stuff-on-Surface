import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
yellow = (200,200,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tanks')
#img = pygame.image.load('snakehead.png')
#appleimg = pygame.image.load('apple.png')
#icon = pygame.image.load('apple.png')
#pygame.display.set_icon(icon)

clock = pygame.time.Clock()

#block_size = 20
#AppleThickness = 30
FPS = 30
smallfont = pygame.font.SysFont("comicsansms", 25)
mediumfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

font = pygame.font.SysFont(None, 25)

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        message_to_screen("Welcome to Tanks!", green, -100, size="large")
        message_to_screen("The Objective of the game is to shoot and destroy",
                          black, -30, size = "small")
        message_to_screen("The enemy tank before they destroy you.",
                          black, 10, size="small")
        message_to_screen("The more enemies you hit, the harder it gets",
                          black, 50, size="small")
        message_to_screen("Press C to play, P to pause, or Q to quit",
                          black, 180, size="small")
        pygame.display.update()
        clock.tick(15)




def text_objects(text, color, size):
    if size == 'small':
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = mediumfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text,True,color)
    return textSurface, textSurface.get_rect()

def pause():
    paused = True
    message_to_screen("Paused", black, -100, size="large")
    message_to_screen('Press C to continue or Q to quit.', black, 25, size="small")
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        #gameDisplay.fill(white)

        clock.tick(5)


def score(score):
    text = smallfont.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, [0,0])




def message_to_screen(msg, color, y_displace=0, size = 'small'):
    # screen_text = font.render(msg, True, color)
    # gameDisplay.blit(screen_text, [display_width / 2, display_height / 2])
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2)+ y_displace
    gameDisplay.blit(textSurf, textRect)

def gameLoop():
    gameExit = False
    gameOver = False

    while not gameExit:
        if gameOver == True:
            # gameDisplay.fill(white)
            message_to_screen("Game over", red, y_displace=-50, size="large")
            message_to_screen("Press C to play again or Q to quit", black, y_displace=50, size="medium")
            pygame.display.update()
        while gameOver == True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_p:
                    pause()
                elif event.key == pygame.K_t:
                    game_intro()
                    gameLoop()

        gameDisplay.fill(white)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()