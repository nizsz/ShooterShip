import pygame

class Entity:
    """Classe base para todos os objetos do jogo."""
    def __init__(self, name: str, surf: pygame.Surface, rect: pygame.Rect):
        self.name: str = name
        self.surf: pygame.Surface = surf
        self.rect: pygame.Rect = rect

    def move(self) -> None:
        pass
