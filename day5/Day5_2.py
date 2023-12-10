#Re-reading the almanac,it looks like the seeds: line actually describes ranges of seed numbers.
#The values on the initial seeds: line come in pairs.
#Within each pair, the first value is the start of the range and the second value is the length of the range.

#What is the lowest location number
#that corresponds to any of the initial seed numbers?

import re

with open('inputDay5.txt') as file:
    input=file.read().splitlines()

seed_data=[]   
for seed in re.findall(r'\d+', input[0]):
    seed_data.append(int(seed))
    
seed_ranges=[]
for i in range(0,len(seed_data)-1,2):
    start, length = seed_data[i:i+2]
    seed_ranges.append(range(start, start+length))

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


location = 0
while True:
    s=location
    for m in reversed(maps):
        s = next((source_range.start + (s - destination_range.start)
             for source_range, destination_range in m.items()
             if s in destination_range), s)
    possible_seed = s
    if any(possible_seed in rg for rg in seed_ranges):
        print(location)
        break
    location += 1
