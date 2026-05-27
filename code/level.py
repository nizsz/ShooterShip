import pygame
from entityFactory import EntityFactory


class Level:
    """Fase do jogo que gerencia a lista de entidades (+use EntityFactory)."""

    def __init__(self, window: pygame.Surface, name: str):
        self.window: pygame.Surface = window
        self.name: str = name
        self.entity_list: list = []  # Armazena as entidades geradas

    def run(self) -> None:
        # Instancia e usa a fábrica localmente para criar as entidades (+use)
        factory = EntityFactory()

        player = factory.get_entity("player")
        enemy = factory.get_entity("enemy")
        background = factory.get_entity("background")

        self.entity_list.extend([background, player, enemy])

        for entity in self.entity_list:
            entity.move()
            self.window.blit(entity.surf, entity.rect)
