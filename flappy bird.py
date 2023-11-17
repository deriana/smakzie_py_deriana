import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
GRAVITY = 0.25
FLAP_STRENGTH = 5
PIPE_WIDTH = 80
PIPE_GAP = 200
PIPE_HEIGHT = HEIGHT - PIPE_GAP

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images
background_image = pygame.image.load('background.png')  # Load background image
bird_image = pygame.image.load('bird.png')
pipe_image = pygame.image.load('pipe.png')

# Scale the images
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Scale background to match screen size
bird_image = pygame.transform.scale(bird_image, (50, 50))
pipe_image = pygame.transform.scale(pipe_image, (PIPE_WIDTH, HEIGHT))

# Bird attributes
bird_x = 100
bird_y = HEIGHT // 2
bird_vel = 0

# Pipe attributes
pipes = []
pipe_timer = 100

# Score
score = 0
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_vel = -FLAP_STRENGTH

    # Bird physics
    bird_y += bird_vel
    bird_vel += GRAVITY

    # Pipe generation
    pipe_timer -= 1
    if pipe_timer == 0:
        pipe_x = WIDTH
        pipe_gap_y = random.randint(100, HEIGHT - PIPE_GAP - 100)  # Determine gap height
        pipe_height_top = pipe_gap_y  # Height of the top pipe
        pipe_height_bottom = HEIGHT - (pipe_gap_y + PIPE_GAP)  # Height of the bottom pipe
        pipes.append([pipe_x, pipe_height_top, pipe_height_bottom])
        pipe_timer = 100

    # Move pipes
    for pipe in pipes:
        pipe[0] -= 2

    # Remove off-screen pipes
    if pipes and pipes[0][0] < -PIPE_WIDTH:
        pipes.pop(0)

    # Collision detection
    for pipe in pipes:
        if bird_x + 30 > pipe[0] and bird_x < pipe[0] + PIPE_WIDTH:
            if bird_y < pipe[1] or bird_y + 30 > pipe[2]:
                running = False

    # Increase score
    if pipes and bird_x > pipes[0][0] + PIPE_WIDTH:
        score += 1
        pipes.pop(0)

    # Draw everything
    screen.blit(background_image, (0, 0))  # Display background
    for pipe in pipes:
        screen.blit(pipe_image, (pipe[0], pipe[1] - PIPE_HEIGHT))
        screen.blit(pipe_image, (pipe[0], pipe[2] + PIPE_GAP))
    screen.blit(bird_image, (bird_x, bird_y))
    score_text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (10, 10))
    pygame.display.update()

# Game over screen
game_over_font = pygame.font.Font(None, 72)
game_over_text = game_over_font.render("SKILL ISSUEE !!", True, BLUE)
game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(game_over_text, game_over_rect)
pygame.display.update()

# Wait for a key press to exit
waiting_for_key = True
while waiting_for_key:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting_for_key = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                waiting_for_key = False
            if event.key == pygame.K_SPACE:
                waiting_for_key = False
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
