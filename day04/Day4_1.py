#each card has two lists of numbers separated by a vertical bar (|):
#a list of winning numbers and then a list of numbers you have.
#The first match makes the card worth one point and
#each match after the first doubles the point value of that card.
#How many points are they worth in total?
import re
import math

with open('inputDay4.txt') as file:
    input=file.read().splitlines()

total=0   
for line in input:
    n=0
    x = line.find(':')
    list=re.split('  | ', line[x+2:])
    if list[0]=='':
        del list[0]
    i= list.index('|')
    for num in list[i+1:]:
        if num in list[0:i]:
            n+=1
    if n!=0:
        card=2**(n-1)
    else:
        card=0
    total+=card
print(total)
