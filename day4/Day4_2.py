#There's no such thing as "points".
#Instead, you win more scratchcards equal to the number of winning numbers you have.
#Specifically, you win copies of the scratchcards below the winning card equal to the number of matches.
#So, if card 10 were to have 5 matching numbers, you would win one copy each of cards 11, 12, 13, 14, and 15.
#How many total scratchcards do you end up with?
import re
import math

with open('inputDay4.txt') as file:
    input=file.read().splitlines()

sum=0
card=0
scratchcards={}
for c in range(1,len(input)+1):
    scratchcards[c]=1

for line in input:
    n=0
    card+=1
    x = line.find(':')
    list=re.split('  | ', line[x+2:])
    if list[0]=='':
        del list[0]
    i= list.index('|')
    for num in list[i+1:]:
        if num in list[0:i]:
            n+=1
    for m in range(1,n+1):
        scratchcards[card+m]+=scratchcards[card]
    sum+=scratchcards[card]
    
print(sum)

        
