#CSCI 1133 Homework 3
#Erik Lindeman
#Problem D
game = True
turn = 1
used1 = []
used2 = []
row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']
oneCol1 = 0
oneCol2 = 0
oneCol3 = 0
oneRow1 = 0
oneRow2 = 0
oneRow3 = 0
oneDiag1 = 0
oneDiag2 = 0
twoCol1 = 0
twoCol2 = 0
twoCol3 = 0
twoRow1 = 0
twoRow2 = 0
twoRow3 = 0
twoDiag1 = 0
twoDiag2 = 0
winner = 0
win = False
def move(moveVar,who):
    if(moveVar<=2):
        row1[moveVar] = who
    elif(moveVar<=5):
        row2[moveVar-3] = who
    else:
        row3[moveVar-6] = who
    print("",row1,'\n',row2,'\n',row3)

def score(moveVar, who):
    if(who == "x"):
        if(moveVar<3):
            oneRow1+=1
            if(oneRow1>=3):
                win=True
        elif(moveVar<6):
            oneRow2+=1
            if(oneRow2>=3):
                win=True
        elif(moveVar<9):
            oneRow3+=1
            if(oneRow3>=3):
                win=True
    else:
        if(moveVar<3):
            twoRow1+=1
            if(twoRow1>=3):
                win=True
        elif(moveVar<6):
            twoRow2+=1
            if(twoRow2>=3):
                win=True
        elif(moveVar<9):
            twoRow3+=1
            if(twoRow3>=3):
                win=True
while(game):
    if(turn%2==1):
        moveVar = int(input("Player 1, where would you like to move?: "))
        if(not(moveVar in used1)and not(moveVar in used2)):
            who = "x"
            turn+=1
            actuallyMove = True
            used1.append(moveVar)
        else:
            print("This space has already been taken.  Please try again!")
            actuallyMove = False
    else:
        moveVar = int(input("Player 2, where would you like to move?: "))
        if(not(moveVar in used1)and not(moveVar in used2)):
            who = "o"
            turn+=1
            actuallyMove = True
            used2.append(moveVar)
        else:
            print("This space has already been taken.  Please try again!")
            actuallyMove = False
    if(actuallyMove):
        move(moveVar,who)
        score(moveVar, who)
    if(win):
        game = False
        if(who == "x"):
            winner = "1"
        else:
            winner = "2"
        print("Player {} wins!".format(winner))
    if(turn>9):
        game = False
        print("The game was a tie")
