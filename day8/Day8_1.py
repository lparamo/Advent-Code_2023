#one of the documents contains a list of left/right instructions, and the rest
#of the documents seem to describe some kind of network of labeled nodes.
#You feel like AAA is where you are now,
#and you have to follow the left/right instructions until you reach ZZZ.
#How many steps are required to reach ZZZ?
import re

with open('inputDay8.txt') as file:
    input=file.read().splitlines()

instructions=[] #list of left/right instructions
for step in input[0]:
    instructions.append(step)

network={} #dictionary with the network of labeled nodes.
for nodes in input[2:]:
    node, left, right = nodes[0:3], nodes[7:10], nodes[12:15]
    network[node]=[left,right]


total_steps=0
node='AAA'
while node!='ZZZ':
    s=0
    ins = total_steps % len(instructions)
    instruction=instructions[ins]
    if instruction=='R':
        s=1
    node=network[node][s]
    total_steps+=1
    
print(total_steps)
