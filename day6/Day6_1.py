#you get a sheet of paper that lists the time allowed for each race and also
#the best distance ever recorded in that race. To guarantee you win the grand prize,
#you need to make sure you go farther in each race than the current record holder.

#Your toy boat has a starting speed of zero millimeters per millisecond.
#For each whole millisecond you spend at the beginning of the race holding down the button,
#the boat's speed increases by one millimeter per millisecond.

#Determine the number of ways you could beat the record in each race.
#What do you get if you multiply these numbers together?

import re
import math

with open('inputDay6.txt') as file:
    input=file.read().splitlines()

time=[]   
for t in re.findall(r'\d+', input[0]):
    time.append(int(t))

record=[]   
for r in re.findall(r'\d+', input[1]):
    record.append(int(r))

ways=[] #list with the number of ways to beat the record in each race
for race in range(0,len(time)):
    n=0 #counting the number of ways to beat the record in each race
    for t in range(0,time[race]+1): #t: milliseconds holding the button(=speed)
        tot_dist=(time[race]-t)*t
        if tot_dist>record[race]:
            n+=1
    ways.append(n)

print(ways)
print(math.prod(ways))
        
        
