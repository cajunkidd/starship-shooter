#Player Class

import pygame
import os
import random

from enemy import Mob

WIDTH = 700
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

spear = os.path.join("bullet.png")
rabbit = os.path.join("ship.png")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(rabbit)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = 500
        self.speedx = 0
        self.rect.centerx = WIDTH / 2
        
        self.radius = 20
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()


    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet) 

    def update(self):
        self.speedx = 0
        dist = 10
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            self.rect.y += dist
        elif key[pygame.K_UP]:
            self.rect.y -= dist
        if key[pygame.K_RIGHT]:
            self.rect.x += dist
        elif key[pygame.K_LEFT]:
            self.rect.x -= dist
        if key[pygame.K_SPACE]:
            self.shoot()

          
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(spear)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
            all_sprites.add(bullet)
            bullets.add(bullet)   
