import re

def hand_type(hand): 
    dif=0
    jokers=0
    for i in range(0,4):
        for j in range(i+1,5):
            if hand[i]!=hand[j]:
                dif+=1
        if hand[i]=='J':
            jokers+=1
    if hand[4]=='J':
        jokers+=1

    if dif==0:
        return 6 #6: five of  kind
    elif dif==4:
        if jokers<=1:
            return (5+jokers) #5: four of  kind
        if jokers==4:
            return 6
    elif dif==6:
        if jokers<=2:
            return (4+jokers)  #4: full house
        if jokers==3:
            return 6
    elif dif==7:
        if jokers==0:
            return 3 #3: three of  kind
        if jokers>0:
            return 5
    elif dif==8:
        if jokers==0:
            return 2 #2: two pair
        if jokers>=1:
            return (3+jokers)
    elif dif==9:
        if jokers==0:
            return 1  #1: one pair
        if jokers>0:
            return 3
    elif dif==10:
        return (0+jokers) #0: high card

def code_hand_cards(hand):
    strength_order = 'J23456789TQKA'
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