import numpy as np

print("\n==================== SUDOKU SOLVER ====================")
print("Can't find the solution to your sudoku puzzle? Fret not, because we've got you! This program will find it for you.")

while True:
    readiness = input("\nDo you want to proceed? ")
    if readiness.lower() == "yes":
        break
    elif readiness.lower() == "no":
        print("\nGood bye...")
        exit()

puzzle1 = [[0, 0, 0, 2, 6, 0, 7, 0, 1], [6, 8, 0, 0, 7, 0, 0, 9, 0], [1, 9, 0, 0, 0, 4, 5, 0, 0], [8, 2, 0, 1, 0, 0, 0, 4, 7], [0, 0, 4, 6, 0, 2, 9, 0, 0], [0, 5, 0, 0, 0, 3, 0, 2, 8], [0, 0, 9, 3, 0, 0, 0, 7, 4], [0, 4, 0, 0, 5, 0, 0, 3, 6], [7, 0, 3, 0, 1, 8, 0, 0, 0]]

puzzle2 = [[2, 0, 0, 3, 0, 0, 0, 0, 0], [8, 0, 4, 0, 6, 2, 0, 0, 3], [0, 1, 3, 8, 0, 0, 2, 0, 0], [0, 0, 0, 0, 2, 0, 3, 9, 0], [5, 0, 7, 0, 0, 0, 6, 2, 1], [0, 3, 2, 0, 0, 6, 0, 0, 0], [0, 2, 0, 0, 0, 9, 1, 4, 0], [6, 0, 1, 2, 5, 0, 8, 0, 9], [0, 0, 0, 0, 0, 1, 0, 0, 2]]

puzzle3 = [[1, 0, 0, 4, 8, 9, 0, 0, 6], [7, 3, 0, 0, 5, 0, 0, 4, 0], [4, 6, 0, 0, 0, 1, 2, 9, 5], [3, 8, 7, 1, 2, 0, 6, 0, 0], [5, 0, 1, 7, 0, 3, 0, 0, 8], [0, 4, 6, 0, 9, 5, 7, 1, 0], [9, 1, 4, 6, 0, 0, 0, 8, 0], [0, 2, 0, 0, 4, 0, 0, 3, 7], [8, 0, 3, 5, 1, 2, 0, 0, 4]]

puzzle4 = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6], [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]]

chosenPuzzle = int(input("Which puzzle do you want to find a solution for? (1/2/3/4): "))
if chosenPuzzle == 1:
    chosenPuzzle = puzzle1
elif chosenPuzzle == 2:
    chosenPuzzle = puzzle2
elif chosenPuzzle == 3:
    chosenPuzzle = puzzle3
elif chosenPuzzle == 4:
    chosenPuzzle = puzzle4

print(np.matrix(chosenPuzzle))

def possible(row, column, answer):
    global chosenPuzzle

    for i in range(0, 9):
        if chosenPuzzle [row][i] == answer:
            return False

    for i in range(0, 9):
        if chosenPuzzle [i][column] == answer:
            return False

    subBoxRow = (row//3)*3
    subBoxCol = (column//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if chosenPuzzle[subBoxRow + 1][subBoxCol + j] == answer:
                return False

    return True

def solve():
    global chosenPuzzle
    for row in range(9):
        for column in range(9):
            if chosenPuzzle[row][column] == 0:
                for answer in range(1, 10):
                    if possible(row, column, answer):
                        chosenPuzzle[row][column] = answer
                        solve()
                        chosenPuzzle[row][column] = 0
                return
    
    print(np.matrix(chosenPuzzle))

solve()