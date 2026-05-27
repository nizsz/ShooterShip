import pygame
from game import Game

class Menu:
    """Menu inicial. Composição forte com Game (+own)."""
    def __init__(self, window: pygame.Surface):
        self.window: pygame.Surface = window
        # Relação de composição direta indicada pelo losango preto (+own)
        self.game: Game = Game(self.window)

    def run(self) -> None:
        self.game.run()
