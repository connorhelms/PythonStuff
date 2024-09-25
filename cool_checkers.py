import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cool Checkers")

# Define cool colors
DARK_PURPLE = (75, 0, 130)
LIGHT_BLUE = (173, 216, 230)
NEON_RED = (255, 20, 147)
NEON_GREEN = (57, 255, 20)
YELLOW = (255, 255, 0)

# Board setup
board_size = 8
square_size = width // board_size

# Piece setup
piece_radius = square_size // 2 - 10

# Initialize the board
board = [[0 for _ in range(board_size)] for _ in range(board_size)]

def init_board():
    for row in range(board_size):
        for col in range(board_size):
            if (row + col) % 2 == 1:
                if row < 3:
                    board[row][col] = 1  # Player 1 pieces
                elif row > 4:
                    board[row][col] = 2  # Player 2 pieces

def draw_board():
    for row in range(board_size):
        for col in range(board_size):
            color = LIGHT_BLUE if (row + col) % 2 == 0 else DARK_PURPLE
            pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))

def draw_pieces():
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] != 0:
                color = NEON_RED if board[row][col] in [1, 3] else NEON_GREEN
                center = (col * square_size + square_size // 2, row * square_size + square_size // 2)
                pygame.draw.circle(screen, color, center, piece_radius)
                if board[row][col] in [3, 4]:  # King pieces
                    pygame.draw.circle(screen, YELLOW, center, piece_radius // 2)

def get_square_under_mouse(pos):
    x, y = pos
    row = y // square_size
    col = x // square_size
    return (row, col) if 0 <= row < board_size and 0 <= col < board_size else None

def is_valid_move(board, start, end, player):
    start_row, start_col = start
    end_row, end_col = end
    
    # Check if the move is diagonal
    if abs(end_row - start_row) != abs(end_col - start_col):
        return False
    
    # Check if the move is forward (unless it's a king)
    if board[start_row][start_col] != player + 2:  # Not a king
        if player == 1 and end_row <= start_row:
            return False
        if player == 2 and end_row >= start_row:
            return False
    
    # Check if it's a valid single move or jump
    if abs(end_row - start_row) == 1:
        return board[end_row][end_col] == 0
    elif abs(end_row - start_row) == 2:
        jump_row = (start_row + end_row) // 2
        jump_col = (start_col + end_col) // 2
        return board[end_row][end_col] == 0 and board[jump_row][jump_col] in [3 - player, 5 - player]
    
    return False

def make_move(board, start, end, player):
    start_row, start_col = start
    end_row, end_col = end
    
    # Move the piece
    board[end_row][end_col] = board[start_row][start_col]
    board[start_row][start_col] = 0
    
    # Check if it was a jump and remove the jumped piece
    if abs(end_row - start_row) == 2:
        jump_row = (start_row + end_row) // 2
        jump_col = (start_col + end_col) // 2
        board[jump_row][jump_col] = 0
    
    # Check for king promotion
    if (player == 1 and end_row == board_size - 1) or (player == 2 and end_row == 0):
        board[end_row][end_col] = player + 2

    return abs(end_row - start_row) == 2  # Return True if it was a jump

def get_valid_jumps(board, row, col, player):
    valid_jumps = []
    directions = [(2, 2), (2, -2), (-2, 2), (-2, -2)]
    
    for d_row, d_col in directions:
        new_row, new_col = row + d_row, col + d_col
        if 0 <= new_row < board_size and 0 <= new_col < board_size:
            if is_valid_move(board, (row, col), (new_row, new_col), player):
                valid_jumps.append((new_row, new_col))
    
    return valid_jumps

def main():
    init_board()
    selected = None
    player_turn = 1
    jumping = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                square = get_square_under_mouse(pos)
                if square:
                    row, col = square
                    if selected is None:
                        if board[row][col] in [player_turn, player_turn + 2]:
                            selected = (row, col)
                    else:
                        if (row, col) != selected:
                            if is_valid_move(board, selected, (row, col), player_turn):
                                jumped = make_move(board, selected, (row, col), player_turn)
                                if jumped:
                                    valid_jumps = get_valid_jumps(board, row, col, player_turn)
                                    if valid_jumps:
                                        selected = (row, col)
                                        jumping = True
                                    else:
                                        player_turn = 3 - player_turn
                                        jumping = False
                                else:
                                    player_turn = 3 - player_turn
                                    jumping = False
                            if not jumping:
                                selected = None
                        else:
                            selected = None

        screen.fill((0, 0, 0))
        draw_board()
        draw_pieces()

        if selected:
            row, col = selected
            pygame.draw.rect(screen, YELLOW, (col * square_size, row * square_size, square_size, square_size), 4)

        pygame.display.flip()

if __name__ == "__main__":
    main()