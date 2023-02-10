import numpy as np

print("\n==================== SUDOKU SOLVER ====================")
print("Can't find the solution to your sudoku puzzle? Fret not, \nbecause we've got you! This program will find it for you.")

while True:
    readiness = input("\nDo you want to proceed? ")
    if readiness.lower() == "yes":
        break
    elif readiness.lower() == "no":
        print("\nGood bye...")
        exit()

puzzleSize = 0
subBoxMultiplier = 0
subBoxDividerX = 0
subBoxDividerY = 0
answerRange = 0

size = int(input("What size of the puzzle do you want to find a solution for? (3/6/9)"))
if size == 3:
    puzzleSize = 3
    subBoxMultiplier = 1
    subBoxDividerX = 1
    subBoxDividerY = 1
    answerRange = 3

puzzle1 = [[0, 0, 0, 2, 6, 0, 7, 0, 1], [6, 8, 0, 0, 7, 0, 0, 9, 0], [1, 9, 0, 0, 0, 4, 5, 0, 0], [8, 2, 0, 1, 0, 0, 0, 4, 7], [0, 0, 4, 6, 0, 2, 9, 0, 0], [0, 5, 0, 0, 0, 3, 0, 2, 8], [0, 0, 9, 3, 0, 0, 0, 7, 4], [0, 4, 0, 0, 5, 0, 0, 3, 6], [7, 0, 3, 0, 1, 8, 0, 0, 0]]

puzzle2 = [[2, 0, 0, 3, 0, 0, 0, 0, 0], [8, 0, 4, 0, 6, 2, 0, 0, 3], [0, 1, 3, 8, 0, 0, 2, 0, 0], [0, 0, 0, 0, 2, 0, 3, 9, 0], [5, 0, 7, 0, 0, 0, 6, 2, 1], [0, 3, 2, 0, 0, 6, 0, 0, 0], [0, 2, 0, 0, 0, 9, 1, 4, 0], [6, 0, 1, 2, 5, 0, 8, 0, 9], [0, 0, 0, 0, 0, 1, 0, 0, 2]]

puzzle3 = [[1, 0, 0, 4, 8, 9, 0, 0, 6], [7, 3, 0, 0, 5, 0, 0, 4, 0], [4, 6, 0, 0, 0, 1, 2, 9, 5], [3, 8, 7, 1, 2, 0, 6, 0, 0], [5, 0, 1, 7, 0, 3, 0, 0, 8], [0, 4, 6, 0, 9, 5, 7, 1, 0], [9, 1, 4, 6, 0, 0, 0, 8, 0], [0, 2, 0, 0, 4, 0, 0, 3, 7], [8, 0, 3, 5, 1, 2, 0, 0, 4]]

puzzle4 = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6], [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]]

puzzle5 = [[0, 2, 6, 0, 0, 0, 8, 1, 0], [3, 0, 0, 7, 0, 8, 0, 0, 6], [4, 0, 0, 0, 5, 0, 0, 0, 7], [0, 5, 0, 1, 0, 7, 0, 9, 0], [0, 0, 3, 9, 0, 5, 1, 0, 0], [0, 4, 0, 3, 0, 2, 0, 5, 0], [1, 0, 0, 0, 3, 0, 0, 0, 2], [5, 0, 0, 2, 0, 4, 0, 0, 9], [0, 3, 8, 0, 0, 0, 4, 6, 0]]

chosenPuzzle = int(input("Which puzzle do you want to find a solution for? (1/2/3/4/5): "))
if chosenPuzzle == 1:
    chosenPuzzle = puzzle1
elif chosenPuzzle == 2:
    chosenPuzzle = puzzle2
elif chosenPuzzle == 3:
    chosenPuzzle = puzzle3
elif chosenPuzzle == 4:
    chosenPuzzle = puzzle4
elif chosenPuzzle == 5:
    chosenPuzzle = puzzle5

print(np.matrix(chosenPuzzle))

def possible(row, column, answer):
    global chosenPuzzle

    for i in range(0, 9): # checks if the number is already in the row 
        if chosenPuzzle [row][i] == answer:
            return False

    for i in range(0, 9): # checks if the number is already in the column 
        if chosenPuzzle [i][column] == answer:
            return False

    subBoxRow = (row//3)*3
    subBoxCol = (column//3)*3
    for i in range(0, 3): # checks if the number is already in the sub box of the puzzle 
        for j in range(0, 3):
            if chosenPuzzle[subBoxRow + 1][subBoxCol + j] == answer:
                return False

    return True

def solve():
    global chosenPuzzle
    for row in range(9):
        for column in range(9):
            if chosenPuzzle[row][column] == 0: # checks if the certain spot is blank
                for answer in range(1, 10): # iterates numbers 1 to 9 to the blank spot
                    if possible(row, column, answer):
                        chosenPuzzle[row][column] = answer # if the number satisfies the rules of the puzzle, it will be written
                        solve()
                        chosenPuzzle[row][column] = 0 # if the number does not satisfy the rules, it will go back to 0 or be blank again
                return
    
    print(np.matrix(chosenPuzzle))

solve()