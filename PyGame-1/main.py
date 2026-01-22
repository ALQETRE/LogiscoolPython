import pygame

pygame.init()

WIDTH = 900
HEIGHT = 500

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game!")

FPS = 60
RED_VEL = 3
YELLOW_VEL = 6

RED_SHIP_ASSET = "Assets\\spaceship_red.png"
YELLOW_SHIP_ASSET = "Assets\\spaceship_yellow.png"

SHIP_WIDTH = 60
SHIP_HEIGHT = 80

RED_SHIP_SPRITE = pygame.image.load(RED_SHIP_ASSET)
RED_SHIP_SPRITE = pygame.transform.rotate(RED_SHIP_SPRITE, -90)
RED_SHIP_SPRITE = pygame.transform.scale(RED_SHIP_SPRITE, (SHIP_WIDTH, SHIP_HEIGHT))

YELLOW_SHIP_SPRITE = pygame.image.load(YELLOW_SHIP_ASSET)
YELLOW_SHIP_SPRITE = pygame.transform.rotate(YELLOW_SHIP_SPRITE, 90)
YELLOW_SHIP_SPRITE = pygame.transform.scale(YELLOW_SHIP_SPRITE, (SHIP_WIDTH, SHIP_HEIGHT))

RED_SHIP = pygame.rect.Rect(WIDTH/4*3-(SHIP_WIDTH/2), HEIGHT/2-(SHIP_HEIGHT/2), SHIP_WIDTH, SHIP_HEIGHT)
YELLOW_SHIP = pygame.rect.Rect(WIDTH/4-(SHIP_WIDTH/2), HEIGHT/2-(SHIP_HEIGHT/2), SHIP_WIDTH, SHIP_HEIGHT)


WHITE = (255, 255, 255)
RED = (255, 0, 0)

WINDOW.fill(WHITE)
pygame.display.update()

def handle_red_input(keys_pressed):
    if keys_pressed[pygame.K_UP]:
        RED_SHIP.y -= RED_VEL
    if keys_pressed[pygame.K_DOWN]:
        RED_SHIP.y += RED_VEL

    if keys_pressed[pygame.K_LEFT]:
        RED_SHIP.x -= RED_VEL
    if keys_pressed[pygame.K_RIGHT]:
        RED_SHIP.x += RED_VEL

def handle_yellow_input(keys_pressed):
    if keys_pressed[pygame.K_w]:
        YELLOW_SHIP.y -= YELLOW_VEL
    if keys_pressed[pygame.K_s]:
        YELLOW_SHIP.y += YELLOW_VEL

    if keys_pressed[pygame.K_a]:
        YELLOW_SHIP.x -= YELLOW_VEL
    if keys_pressed[pygame.K_d]:
        YELLOW_SHIP.x += YELLOW_VEL

def draw():
    WINDOW.fill(WHITE)
    WINDOW.blit(RED_SHIP_SPRITE, RED_SHIP)
    WINDOW.blit(YELLOW_SHIP_SPRITE, YELLOW_SHIP)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        handle_red_input(keys_pressed)
        handle_yellow_input(keys_pressed)
        draw()

if __name__ == "__main__":
    main()