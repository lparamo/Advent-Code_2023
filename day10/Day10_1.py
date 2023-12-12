#input: sketch of all of the surface pipes you can see
'''The pipes are arranged in a two-dimensional grid of tiles:
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on 
    this tile, but your sketch doesn't show what shape the pipe has.
Every pipe in the main loop connects to its two neighbors 
(including S, which will have exactly two pipes connecting to it,
 and which is assumed to connect back to those two pipes).
 
 Find the single giant loop starting at S.
How many steps along the loop does it take to get from the starting
 position to the point farthest from the starting position?'''

pipes = {
    '|': ((0,-1),(0,1)),  #(0,-1)-(0,1) north-south.
    '-': ((1,0),(-1,0)),  #(1,0)-(-1,0) east-west
    'L': ((0,-1),(1,0)),  #(0,-1)-(1,0) north-east
    'J': ((0,-1),(-1,0)),  #(0,-1)-(-1,0) north-west
    '7': ((0,1),(-1,0)),  #(0,1)-(-1,0) south-west
    'F': ((0,1),(1,0)),  #(0,1)-(1,0) south-east
}

with open('inputDay10.txt') as file:
    input=file.read().splitlines()

for line in input:
    surface = [list(line) for line in input]

start = None
for (y,row) in enumerate(surface): #Search for starting position S
    if 'S' in row:
        start = (row.index('S'), y)
        break

loop = [start]
next = set([(0,-1),(0,1),(1,0),(-1,0)])
tile =''
while True:
    for d in next:
        n = (loop[-1][0]+d[0],loop[-1][1]+d[1])
        #is n off-limits?
        x,y = n[0], n[1]
        if (x < 0) or (x >= len(surface[0])) or (y < 0) or (y >= len(surface)):
            tile='.'
        else:
            tile=surface[y][x]

        if tile == '.':
            continue
        if tile == 'S':
            break

        oppo_d=(d[0]*(-1),d[1]*(-1))
        neighbors=pipes[tile]
        if oppo_d==neighbors[0] or oppo_d==neighbors[1]:
            next = set(neighbors)
            next.remove(oppo_d)
            loop.append(n)
            break

    if tile == 'S': #end the loop
            break
print(len(loop)/2) #we want the farthest position from the starting position (halfway)