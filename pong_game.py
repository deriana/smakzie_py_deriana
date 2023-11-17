import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Konstanta
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_SPEED = 5
PADDLE_SPEED = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Inisialisasi layar permainan
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Fungsi untuk menggambar paddle
def draw_paddle(paddle):
    pygame.draw.rect(screen, WHITE, paddle)

# Fungsi untuk menggambar bola
def draw_ball(ball):
    pygame.draw.ellipse(screen, WHITE, ball)

# Fungsi untuk menggerakkan paddle
def move_paddle(paddle, direction):
    paddle.move_ip(0, direction * PADDLE_SPEED)
    if paddle.top < 0:
        paddle.top = 0
    if paddle.bottom > SCREEN_HEIGHT:
        paddle.bottom = SCREEN_HEIGHT

# Fungsi untuk menggerakkan bola
def move_ball(ball, ball_speed):
    ball.move_ip(ball_speed[0], ball_speed[1])
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed[1] = -ball_speed[1]

# Fungsi untuk mengatur ulang posisi bola
def reset_ball(ball):
    ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Fungsi untuk menggambar menu
def draw_menu():
    screen.fill(BLACK)
    start_singleplayer_text = font.render("Main Sendiri (tekan 1)", True, WHITE)
    start_multiplayer_text = font.render("Main Berdua (tekan 2)", True, WHITE)
    exit_text = font.render("Keluar (tekan Q)", True, WHITE)
    high_score_text = font.render("Poin Tertinggi: " + str(high_score), True, WHITE)
    screen.blit(start_singleplayer_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 60))
    screen.blit(start_multiplayer_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20))
    screen.blit(exit_text, (SCREEN_WIDTH // 2 - 60, SCREEN_HEIGHT // 2 + 20))
    screen.blit(high_score_text, (10, 10))

# Inisialisasi paddle pemain 1 dan pemain 2
player1_paddle = pygame.Rect(50, (SCREEN_HEIGHT // 2) - 50, 10, 100)
player2_paddle = pygame.Rect(SCREEN_WIDTH - 60, (SCREEN_HEIGHT // 2) - 50, 10, 100)

# Inisialisasi bola
ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 10, 10)
ball_speed = [random.choice((1, -1)) * BALL_SPEED, random.choice((1, -1)) * BALL_SPEED]

# Variabel permainan
player1_score = 0
player2_score = 0
font = pygame.font.Font(None, 36)

# Poin tertinggi (high score)
high_score = 0

# Status permainan
in_menu = True
in_game = False
single_player_mode = False

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if in_menu:
                if event.key == pygame.K_1:
                    in_menu = False
                    in_game = True
                    single_player_mode = True
                elif event.key == pygame.K_2:
                    in_menu = False
                    in_game = True
                    single_player_mode = False
                elif event.key == pygame.K_q:
                    running = False
            elif in_game:
                if event.key == pygame.K_q:
                    in_menu = True
                    in_game = False

    if in_game:
        keys = pygame.key.get_pressed()
        if single_player_mode:
            # Kontrol pemain 1
            if keys[pygame.K_w]:
                move_paddle(player1_paddle, -1)
            if keys[pygame.K_s]:
                move_paddle(player1_paddle, 1)
            
            # Kontrol pemain 2 (komputer)
            if ball_speed[0] > 0:
                if ball.centery < player2_paddle.centery:
                    move_paddle(player2_paddle, -1)
                elif ball.centery > player2_paddle.centery:
                    move_paddle(player2_paddle, 1)
        else:
            # Kontrol pemain 1
            if keys[pygame.K_w]:
                move_paddle(player1_paddle, -1)
            if keys[pygame.K_s]:
                move_paddle(player1_paddle, 1)
            
            # Kontrol pemain 2 (Player 2)
            if keys[pygame.K_UP]:
                move_paddle(player2_paddle, -1)
            if keys[pygame.K_DOWN]:
                move_paddle(player2_paddle, 1)

        move_ball(ball, ball_speed)

        # Cek tabrakan dengan paddle pemain 1
        if ball.colliderect(player1_paddle) and ball_speed[0] < 0:
            ball_speed[0] = -ball_speed[0]

        # Cek tabrakan dengan paddle pemain 2
        if ball.colliderect(player2_paddle) and ball_speed[0] > 0:
            ball_speed[0] = -ball_speed[0]

        # Cek jika bola keluar dari layar
        if ball.left < 0:
            player2_score += 1
            reset_ball(ball)
            ball_speed = [BALL_SPEED, random.choice((1, -1)) * BALL_SPEED]
        if ball.right > SCREEN_WIDTH:
            player1_score += 1
            if player1_score > high_score:
                high_score = player1_score
            reset_ball(ball)
            ball_speed = [-BALL_SPEED, random.choice((1, -1)) * BALL_SPEED] 

    if in_menu:
        draw_menu()
    elif in_game:
        # Menggambar layar
        screen.fill(BLACK)
        draw_paddle(player1_paddle)
        draw_paddle(player2_paddle)
        draw_ball(ball)

        # Menampilkan skor
        player1_text = font.render(str(player1_score), True, WHITE)
        player2_text = font.render(str(player2_score), True, WHITE)
        screen.blit(player1_text, (SCREEN_WIDTH // 4, 20))
        screen.blit(player2_text, (3 * SCREEN_WIDTH // 4 - 30, 20))

    pygame.display.update()
    clock.tick(60)  # Kecepatan permainan

pygame.quit()
