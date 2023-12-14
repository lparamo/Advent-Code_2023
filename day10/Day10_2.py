#How many tiles are enclosed by the loop?

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
for y,row in enumerate(surface): #Search for starting position S
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

#part2: we study the different regions that are created
#by the intersections of the loop   
#First we change the startig S for the pipe it really is.
dir1=(loop[-1][0]-loop[0][0],loop[-1][1]-loop[0][1])
dir2=(loop[1][0]-loop[0][0],loop[1][1]-loop[0][1])

if ((dir1,dir2))==pipes['|']or((dir2,dir1))==pipes['|']:
    surface[start[1]][start[0]]='|'
    print('S is',surface[start[1]][start[0]])
elif ((dir1,dir2))==pipes['-']or((dir2,dir1))==pipes['-']:
    surface[start[1]][start[0]]='-'
    print('S is',surface[start[1]][start[0]])
elif ((dir1,dir2))==pipes['L']or((dir2,dir1))==pipes['L']:
    surface[start[1]][start[0]]='L'
    print('S is',surface[start[1]][start[0]])
elif ((dir1,dir2))==pipes['J']or((dir2,dir1))==pipes['J']:
    surface[start[1]][start[0]]='J'
    print('S is',surface[start[1]][start[0]])
elif ((dir1,dir2))==pipes['7']or((dir2,dir1))==pipes['7']:
    surface[start[1]][start[0]]='7'
    print('S is',surface[start[1]][start[0]])
elif ((dir1,dir2))==pipes['F']or((dir2,dir1))==pipes['F']:
    surface[start[1]][start[0]]='F'
    print('S is',surface[start[1]][start[0]])

is_region = False
count=0
last_corner=None
for y,row in enumerate(surface):
    for x, tile in enumerate(row):
        if (x,y) not in loop and is_region:
            count += 1
        elif (x,y) in loop:
            if tile == '|':   
                is_region = not is_region 
            elif tile == '-':
                continue
            if tile=='F'or tile=='L':
                last_corner=tile
            elif tile == "7":
                if last_corner == "L":
                    is_region = not is_region
                last_corner = None
            elif tile == "J":
                if last_corner == "F":
                    is_region = not is_region
                last_corner = None
print(count)