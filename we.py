import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Konstanta
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
LINE_COLOR = (0, 0, 0)
LINE_WIDTH = 15
BOARD_SIZE = 3
SQUARE_SIZE = SCREEN_WIDTH // BOARD_SIZE
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 15
CIRCLE_COLOR = (0, 0, 255)
CROSS_COLOR = (255, 0, 0)

# Warna latar
BACKGROUND_COLOR = (255, 255, 255)

# Inisialisasi layar
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Grid untuk papan permainan
board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Fungsi untuk menggambar garis horizontal dan vertikal
def draw_lines():
    for row in range(1, BOARD_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (SCREEN_WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (row * SQUARE_SIZE, 0), (row * SQUARE_SIZE, SCREEN_HEIGHT), LINE_WIDTH)

# Fungsi untuk menggambar simbol (X atau O)
def draw_symbols():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE, row * SQUARE_SIZE), ((col + 1) * SQUARE_SIZE, (row + 1) * SQUARE_SIZE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, ((col + 1) * SQUARE_SIZE, row * SQUARE_SIZE), (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE), CROSS_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), CIRCLE_RADIUS, CIRCLE_WIDTH)
# Fungsi untuk menampilkan pesan peringatan saat ada pemenang atau seri
def show_message(message):
    font = pygame.font.Font(None, 36)
    text = font.render(message, True, (0, 0, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(1500)# Fungsi untuk memeriksa pemenang
def check_winner(player):
    # Cek baris
    for row in range(BOARD_SIZE):
        if all(board[row][col] == player for col in range(BOARD_SIZE)):
            return True

    # Cek kolom
    for col in range(BOARD_SIZE):
        if all(board[row][col] == player for row in range(BOARD_SIZE)):
            return True

    # Cek diagonal
    if all(board[i][i] == player for i in range(BOARD_SIZE)) or all(board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)):
        return True

    return False

# Fungsi untuk mengisi papan
def place_marker(row, col, player):
    if board[row][col] == '':
        board[row][col] = player
        return True
    return False

# Fungsi untuk mereset papan
def reset_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            board[row][col] = ''

# Fungsi utama
def main():
    player_turn = 'X'
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col = x // SQUARE_SIZE
                row = y // SQUARE_SIZE

                if place_marker(row, col, player_turn):
                    if check_winner(player_turn):
                        game_over = True
                        show_message(f'Player {player_turn} wins!')
                    elif all(board[i][j] != '' for i in range(BOARD_SIZE) for j in range(BOARD_SIZE)):
                        game_over = True
                        show_message("It's a draw!")
                    player_turn = 'O' if player_turn == 'X' else 'X'

            if game_over:
                show_message("Press 'R' to restart or 'Q' to quit.")
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        reset_board()
                        game_over = False
                        player_turn = 'X'
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

        screen.fill(BACKGROUND_COLOR)
        draw_lines()
        draw_symbols()

        pygame.display.update()

if __name__ == '__main__':
    main()