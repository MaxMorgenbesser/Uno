



def genRandomCard():
    class cards:
        y1 = ['Yellow',1]
        y2 = ['Yellow',2]
        y3 = ['Yellow',3]
        y4 = ['Yellow',4]
        y5 = ['Yellow',5]
        y6 = ['Yellow',6]
        y7 = ['Yellow',7]
        y8 = ['Yellow',8]
        y9 = ['Yellow',9]
        r1 = ['red',1]
        r2 = ['red',2]
        r3 = ['red',3]
        r4 = ['red',4]
        r5 = ['red',5]
        r6 = ['red',6]
        r7 = ['red',7]
        r8 = ['red',8]
        r9 = ['red',9]
        b1 = ['blue', 1]
        b2 = ['blue', 2]
        b3 = ['blue', 3]
        b4 = ['blue', 4]
        b5 = ['blue', 5]
        b6 = ['blue', 6]
        b7 = ['blue', 7]
        b8 = ['blue', 8]
        b9 = ['blue', 9]
        g1 = ['green', 1]
        g2 = ['green', 2]
        g3 = ['green', 3]
        g4 = ['green', 4]
        g5 = ['green', 5]
        g6 = ['green', 6]
        g7 = ['green', 7]
        g8 = ['green', 8]
        g9 = ['green', 9]
        wc = ['Choose Color']
        wc4 = ['Choose Color', 'Take four']
        wc2 = ['Choose Color', 'Take 2']
        rev = ['reverse order']
        skip = ['Skip next player']
    import random
    rNum=random.randint(0,41)
    if rNum ==0:
        rCard = cards.y1
        return rCard
    elif rNum == 1:
        rCard = cards.y2
        return  rCard
    elif rNum == 2:
        rCard = cards.y3
        return  rCard
    elif rNum == 3:
        rCard = cards.y4
        return  rCard
    elif rNum == 4:
        rCard = cards.y5
        return  rCard
    elif rNum == 5:
        rCard = cards.y6
        return  rCard
    elif rNum == 6:
        rCard = cards.y7
        return  rCard
    elif rNum == 7:
        rCard = cards.y8
        return  rCard
    elif rNum == 8:
        rCard = cards.y9
        return  rCard
    elif rNum == 9:
        rCard = cards.r1
        return  rCard
    elif rNum == 10:
        rCard = cards.r2
        return  rCard
    elif rNum == 11:
        rCard = cards.r3
        return  rCard
    elif rNum == 12:
        rCard = cards.r4
        return  rCard
    elif rNum == 13:
        rCard = cards.r5
        return  rCard
    elif rNum == 14:
        rCard = cards.r5
        return  rCard
    elif rNum == 15:
        rCard = cards.r6
        return  rCard
    elif rNum == 16:
        rCard = cards.r7
        return  rCard
    elif rNum == 17:
        rCard = cards.r8
        return  rCard
    elif rNum == 18:
        rCard = cards.r9
        return  rCard
    elif rNum == 19:
        rCard = cards.b1
        return  rCard
    elif rNum == 20:
        rCard = cards.b2
        return  rCard
    elif rNum == 21:
        rCard = cards.b3
        return  rCard
    elif rNum == 22:
        rCard = cards.b4
        return  rCard
    elif rNum == 23:
        rCard = cards.b5
        return  rCard
    elif rNum == 24:
        rCard = cards.b6
        return  rCard
    elif rNum == 25:
        rCard = cards.b7
        return  rCard
    elif rNum == 26:
        rCard = cards.b8
        return  rCard
    elif rNum == 27:
        rCard = cards.b9
        return  rCard
    elif rNum == 28:
        rCard = cards.g1
        return  rCard
    elif rNum == 29:
        rCard = cards.g2
        return  rCard
    elif rNum == 30:
        rCard = cards.g3
        return  rCard
    elif rNum == 31:
        rCard = cards.g4
        return  rCard
    elif rNum == 32:
        rCard = cards.g5
        return  rCard
    elif rNum == 33:
        rCard = cards.g6
        return  rCard
    elif rNum == 34:
        rCard = cards.g7
        return  rCard
    elif rNum == 35:
        rCard = cards.g8
        return  rCard
    elif rNum == 36:
        rCard = cards.g9
        return  rCard
    elif rNum == 37:
        rCard = cards.wc
        return  rCard
    elif rNum == 38:
        rCard = cards.wc2
        return  rCard
    elif rNum == 39:
        rCard = cards.wc4
        return  rCard
    elif rNum == 40:
        rCard = cards.rev
        return  rCard
    elif rNum == 41:
        rCard = cards.skip
        return  rCard

def howManyPlayers():
    numPlayers=1
    while numPlayers <2 or numPlayers > 4:
        numPlayers=int(input(' Select a number of players from 2-4: '))
        if numPlayers <2 or numPlayers > 4:
            print('Try again, choose a number of players between 2 and 4 inclusive')
    return numPlayers
 
def playGame():
    Start=input("Welcome to Uno, would you like to start the game? (y/n)? ")
    return Start
    
    
    
def main():
    start = playGame()
    if start.upper()=='Y':
        numPlayers=howManyPlayers()
    else:
        print('Okay please come back later')
        exit()
        
     

# print(howManyPlayers())
main()
    
    
    
    
# print(genRandomCard())