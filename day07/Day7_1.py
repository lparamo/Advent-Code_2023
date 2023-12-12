#To play Camel Cards, you are given a list of hands and their corresponding bid.
#Each hand wins an amount equal to its bid multiplied by its rank,
#where the weakest hand gets rank 1,
#the second-weakest hand gets rank 2,
#and so on up to the strongest hand.

#Find the rank of every hand in your set. What are the total winnings?

import re

def hand_type(hand): 
    dif=0
    for i in range(0,4):
        for j in range(i+1,5):
            if hand[i]!=hand[j]:
                dif+=1
    if dif==0:
        return 6 #6: five of  kind
    elif dif==4:
        return 5 #5: four of  kind
    elif dif==6:
        return 4 #4: full house
    elif dif==7:
        return 3 #3: three of  kind
    elif dif==8:
        return 2 #2: two pair
    elif dif==9:
        return 1 #1: one pair
    elif dif==10:
        return 0 #0: high card

def code_hand_cards(hand):
    strength_order = '23456789TJQKA'
    code=[]
    for card in hand:
        code.append(strength_order.index(card))
    return code

with open('inputDay7.txt') as file:
    input=file.read().splitlines()
    
hands=[]
for line in input:
    hand,bid=line.split(' ')
    hand_data=(hand_type(hand),code_hand_cards(hand),int(bid))
    hands.append(hand_data)

hands.sort()

total=0
for h in range (1,len(hands)+1):
    total+=h*hands[h-1][2]
print(total)
    
    

    
    
