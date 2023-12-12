'''Start at every node that ends with A and follow all of the paths at the same
time until they all simultaneously end up at nodes that end with Z.

How many steps does it take before you're only on nodes that end with Z?'''

import re
import math

with open('inputDay8.txt') as file:
    input=file.read().splitlines()

instructions=[] #list of left/right instructions
for step in input[0]:
    instructions.append(step)

network={} #dictionary with the network of labeled nodes.
ends_A=[] #list with nodes that end with A
for nodes in input[2:]:
    node, left, right = nodes[0:3], nodes[7:10], nodes[12:15]
    network[node]=[left,right]
    if node[2]=='A':
        ends_A.append(node)

end_list=ends_A
total_steps=[0 for a in ends_A] #list of total steps for each node

def isok(list):
    for t in total_steps:
        if t==0:
            return False
    return True

step=0
while isok(end_list)==False:
    s=0
    ins = step % len(instructions)
    instruction=instructions[ins]
    if instruction=='R':
        s=1
    step+=1
    for n in range(0,len(end_list)):
        end_list[n]=network[end_list[n]][s]
        if end_list[n][2]=='Z' and total_steps[n]==0:
            total_steps[n]=step
            
print(total_steps)
print(math.lcm(*total_steps))
'''We print the LCM of the list of total steps for each node,
that would be the number of steps needed to reach the nodes that
end with Z at same time'''
