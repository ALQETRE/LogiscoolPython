import pygame
from random import randrange

# Print score to the console

# Score je kolik platforem jsme udělali
# Nebo max výška kam jsme se dostali


WIDTH = 400
HEIGHT = 450

background = pygame.transform.scale(pygame.image.load("Assets/background.png"), (1000, 500))

FPS = 60

GRAVITY = 0.5

RED = (242, 80, 80)
GREEN = (53, 148, 52)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# RGB

PLATFORM_HEIGHT = 5
PLATFORM_COLOR = RED

platfor_sprite = pygame.image.load("Assets/platform.png")

PLAYER_HEIGHT = 45
PLAYER_WIDTH = 30
PLAYER_COLOR = GREEN

player_sprite = pygame.transform.scale(pygame.image.load("Assets/player.png"), (75, 65))


ACC = 1
MAX_SPEED = 6
FRIC = 1
JUMP = 13

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")

clock = pygame.time.Clock()

platforms = [pygame.rect.Rect(-5, HEIGHT - 30, WIDTH + 10, PLATFORM_HEIGHT)]
platform_speeds = [0]


player = pygame.rect.Rect(100, 300, PLAYER_WIDTH, PLAYER_HEIGHT)

vel_x = 0
vel_y = 0

already_jump = False


def draw_platforms():
    for i, platform in enumerate(platforms):
        speed = platform_speeds[i]
        platform.x += speed

        if platform.x > WIDTH:
            platform.x = -platform.width
        elif platform.x < -platform.width:
            platform.x = WIDTH


        window.blit(pygame.transform.scale(platfor_sprite, (platform.width, 30)), platform)
        # pygame.draw.rect(window, PLATFORM_COLOR, platform)

def draw_player():
    global vel_y, vel_x, already_jump

    vel_y += GRAVITY
    player.y += vel_y

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:
        vel_x -= ACC
    elif pressed_keys[pygame.K_RIGHT]:
        vel_x += ACC
    else:
        if vel_x > 0:
            vel_x -= FRIC
            if vel_x < 0:
                vel_x = 0
        elif vel_x < 0:
            vel_x += FRIC
            if vel_x > 0:
                vel_x = 0

    if vel_x > MAX_SPEED:
        vel_x = MAX_SPEED

    elif vel_x < -MAX_SPEED:
        vel_x = -MAX_SPEED
        
    player.x += vel_x

    can_jump = False
    
    for i, platform in enumerate(platforms):
        if player.colliderect(platform):
            player.y = platform.y - PLAYER_HEIGHT
            vel_y = 0
            can_jump = True

            player.x += platform_speeds[i]

    if player.x > WIDTH:
        player.x = -player.width
    elif player.x < -player.width:
        player.x = WIDTH 

    if can_jump and not already_jump:
        if pressed_keys[pygame.K_UP]:
            vel_y = -JUMP
            already_jump = True
        
    if not pressed_keys[pygame.K_UP]:
        already_jump = False


    # pygame.draw.rect(window, PLAYER_COLOR, player)
    window.blit(player_sprite, (player.centerx - 40, player.centery - 28))


def make_platform():
    global platforms, platform_speeds

    width = randrange(50, 80)
    x = randrange(0, WIDTH - width)
    y = platforms[-1].y - 120
    platform = pygame.rect.Rect(x, y, width, PLATFORM_HEIGHT)

    speed = 0
    random = randrange(0, 4)
    if random == 0:
        speed = 1
    elif random == 1:
        speed = -1

    platforms.append(platform)
    platform_speeds.append(speed)

def move_screen():
    player.y += 3
    for platform in platforms:
        platform.y += 3

        if platform.y > HEIGHT:
            idx = platforms.index(platform)
            platforms.remove(platform)
            platform_speeds.pop(idx)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # window.fill(BLACK)

    window.blit(background, (-300, 0))

    if player.y < HEIGHT / 3:
        move_screen()

    if platforms[-1].y > -30:
        make_platform()

    draw_platforms()
    draw_player()

    pygame.display.update()

    clock.tick(FPS)