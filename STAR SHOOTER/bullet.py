#Bullet Class

import pygame
import os
import random
from enemy import Mob
from player import Player


spear = os.path.join("bullet.png")

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(spear)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
            all_sprites.add(bullet)
            bullets.add(bullet)   
