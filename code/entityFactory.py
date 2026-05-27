import pygame
from entity import Entity
from player import Player
from enemy import Enemy
from background import Background

class EntityFactory:
    """Fábrica responsável por criar instâncias de entidades (+create)."""
    def get_entity(self, entity_type: str) -> Entity:
        surface_dummy = pygame.Surface((32, 32))
        rect_dummy = surface_dummy.get_rect()

        if entity_type.lower() == "player":
            return Player(name="Player1", surf=surface_dummy, rect=rect_dummy)
        elif entity_type.lower() == "enemy":
            return Enemy(name="Enemy1", surf=surface_dummy, rect=rect_dummy)
        elif entity_type.lower() == "background":
            return Background(name="Bg1", surf=surface_dummy, rect=rect_dummy)
        else:
            raise ValueError(f"Tipo de entidade desconhecido: {entity_type}")
