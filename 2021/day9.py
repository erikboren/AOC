import math

with open("day9 input.txt") as my_file:
    data = my_file.read().splitlines()
    
rows = []

for line in data:
    rows.append([int(x) for x in line])


xmax = len(rows[0])
ymax =len(rows)
res = 0
low_points = []
for y,row in enumerate(rows):
    for x, point in enumerate(row):
        neighbours = []
        for xpos in range(max(0,x-1), min(xmax,x+2)):
            if xpos != x:
                neighbours.append(rows[y][xpos])
        for ypos in range(max(0,y-1), min(ymax,y+2)):
            if ypos != y:
                neighbours.append(rows[ypos][x])
        
        if min(neighbours) > point:
            res += point+1
            low_points.append([y,x])
print(res)


basins = []

def basin(low_point,):
    
    bpoints = set()
    checked = []
    
    que = [low_point]
    bpoints.add(str(low_point[0])+str(low_point[1]))
    while len(que) >0:
        point = que.pop(0)
        
        if point in checked:
            next
        
        y = point[0]
        x = point[1]
        height = rows[y][x]
        
        for xpos in range(max(0,x-1), min(xmax,x+2)):
            if xpos != x and rows[y][xpos] > height and rows[y][xpos] < 9:
                que.append([y,xpos])
                bpoints.add(str(y) + str(xpos))
        for ypos in range(max(0,y-1), min(ymax,y+2)):
            if ypos != y and rows[ypos][x] > height and rows[ypos][x] < 9:
                que.append([ypos,x])
                bpoints.add(str(ypos) + str(x))
        
        checked.append(point)
    
    return len(bpoints)

for low_point in low_points:
    basins.append(basin(low_point))
    
    if len(basins)>3:
        basins.sort(reverse=True)
        basins = basins[0:3]
        
print(math.prod(basins))