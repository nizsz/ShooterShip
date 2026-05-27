import pygame
from game import Game

class Menu:
    """Menu inicial. Composição forte com Game (+own)."""
    def __init__(self, window):
        self.window = window

    def run(self) -> None:
        self.game.run()
