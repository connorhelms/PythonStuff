import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Campfire")

# Colors
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (139, 69, 19)

# Fire properties
fire_width = 100
fire_height = 150
fire_x = width // 2 - fire_width // 2
fire_y = height - fire_height - 50

# Log properties
log_width = 120
log_height = 30

# Particle class
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(2, 6)
        self.color = random.choice([ORANGE, RED, YELLOW])
        self.speed = random.uniform(1, 3)

    def move(self):
        self.y -= self.speed
        self.x += random.uniform(-0.5, 0.5)
        self.size -= 0.1
        if self.size < 0:
            self.size = 0

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))

def draw_logs(x, y):
    # Draw three logs
    pygame.draw.rect(screen, BROWN, (x - 10, y + fire_height, log_width, log_height))
    pygame.draw.rect(screen, BROWN, (x + 20, y + fire_height + 15, log_width, log_height))
    pygame.draw.rect(screen, BROWN, (x - 20, y + fire_height + 30, log_width, log_height))

# Main game loop
def main():
    global fire_x, fire_y, fire_width, fire_height, width, height

    print("Starting main function")
    clock = pygame.time.Clock()
    particles = []

    running = True
    while running:
        print("Entering game loop")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # Create new particles
        for _ in range(10):
            particles.append(Particle(fire_x + random.randint(0, fire_width),
                                      fire_y + fire_height))

        # Update and draw particles
        for particle in particles[:]:
            particle.move()
            particle.draw()
            if particle.size <= 0:
                particles.remove(particle)

        # Draw logs
        draw_logs(fire_x, fire_y)

        # Draw fire base
        pygame.draw.rect(screen, RED, (fire_x, fire_y + fire_height - 20, fire_width, 20))

        # Move fire horizontally
        fire_x += random.uniform(-1, 1)
        fire_x = max(0, min(width - fire_width, fire_x))

        pygame.display.flip()
        clock.tick(60)

    print("Exiting game loop")
    pygame.quit()

print("Script is running")
if __name__ == "__main__":
    print("Calling main function")
    main()