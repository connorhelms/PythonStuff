import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Skeleton Walking with Celestial Events")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Skeleton properties
skeleton_width = 60
skeleton_height = 100
skeleton_x = 0
skeleton_y = height - skeleton_height - 50  # 50 pixels above the bottom

# Street properties
street_height = 100

# Animation properties
walk_cycle = [0, 1, 2, 1]  # Indices for walking animation
current_frame = 0
animation_speed = 5  # Frames per animation change

# Shooting star properties
shooting_stars = []
shooting_star_chance = 0.02  # 2% chance per frame

# Meteor properties
meteor_x = width
meteor_y = 0
meteor_speed = 2
meteor_size = 40

# Main game loop
clock = pygame.time.Clock()
frame_count = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw shooting stars
    if random.random() < shooting_star_chance:
        shooting_stars.append([random.randint(0, width), random.randint(0, height // 2), random.randint(5, 15)])

    for star in shooting_stars:
        pygame.draw.line(screen, WHITE, (star[0], star[1]), (star[0] + star[2], star[1] + star[2]), 2)
        star[0] -= 5
        star[1] += 5
        if star[0] < 0 or star[1] > height:
            shooting_stars.remove(star)

    # Draw and move meteor
    pygame.draw.circle(screen, ORANGE, (int(meteor_x), int(meteor_y)), meteor_size)
    meteor_x -= meteor_speed
    meteor_y += meteor_speed // 2
    if meteor_x < -meteor_size or meteor_y > height:
        meteor_x = width + meteor_size
        meteor_y = random.randint(-meteor_size, height // 3)

    # Draw the street
    pygame.draw.rect(screen, GRAY, (0, height - street_height, width, street_height))

    # Draw the skeleton
    current_pose = walk_cycle[current_frame]
    
    # Skeleton body
    # Spine
    pygame.draw.line(screen, WHITE, (skeleton_x + skeleton_width // 2, skeleton_y), 
                     (skeleton_x + skeleton_width // 2, skeleton_y + skeleton_height), 3)
    
    # Ribs
    for i in range(4):
        y = skeleton_y + 20 + i * 20
        pygame.draw.line(screen, WHITE, (skeleton_x + skeleton_width // 2 - 20, y), 
                         (skeleton_x + skeleton_width // 2 + 20, y), 2)
    
    # Shoulders
    pygame.draw.line(screen, WHITE, (skeleton_x + 10, skeleton_y + 20), 
                     (skeleton_x + skeleton_width - 10, skeleton_y + 20), 3)
    
    # Arms
    pygame.draw.line(screen, WHITE, (skeleton_x + 10, skeleton_y + 20), 
                     (skeleton_x + 5, skeleton_y + skeleton_height - 20), 2)
    pygame.draw.line(screen, WHITE, (skeleton_x + skeleton_width - 10, skeleton_y + 20), 
                     (skeleton_x + skeleton_width - 5, skeleton_y + skeleton_height - 20), 2)
    
    # Pelvis
    pygame.draw.line(screen, WHITE, (skeleton_x + 15, skeleton_y + skeleton_height - 10), 
                     (skeleton_x + skeleton_width - 15, skeleton_y + skeleton_height - 10), 3)

    # Head
    pygame.draw.circle(screen, WHITE, (skeleton_x + skeleton_width // 2, skeleton_y - 20), 20)
    
    # Eyes
    pygame.draw.circle(screen, BLACK, (skeleton_x + skeleton_width // 2 - 7, skeleton_y - 25), 5)
    pygame.draw.circle(screen, BLACK, (skeleton_x + skeleton_width // 2 + 7, skeleton_y - 25), 5)
    
    # Legs
    if current_pose == 0:
        pygame.draw.line(screen, WHITE, (skeleton_x + 15, skeleton_y + skeleton_height), 
                         (skeleton_x + 15, skeleton_y + skeleton_height + 40), 3)
        pygame.draw.line(screen, WHITE, (skeleton_x + skeleton_width - 15, skeleton_y + skeleton_height), 
                         (skeleton_x + skeleton_width - 15, skeleton_y + skeleton_height + 40), 3)
    elif current_pose == 1:
        pygame.draw.line(screen, WHITE, (skeleton_x + 15, skeleton_y + skeleton_height), 
                         (skeleton_x + 30, skeleton_y + skeleton_height + 40), 3)
        pygame.draw.line(screen, WHITE, (skeleton_x + skeleton_width - 15, skeleton_y + skeleton_height), 
                         (skeleton_x + skeleton_width - 30, skeleton_y + skeleton_height + 40), 3)
    elif current_pose == 2:
        pygame.draw.line(screen, WHITE, (skeleton_x + 15, skeleton_y + skeleton_height), 
                         (skeleton_x, skeleton_y + skeleton_height + 40), 3)
        pygame.draw.line(screen, WHITE, (skeleton_x + skeleton_width - 15, skeleton_y + skeleton_height), 
                         (skeleton_x + skeleton_width, skeleton_y + skeleton_height + 40), 3)

    # Move the skeleton
    skeleton_x += 2
    if skeleton_x > width:
        skeleton_x = -skeleton_width

    # Update animation frame
    frame_count += 1
    if frame_count % animation_speed == 0:
        current_frame = (current_frame + 1) % len(walk_cycle)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
sys.exit()