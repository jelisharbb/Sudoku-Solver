import numpy as np

print("\n==================== SUDOKU SOLVER ====================")
print("Can't find the solution to your sudoku puzzle? Fret not, \nbecause we've got you! This program will find it for you.")

while True:
    readiness = input("\nDo you want to proceed? (Yes/No): ")
    if readiness.lower() == "yes":
        break
    elif readiness.lower() == "no":
        print("\n====================== GOOD BYE ======================\n")
        exit()
    else:
        print("Answer yes or no only.")

puzzleSize = 0
subBoxMultiplierX = 0
subBoxMultiplierY = 0
subBoxDividerX = 0
subBoxDividerY = 0
answerRangeIndex = 0

while True: 
    size = int(input("What size of the puzzle do you want to find a solution for? (3/4/6/8/9): "))

    if size == 3:
        puzzleSize = 3
        subBoxDividerX = 1
        subBoxDividerY = 1
        subBoxMultiplierX = 1
        subBoxMultiplierY = 1
        answerRangeIndex = 4

        # 3 by 3 puzzles
        puzzle3_1 = [[2, 0, 3], [1, 0, 0], [0, 0, 1]]
        puzzle3_2 = [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
        puzzle3_3 = [[0, 1, 0], [0, 0, 3], [2, 0, 0]]
        puzzle3_4 = [[0, 3, 0], [0, 1, 0], [1, 0, 0]]
        puzzle3_5 = [[0, 0, 1], [1, 0, 0], [0, 0, 3]]

        print("\nPuzzle 1:")
        print(np.matrix(puzzle3_1))
        print("\nPuzzle 2:")
        print(np.matrix(puzzle3_2))
        print("\nPuzzle 3:")
        print(np.matrix(puzzle3_3))
        print("\nPuzzle 4:")
        print(np.matrix(puzzle3_4))
        print("\nPuzzle 5:")
        print(np.matrix(puzzle3_5))

        chosenPuzzle3 = int(input("\nWhich among the 3x3 puzzle do you want to find a solution for? (1/2/3/4/5): ")) 
        if chosenPuzzle3 == 1:
            finalPuzzle = puzzle3_1
        elif chosenPuzzle3 == 2:
            finalPuzzle = puzzle3_2
        elif chosenPuzzle3 == 3:
            finalPuzzle = puzzle3_3
        elif chosenPuzzle3 == 4:
            finalPuzzle = puzzle3_4
        elif chosenPuzzle3 == 5:
            finalPuzzle = puzzle3_5

        break

    elif size == 4:
        puzzleSize = 4
        subBoxDividerX = 2
        subBoxDividerY = 2
        subBoxMultiplierX = 2
        subBoxMultiplierY = 2
        answerRangeIndex = 5

        # 4 by 4 puzzles
        puzzle4_1 = [[1, 0, 3, 0], [0, 0, 4, 0], [0, 1, 0, 0], [0, 2, 0, 0]]
        puzzle4_2 = [[2, 0, 3, 0], [0, 0, 0, 4], [0, 0, 0, 3], [0, 0, 0, 2]]
        puzzle4_3 = [[0, 0, 3, 1], [0, 0, 0, 0], [0, 0, 0, 0], [3, 1, 4, 2]]
        puzzle4_4 = [[0, 4, 0, 0], [2, 0, 3, 4], [1, 3, 0, 0], [0, 0, 0, 0]]
        puzzle4_5 = [[4, 0, 0, 0], [0, 1, 0, 3], [0, 0, 0, 0], [1, 0, 3, 0]]

        print("\nPuzzle 1:")
        print(np.matrix(puzzle4_1))
        print("\nPuzzle 2:")
        print(np.matrix(puzzle4_2))
        print("\nPuzzle 3:")
        print(np.matrix(puzzle4_3))
        print("\nPuzzle 4:")
        print(np.matrix(puzzle4_4))
        print("\nPuzzle 5:")
        print(np.matrix(puzzle4_5))

        chosenPuzzle4 = int(input("Which among the 4x4 puzzle do you want to find a solution for? (1/2/3/4/5): ")) 
        if chosenPuzzle4 == 1:
            finalPuzzle = puzzle4_1
        elif chosenPuzzle4 == 2:
            finalPuzzle = puzzle4_2
        elif chosenPuzzle4 == 3:
            finalPuzzle = puzzle4_3
        elif chosenPuzzle4 == 4:
            finalPuzzle = puzzle4_4
        elif chosenPuzzle4 == 5:
            finalPuzzle = puzzle4_5

        break

    elif size == 6:
        puzzleSize = 6
        subBoxDividerX = 3
        subBoxDividerY = 2
        subBoxMultiplierX = 3
        subBoxMultiplierY = 2
        answerRangeIndex = 7

        # 6 by 6 puzzles
        puzzle6_1 =[[0, 0, 6, 0, 1, 0], [4, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2], [6, 0, 0, 0, 0, 0], [0, 0, 0, 0, 4, 5], [0, 2, 0, 3, 0, 0]]
        puzzle6_2 =[[0, 0, 1, 0, 0, 0], [0, 0, 0, 6, 0, 0], [1, 0, 0, 0, 3, 0], [0, 4, 0, 0, 0, 2], [0, 0, 2, 0, 0, 0], [0, 0, 0, 2, 0, 0]]
        puzzle6_3 =[[0, 0, 0, 1, 5, 0], [2, 5, 1, 0, 3, 0], [1, 0, 2, 3, 4, 0], [0, 3, 5, 2, 0, 6], [0, 1, 0, 4, 2, 3], [0, 2, 4, 0, 0, 0]]
        puzzle6_4 =[[1, 0, 0, 4, 6, 3], [3, 6, 4, 0, 2, 0], [5, 0, 0, 0, 4, 0], [0, 2, 0, 0, 0, 1], [0, 4, 0, 5, 3, 2], [2, 3, 5, 0, 0, 4]]
        puzzle6_5 =[[1, 0, 4, 6, 0, 5], [0, 0, 0, 1, 0, 0], [6, 1, 5, 4, 0, 2], [3, 0, 2, 5, 6, 1], [0, 0, 3, 0, 0, 0], [2, 0, 1, 3, 0, 4]]

        print("\nPuzzle 1:")
        print(np.matrix(puzzle6_1))
        print("\nPuzzle 2:")
        print(np.matrix(puzzle6_2))
        print("\nPuzzle 3:")
        print(np.matrix(puzzle6_3))
        print("\nPuzzle 4:")
        print(np.matrix(puzzle6_4))
        print("\nPuzzle 5:")
        print(np.matrix(puzzle6_5))

        chosenPuzzle6 = int(input("Which among the 6x6 puzzle do you want to find a solution for? (1/2/3/4/5): ")) 
        if chosenPuzzle6 == 1:
            finalPuzzle = puzzle6_1
        elif chosenPuzzle6 == 2:
            finalPuzzle = puzzle6_2
        elif chosenPuzzle6 == 3:
            finalPuzzle = puzzle6_3
        elif chosenPuzzle6 == 4:
            finalPuzzle = puzzle6_4
        elif chosenPuzzle6 == 5:
            finalPuzzle = puzzle6_5

        break

    elif size == 8:
        puzzleSize = 8
        subBoxDividerX = 4
        subBoxDividerY = 2
        subBoxMultiplierX = 4
        subBoxMultiplierY = 2
        answerRangeIndex = 9

        # 8 by 8 puzzles
        puzzle8_1 = [[4, 0, 0, 2, 1, 0, 3, 0], [0, 7, 0, 0, 0, 2, 0, 0], [0, 0, 2, 0, 5, 0, 7, 0], [7, 0, 0, 5, 0, 0, 0, 3], [6, 0, 0, 0, 3, 0, 0, 1], [0, 1, 0, 3, 0, 8, 0, 0], [0, 0, 7, 0, 0, 0, 8, 0], [0, 6, 0, 8, 4, 0, 0, 5]]
        puzzle8_2 = [[2, 0, 0, 0, 1, 0, 3, 8], [3, 1, 6, 0, 0, 7, 0, 2], [0, 4, 5, 0, 0, 0, 8, 0], [1, 0, 0, 2, 6, 4, 7, 5], [0, 0, 4, 7, 5, 0, 0, 0], [5, 2, 0, 0, 7, 0, 6, 0], [0, 7, 1, 3, 0, 0, 0, 6], [4, 6, 0, 0, 8, 0, 0, 0]]
        puzzle8_3 = [[0, 4, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 8, 4], [0, 0, 0, 8, 0, 0, 0, 0], [0, 0, 0, 3, 0, 0, 5, 6], [0, 3, 0, 0, 0, 0, 4, 2], [5, 0, 0, 0, 0, 3, 0, 1], [1, 0, 0, 0, 0, 5, 2, 0], [0, 0, 3, 5, 0, 6, 0, 0]]
        puzzle8_4 = [[3, 0, 8, 0, 0, 1, 0, 5], [0, 0, 0, 7, 8, 0, 0, 0], [4, 0, 1, 0, 0, 8, 0, 3], [0, 8, 0, 2, 5, 0, 4, 0], [0, 5, 0, 1, 3, 0, 7, 0], [8, 0, 7, 0, 0, 6, 0, 2], [0, 0, 0, 6, 2, 0, 0, 0], [7, 0, 2, 0, 0, 5, 0, 6]]
        puzzle8_5 = [[0, 0, 7, 0, 0, 0, 6, 0], [0, 0, 0, 0, 2, 4, 0, 1], [0, 0, 0, 5, 0, 8, 0, 2], [2, 0, 0, 6, 0, 0, 4, 0], [0, 7, 0, 0, 3, 0, 0, 8], [6, 0, 3, 0, 5, 0, 0, 0], [3, 0, 1, 7, 0, 0, 0, 0], [0, 2, 0, 0, 0, 1, 0, 0]]

        print("\nPuzzle 1:")
        print(np.matrix(puzzle8_1))
        print("\nPuzzle 2:")
        print(np.matrix(puzzle8_2))
        print("\nPuzzle 3:")
        print(np.matrix(puzzle8_3))
        print("\nPuzzle 4:")
        print(np.matrix(puzzle8_4))
        print("\nPuzzle 5:")
        print(np.matrix(puzzle8_5))

        chosenPuzzle8 = int(input("Which among the 8x8 puzzle do you want to find a solution for? (1/2/3/4/5): ")) 
        if chosenPuzzle8 == 1:
            finalPuzzle = puzzle8_1
        elif chosenPuzzle8 == 2:
            finalPuzzle = puzzle8_2
        elif chosenPuzzle8 == 3:
            finalPuzzle = puzzle8_3
        elif chosenPuzzle8 == 4:
            finalPuzzle = puzzle8_4
        elif chosenPuzzle8 == 5:
            finalPuzzle = puzzle8_5

        break

    elif size == 9:
        puzzleSize = 9
        subBoxDividerX = 3
        subBoxDividerY = 3
        subBoxMultiplierX = 3
        subBoxMultiplierY = 3
        answerRangeIndex = 10

        # 9 by 9 puzzles
        puzzle9_1 = [[0, 0, 0, 2, 6, 0, 7, 0, 1], [6, 8, 0, 0, 7, 0, 0, 9, 0], [1, 9, 0, 0, 0, 4, 5, 0, 0], [8, 2, 0, 1, 0, 0, 0, 4, 7], [0, 0, 4, 6, 0, 2, 9, 0, 0], [0, 5, 0, 0, 0, 3, 0, 2, 8], [0, 0, 9, 3, 0, 0, 0, 7, 4], [0, 4, 0, 0, 5, 0, 0, 3, 6], [7, 0, 3, 0, 1, 8, 0, 0, 0]]
        puzzle9_2 = [[2, 0, 0, 3, 0, 0, 0, 0, 0], [8, 0, 4, 0, 6, 2, 0, 0, 3], [0, 1, 3, 8, 0, 0, 2, 0, 0], [0, 0, 0, 0, 2, 0, 3, 9, 0], [5, 0, 7, 0, 0, 0, 6, 2, 1], [0, 3, 2, 0, 0, 6, 0, 0, 0], [0, 2, 0, 0, 0, 9, 1, 4, 0], [6, 0, 1, 2, 5, 0, 8, 0, 9], [0, 0, 0, 0, 0, 1, 0, 0, 2]]
        puzzle9_3 = [[1, 0, 0, 4, 8, 9, 0, 0, 6], [7, 3, 0, 0, 5, 0, 0, 4, 0], [4, 6, 0, 0, 0, 1, 2, 9, 5], [3, 8, 7, 1, 2, 0, 6, 0, 0], [5, 0, 1, 7, 0, 3, 0, 0, 8], [0, 4, 6, 0, 9, 5, 7, 1, 0], [9, 1, 4, 6, 0, 0, 0, 8, 0], [0, 2, 0, 0, 4, 0, 0, 3, 7], [8, 0, 3, 5, 1, 2, 0, 0, 4]]
        puzzle9_4 = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6], [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]]
        puzzle9_5 = [[0, 2, 6, 0, 0, 0, 8, 1, 0], [3, 0, 0, 7, 0, 8, 0, 0, 6], [4, 0, 0, 0, 5, 0, 0, 0, 7], [0, 5, 0, 1, 0, 7, 0, 9, 0], [0, 0, 3, 9, 0, 5, 1, 0, 0], [0, 4, 0, 3, 0, 2, 0, 5, 0], [1, 0, 0, 0, 3, 0, 0, 0, 2], [5, 0, 0, 2, 0, 4, 0, 0, 9], [0, 3, 8, 0, 0, 0, 4, 6, 0]]

        print("\nPuzzle 1:")
        print(np.matrix(puzzle9_1))
        print("\nPuzzle 2:")
        print(np.matrix(puzzle9_2))
        print("\nPuzzle 3:")
        print(np.matrix(puzzle9_3))
        print("\nPuzzle 4:")
        print(np.matrix(puzzle9_4))
        print("\nPuzzle 5:")
        print(np.matrix(puzzle9_5))

        chosenPuzzle6 = int(input("Which among the 9x9 puzzle do you want to find a solution for? (1/2/3/4/5): ")) 
        if chosenPuzzle6 == 1:
            finalPuzzle = puzzle9_1
        elif chosenPuzzle6 == 2:
            finalPuzzle = puzzle9_2
        elif chosenPuzzle6 == 3:
            finalPuzzle = puzzle9_3
        elif chosenPuzzle6 == 4:
            finalPuzzle = puzzle9_4
        elif chosenPuzzle6 == 5:
            finalPuzzle = puzzle9_5

        break

    else:
        print("Puzzle sizes are only 3, 4, 6, 8, and 9.")

print("\nYour Chosen Puzzle:")
print(np.matrix(finalPuzzle))

def possible(row, column, answer):
    global finalPuzzle

    for i in range(0, puzzleSize): # checks if the number is already in the row 
        if finalPuzzle [row][i] == answer:
            return False

    for i in range(0, puzzleSize): # checks if the number is already in the column 
        if finalPuzzle [i][column] == answer:
            return False

    subBoxRow = (row // subBoxDividerY) * subBoxMultiplierY
    subBoxCol = (column // subBoxDividerX) * subBoxMultiplierX
    for i in range(0, subBoxMultiplierY): # checks if the number is already in the sub box of the puzzle 
        for j in range(0, subBoxMultiplierX):
            if finalPuzzle[subBoxRow + i][subBoxCol + j] == answer:
                return False

    return True

def solve():
    global finalPuzzle
    for row in range(puzzleSize):
        for column in range(puzzleSize):
            if finalPuzzle[row][column] == 0: # checks if the certain spot is blank
                for answer in range(1, answerRangeIndex): # iterates numbers 1 to the highest possible number to the blank spot
                    if possible(row, column, answer):
                        finalPuzzle[row][column] = answer # if the number satisfies the rules of the puzzle, it will be written
                        solve()
                        finalPuzzle[row][column] = 0 # if the number does not satisfy the rules, it will go back to 0 or be blank again
                return
    
    print("\nSolution:")
    print(np.matrix(finalPuzzle))
    print()

solve()