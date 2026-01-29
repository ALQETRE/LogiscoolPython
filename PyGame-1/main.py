import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH = 900
HEIGHT = 500

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game!")

FPS = 60
RED_VEL = 3
YELLOW_VEL = 6
BULLET_VEL = 10

RED_SHIP_ASSET = "Assets\\spaceship_red.png"
YELLOW_SHIP_ASSET = "Assets\\spaceship_yellow.png"

SHIP_WIDTH = 60
SHIP_HEIGHT = 80

BULLET_WIDTH = 10
BULLET_HEIGHT = 5

MAX_BULLETS = 3

red_bullets = []
yellow_bullets = []

RED_SHIP_SPRITE = pygame.image.load(RED_SHIP_ASSET)
RED_SHIP_SPRITE = pygame.transform.rotate(RED_SHIP_SPRITE, -90)
RED_SHIP_SPRITE = pygame.transform.scale(RED_SHIP_SPRITE, (SHIP_WIDTH, SHIP_HEIGHT))

YELLOW_SHIP_SPRITE = pygame.image.load(YELLOW_SHIP_ASSET)
YELLOW_SHIP_SPRITE = pygame.transform.rotate(YELLOW_SHIP_SPRITE, 90)
YELLOW_SHIP_SPRITE = pygame.transform.scale(YELLOW_SHIP_SPRITE, (SHIP_WIDTH, SHIP_HEIGHT))

RED_SHIP = pygame.rect.Rect(WIDTH/4*3-(SHIP_WIDTH/2), HEIGHT/2-(SHIP_HEIGHT/2), SHIP_WIDTH, SHIP_HEIGHT)
YELLOW_SHIP = pygame.rect.Rect(WIDTH/4-(SHIP_WIDTH/2), HEIGHT/2-(SHIP_HEIGHT/2), SHIP_WIDTH, SHIP_HEIGHT)

red_health = 10
yellow_health = 5


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

HEALTH_FONT = pygame.font.SysFont("arial", 40)
FULLSCRENE_FONT = pygame.font.SysFont("arial", 100)

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

    RED_SHIP.x = max(RED_SHIP.x, 0)
    RED_SHIP.x = min(RED_SHIP.x, WIDTH-SHIP_WIDTH)

    RED_SHIP.y = max(RED_SHIP.y, 0)
    RED_SHIP.y = min(RED_SHIP.y, HEIGHT-SHIP_HEIGHT)

def handle_yellow_input(keys_pressed):
    if keys_pressed[pygame.K_w]:
        YELLOW_SHIP.y -= YELLOW_VEL
    if keys_pressed[pygame.K_s]:
        YELLOW_SHIP.y += YELLOW_VEL

    if keys_pressed[pygame.K_a]:
        YELLOW_SHIP.x -= YELLOW_VEL
    if keys_pressed[pygame.K_d]:
        YELLOW_SHIP.x += YELLOW_VEL

    YELLOW_SHIP.x = max(YELLOW_SHIP.x, 0)
    YELLOW_SHIP.x = min(YELLOW_SHIP.x, WIDTH-SHIP_WIDTH)

    YELLOW_SHIP.y = max(YELLOW_SHIP.y, 0)
    YELLOW_SHIP.y = min(YELLOW_SHIP.y, HEIGHT-SHIP_HEIGHT)

def handle_bullets():
    global red_health, yellow_health

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if YELLOW_SHIP.colliderect(bullet):
            yellow_health -= 1
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if RED_SHIP.colliderect(bullet):
            red_health -= 1
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

def draw():
    WINDOW.fill(WHITE)

    red_health_text = HEALTH_FONT.render(f"Red: {red_health}hp", True, BLACK)
    yellow_health_text = HEALTH_FONT.render(f"Yello: {yellow_health}hp", True, BLACK)

    WINDOW.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WINDOW.blit(yellow_health_text, (10, 10))

    for bullet in red_bullets:
        pygame.draw.rect(WINDOW, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WINDOW, YELLOW, bullet)

    WINDOW.blit(RED_SHIP_SPRITE, RED_SHIP)
    WINDOW.blit(YELLOW_SHIP_SPRITE, YELLOW_SHIP)
    pygame.display.update()

def win_condition():
    if red_health <= 0:
        text = FULLSCRENE_FONT.render("YELLOW WON!!!", True, BLACK)

        WINDOW.blit(text, ( (WIDTH//2) - (text.get_width()//2), (HEIGHT//2) - (text.get_height()//2) ))
        pygame.display.update()
        pygame.time.delay(3000)
        return False
    
    elif yellow_health <= 0:
        text = FULLSCRENE_FONT.render("RED WON!!!", True, BLACK)

        WINDOW.blit(text, ( (WIDTH//2) - (text.get_width()//2), (HEIGHT//2) - (text.get_height()//2) ))
        pygame.display.update()
        pygame.time.delay(3000)
        return False
    
    return True

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RSHIFT:
                    if len(red_bullets) < MAX_BULLETS:
                        bullet = pygame.Rect(RED_SHIP.x, RED_SHIP.y+(RED_SHIP.height//2), BULLET_WIDTH, BULLET_HEIGHT)
                        red_bullets.append(bullet)

                if event.key == pygame.K_LSHIFT:
                    if len(yellow_bullets) < MAX_BULLETS:
                        bullet = pygame.Rect(YELLOW_SHIP.x + YELLOW_SHIP.width, YELLOW_SHIP.y+(YELLOW_SHIP.height//2), BULLET_WIDTH, BULLET_HEIGHT)
                        yellow_bullets.append(bullet)
        
        keys_pressed = pygame.key.get_pressed()
        handle_red_input(keys_pressed)
        handle_yellow_input(keys_pressed)
        handle_bullets()
        draw()
        run = win_condition()

if __name__ == "__main__":
    main()