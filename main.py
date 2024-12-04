import pygame, sys
from pygame import mixer
from button import Button

#initializes all Pygame modules
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("The Song of Anathema")

#define global constants here
BACKGROUND_COLOR = (65, 55, 84)
HIGHLIGHTED_COLOR = (179, 140, 68)
NON_HIGHLIGHTED_COLOR = (193, 184, 206)

#load assets/sprite stuff here
BG = pygame.image.load("assets/Background.png")

PLAYER = pygame.image.load("assets/Player.png")
PLAYER_RECT = pygame.Rect(50, 50, 50, 50) #modify these parameters to customize hitbox

ENTITY = pygame.Rect(960, 360, 80, 80)

#re-size assets here
PLAYER = pygame.transform.scale(PLAYER, (75, 75))

#background sound
mixer.music.load("assets/background.wav")
mixer.music.play(-1)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

#play screen
def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #render background (BACKGROUND_COLOR is what we'll call a global constant)
        SCREEN.fill(BACKGROUND_COLOR)

        #define constants here
        PLAY_TEXT = get_font(45).render("Collision Demonstration", True, HIGHLIGHTED_COLOR)
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
        PLAYER_VELOCITY = 0.75

        #LEVEL_ONE_BUTTON = Button(image=pygame.image.load("assets/") finish this for level select

        #draws all assets/objects onto screen
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        #SCREEN.blit(add level buttons)
        SCREEN.blit(PLAYER, PLAYER_RECT) #draws the player + associates the proper hitbox
        pygame.draw.rect(SCREEN, (0, 255, 0), PLAYER_RECT, 2) #toggle to show player hitbox
        pygame.draw.rect(SCREEN, (0, 0, 0), ENTITY, 4) #draws the rectangle defined as ENTITY

        #checking for collisions
        if PLAYER_RECT.colliderect(ENTITY):
            pygame.draw.rect(SCREEN, (255, 0, 0), ENTITY, 4)

        PLAY_BACK = Button(image=None, pos=(640, 600),
                            text_input="BACK", font=get_font(75), base_color=NON_HIGHLIGHTED_COLOR, hovering_color=HIGHLIGHTED_COLOR)

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        #movement for the player
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_w]:
            PLAYER_RECT.y -= PLAYER_VELOCITY
        if userInput[pygame.K_a]:
            PLAYER_RECT.x -= PLAYER_VELOCITY
        if userInput[pygame.K_s]:
            PLAYER_RECT.y += PLAYER_VELOCITY
        if userInput[pygame.K_d]:
            PLAYER_RECT.x += PLAYER_VELOCITY

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

#options screen
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(BACKGROUND_COLOR)

        OPTIONS_TEXT = get_font(45).render("Put all of your settings here", True, HIGHLIGHTED_COLOR)
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color=NON_HIGHLIGHTED_COLOR, hovering_color=HIGHLIGHTED_COLOR)

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

#main menu screen
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("The Song of Anathema", True, NON_HIGHLIGHTED_COLOR)
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color=NON_HIGHLIGHTED_COLOR, hovering_color=HIGHLIGHTED_COLOR)
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color=NON_HIGHLIGHTED_COLOR, hovering_color=HIGHLIGHTED_COLOR)
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color=NON_HIGHLIGHTED_COLOR, hovering_color=HIGHLIGHTED_COLOR)

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
