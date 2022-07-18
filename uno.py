
def genRandomCard():
    class cards:
        y1 = ['Yellow', 1]
        y2 = ['Yellow', 2]
        y3 = ['Yellow', 3]
        y4 = ['Yellow', 4]
        y5 = ['Yellow', 5]
        y6 = ['Yellow', 6]
        y7 = ['Yellow', 7]
        y8 = ['Yellow', 8]
        y9 = ['Yellow', 9]
        r1 = ['red', 1]
        r2 = ['red', 2]
        r3 = ['red', 3]
        r4 = ['red', 4]
        r5 = ['red', 5]
        r6 = ['red', 6]
        r7 = ['red', 7]
        r8 = ['red', 8]
        r9 = ['red', 9]
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
        # wc = ['Choose Color']
        # wc4 = ['Choose Color', 'Take four']
        # wc2 = ['Choose Color', 'Take 2']
        # rev = ['reverse order']
        # skip = ['Skip next player']
    import random
    rNum = random.randint(0, 36)
    if rNum == 0:
        rCard = cards.y1
        return rCard
    elif rNum == 1:
        rCard = cards.y2
        return rCard
    elif rNum == 2:
        rCard = cards.y3
        return rCard
    elif rNum == 3:
        rCard = cards.y4
        return rCard
    elif rNum == 4:
        rCard = cards.y5
        return rCard
    elif rNum == 5:
        rCard = cards.y6
        return rCard
    elif rNum == 6:
        rCard = cards.y7
        return rCard
    elif rNum == 7:
        rCard = cards.y8
        return rCard
    elif rNum == 8:
        rCard = cards.y9
        return rCard
    elif rNum == 9:
        rCard = cards.r1
        return rCard
    elif rNum == 10:
        rCard = cards.r2
        return rCard
    elif rNum == 11:
        rCard = cards.r3
        return rCard
    elif rNum == 12:
        rCard = cards.r4
        return rCard
    elif rNum == 13:
        rCard = cards.r5
        return rCard
    elif rNum == 14:
        rCard = cards.r5
        return rCard
    elif rNum == 15:
        rCard = cards.r6
        return rCard
    elif rNum == 16:
        rCard = cards.r7
        return rCard
    elif rNum == 17:
        rCard = cards.r8
        return rCard
    elif rNum == 18:
        rCard = cards.r9
        return rCard
    elif rNum == 19:
        rCard = cards.b1
        return rCard
    elif rNum == 20:
        rCard = cards.b2
        return rCard
    elif rNum == 21:
        rCard = cards.b3
        return rCard
    elif rNum == 22:
        rCard = cards.b4
        return rCard
    elif rNum == 23:
        rCard = cards.b5
        return rCard
    elif rNum == 24:
        rCard = cards.b6
        return rCard
    elif rNum == 25:
        rCard = cards.b7
        return rCard
    elif rNum == 26:
        rCard = cards.b8
        return rCard
    elif rNum == 27:
        rCard = cards.b9
        return rCard
    elif rNum == 28:
        rCard = cards.g1
        return rCard
    elif rNum == 29:
        rCard = cards.g2
        return rCard
    elif rNum == 30:
        rCard = cards.g3
        return rCard
    elif rNum == 31:
        rCard = cards.g4
        return rCard
    elif rNum == 32:
        rCard = cards.g5
        return rCard
    elif rNum == 33:
        rCard = cards.g6
        return rCard
    elif rNum == 34:
        rCard = cards.g7
        return rCard
    elif rNum == 35:
        rCard = cards.g8
        return rCard
    elif rNum == 36:
        rCard = cards.g9
        return rCard
    elif rNum == 37:
        rCard = cards.wc
        return rCard
    elif rNum == 38:
        rCard = cards.wc2
        return rCard
    elif rNum == 39:
        rCard = cards.wc4
        return rCard
    elif rNum == 40:
        rCard = cards.rev
        return rCard
    elif rNum == 41:
        rCard = cards.skip
        return rCard


def checkUserChoseWrong(Arr1,Arr2):
    if Arr1[0] != Arr2[0] and Arr1[1] != Arr2[1]:
        return False
    
def checkCanPlay(Arr1,Arr2):
    i=0
    x=0
    while i<len(Arr1):
        indList=(Arr1[i])
    #print(indList)
        if Arr2[0] == indList[0] or Arr2[1] == indList[1]:
            x+=1
        i+=1
    if x==0:
        return False
    
    
    
def howManyPlayers():
    numPlayers = 1
    while numPlayers < 2 or numPlayers > 4:
        numPlayers = int(input(' Select a number of players from 2-4: '))
        if numPlayers < 2 or numPlayers > 4:
            print('Try again, choose a number of players between 2 and 4 inclusive')
    return numPlayers


def playGame():

    Start = input("Welcome to Uno, would you like to start the game? (y/n)? ")
    return Start


def getNames(numPlayers):
    nameList = []
    p1Name = input("Please enter the name of player 1: ")
    p2Name = input("Please enter the name of player 2: ")
    nameList.append(p1Name)
    nameList.append(p2Name)
    if numPlayers == 3:
        p3Name = input('Please enter the name of player 3: ')
        nameList.append(p3Name)
    if numPlayers == 4:
        p3Name = input('Please enter the name of player 3: ')
        p4Name = input('Please enter the name of player 4: ')
        nameList.append(p3Name)
        nameList.append(p4Name)
    return nameList
# print(getNames(2))



def main():
    p1Cards=[]
    p2Cards=[]
    p3Cards=[]
    p4Cards=[]
    start = playGame()
    if start.upper() == 'Y':
        numPlayers = howManyPlayers()
        NamesArr = getNames(numPlayers)
        p1Name = NamesArr[0]
        p2Name = NamesArr[1]
        for x in range(5):
            p1Cards.append(genRandomCard())
            p2Cards.append(genRandomCard())
        if numPlayers == 3:
            p3Name = NamesArr[2]
            for x in range(5):
                p3Cards.append(genRandomCard())
        if numPlayers == 4:
            p3Name = NamesArr[2]
            p4Name = NamesArr[3]
            for x in range(5):
                p3Cards.append(genRandomCard())
                p4Cards.append(genRandomCard())
        if numPlayers==2:
           
            firstCard=genRandomCard()
            print(p1Name,'You go first the card on the table is',firstCard,'\n','These are your cards', p1Cards)
            while checkCanPlay(p1Cards,firstCard) == False:
                print('You do not have a card to play please pick up another')
                p1Cards.append(genRandomCard())
            print(p1Cards)  
            cardChosen=int(input('Please choose the proper index of the card you would like to play: '))
            while checkUserChoseWrong(p1Cards[cardChosen],firstCard) == False:
                cardChosen=int(input('Please choose the index of another card: '))
            print( p2Name,'these are your cards', p2Cards)
            print('The last card played was',p1Cards[cardChosen])
            print('Your cards are', p2Cards)
            nextCard=int(input('Select the index of the card you would like to play: '))
            #p1Cards.remove(p1Cards[cardChosen])
           
            while checkUserChoseWrong(p2Cards[nextCard],p1Cards[cardChosen]) == False:
                nextCard=int(input('Please choose the index of another card: '))
            p1Cards.remove(p1Cards[cardChosen])
            p2Cards.remove(p2Cards[nextCard])
            print(p1Cards,'\n',p2Cards)
           # while (len(p1Cards) != 0 or len(p2Cards) != 0 ):
                
            

    else:
        print('Okay please come back later')
        exit()


# print(howManyPlayers())
main()


# print(genRandomCard())
