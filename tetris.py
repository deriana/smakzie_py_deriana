import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Konstanta
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
BLOCK_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Membuat layar permainan
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Fungsi untuk menggambar bentuk
def draw_shape(shape, color):
    for block in shape:
        pygame.draw.rect(screen, color, [block[0] * BLOCK_SIZE, block[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE])

# Inisialisasi bentuk
shapes = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 1], [0, 1, 0], [0, 1, 0]],
    [[1, 1, 1], [0, 0, 1], [0, 0, 1]]
]

# Variabel permainan
current_shape = random.choice(shapes)
shape_x = SCREEN_WIDTH // BLOCK_SIZE // 2 - 1
shape_y = 0
score = 0

# Fungsi untuk memeriksa apakah bentuk dapat bergerak
def can_move(shape, x, y):
    for block in shape:
        block_x = x + block[0]
        block_y = y + block[1]
        if block_x < 0 or block_x >= SCREEN_WIDTH // BLOCK_SIZE or block_y >= SCREEN_HEIGHT // BLOCK_SIZE:
            return False
    return True

# Fungsi untuk menghapus baris yang penuh
def remove_full_rows():
    for row in range(SCREEN_HEIGHT // BLOCK_SIZE - 1, -1, -1):
        if all(screen.get_at((col * BLOCK_SIZE, row * BLOCK_SIZE)) == WHITE for col in range(SCREEN_WIDTH // BLOCK_SIZE)):
            pygame.draw.rect(screen, BLACK, (0, row * BLOCK_SIZE, SCREEN_WIDTH, BLOCK_SIZE))
            for above_row in range(row - 1, -1, -1):
                for col in range(SCREEN_WIDTH // BLOCK_SIZE):
                    color = screen.get_at((col * BLOCK_SIZE, above_row * BLOCK_SIZE))
                    pygame.draw.rect(screen, color, (col * BLOCK_SIZE, (above_row + 1) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and can_move(current_shape, shape_x - 1, shape_y):
        shape_x -= 1
    if keys[pygame.K_RIGHT] and can_move(current_shape, shape_x + 1, shape_y):
        shape_x += 1
    if keys[pygame.K_DOWN] and can_move(current_shape, shape_x, shape_y + 1):
        shape_y += 1

    new_shape_y = shape_y
    while can_move(current_shape, shape_x, new_shape_y + 1):
        new_shape_y += 1

    if new_shape_y != shape_y:
        shape_y = new_shape_y
    else:
        if can_move(current_shape, shape_x, shape_y + 1):
            shape_y += 1
        else:
            for block in current_shape:
                block_x = shape_x + block[0]
                block_y = shape_y + block[1]
                pygame.draw.rect(screen, WHITE, [block_x * BLOCK_SIZE, block_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE])
            remove_full_rows()
            current_shape = random.choice(shapes)
            shape_x = SCREEN_WIDTH // BLOCK_SIZE // 2 - 1
            shape_y = 0

    screen.fill(BLACK)
    draw_shape(current_shape, WHITE)

    pygame.display.update()
    clock.tick(5)  # Kecepatan permainan

pygame.quit()

