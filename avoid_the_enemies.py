import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Warna
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Ukuran layar
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Inisialisasi layar
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Koordinat awal burung
bird_x = SCREEN_WIDTH // 4
bird_y = SCREEN_HEIGHT // 2

# Ukuran burung
bird_radius = 15

# Kecepatan jatuh burung
bird_speed = 0

# Gravitasi
gravity = 0.5

# Kecepatan lompat burung
jump_strength = 10

# Rintangan
obstacle_width = 50
obstacle_height = random.randint(150, 400)
obstacle_x = SCREEN_WIDTH
obstacle_y = random.randint(200, 400)
obstacle_speed = 5

# Skor
score = 0

# Font
font = pygame.font.Font(None, 36)

# Loop permainan
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = -jump_strength

    # Menggerakkan burung
    bird_speed += gravity
    bird_y += bird_speed

    # Menggerakkan rintangan
    obstacle_x -= obstacle_speed

    # Memeriksa tabrakan dengan rintangan
    if obstacle_x < 0:
        obstacle_x = SCREEN_WIDTH
        obstacle_height = random.randint(150, 400)
        obstacle_y = random.randint(200, 400)
        score += 1

    if bird_x + bird_radius > obstacle_x and bird_x - bird_radius < obstacle_x + obstacle_width:
        if bird_y - bird_radius < obstacle_y or bird_y + bird_radius > obstacle_y + obstacle_height:
            running = False

    # Memeriksa jika burung menyentuh atas atau bawah layar
    if bird_y + bird_radius > SCREEN_HEIGHT or bird_y - bird_radius < 0:
        running = False

    # Menggambar objek di layar
    screen.fill(WHITE)
    pygame.draw.circle(screen, GREEN, (bird_x, int(bird_y)), bird_radius)
    pygame.draw.rect(screen, GREEN, (obstacle_x, 0, obstacle_width, obstacle_y))
    pygame.draw.rect(screen, GREEN, (obstacle_x, obstacle_y + obstacle_height, obstacle_width, SCREEN_HEIGHT - obstacle_y - obstacle_height))

    # Menggambar skor
    text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(text, (10, 10))
    
    pygame.display.update()

# Menutup Pygame
pygame.quit()
