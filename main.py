import random


    



def drawCard(chosen_cards):

    if len(chosen_cards) == 52:
        return
    
    xRandom = random.randint(0, 3)
    yRandom = random.randint(0, 12)
    indiv = False
    while indiv == False:
        indiv = True
        for i in range (0, len(chosen_cards)):
            if chosen_cards[i][0] == xRandom and chosen_cards[i][1] == yRandom:
                xRandom = random.randint(0, 3)
                yRandom = random.randint(0, 12)
                indiv = False
                break

    chosen_cards.append([xRandom, yRandom])

    return [xRandom, yRandom]


def printCard(card):

    print(" ___")
    if len(numbers[card[1]]) == 2:
        print("|" + numbers[card[1]] + suits[card[0]] + "|")
    else: print("|" + numbers[card[1]] + " " + suits[card[0]] + "|")

    print("|   |")
    print(" ---")

def setUpBoard(chosen_cards, board):
    for i in range(len(board)):
        for j in range(0, i):
            board[i].append([drawCard(chosen_cards), "x"])
            
        board[i].append([drawCard(chosen_cards), "o"])
        #print (board[i])

    
    return board


def maxBoard(board):
    maxCards = 0

    for i in range(len(board)):
        if len(board[i]) > maxCards:
            maxCards = len(board[i])

    #print (maxCards)

    return maxCards



def printBoard(board):
    j = 0
    maxCards = maxBoard(board)
    
    
    print ("")
    #below is the code for setting up foundations
    for k in range(4):
        
        print (" ___ ", end = "")
        
    print("")

    
    for i in range(4):
        if foundations[i] == []:
            print("|   |", end = "")
        else:
            
            if len(numbers[foundations[i][-1][1]]) == 2:
                print("|" + numbers[foundations[i][-1][1]] + suits[foundations[i][-1][0]] + "|", end = "")
            else:
                print("|" + numbers[foundations[i][-1][1]] + " " + suits[foundations[i][-1][0]] + "|", end = "")
    print("")

    for i in range(4):
        if foundations[i] == []:
            print("|___|", end = "")
        else:   
            
        
            print("|___|", end = "")

    print("")

    print("")

    
        
    #below is the code for setting up the main board
    print("  ", end = "")
    for i in range(len(board)):
        print("  " + str(i) + "  ", end = "")

    print("")
    print("  ", end = "")

    for k in range(len(board)):
        if board[k] != []:
            print (" ___ ", end = "")
        else:
            print("     ", end = "")
    print("")

    

    while j < maxCards:
        if len(str(j)) > 1:
            print(j, end = "")
        else:
            print(str(j) + " ", end = "")
        
        for i in range(len(board)):


            try:
                board[i][j+1]

                
            except IndexError:
                try: board[i][j][1] = "o"
                except IndexError: pass
            
            try:
                if board[i][j][1] == "o":
                    
                    if len(numbers[board[i][j][0][1]]) == 2:
                        print("|" + numbers[board[i][j][0][1]] + suits[board[i][j][0][0]] + "|", end = "")
                    else:
                        print("|" + numbers[board[i][j][0][1]] + " " + suits[board[i][j][0][0]] + "|", end = "")
                else:
                    print("|###|", end = "")
                    

            except IndexError:
                
                print("     ", end = "") #5 spaces
                
        print ("")
        print("  ", end = "")

        for k in range(len(board)):
            try:
                board[k][j+1]

                print("+---+", end = "")
                
            except IndexError:
                try:
                    board[k][j]

                    print("|___|", end = "")
                except IndexError:
                    print("     ", end = "")

        print ("")

        j+=1

    #for the pile of new cards

    try:
        if inew != 0:
            print()
            printCard(newpile[inew][0])
    except IndexError:
        pass
        
    


    

def moveCard(board, fr, to): #fr is two co-ords, 1 for the row, another for the column
    #i have no idea what the difference is i'm lame
    

    try:
        if moveCorrect(board[fr[0]][fr[1]][0], board[to][len(board[to]) - 1][0]):
            temp = board[fr[0]][fr[1]:]

            aim = fr[1]

            while len(board[fr[0]]) > fr[1]:
                 board[fr[0]].pop(fr[1])
                    

                    
            board[to].extend(temp)

        else:
            print ("Oops, please abide to the rules, thank you!!")
    except IndexError:
        if moveCorrect(board[fr[0]][fr[1]][0], []):
            temp = board[fr[0]][fr[1]:]

            aim = fr[1]

            while len(board[fr[0]]) > fr[1]:
                board[fr[0]].pop(fr[1])
                

                
            board[to].extend(temp)
    
        
    
def moveNew(board, to, inew):

    try:
        if moveCorrect(newpile[inew][0], board[to][len(board[to]) - 1][0]):
            board[to].extend([newpile.pop(inew)])
            return inew - 1
        

        else:
            print ("Oops, please abide to the rules, thank you!!")
    except IndexError:
        if moveCorrect(newpile[inew][0], []):
            board[to].extend([newpile.pop(inew)])
            return inew - 1
            

def getNew(inew):
    
    if inew < len(newpile) - 1:
        return (inew + 1)
    elif len(newpile) > 0:
        return 0
    else:
        print("no more cards to turn over!")

def makeNew(newpile):
    while True:
        temp = drawCard(chosen_cards)
        if temp != None:
            newpile.append([temp, "o"])
        else:
            break
        
#LOGIC LOGIC LOGIC LOGIC LOGIC

def moveCorrect(card, toCard):

    
   
    if card[1] == 12 and toCard == []:
        return True
    elif (card[0] % 2) != (toCard[0] % 2) and card[1] == toCard[1] - 1:
        return True
    else:
        return False

def foundationMove(foundations, fr):
    card = board[fr[0]][fr[1]][0]
    try:
        if foundations[card[0]][-1][0] == card[0] and foundations[card[0]][-1][1] == card[1] - 1:
            foundations[card[0]].append(card)
            board[fr[0]].pop()
    except IndexError:
        
        if card[1] == 0:
            foundations[card[0]].append(card)
            board[fr[0]].pop()
        else:
            print("Oops, something went wrong!")

    return False


def newFoundationMove(foundations, newpile):
    card = newpile[inew][0]

    try:
        if foundations[card[0]][-1][0] == card[0] and foundations[card[0]][-1][1] == card[1] - 1:
            foundations[card[0]].append(card)
            newpile.pop(inew)
            return inew - 1
    except IndexError:
        
        if card[1] == 0:
            foundations[card[0]].append(card)
            newpile.pop(inew)
            return inew - 1
        else:
            print("Oops, something went wrong!")
    

#I should probably put this on a different document but yolo

suits = ["s", "h", "c", "d"]

board = [[], [], [], [], [], []]

numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

chosen_cards = []

newpile = [["x"]]

inew = 0

foundations = [[],[],[],[]]


printBoard(setUpBoard(chosen_cards, board))



makeNew(newpile)



testboard = [[[[0, 0], 'o']],
         [[[0, 5], 'x'], [[0, 1], 'o']],
         [[[1, 2], 'x'], [[0, 8], 'x'], [[0, 2], 'o']],
         [[[0, 10], 'x'], [[3, 3], 'x'], [[2, 7], 'x'], [[0, 3], 'o']],
         [[[1, 3], 'x'], [[3, 6], 'x'], [[2, 1], 'x'], [[3, 11], 'x'], [[0, 4], 'o']],
         [[[1, 12], 'x'], [[2, 6], 'x'], [[1, 10], 'x'], [[3, 10], 'x'], [[2, 12], 'x'], [[0, 5], 'o']]]


                                                                                                                                                            

while True:
    try:

        fr = [int(input("> ")), int(input("> "))]
        try:
            to = int(input("> "))

            moveCard(board, fr, to)
        except ValueError:
            foundationMove(foundations, fr)

    except ValueError:
        inp = input("Move? ")
        if inp == "y":
            try:
                inew = moveNew(board, int(input("> ")), inew)
            #print (board)
            except ValueError:
                inew = newFoundationMove(foundations, newpile)
                
        
        
        else:
            inew = getNew(inew)
            print(inew)

    
    

    

    printBoard(board)
    total = 0
    for i in range(4):
        total += len(foundations[i])

    if total == 52:
        print("Woo!! You've actually won?? I can't believe this!!")
    
    
    
