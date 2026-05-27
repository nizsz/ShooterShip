import pygame
from level import Level

class Game:
    """Classe principal. Composição: possui 1 ou mais Levels (1..*)."""
    def __init__(self, window: pygame.Surface):
        self.window: pygame.Surface = window
        # Composição estrita: cria as instâncias de Level internamente
        self.levels: list[Level] = [
            Level(self.window, "Fase 1"),
            Level(self.window, "Fase 2")
        ]

    def run(self) -> None:
        for level in self.levels:
            level.run()
