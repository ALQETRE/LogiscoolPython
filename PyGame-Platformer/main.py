import pygame
from random import randrange

WIDTH = 400
HEIGHT = 450

FPS = 60

GRAVITY = 0.5

RED = (242, 80, 80)
GREEN = (53, 148, 52)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# RGB

PLATFORM_HEIGHT = 10
PLATFORM_COLOR = RED

PLAYER_HEIGHT = 45
PLAYER_WIDTH = 30
PLAYER_COLOR = GREEN

ACC = 1
MAX_SPEED = 6
FRIC = 1
JUMP = 13

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")

clock = pygame.time.Clock()

platforms = [pygame.rect.Rect(0, HEIGHT - PLATFORM_HEIGHT, WIDTH, PLATFORM_HEIGHT)]


player = pygame.rect.Rect(100, 300, PLAYER_WIDTH, PLAYER_HEIGHT)

vel_x = 0
vel_y = 0

already_jump = False


def draw_platforms():
    for platform in platforms:
        pygame.draw.rect(window, PLATFORM_COLOR, platform)

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

    if player.x > WIDTH:
        player.x = 0
    elif player.x < 0:
        player.x = WIDTH 

    can_jump = False
    
    for platform in platforms:
        if player.colliderect(platform):
            player.y = platform.y - PLAYER_HEIGHT
            vel_y = 0
            can_jump = True

    if can_jump and not already_jump:
        if pressed_keys[pygame.K_UP]:
            vel_y = -JUMP
            already_jump = True
        
    if not pressed_keys[pygame.K_UP]:
        already_jump = False

    pygame.draw.rect(window, PLAYER_COLOR, player)


def make_platform():
    global platforms

    width = randrange(50, 80)
    x = randrange(0, WIDTH - width)
    y = platforms[-1].y - 120
    platform = pygame.rect.Rect(x, y, width, PLATFORM_HEIGHT)

    platforms.append(platform)

def move_screen():
    player.y += 3
    for platfor in platforms:
        platfor.y += 3

        if platfor.y > HEIGHT:
            platforms.remove(platfor)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    window.fill(BLACK)

    if player.y < HEIGHT / 3:
        move_screen()

    if platforms[-1].y > -30:
        make_platform()

    draw_platforms()
    draw_player()

    pygame.display.update()

    clock.tick(FPS)