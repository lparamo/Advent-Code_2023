#Determine which games would have been possible
#if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes.
#What is the sum of the IDs of those games?

def ispossible(list):
    for i in range(3,len(list),2):
        if list[i]=='red':
            if int(list[i-1])>12:
                return False
        elif list[i]=='green':
            if int(list[i-1])>13:
                return False
        else:
            if int(list[i-1])>14:
                return False
    return True

import re
with open('inputDay2.txt') as file:
    input=file.read().splitlines()

sum_ids=0   
game=0
for line in input:
    game+=1
    list=re.split(': |, |; | ',line)
    if ispossible(list):
        sum_ids+=game
print(sum_ids)        
    
    
