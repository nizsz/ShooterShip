import random

from code.background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.enemy import Enemy
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case "Level1Cloud":
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f"Level1Cloud{i}", (0, 0)))
                    list_bg.append(Background(f"Level1Cloud{i}", (WIN_WIDTH, 0)))
                return list_bg
            case "PlayerOne":
                return Player(f"PlayerOne", (10, WIN_HEIGHT / 2 - 30))
            case "PlayerTwo":
                return Player(f"PlayerTwo", (10, WIN_HEIGHT / 2 + 30))
            case "EnemyOne":
                return Enemy(f"EnemyOne", (WIN_WIDTH + 10, random.randint(40,WIN_HEIGHT - 40)))
            case "EnemyTwo":
                return Enemy(f"EnemyTwo", (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))