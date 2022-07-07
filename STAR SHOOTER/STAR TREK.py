#Main Loop

import pygame
import os
import random






WIDTH = 900
HEIGHT = 800
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
SNOW = (255, 250, 250)
LIGHT_YELLOW = (255, 255, 224)
MINT_CREAM = (245, 255, 250)
LIGHT_SKY_BLUE = (135, 206, 235)
LIGHTCYAN = (224, 255, 255)
DIMGRAY = (105, 105, 105)
ALICEBLUE = (240, 248, 255)
AZURE = (240, 255, 255)
DARKGRAY = (105, 105, 105)




screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.init()
pygame.mixer.init()

background = pygame.image.load("bigtime.png")
update_background = pygame.transform.scale(background, (1800, 900))
background_rect = update_background.get_rect()
spear = os.path.join("shot.png")
rabbit = os.path.join("ship.png")
rat = os.path.join("altship.png")
explosion = os.path.join("dead.png")
shot = os.path.join("shoot.wav")
pop = os.path.join("explode.wav")
shoot_sound = pygame.mixer.Sound("shoot.wav")





font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, SNOW)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(rabbit)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT - 100
        self.speedx = 5
        self.rect.centerx = WIDTH / 2
        self.radius = 40
        self.shoot_delay = 400
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        self.speedx = 0
        dist = 15
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


    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            shoot_sound.play()

    


"""class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = pygame.image.load(explosion)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 2

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion[self.size]):
                self.kill()
                """


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(rat)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(900, 920)
        self.speedy = random.randrange(5, 10)
        self.speedx = random.randrange(2, 7)
        self.radius = 40
        self.rect.top = 900


    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-10, 0)
            self.speedy = random.randrange(4, 9)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.image.load(spear)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -50

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()



all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(14):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

"""explosion_list = []
for i in range(9):
    explosion_list.append(explosion)
    """

score = 0

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    all_sprites.update()

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score += 1

        """expl = Explosion(hit.rect.center, 20)
        all_sprites.add(expl)
        
        
        all_sprites.add(m)
        mobs.add(m)
        """


    damage = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
    if damage:
        running = False
        

    
    screen.fill(WHITE)
    screen.blit(update_background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)
    pygame.display.update()

pygame.quit()
    


