#  File: Bowling.py
#  Description: This program calculates and outputs the scores of several ten pin bowling games.
#  Student's Name: Elias Ansari
#  Student's UT EID: eaa957
#  Course Name: CS 313E 
#  Unique Number: 50940

#################################################################################


def strike (turn1, turn2, newScore):
    frameScore = 10
    if (turn1 == "X"):
        frameScore += 10
        if (turn2 == "X"):
            frameScore += 10
        elif (turn2 == "-"):
            frameScore += 0
        else:
            frameScore += int(turn2)
    elif (turn1 == "-"):
        frameScore += 0
        if (turn2 == "-"):
            frameScore += 0
        elif (turn2 == "/"):
            frameScore += 10
        else:
            frameScore += int(turn2)
    else:
        if (turn2 == "/"):
            frameScore += 10
        elif turn2 == "-":
            frameScore += int(turn1)
        else:
            frameScore += (int(turn1) + int(turn2))
        
    newScore += frameScore
    return (newScore)
        
    
def spare(turn1, newScore):
    frameScore = 10
    if (turn1 == "X"):
        frameScore += 10
    elif (turn1 == "-"):
        frameScore += 0
    else:
        frameScore += int(turn1)
        

    newScore += frameScore
    return (newScore)

def reg(turn1, turn2, turn3, newScore):
    if (turn2 == "/"):
        newScore = spare(turn3, newScore)
        return (newScore)
    elif (turn1 == "-"):
        if (turn2 == "/"):
            newScore += 10
        elif (turn2 == "-"):
            return(newScore)
        else:
            newScore += int(turn2)
            return (newScore)
    else:
        newScore += int(turn1)
        if (turn2 == "-"):
            return(newScore)
        elif (turn2 == "/"):
            newScore += 10
        else:
            newScore += int(turn2)
        return(newScore)
             
def main():
    #  open the file scores.txt
    f = open ("scores.txt","r")

    

    #  read all the lines from the text file scores.txt, where 'lines' represents game read on each line
    for lines in f:
        lines = lines.rstrip("\n")

        #  define variables, where count is an index counter, newScore is
        #  the current score, frame is the frame counter, and table is a
        #  list that appends the newScore
        count = 0
        newScore = 0
        frame = 1
        table = []

        # convert each game into a list
        lines = lines.split()

        # while statement for the first 9 frames
        while (frame <= 9):
            if (lines[count] == "X"):
                newScore = strike(lines[count+1], lines[count+2], newScore)
                count += 1
                table.append(newScore)
                frame += 1

            else:
                newScore = reg(lines[count], lines[count+1], lines[count+2], newScore)
                count += 2
                table.append(newScore)
                frame += 1
        
        # 10th frame conditional statements
        if (lines[count] == "X"):
            newScore = strike(lines[count+1], lines[count+2], newScore)
        elif (lines[count+1] == "/"):
            newScore = spare(lines[count+2], newScore)
        else:
            if (lines[count] == "-"):
                newScore += 0

            else:
                if (lines[count+1] == "-"):
                    newScore += 0
                else:   
                    newScore += int(lines[count]) + int(lines[count+1])
        table.append(newScore)

        #  while statement that creates string of each game for the first 9 frames
        counter = 0
        gameLine = "|"
        while (len(gameLine) <= 36):
            if (lines[counter] == "X"):
                gameLine += "X  |"
                counter += 1
            else:
                (lines[counter] == "/")
                gameLine += lines[counter] + " " + lines[counter+1] + "|"
                counter += 2

        #  if-elif-else statement that creates string of each game for the 10th frame
        if (lines[counter] == "X"):
            gameLine += "X " + lines[counter+1] + " " + lines[counter+2] + "|"
        elif (lines[counter+1] == "/"):
            gameLine += lines[counter] + " / " + lines[counter+2] + "|"
        else:
            gameLine += lines[counter] + " " + lines[counter+1] + "  |"

        gameScoring = "|"
        for i in range (0,9):
            if (len(str(table[i])) == 1):
                gameScoring += "  " + str(table[i]) + "|"
            elif (len(str(table[i])) == 2):
                gameScoring += " " + str(table[i]) + "|"
            else:
                gameScoring += str(table[9]) + "|"
        if (len(str(table[9])) == 1):
            gameScoring += "    " + str(table[9]) + "|"
        elif (len(str(table[9])) == 2):
            gameScoring += "   " + str(table[9]) + "|"
        else:
            gameScoring += "  " + str(table[9]) + "|"

        #  print output
        print("  1   2   3   4   5   6   7   8   9    10")
        print("+---+---+---+---+---+---+---+---+---+-----+")
        print(gameLine)
        print(gameScoring)
        print("+---+---+---+---+---+---+---+---+---+-----+\n")
    
    # close file
    f.close()

main()
