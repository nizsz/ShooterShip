import pygame
from code.menu import Menu
from code.const import WIN_WINDTH,WIN_HEIGHT

class Game:
    """Classe principal"""
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WINDTH, WIN_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()

            pass

