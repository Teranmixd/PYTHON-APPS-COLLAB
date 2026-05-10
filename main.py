import sys
import pygame

def run_game():

    pygame.init()

    clock = pygame.time.Clock()


    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Runner_Game")

    # Load images
    character = pygame.image.load('Resources/character.jpg').convert()
    character.set_colorkey((255, 255, 255))
    character = pygame.transform.scale(character,(100,200))
    character_x_pos = 0

    ground = pygame.image.load('Resources/ground.jpg')
    ground = pygame.transform.scale(ground,(1200,150))


    sky = pygame.image.load('Resources/sky.jpg')
    sky = pygame.transform.scale(sky, (1200, 800))

    font = pygame.font.Font('Resources/woff2/woff2/PixelCode.woff2', 70)
    text = font.render("MY GAME", False, 'Black')

    dragon = pygame.image.load('Resources/dragon.jpg').convert()
    dragon.set_colorkey((255,255,255))
    dragon = pygame.transform.scale(dragon,(50,100))
    dragon_x_pos = 400
    dragon_y_pos = 480

    while True:

        # Events
        for event in pygame.event.get():
         if dragon_x_pos<=0:
             dragon_x_pos =  1200
             break
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        screen.blit(sky, (0, 0))


       screen.blit(character, (character_x_pos, 500))

        screen.blit(ground, (0, 680))

       screen.blit(text,(380,20))

        screen.blit(dragon,(dragon_x_pos, dragon_y_pos ))
        dragon_x_pos -=4

        # Update screen
        pygame.display.update()

        # FPS
        clock.tick(60)

run_game()
