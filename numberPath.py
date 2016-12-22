#  File: numberPath.py
#  Description: This program recursively goes through a maze of numbers to an end point.
#  Student's Name: Elias Ansari
#  Student's UT EID: eaa957
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 4/12/16
#  Date Last Modified: 
#############################################################################
from copy import deepcopy

class Problem():
    def __init__ (self, grid, pathHistory, currRow, currColumn, sumNumbers):
        self.grid = grid
        self.pathHistory = pathHistory
        self.currRow = currRow
        self.currColumn = currColumn
        self.sumNumbers = sumNumbers

    def showGrid(self):
        # print grid
        grid = self.grid
        for i in range(len(grid)):
            line = grid[i]
            printLine = ""
            for j in range (len(line)):
                if (len(line[j]) == 1):
                    printLine += line[j] + "    "
                elif (len(line[j]) == 2):
                    printLine += line[j] + "   "
                elif (len(line[j]) == 3):
                    printLine += line[j] + "  "
                else:
                    printLine += line[j] + " "
            print (printLine)

# function to go through maze recursively
def solve(problem):
    print ("\nProblem is now:")
    print ("     Grid: \n")
    problem.showGrid()
    print ("History: ", problem.pathHistory)
    print ("Start point: ({},{})".format(problem.currRow, problem.currColumn))
    print ("Sum: ", problem.sumNumbers)
    print ("\nIs this the goal state?")

    if problem.currRow == endRow and problem.currColumn == endCol and problem.sumNumbers == targetValue:
        print ("Success! Goal was reached. Path History: {}".format(problem.pathHistory))
        return (problem.pathHistory)
    else:
        if problem.sumNumbers > targetValue:
            print("No. Target value exceeded. Let's go back and try again.")
            return None
        else:
            if isValid(problem, "right"):   #move right\
                print ("Yes! Go on.")
                newRow = problem.currRow
                newCol = problem.currColumn + 1
                newGrid = deepcopy(problem.grid)
                totalSum = problem.sumNumbers + int(problem.grid[newRow][newCol])
                newPath = deepcopy(problem.pathHistory)
                newPath.append(int(problem.grid[newRow][newCol]))
                newGrid[newRow][newCol] = "None"
                currentProblem = Problem (newGrid, newPath, newRow, newCol, totalSum)
                result = solve(currentProblem)
                if (result != None):
                    return (problem.pathHistory)
            if isValid(problem, "up"):    #move up\
                print ("Yes! Go on.")
                newRow = problem.currRow -1
                newCol = problem.currColumn
                newGrid = deepcopy(problem.grid)
                totalSum = problem.sumNumbers + int(problem.grid[newRow][newCol])
                newPath = deepcopy(problem.pathHistory)
                newPath.append(int(problem.grid[newRow][newCol]))
                newGrid[newRow][newCol] = "None"
                currentProblem = Problem (newGrid, newPath, newRow, newCol, totalSum)
                result = solve(currentProblem)
                if (result != None):
                    return (problem.pathHistory)
            if isValid(problem, "down"):   #move down\
                print ("Yes! Go on.")

                newRow = problem.currRow + 1
                newCol = problem.currColumn
                newGrid = deepcopy(problem.grid)
                totalSum = problem.sumNumbers + int(problem.grid[newRow][newCol])
                newPath = deepcopy(problem.pathHistory)
                newPath.append(int(problem.grid[newRow][newCol]))
                newGrid[newRow][newCol] = "None"
                currentProblem = Problem (newGrid, newPath, newRow, newCol, totalSum)
                result = solve(currentProblem)
                if (result != None):
                    return (problem.pathHistory)
            if isValid(problem, "left"): #move left\
                print ("Yes! Go on.")

                newRow = problem.currRow
                newCol = problem.currColumn - 1
                newGrid = deepcopy(problem.grid)
                totalSum = problem.sumNumbers + int(problem.grid[newRow][newCol])
                newPath = deepcopy(problem.pathHistory)
                newPath.append(int(problem.grid[newRow][newCol]))
                newGrid[newRow][newCol] = "None"
                currentProblem = Problem (newGrid, newPath, newRow, newCol, totalSum)
                result = solve(currentProblem)
                if (result != None):
                    return (problem.pathHistory)
            else:
                print("Hmmm....Let's go back and try again.")
                return None
        
# function to move up, down, right, or left    
def isValid (problem, direction):

    # move right if...
    if (direction == "right"):
        print ("No. Can I move right?")
        movingColumn = problem.currColumn + 1
        movingRow = problem.currRow
        if 0 <= movingColumn < gridCols and 0 <= movingRow < gridRows and problem.grid[movingRow][movingColumn] != "None":
            return True
        else:
            return False
    # move up if...
    elif (direction == "up"):
        print ("No. Can I move up?")
        movingColumn = problem.currColumn
        movingRow = problem.currRow - 1
        if 0 <= movingColumn < gridCols and 0 <= movingRow < gridRows and problem.grid[movingRow][movingColumn] != "None":
            return True
        else:
            return False
    # move down if...
    elif (direction == "down"):
        print ("No. Can I move down?")
        movingColumn = problem.currColumn
        movingRow = problem.currRow + 1
        if 0 <= movingColumn < gridCols and 0 <= movingRow < gridRows and problem.grid[movingRow][movingColumn] != "None":
            return True
        else:
            return False
    # move left if...
    else:
        print ("No. Can I move left?")
        movingColumn = problem.currColumn - 1
        movingRow = problem.currRow
        if 0 <= movingColumn < gridCols and 0 <= movingRow < gridRows and problem.grid[movingRow][movingColumn] != "None":
            return True
        else:
            return False

def main():

    # open file
    file = open("pathdata.txt", "r")

    lineOne = file.readline()
    lineOne = lineOne.strip().split(" ")

    # define and create variables
    global targetValue
    targetValue = int(lineOne[0])

    global gridRows
    gridRows = int(lineOne[1])

    global gridCols
    gridCols = int(lineOne[2])

    startRow = int(lineOne[3])

    startCol = int(lineOne[4])

    global endRow
    endRow = int(lineOne[5])

    global endCol
    endCol = int(lineOne[6])

    grid = file.readlines()
    
    # organize line
    for i in range (len(grid)):
        grid[i] = grid[i].strip("\n").split()

    pathHistory = []
    sumNumbers = 0
    problem = Problem (grid, pathHistory, startRow, startCol, sumNumbers)
    print ("Initial grid:\n")
    problem.showGrid()
    
    startPoint = int(grid[startRow][startCol])
    pathHistory = [startPoint]
    sumNumbers = startPoint
    grid[startRow][startCol] = "None"

    problem = Problem (grid, pathHistory, startRow, startCol, sumNumbers)
    solve(problem)

    # close file
    file.close()




main()
