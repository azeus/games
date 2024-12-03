import random

def generate_sudoku_puzzle(size):
    """Generates a valid Sudoku puzzle with some cells blank for the given size."""
    def is_valid(board, row, col, num):
        # Check if the number can be placed in the given cell
        for i in range(size):
            if board[row][i] == num or board[i][col] == num:
                return False
        subgrid_size = int(size ** 0.5)
        start_row, start_col = row - row % subgrid_size, col - col % subgrid_size
        for i in range(subgrid_size):
            for j in range(subgrid_size):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve(board):
        for row in range(size):
            for col in range(size):
                if board[row][col] == 0:
                    for num in range(1, size + 1):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    board = [[0] * size for _ in range(size)]
    for _ in range(size):
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        num = random.randint(1, size)
        if is_valid(board, row, col, num):
            board[row][col] = num
    solve(board)
    # Remove some cells for the puzzle
    for _ in range(size * size // 2):
        board[random.randint(0, size - 1)][random.randint(0, size - 1)] = 0
    return board

def print_sudoku(board):
    for row in board:
        print(' '.join(str(num) if num != 0 else '.' for num in row))

print("Generated Sudoku:")
print_sudoku(generate_sudoku_puzzle(9))