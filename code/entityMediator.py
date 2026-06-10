from code.const import WIN_WIDTH
from code.enemy import Enemy
from code.enemyShoot import EnemyShoot
from code.entity import Entity
from code.player import Player
from code.playerShoot import PlayerShoot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, PlayerShoot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShoot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent_one, ent_two):
        valid_interaction = False
        if isinstance(ent_one, Enemy) and isinstance(ent_two, PlayerShoot):
            valid_interaction = True

        elif isinstance(ent_one, PlayerShoot) and isinstance(ent_two, Enemy):
            valid_interaction = True

        elif isinstance(ent_one, Player) and isinstance(ent_two, EnemyShoot):
            valid_interaction = True

        elif isinstance(ent_one, EnemyShoot) and isinstance(ent_two, Player):
            valid_interaction = True

        if valid_interaction:  # if valid_interaction == True:
            if (ent_one.rect.right >= ent_two.rect.left and
                    ent_one.rect.left <= ent_two.rect.right and
                    ent_one.rect.bottom >= ent_two.rect.top and
                    ent_one.rect.top <= ent_two.rect.bottom):
                ent_one.health -= ent_two.damage
                ent_two.health -= ent_one.damage
                ent_one.last_dmg = ent_two.name
                ent_two.last_dmg = ent_one.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == "PlayerOneShoot":
            for ent in entity_list:
                if ent.name == "PlayerOne":
                    ent.score += enemy.score
        elif enemy.last_dmg == "PlayerTwoShoot":
            for ent in entity_list:
                if ent.name == "PlayerTwo":
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity_one = entity_list[i]
            EntityMediator.__verify_collision_window(entity_one)
            for j in range(i + 1, len(entity_list)):
                entity_two = entity_list[j]
                EntityMediator.__verify_collision_entity(entity_one, entity_two)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Entity):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)