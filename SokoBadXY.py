from random import randint

def boardToString(gameBoard):
    outString=""
    charcount=0
    for y in range(len(gameBoard[0])):
        for x in range(len(gameBoard)):
            tile=gameBoard[x][y]
            if tile == 0:
                outString+="\u2b1c"#blank
            elif tile == 1:
                outString+="\u2b1b"#square
            elif tile == 2:
                outString+="\u26d4"#hole placeholder
            elif tile >= 30:
                outString+="\u274c"#box placeholder
            elif tile >= 10:
                outString+="\u1f600"#smile
        outString+="\n"
    return outString


def newGame(x, y, level=1):
    gameBoard=[]
    playerY=0
    playerX=0
    holes=0
    holescovered=0
    
    gameBoard.append([1]*y)#create blank board
    for row in range(x-2):
        gameBoard.append([1]+[0]*(y-2)+[1])
    gameBoard.append([1]*y)

    playerY=randint(1,y-1)#randomly add player
    playerX=randint(1,x-1)
    while gameBoard[playerX][playerY] != 0:
        playerY=randint(1,y-1)
        playerX=randint(1,x-1)
    gameBoard[playerX][playerY]+=10

    for i in range(level):
        tilegenY=randint(2,y-3)#randomly add crates
        tilegenX=randint(2,x-3)
        while gameBoard[tilegenX][tilegenY] != 0:
            tilegenY=randint(2,y-3)
            tilegenX=randint(2,x-3)
        gameBoard[tilegenX][tilegenY]=30

    for i in range(level):
        tilegenY=randint(2,y-3)#randomly add crate holes
        tilegenX=randint(2,x-3)
        while gameBoard[tilegenX][tilegenY] != 0:
            tilegenY=randint(2,y-3)
            tilegenX=randint(2,x-3)
        gameBoard[tilegenX][tilegenY]=2
        holes+=1

    game=[gameBoard,[playerX,playerY],level,holes,holescovered]
    return game



def iterateGame(game, move):
    targetPos=[0,0]
    playerPos=game[1]
    targetPos[0]=playerPos[0]+move[0]
    targetPos[1]=playerPos[1]+move[1]
    if game[0][targetPos[0]][targetPos[1]] in [0,2]:
        game[0][targetPos[0]][targetPos[1]]+=10
        game[0][playerPos[0]][playerPos[1]]-=10
        game[1]=targetPos
    elif game[0][targetPos[0]][targetPos[1]] >= 30:
        if game[0][targetPos[0]+move[0]][targetPos[1]+move[1]] in [0,2]:
            game[0][targetPos[0]+move[0]][targetPos[1]+move[1]]+=30
            if game[0][targetPos[0]+move[0]][targetPos[1]+move[1]] == 32:
                game[4]+=1
            game[0][targetPos[0]][targetPos[1]]-=30
            if game[0][targetPos[0]][targetPos[1]] == 2:
                game[4]-=1



            game[0][targetPos[0]][targetPos[1]]+=10
            game[0][playerPos[0]][playerPos[1]]-=10
            game[1]=targetPos


    return game
    



game=newGame(10,11,3)
while True:
    print(boardToString(game[0]))
    userin=input("input:")
    if userin in ["w","a","s","d"]:
        if userin == "w":
            movedir=[0,-1]
        elif userin == "a":
            movedir=[-1,0]
        elif userin == "s":
            movedir=[0,1]
        elif userin == "d":
            movedir=[1,0]

    else:
        movedir=[0,0]
    game=iterateGame(game,movedir)
    if game[4]==game[3]:
        break

print("WIN!\n")
print("Final Board Position:")
print(boardToString(game[0]))
    

