import random
import string

def generate_word_search(words, size):
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    directions = [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]

    for word in words:
        word_placed = False
        while not word_placed:
            direction = random.choice(directions)
            row_start = random.randint(0, size - 1)
            col_start = random.randint(0, size - 1)
            row, col = row_start, col_start
            word_fits = True

            for letter in word:
                if not (0 <= row < size and 0 <= col < size) or (grid[row][col] not in (' ', letter)):
                    word_fits = False
                    break
                row += direction[0]
                col += direction[1]

            if word_fits:
                row, col = row_start, col_start
                for letter in word:
                    grid[row][col] = letter
                    row += direction[0]
                    col += direction[1]
                word_placed = True

    for i in range(size):
        for j in range(size):
            if grid[i][j] == ' ':
                grid[i][j] = random.choice(string.ascii_uppercase)
    return grid

def display_word_search(grid):
    for row in grid:
        print(' '.join(row))

words = ["PYTHON", "WORD", "SEARCH", "PUZZLE", "GRID"]
size = 10
grid = generate_word_search(words, size)
display_word_search(grid)