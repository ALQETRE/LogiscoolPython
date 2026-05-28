import pygame


WIDTH = 400
HEIGHT = 450

FPS = 60

GRAVITY = 0.5

RED = (242, 80, 80)
GREEN = (53, 148, 52)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PLATFORM_HEIGHT = 30
PLATFORM_COLOR = RED

PLAYER_HEIGHT = 45
PLAYER_WIDTH = 30
PLAYER_COLOR = GREEN

ACC = 1
MAX_SPEED = 40
FRIC = 1

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")

clock = pygame.time.Clock()


platforms = [pygame.rect.Rect(0, HEIGHT - PLATFORM_HEIGHT, WIDTH, PLATFORM_HEIGHT)]


player = pygame.rect.Rect(100, 300, PLAYER_WIDTH, PLAYER_HEIGHT)

vel_x = 0
vel_y = -15


def draw_platforms():
    for platform in platforms:
        pygame.draw.rect(window, PLATFORM_COLOR, platform)

def draw_player():
    global vel_y, vel_x

    vel_y += GRAVITY
    player.y += vel_y

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:
        print("LEFT")
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

    for platform in platforms:
        if player.colliderect(platform):
            player.y = platform.y - PLAYER_HEIGHT
            vel_y = 0

    pygame.draw.rect(window, PLAYER_COLOR, player)



while True:
    window.fill(BLACK)

    draw_platforms()
    draw_player()

    pygame.display.update()

    clock.tick(FPS)