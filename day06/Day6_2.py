#There's really only one race -
#ignore the spaces between the numbers on each line.

#Now, you have to figure out how many ways there are to win this single race.

import re


with open('inputDay6.txt') as file:
    input=file.read().splitlines()

time_list=re.findall(r'\d+', input[0])
time=''
for t in time_list:
    time+=str(t)
time=int(time)

record_list=re.findall(r'\d+', input[1])
record=''
for r in record_list:
    record+=str(r)
record=int(record)


ways=0 #counting the number of ways to beat the record in each race
for t in range(0,time+1): #t: milliseconds holding the button(=speed)
    tot_dist=(time-t)*t
    if tot_dist>record:
        ways+=1
        
print(ways)

        
