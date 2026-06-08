# C
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_SELECTION = (255, 255, 0)

#E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {
    "Level1Cloud0": 0,
    "Level1Cloud1": 1,
    "Level1Cloud2": 2,
    "Level1Cloud3": 3,
    "PlayerOne": 3,
    "PlayerTwo": 3,
    "EnemyOne": 2,
    "EnemyTwo": 1
}


# M
MENU_OPTION = ("NEW GAME 1P",
               "NEW GAME 2P - COOPERATIVE",
               "NEW GAME 2P - COMPETITIVE",
               "SCORE",
               "EXIT"
               )

# P
PLAYER_KEY_UP = {
    'PlayerOne': pygame.K_UP,
    'PlayerTwo': pygame.K_w
}

PLAYER_KEY_DOWN = {
    'PlayerOne': pygame.K_DOWN,
    'PlayerTwo': pygame.K_s
}

PLAYER_KEY_LEFT = {
    'PlayerOne': pygame.K_LEFT,
    'PlayerTwo': pygame.K_a
}

PLAYER_KEY_RIGHT = {
    'PlayerOne': pygame.K_RIGHT,
    'PlayerTwo': pygame.K_d
}

PLAYER_KEY_SHOOT = {
    'PlayerOne': pygame.K_RCTRL,
    'PlayerTwo': pygame.K_LCTRL
}

# S

SPAWN_TIME = 4000

# W
WIN_WIDTH= 576
WIN_HEIGHT= 324