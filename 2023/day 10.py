with open("day 10 example2.txt") as my_file:
    grid = my_file.read().splitlines()


# find "S"
def findStart(grid):
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "S":
                return (y,x)

start = findStart(grid)              

def gridSymbol(grid,pos):
    return grid[pos[0]][pos[1]]

def checkValid(pos1, pos2):
    pos2sym = gridSymbol(grid, pos2)
    if pos2sym == ".":
        return False
    if abs(pos1[0]-pos2[0]) == 1 and abs(pos1[1]-pos2[1]) == 1:
        return False
    pos1sym = gridSymbol(grid, pos1)
    
    
    # new-current
    #above --> below, left --> right, every one can connect with everything except for themselves (except for - and |) length is always 6
    
    #  |, -, F, 7, J, L
    relative_positon = tuple(map(lambda i, j: i - j, pos1, pos2))
    moves_allowed= {
        "|" : [ ["|", (-1, 0)], ["|", (1, 0)], ["F", (1, 0)], ["7", (1, 0)], ["J", (-1, 0)], ["L", (-1, 0)]], 
        "-" : [["-", (0, 1)], ["-", (0, -1)], ["F",( 0, 1)], ["7", (0, -1)], ["J", (0, -1)], ["L", (0, 1)]],
        "F" : [["|", (-1, 0)], ["-", (0,-1)], ["7", (0, -1)], ["J", (0, -1)], ["J", (-1, 0)], ["L", (-1, 0)]],
        "7" : [["|", (-1, 0)], ["-", (0, 1)], ["F", (0, 1)], ["J", (-1, 0)], ["L", (-1, 0)], ["L", (0, 1)]],
        "J" : [["|", (1, 0)], ["-", (0, 1)], ["F", (1, 0)], ["F", (0, 1)], ["7", (1, 0)], ["L", (0, 1)]],
        "L" : [[ "|", (1, 0)], ["-", (0, -1)], ["F", (1, 0)], ["7", (1, 0)], ["7", (0, -1)], ["J", (0, -1)]],
        "S" : [[ "|", (1, 0)], [ "|", (-1, 0)], ["-", (0, 1)], ["-", (0, -1)], ["F", (0, 1)], ["F", (1, 0)], ["7", (1, 0)], ["7", (0, -1)], ["J", (0, -1)], ["J", (-1, 0)], ["L", (0, 1)],["L", (-1, 0)]]
        
    }
    if pos2sym != "S":
        moves_allowed = [x[1]  for x in moves_allowed[pos1sym] if x[0] == pos2sym and x[1] == relative_positon]
        
    else:
        moves_allowed = [x[1]  for x in moves_allowed[pos1sym] if x[1] == relative_positon]

    return relative_positon in moves_allowed

def getAdjacent(pos,grid):
    ys = [max(pos[0]-1,0), pos[0], min(pos[0]+1,len(grid)-1)]
    xs = [max(pos[1]-1,0), pos[1], min(pos[1]+1, len(grid[pos[1]])-1)]

    ys = set(ys)
    xs = set(xs)

    adjacent = []
    for x in xs:
        for y in ys:
            if (y,x) != pos and checkValid(pos,(y,x)):
                adjacent.append([(y, x), grid[y][x] ])
    
    assert len(adjacent) >= 2
    return adjacent


def nextMove(pos, grid, visited):

    adjacents = getAdjacent(pos,grid)

    nextMove = None

    for adjacent in adjacents:
        if adjacent[0] not in visited:
            pos = adjacent[0]
            visited.append(pos)
            return pos, visited
    adjacentTuples = [x[0] for x in adjacents]
    
    if start in adjacentTuples:
        pos = start
        visited.append(pos)
        return pos, visited

    assert False 
def solvep1(start,grid):
    pos = start

    visited = []
    visited.append(pos)

    pos, visited = nextMove(pos, grid, visited)

    while pos != start:
        pos, visited = nextMove(pos, grid, visited)

    return visited


visited = solvep1(start,grid)
p1 = int((len(visited)-1)/2)

print(p1)


