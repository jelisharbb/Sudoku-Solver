import numpy as np

print("\n==================== SUDOKU SOLVER ====================")
print("Can't find the solution to your sudoku puzzle? Fret not, because we've got you! This program will find it for you.")

while True:
    readiness = input("\nDo you want to proceed? ")
    if readiness.lower() == "yes":
        break

puzzle = [[0, 0, 0, 2, 6, 0, 7, 0, 1], [6, 8, 0, 0, 7, 0, 0, 9, 0], [1, 9, 0, 0, 0, 4, 5, 0, 0], [8, 2, 0, 1, 0, 0, 0, 4, 7], [0, 0, 4, 6, 0, 2, 9, 0, 0], [0, 5, 0, 0, 0, 3, 0, 2, 8], [0, 0, 9, 3, 0, 0, 0, 7, 4], [0, 4, 0, 0, 5, 0, 0, 3, 6], [7, 0, 3, 0, 1, 8, 0, 0, 0]]

print(np.matrix(puzzle))

def possible(row, column, answer):
    global puzzle

    for i in range(0, 9):
        if puzzle [row][i] == answer:
            return False

    for i in range(0, 9):
        if puzzle [i][column] == answer:
            return False

    subBoxRow = (row//3)*3
    subBoxCol = (column//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if puzzle[subBoxRow + 1][subBoxCol + j] == answer:
                return False

    return True

def solve():
    global puzzle
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == 0:
                for answer in range(1, 10):
                    if possible(row, column, answer):
                        puzzle[row][column] = answer
                        solve()
                        puzzle[row][column] = 0
                return
    
    print(np.matrix(puzzle))

solve()