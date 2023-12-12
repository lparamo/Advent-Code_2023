#The almanac (your puzzle input) lists all of the seeds that need to be planted.
#It also lists what type of soil to use with each kind of seed,
#what type of fertilizer to use with each kind of soil,
#what type of water to use with each kind of fertilizer, and so on.
#Rather than list every source number and its corresponding destination number one by one,
#the maps describe entire ranges of numbers that can be converted.
#Each line within a map contains three numbers: the destination range start,
#the source range start, and the range length.
#Any source numbers that aren't mapped correspond to the same destination number.

#Using these maps, find the lowest location number that corresponds to any of the initial seeds.
import re

with open('inputDay5.txt') as file:
    input=file.read().splitlines()

seeds=[]   
for seed in re.findall(r'\d+', input[0]):
    seeds.append(int(seed))

n=-1
maps=[]

for line in input[2:]:
    if line.find('map')!=-1:
        n+=1
        maps.append(dict())
    elif len(line)!=0:
        m=re.split(' ',line)
        destination=int(m[0])
        source=int(m[1])
        r=int(m[2])
        maps[n][range(source, source+r)] = range(destination, destination+r)

loc=[]
for s in seeds:
    for m in maps:
        s = next((destination_range.start + (s - source_range.start)
             for source_range, destination_range in m.items()
             if s in source_range),s)
    loc.append(s)
    
print(min(loc))
