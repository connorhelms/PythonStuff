import pygame
import pygame.freetype  # Import freetype module for better text rendering
import pygame.freetype  # Import freetype module for better text rendering
import sys
from pygame.locals import QUIT, KEYDOWN, K_y, K_n
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("RGB Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle properties
paddle_width = 15
paddle_height = 90
paddle_speed = 5

# Ball properties
ball_size = 15
ball_speed_x = 7
ball_speed_y = 7

# Create paddles
player = pygame.Rect(50, height//2 - paddle_height//2, paddle_width, paddle_height)
opponent = pygame.Rect(width - 50 - paddle_width, height//2 - paddle_height//2, paddle_width, paddle_height)

# Create ball
ball = pygame.Rect(width//2 - ball_size//2, height//2 - ball_size//2, ball_size, ball_size)

# RGB color for the ball
ball_color = [255, 0, 0]  # Start with red

# Clock for controlling the frame rate
clock = pygame.time.Clock()

def move_paddle(paddle, up=True):
    if up:
        paddle.y -= paddle_speed
    else:
        paddle.y += paddle_speed
    paddle.y = max(0, min(height - paddle_height, paddle.y))

def move_ball(ball):
    global ball_speed_x, ball_speed_y, ball_color
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Bounce off top and bottom
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1
        ball_color = [random.randint(0, 255) for _ in range(3)]

    # Bounce off paddles
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
        ball_color = [random.randint(0, 255) for _ in range(3)]

    # Reset ball if it goes out of bounds
    if ball.left <= 0 or ball.right >= width:
        ball.center = (width//2, height//2)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            move_paddle(player, up=True)
        if keys[pygame.K_s]:
            move_paddle(player, up=False)

        # Simple AI for opponent
        if opponent.centery < ball.centery:
            move_paddle(opponent, up=False)
        elif opponent.centery > ball.centery:
            move_paddle(opponent, up=True)

        move_ball(ball)

        # Drawing
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, player)
        pygame.draw.rect(screen, WHITE, opponent)
        pygame.draw.ellipse(screen, ball_color, ball)
        pygame.draw.aaline(screen, WHITE, (width//2, 0), (width//2, height))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
