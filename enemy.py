import pygame
import math
from settings import path_enemy_1, path_enemy_2, Color

# initialization
pygame.init()
color = Color()  # import color
image_enemy = pygame.image.load('images/enemy.png')  # import enemy's image

class Enemy:
    def __init__(self):     # set enemy size, hp, point, move, path
        self.width = 40
        self.height = 50
        self.image = pygame.transform.scale(image_enemy, (self.width, self.height))
        self.health = 5
        self.max_health = 10
        self.path = path_enemy_1
        self.path_pos = 0
        self.move_count = 0
        self.stride = 1
        self.x, self.y = self.path[0]

    def draw_enemy(self, window):   # draw enemy
        window.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))

    def draw_health_bar(self, window):  # draw enemy's hp
        pygame.draw.rect(window, color.red, [self.x - self.width // 2, self.y - self.height // 2 - 5, self.max_health * 4, 5])
        pygame.draw.rect(window, color.green, [self.x - self.width // 2, self.y - self.height // 2 - 5,  self.health * 4, 5])

    def move(self):
        # count the distance of two points
        now_x, now_y = self.path[self.path_pos]
        after_x, after_y = self.path[self.path_pos + 1]
        distance = math.sqrt((now_x - after_x) ** 2 + (now_y - after_y) ** 2)
        max_count = int(distance / self.stride)
        # count the new point
        if self.move_count < max_count:
            unit_vector_x = (after_x - now_x) / distance
            unit_vector_y = (after_y - now_y) / distance
            delta_x = unit_vector_x * self.stride
            delta_y = unit_vector_y * self.stride
            self.x += delta_x
            self.y += delta_y
            self.move_count += 1
        else:
            self.path_pos += 1
            self.move_count = 0

class EnemyGroup:
    def __init__(self):  # create enemy group
        self.gen_count = 0
        self.gen_period = 120
        self.reserved_members = []
        self.expedition = [Enemy()]
        self.wave_count = 0

    def campaign(self):
        if not self.is_empty():
            if self.gen_count == self.gen_period:      # every period(120) pass, put enemy group in game
                self.expedition.append(self.reserved_members.pop())
                self.gen_count = 0
            else:
                self.gen_count += 1

    def generate(self, number):
        # set the number of enemies
        for i in range(0, number):
            i = Enemy()
            if self.wave_count % 2 == 1:  # if times of wave equal even, enemy will pop in path_enemy_2
                i.path = path_enemy_2
                i.x, i.y = i.path[0]
            self.reserved_members.append(i)
        self.wave_count += 1  # count times of wave

    def get(self):
        """
        Get the enemy list
        """
        return self.expedition

    def is_empty(self):
        """
        Return whether the enemy is empty (so that we can move on to next wave)
        """
        return False if self.reserved_members else True

    def retreat(self, enemy):
        """
        Remove the enemy from the expedition
        :param enemy: class Enemy()
        :return: None
        """
        self.expedition.remove(enemy)





