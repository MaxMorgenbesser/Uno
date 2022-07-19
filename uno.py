
def genRandomCard():
    import random
    rNum=random.randint(0,9)
    rNum2=random.randint(0,2)
    if rNum2 ==0:
        color='Red'
    if rNum2 ==1:
        color = 'Yellow'
    if rNum2==2:
        color = 'Green'
    return [color,rNum]
    
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
    else:
        return True

def twoPlayer(p1Name,p2Name,p1Cards,p2Cards) :
    p2Played=genRandomCard()
    print(p2Played)
    print(p1Name, 'is First')
    #checks player 1 has a card to play
    while len(p1Cards) !=0 and len(p2Cards) !=0:
        while checkCanPlay(p1Cards,p2Played) == False:
            print('You do not have a card to play please pick up another')
            p1Cards.append(genRandomCard())
        else:
            print('these are',p1Name+'\'s cards\n',p1Cards)
            print('this is the card played',p2Played)
    #takes the index as input for p1s choice
        p1Choice=int(input('Please enter the index of the card you would like to play: \n'))
        while checkUserChoseWrong(p1Cards[p1Choice],p2Played) == False:
            print(p1Cards)
            p1Choice=int(input('Please choose the index of a matching card: '))
        #saving player ones choice for later
        p1Played=p1Cards[p1Choice]
        #removing p1s choice from his deck
        p1Cards.remove(p1Cards[p1Choice])
        #test
        print(p1Played)
        #shows p1 their cards after their turn
        print(p1Name,'These are your cards now,',p1Cards)
        #player 2's turn
        print(p2Name, 'These are your cards',p2Cards)
        while checkCanPlay(p2Cards,p1Played) == False:
            print('You do not have a card to play please pick up another')
            p2Cards.append(genRandomCard())
            
        print('these are',p2Name+'\'s cards\n',p2Cards)
        print('this is the card played',p1Played)
        p2Choice=int(input('Please enter the index of the card you would like to play: \n'))
        while checkUserChoseWrong(p2Cards[p2Choice],p1Played) == False:
            print(p2Cards)
            p2Choice=int(input('Please choose the index of a matching card: '))
        p2Played=p2Cards[p2Choice]
        p2Cards.remove(p2Cards[p2Choice])
        print(p2Name, 'these are your cards now',p2Cards)
    if len(p1Cards)==0:
        print('Congratulations',p1Name,'You Won!')
        exit()
    else:
        print('Congratulations',p2Name,'You Won!')
        exit()   
   
def threePlayer(p1Name,p2Name,p3Name,p1Cards,p2Cards,p3Cards):
    p3Played=genRandomCard()
    print(p3Played)
    print(p1Name, 'is First')
    #checks player 1 has a card to play
    while len(p1Cards) !=0 and len(p2Cards) !=0 and len(p3Cards) != 0:
        while checkCanPlay(p1Cards,p3Played) == False:
            print('You do not have a card to play please pick up another')
            p1Cards.append(genRandomCard())
        else:
            print('these are',p1Name+'\'s cards\n',p1Cards)
            print('this is the card played',p3Played)
    #takes the index as input for p1s choice
        p1Choice=int(input('Please enter the index of the card you would like to play: \n'))
        while checkUserChoseWrong(p1Cards[p1Choice],p3Played) == False:
            print(p1Cards)
            p1Choice=int(input('Please choose the index of a matching card: '))
        #saving player ones choice for later
        p1Played=p1Cards[p1Choice]
        #removing p1s choice from his deck
        p1Cards.remove(p1Cards[p1Choice])
        #test
        #print(p1Played)
        #shows p1 their cards after their turn
        print(p1Name,'These are your cards now,',p1Cards)
        #player 2's turn
        print(p2Name, 'These are your cards',p2Cards)
        while checkCanPlay(p2Cards,p1Played) == False:
            print('You do not have a card to play please pick up another')
            p2Cards.append(genRandomCard())
            
        print('these are',p2Name+'\'s cards\n',p2Cards)
        print('this is the card played',p1Played)
        p2Choice=int(input('Please enter the index of the card you would like to play: \n'))
        while checkUserChoseWrong(p2Cards[p2Choice],p1Played) == False:
            print(p2Cards)
            p2Choice=int(input('Please choose the index of a matching card: '))
        p2Played=p2Cards[p2Choice]
        p2Cards.remove(p2Cards[p2Choice])
        print(p2Name, 'these are your cards now',p2Cards)
        # player threes turn
        print(p3Name, 'These are your cards',p3Cards)
        while checkCanPlay(p3Cards,p2Played) == False:
            print('You do not have a card to play please pick up another')
            p3Cards.append(genRandomCard())
            
        print('these are',p3Name+'\'s cards\n',p3Cards)
        print('this is the card played',p2Played)
        p3Choice=int(input('Please enter the index of the card you would like to play: \n'))
        while checkUserChoseWrong(p3Cards[p3Choice],p2Played) == False:
            print(p3Cards)
            p3Choice=int(input('Please choose the index of a matching card: '))
        p3Played=p3Cards[p3Choice]
        p3Cards.remove(p3Cards[p3Choice])
        print(p3Name, 'these are your cards now',p3Cards)
    if len(p1Cards)==0:
        print('Congratulations',p1Name,'You Won!')
        exit()
    elif len(p2Cards)==0:
        print('Congratulations',p2Name,'You Won!')
        exit()   
    else:
         print('Congratulations',p3Name,'You Won!')
         exit()   

def fourPlayer(p1Name,p2Name,p3Name,p4Name,p1Cards,p2Cards,p3Cards,p4Cards):
    p4Played=genRandomCard()
    #print(p3Played)
    print(p1Name, 'is First')
    #checks player 1 has a card to play
    while len(p1Cards) !=0 and len(p2Cards) !=0 and len(p3Cards) != 0 and len(p4Cards)!=0:
        while checkCanPlay(p1Cards,p4Played) == False:
            print('You do not have a card to play please pick up another')
            p1Cards.append(genRandomCard())
        else:
            print('these are',p1Name+'\'s cards\n',p1Cards)
            print('this is the card played',p4Played)
    #takes the index as input for p1s choice
        p1Choice=int(input('Please enter the index of the card you would like to play: \n'))
        while checkUserChoseWrong(p1Cards[p1Choice],p4Played) == False:
            print(p1Cards)
            p1Choice=int(input('Please choose the index of a matching card: '))
        #saving player ones choice for later
        p1Played=p1Cards[p1Choice]
        #removing p1s choice from his deck
        p1Cards.remove(p1Cards[p1Choice])
        #test
        #print(p1Played)
        #shows p1 their cards after their turn
        print(p1Name,'These are your cards now,',p1Cards)
        #player 2's turn
        print(p2Name, 'These are your cards',p2Cards)
        while checkCanPlay(p2Cards,p1Played) == False:
            print('You do not have a card to play please pick up another')
            p2Cards.append(genRandomCard())
            
        print('these are',p2Name+'\'s cards\n',p2Cards)
        print('this is the card played',p1Played)
        p2Choice=int(input('Please enter the index of the card you would like to play: \n'))
        while checkUserChoseWrong(p2Cards[p2Choice],p1Played) == False:
            print(p2Cards)
            p2Choice=int(input('Please choose the index of a matching card: '))
        p2Played=p2Cards[p2Choice]
        p2Cards.remove(p2Cards[p2Choice])
        print(p2Name, 'these are your cards now',p2Cards)
        # player threes turn
        print(p3Name, 'These are your cards',p3Cards)
        while checkCanPlay(p3Cards,p2Played) == False:
            print('You do not have a card to play please pick up another')
            p3Cards.append(genRandomCard())
            
        print('these are',p3Name+'\'s cards\n',p3Cards)
        print('this is the card played',p2Played)
        p3Choice=int(input('Please enter the index of the card you would like to play: \n'))
        while checkUserChoseWrong(p3Cards[p3Choice],p2Played) == False:
            print(p3Cards)
            p3Choice=int(input('Please choose the index of a matching card: '))
        p3Played=p3Cards[p3Choice]
        p3Cards.remove(p3Cards[p3Choice])
        print(p3Name, 'these are your cards now',p3Cards)
        # player 4's turn
        print(p4Name, 'These are your cards',p4Cards)
        while checkCanPlay(p4Cards,p3Played) == False:
            print('You do not have a card to play please pick up another')
            p4Cards.append(genRandomCard())
            
        print('these are',p4Name+'\'s cards\n',p4Cards)
        print('this is the card played',p3Played)
        p4Choice=int(input('Please enter the index of the card you would like to play: \n'))
        while checkUserChoseWrong(p4Cards[p4Choice],p3Played) == False:
            print(p4Cards)
            p4Choice=int(input('Please choose the index of a matching card: '))
        p4Played=p4Cards[p4Choice]
        p4Cards.remove(p4Cards[p4Choice])
        print(p4Name, 'these are your cards now',p4Cards)
    if len(p1Cards)==0:
        print('Congratulations',p1Name,'You Won!')
        exit()
    elif len(p2Cards)==0:
        print('Congratulations',p2Name,'You Won!')
        exit()   
    elif len(p3Cards==0):
         print('Congratulations',p3Name,'You Won!')
         exit()   
    else:
        print('Congratulations',p4Name,'You Won!')
        exit()  

    
    
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
        if numPlayers == 3:
            p3Name=NamesArr[2]
        if numPlayers == 4:
            p3Name=NamesArr[2]
            p4Name=NamesArr[3]
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
            twoPlayer(p1Name,p2Name,p1Cards,p2Cards)
        elif numPlayers==3:
            threePlayer(p1Name,p2Name,p3Name,p1Cards,p2Cards,p3Cards)
        else:
            fourPlayer(p1Name,p2Name,p3Name,p4Name,p1Cards,p2Cards,p3Cards,p4Cards)
           

                
            

    else:
        print('Okay please come back later')
        exit()

main()






