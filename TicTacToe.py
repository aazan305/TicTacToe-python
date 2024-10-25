brett= [[' ' for i in range(3)] for i in range(3)]

def displlayboard(brett):
    for row in range(3):
        print(" | ".join(brett[row]))
        if row <2:
            print("-"*9)
displlayboard(brett)

def move(brett,row,col, player):
    if brett[row][col]==' ':
        brett[row][col]= player
        return True
    else: 
        print("velg et annet")
        return False
    

def velgSpiller():
    spiller=input("velg X eller O : ")
    return spiller

def velgmove(player):
    rowV=int(input("velg row: "))-1
    colV=int(input("velg col: "))-1
    return move(brett,rowV,colV,player)

def erfull(brett):
    for row in brett:
        for cell in row:
            if cell ==' ':
                return False
            
    print("The board is full. Game over!")
    return True
def check_winner(brett, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        # Check rows and columns
        if all(brett[i][j] == player for j in range(3)) or all(brett[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(brett[i][i] == player for i in range(3)) or all(brett[i][2 - i] == player for i in range(3)):
        return True
    return False
def reset(brett):
    
    for row in range(3):
        for col in range(3):
            brett[row][col] =' '


def spill(brett):
    spiller1=velgSpiller()
    spiller2= "X" if spiller1 =="O" else "O"

    movecount=0
    
    while not erfull(brett):
    
        current_player= spiller1 if movecount%2==0 else spiller2
        while  not velgmove(current_player):
            pass
        displlayboard(brett)
        movecount+=1
        if check_winner(brett,current_player) ==True:
            print(f"player {current_player} won!")
            res=input("want to play again: ")
            if res=="Y":
                reset(brett)
                displlayboard(brett)
                movecount=0

            else:
                break
spill(brett)



