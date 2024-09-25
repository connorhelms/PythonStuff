import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake properties
snake_block = 20
snake_speed = 15

# Initialize clock
clock = pygame.time.Clock()

# Font for score display
font = pygame.font.SysFont(None, 50)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, GREEN, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font.render(msg, True, color)
    display.blit(mesg, [width / 6, height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    while not game_over:

        while game_close == True:
            display.fill(BLACK)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill(BLACK)
        pygame.draw.rect(display, RED, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
def draw_pacman_snake(surface, snake_block, snake_list):
    for i, segment in enumerate(snake_list):
        x, y = segment
        if i == len(snake_list) - 1:  # Head of the snake
            # Draw Pac-Man-like head
            angle = 45  # Mouth opening angle
            pygame.draw.circle(surface, YELLOW, (int(x + snake_block / 2), int(y + snake_block / 2)), int(snake_block / 2))
            pygame.draw.polygon(surface, BLACK, [
                (x + snake_block / 2, y + snake_block / 2),
                (x + snake_block, y),
                (x + snake_block, y + snake_block)
            ])
        else:
            # Draw body segments as circles
            pygame.draw.circle(surface, YELLOW, (int(x + snake_block / 2), int(y + snake_block / 2)), int(snake_block / 2))

def draw_food(surface, x, y, snake_block):
    pygame.draw.circle(surface, WHITE, (int(x + snake_block / 2), int(y + snake_block / 2)), int(snake_block / 4))

# Update color constants
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Replace the our_snake function call with the new draw_pacman_snake function
draw_pacman_snake(display, snake_block, snake_List)

# Replace the food drawing code with the new draw_food function
draw_food(display, foodx, foody, snake_block)
