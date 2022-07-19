# from xml.etree.ElementInclude import include


# Arr1=['blue', 33]
# Arr2=['Yellow', 3]
# i=0
# x=0

# if Arr1[0] != Arr2[0] and Arr1[1] != Arr2[1]:
#     print('Fuck')
    
#             firstCard=genRandomCard()
            
#             print(p1Name,'You go first the card on the table is',firstCard,'\n','These are your cards', p1Cards)
#             #checks if player one can play
#             while checkCanPlay(p1Cards,firstCard) == False:
#                 print('You do not have a card to play please pick up another')
#                 p1Cards.append(genRandomCard())
#                 print(p1Cards) 
#             #input for the card thaT P1 CHOOSES      
#             cardChosen=int(input('Please choose the proper index of the card you would like to play: '))
#             #checks if player one chose the right card
#             while checkUserChoseWrong(p1Cards[cardChosen],firstCard) == False:
#                 cardChosen=int(input('Please choose the index of another card: '))
    
#             print('The last card played was',p1Cards[cardChosen])
#             while checkCanPlay(p2Cards,firstCard) == False:
#                 #checks if player two can play the game
#                 print('You do not have a card to play please pick up another')
#                 p2Cards.append(genRandomCard())
#                 print(p2Cards) 
#             print(p2Name,'Your cards are', p2Cards)
#             #takes the index of the card that player two wants to play
#             nextCard=int(input('Select the index of the card you would like to play: '))
#             #p1Cards.remove(p1Cards[cardChosen])
#             #saves as variable to use for later
#             p2Played=p2Cards[nextCard]
#             #checks that p2 chose a playable card
#             while checkUserChoseWrong(p2Cards[nextCard],p1Cards[cardChosen]) == False:
#                 nextCard=int(input('Please choose the index of another card: '))
#             #takes the cards that the players chose out of their lists
#             p1Cards.remove(p1Cards[cardChosen])
#             p2Cards.remove(p2Cards[nextCard])
#             # print(p1Cards,'\n',p2Cards)
#             #while loop to do what was done above again and over and over again
#             while (len(p1Cards) != 0 and len(p2Cards) != 0 ):
#                 print(p1Name, 'it is your turn. \n These are your cards\n',p1Cards)
#                 while checkCanPlay(p1Cards,p2Played) == False:
#                     print('You do not have a card to play please pick up another')
#                     p1Cards.append(genRandomCard())
#                 print('These are your cards:', p1Name,'\n',p1Cards)
#                 p1Played= int(input(' Please input the index of the card you would like to play: '))
#                 while checkUserChoseWrong(p1Cards[p1Played],p2Played)== False:
#                     print('These are your cards\n',p1Cards,'\nPlease choose one that mathces the number or color of', p2Played)
#                     p1Played=int(input('Please select the correct index: '))

# def checkCanPlay(Arr1,Arr2):
#     i=0
#     x=0
#     while i<len(Arr1):
#         indList=(Arr1[i])
#     #print(indList)
#         if Arr2[0] == indList[0] or Arr2[1] == indList[1]:
#             x+=1
#         i+=1
#     if x==0:
#         return False
#     else:
#         return True
    
    
# print(checkCanPlay([['red', 2], ['green', 3], ['Yellow', 5], ['blue', 9], ['blue', 6]],['bue',9]))
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
print(genRandomCard())