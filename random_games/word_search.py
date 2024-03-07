import random
import string

def generate_word_search(words, size):
    # Create an empty grid with additional border
    grid = [[' ' for _ in range(size + 2)] for _ in range(size + 2)]
    directions = [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]

    # Fill the border and inside with random letters
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            grid[i][j] = random.choice(string.ascii_uppercase)

    # Fill the border with random letters
    for i in range(size + 2):
        grid[0][i] = random.choice(string.ascii_uppercase)
        grid[size + 1][i] = random.choice(string.ascii_uppercase)
        grid[i][0] = random.choice(string.ascii_uppercase)
        grid[i][size + 1] = random.choice(string.ascii_uppercase)

    for word in words:
        word_placed = False

        while not word_placed:
            direction = random.choice(directions)
            row_start = random.randint(1, size)
            col_start = random.randint(1, size)
            row, col = row_start, col_start
            word_fits = True

            # Check if word fits in the grid in the selected direction
            for letter in word:
                if not (0 < row <= size and 0 < col <= size) or (grid[row][col] != ' ' and grid[row][col] != letter):
                    word_fits = False
                    break

                row += direction[0]
                col += direction[1]

            # Place word in the grid if it fits
            if word_fits:
                row, col = row_start, col_start

                for letter in word:
                    grid[row][col] = letter
                    row += direction[0]
                    col += direction[1]

                word_placed = True

    return grid

def display_word_search(grid):
    for row in grid:
        print(' '.join(row))

# Example usage
words = ["PYTHON", "WORD", "SEARCH", "PUZZLE", "GENERATE"]
size = 10

grid = generate_word_search(words, size)
display_word_search(grid)
