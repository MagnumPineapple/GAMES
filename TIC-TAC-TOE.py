import pygame

# Inicializar pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definir dimensiones de la ventana
WIDTH = 720
HEIGHT = 720

# Crear la ventana del juego
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Definir el tamaño y la posición de las celdas del tablero
CELL_SIZE = WIDTH // 3
cell_positions = [(x, y) for y in range(0, HEIGHT - 50, CELL_SIZE) for x in range(0, WIDTH, CELL_SIZE)]

# Definir los jugadores
players = ['X', 'O']
current_player = 0

# Crear el tablero del juego
board = [['', '', ''], ['', '', ''], ['', '', '']]

# Crear el scoreboard
scoreboard = {'X': 0, 'O': 0}

# Cargar la fuente de texto
font = pygame.font.Font(None, 30)

# Función para dibujar el tablero y el scoreboard
def draw_board():
    window.fill(WHITE)

    for x, y in cell_positions:
        pygame.draw.rect(window, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)

    for row in range(3):
        for col in range(3):
            cell_value = board[row][col]
            if cell_value != '':
                text = font.render(cell_value, True, BLACK)
                text_rect = text.get_rect(center=(col*CELL_SIZE+CELL_SIZE//2, row*CELL_SIZE+CELL_SIZE//2))
                window.blit(text, text_rect)

    score_text = font.render(f"Victorias:", True, BLACK)
    window.blit(score_text, (10, HEIGHT - 80))

    for i, player in enumerate(players, start=1):
        score_value = scoreboard[player]
        score_label = font.render(f"Jugador {i} ({player}) : {score_value}  |  ", True, BLACK)
        window.blit(score_label, (10 + (i-1) * 200, HEIGHT - 50))

    pygame.display.flip()

# Función para realizar un movimiento
def make_move(row, col):
    if board[row][col] == '':
        board[row][col] = players[current_player]
        draw_board()

        if check_win():
            winner = players[current_player]
            scoreboard[winner] += 1
            win_message = f"¡Jugador {current_player+1} ({winner}) ha ganado!"
            print(win_message)
            message_text = font.render(win_message, True, BLACK)
            window.blit(message_text, (WIDTH // 2 - message_text.get_width() // 2, HEIGHT - 80))
            pygame.display.flip()
            pygame.time.wait(2000)
            reset_board()
        elif check_draw():
            draw_message = "¡Empate!"
            print(draw_message)
            message_text = font.render(draw_message, True, BLACK)
            window.blit(message_text, (WIDTH // 2 - message_text.get_width() // 2, HEIGHT - 80))
            pygame.display.flip()
            pygame.time.wait(2000)
            reset_board()
        else:
            switch_players()

# Función para cambiar de jugador
def switch_players():
    global current_player
    current_player = (current_player + 1) % 2

# Función para verificar si hay un ganador
def check_win():
    # Verificar filas
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return True

    # Verificar columnas
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return True

    # Verificar diagonales
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True

    return False

# Función para verificar si hay un empate
def check_draw():
    return all(cell != '' for row in board for cell in row)

# Función para reiniciar el juego
def reset_board():
    global board
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    draw_board()

# Bucle principal del juego
running = True
draw_board()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            col = mouse_pos[0] // CELL_SIZE
            row = mouse_pos[1] // CELL_SIZE
            make_move(row, col)

pygame.quit()
