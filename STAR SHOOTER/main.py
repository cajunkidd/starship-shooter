#Main Loop

import pygame
import os
import random
from bullet import Bullet
from enemy import Mob
from player import Player




WIDTH = 700
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.init()

background = pygame.image.load("bigtime.png")
update_background = pygame.transform.scale(background, (700, 600))
background_rect = update_background.get_rect()


all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()

all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()


    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score += 50
        

    all_sprites.update()
    screen.fill(WHITE)
    screen.blit(update_background, background_rect)
    all_sprites.draw(screen)
    pygame.display.flip()
    pygame.display.update()

pygame.quit()
    


