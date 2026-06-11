# C
import pygame

C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_SELECTION = (255, 255, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)
C_YELLOW = (255, 255, 0)

#E

ENTITY_DAMAGE = {
    "Level1Cloud0": 0,
    "Level1Cloud1": 0,
    "Level1Cloud2": 0,
    "Level1Cloud3": 0,
    'Level2Cloud0': 0,
    'Level2Cloud1': 0,
    'Level2Cloud2': 0,
    'Level2Cloud3': 0,
    'PlayerOne': 1,
    'PlayerOneShoot': 25,
    'PlayerTwo': 1,
    'PlayerTwoShoot': 20,
    'EnemyOne': 1,
    'EnemyOneShoot': 20,
    'EnemyTwo': 1,
    'EnemyTwoShoot': 15,
}

ENTITY_SCORE = {
    "Level1Cloud0": 0,
    "Level1Cloud1": 0,
    "Level1Cloud2": 0,
    "Level1Cloud3": 0,
    'Level2Cloud0': 0,
    'Level2Cloud1': 0,
    'Level2Cloud2': 0,
    'Level2Cloud3': 0,
    'PlayerOne': 0,
    'PlayerOneShoot': 0,
    'PlayerTwo': 0,
    'PlayerTwoShoot': 0,
    'EnemyOne': 100,
    'EnemyOneShoot': 0,
    'EnemyTwo': 125,
    'EnemyTwoShoot': 0,
}


EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_SPEED = {
    "Level1Cloud0": 0,
    "Level1Cloud1": 1,
    "Level1Cloud2": 2,
    "Level1Cloud3": 3,
    'Level2Cloud0': 0,
    'Level2Cloud1': 1,
    'Level2Cloud2': 2,
    'Level2Cloud3': 3,
    "PlayerOne": 3,
    "PlayerOneShoot": 1,
    "PlayerTwo": 3,
    "PlayerTwoShoot": 1,
    "EnemyOne": 1,
    "EnemyOneShoot": 5,
    "EnemyTwo": 1,
    "EnemyTwoShoot": 2,
}

ENTITY_HEALTH = {
    'Level1Cloud0': 999,
    'Level1Cloud1': 999,
    'Level1Cloud2': 999,
    'Level1Cloud3': 999,
    'Level2Cloud0': 999,
    'Level2Cloud1': 999,
    'Level2Cloud2': 999,
    'Level2Cloud3': 999,
    'PlayerOne': 300,
    'PlayerTwo': 300,
    'EnemyOne': 50,
    'EnemyTwo': 70,
    'PlayerOneShoot': 1,
    'PlayerTwoShoot': 1,
    'EnemyOneShoot': 1,
    'EnemyTwoShoot': 1,
}

ENTITY_SHOOT_DELAY = {
    'PlayerOne': 20,
    'PlayerTwo': 15,
    'EnemyOne': 100,
    'EnemyTwo': 200,
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

SPAWN_TIME = 2000


#T
TIMEOUT_LEVEL = 20000
TIMEOUT_STEP = 100

# W
WIN_WIDTH= 576
WIN_HEIGHT= 324

# S

SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 50),
    'EnterName': (WIN_WIDTH / 2, 80),
    'Label': (WIN_WIDTH / 2, 90),
    'Name': (WIN_WIDTH / 2, 110),
    0: (WIN_WIDTH / 2, 110),
    1: (WIN_WIDTH / 2, 130),
    2: (WIN_WIDTH / 2, 150),
    3: (WIN_WIDTH / 2, 170),
    4: (WIN_WIDTH / 2, 190),
    5: (WIN_WIDTH / 2, 210),
    6: (WIN_WIDTH / 2, 230),
    7: (WIN_WIDTH / 2, 250),
    8: (WIN_WIDTH / 2, 270),
    9: (WIN_WIDTH / 2, 290),
}