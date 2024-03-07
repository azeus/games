import random

def generate_sudoku_puzzle(size):
  """Generates a sudoku puzzle of the given size."""
  puzzle = [[0 for _ in range(size)] for _ in range(size)]
  for i in range(size):
    for j in range(size):
      puzzle[i][j] = random.randint(1, size)
  return puzzle

print(generate_sudoku_puzzle(9))