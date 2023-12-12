#in each game you played, what is the fewest number of cubes of each color
#that could have been in the bag to make the game possible?
#The power of a set of cubes is equal to
#the numbers of red, green, and blue cubes multiplied together.
#What is the sum of the power of these sets?

import re
with open('inputDay2.txt') as file:
    input=file.read().splitlines()

sum_power=0   
for line in input:
    r=0
    g=0
    b=0
    list=re.split(': |, |; | ',line)
    for i in range(3,len(list),2):
        if list[i]=='red':
            if int(list[i-1])>r:
                r=int(list[i-1])
        elif list[i]=='green':
            if int(list[i-1])>g:
                g=int(list[i-1])
        else:
            if int(list[i-1])>b:
                b=int(list[i-1])
    sum_power+=r*g*b
print(sum_power) 
