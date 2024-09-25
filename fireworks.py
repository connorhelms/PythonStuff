import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("8-Bit Fireworks")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Firework particle class
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = random.randint(2, 4)
        self.speed_x = random.uniform(-1, 1)
        self.speed_y = random.uniform(-3, -1)
        self.lifetime = random.randint(30, 60)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_y += 0.05  # Gravity effect
        self.lifetime -= 1

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (int(self.x), int(self.y), self.size, self.size))

# Firework class
class Firework:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.particles = []
        self.exploded = False

    def explode(self):
        for _ in range(50):  # Number of particles
            self.particles.append(Particle(self.x, self.y, self.color))
        self.exploded = True

    def update(self):
        if not self.exploded:
            self.y -= 5  # Move upwards
            if self.y < random.randint(50, 300):
                self.explode()
        else:
            for particle in self.particles:
                particle.update()
            self.particles = [p for p in self.particles if p.lifetime > 0]

    def draw(self, surface):
        if not self.exploded:
            pygame.draw.rect(surface, self.color, (int(self.x), int(self.y), 4, 4))
        for particle in self.particles:
            particle.draw(surface)

# Main game loop
def main():
    clock = pygame.time.Clock()
    fireworks = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # Randomly create new fireworks
        if random.random() < 0.05:
            fireworks.append(Firework(random.randint(0, width), height))

        # Update and draw fireworks
        for firework in fireworks:
            firework.update()
            firework.draw(screen)

        # Remove dead fireworks
        fireworks = [f for f in fireworks if f.particles or not f.exploded]

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
