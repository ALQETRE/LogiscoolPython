import pygame
import random

pygame.init()

WIDTH = 15
HEIGHT = 10

BLOCK_SIZE = 50
SNAKE_SPEED = 7

window = pygame.display.set_mode((WIDTH * BLOCK_SIZE, HEIGHT * BLOCK_SIZE))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

background_color = (173, 198, 237)
snake_color = (22, 128, 25)
apple_color = (247, 72, 72)
score_color = (0, 0, 0)
game_over_color = (112, 0, 77)

score_font = pygame.font.SysFont("Arial", 30)
game_over_font = pygame.font.SysFont("Arial", 40)


def update_frame(snake, snake_len, apple_pos):
    global snake_color
    window.fill(background_color)

    for x, y in snake:
        snake_color = ((snake_color[0] + 2) % 256,(snake_color[1] + 3) % 256, (snake_color[2] + 5) % 256)
        pygame.draw.rect(window, snake_color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


    pygame.draw.rect(window, apple_color, (apple_pos[0] * BLOCK_SIZE, apple_pos[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    score_text = score_font.render(f"Score: {snake_len}", True, score_color)
    window.blit(score_text, (15, 12))

    pygame.display.update()

def move(snake, snake_len, head):
    snake.append(head)
    if len(snake) > snake_len:
        snake.pop(0)

    return snake

def generate_apple():
    apple_x = random.randrange(0, WIDTH)
    apple_y = random.randrange(0, HEIGHT)

    return (apple_x, apple_y)


def game():
    global snake_color


    snake_len = 3
    snake = [ (WIDTH//2, HEIGHT//2) ]

    x = WIDTH // 2
    y = HEIGHT // 2

    dir_x = 0
    dir_y = 0

    apple_pos = generate_apple()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dir_x = -1
                    dir_y = 0
                elif event.key == pygame.K_RIGHT:
                    dir_x = 1
                    dir_y = 0
                elif event.key == pygame.K_UP:
                    dir_x = 0
                    dir_y = -1
                elif event.key == pygame.K_DOWN:
                    dir_x = 0
                    dir_y = 1

        x += dir_x
        y += dir_y

        if x < 0 or x > WIDTH:
            run = False
            continue
        if y < 0 or y > HEIGHT:
            run = False
            continue

        next_move = (x, y)
        snake = move(snake, snake_len, next_move)

        if dir_x != 0 or dir_y != 0:
            for block in snake[:-1]:
                if block == next_move:
                    run = False
                    continue

        for block in snake:
            if block == apple_pos:
                snake_len += 1
                apple_pos = generate_apple()



        update_frame(snake, snake_len, apple_pos)
        clock.tick(SNAKE_SPEED)

    game_over_text = game_over_font.render("Game Over", True, game_over_color)
    window.blit(game_over_text, ((WIDTH*BLOCK_SIZE - game_over_text.get_size()[0])//2, (HEIGHT*BLOCK_SIZE - game_over_text.get_size()[1])//2))
    pygame.display.update()

    while True:
        pass

game()