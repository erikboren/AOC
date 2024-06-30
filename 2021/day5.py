with open("day5 input.txt") as my_file:
    data = my_file.read().splitlines()

p = 2
lines = []

for line in data:
    coords = []
    for point in line.split(" -> "):
        for coord in point.split(","):
            coords.append(int(coord))
    
    if(coords[0] == coords[2]):
        k = "vert"
        m = coords[1] 
    elif(coords[1] == coords[3]):
        k = "hor"
        m = 0
    else:
        k = (coords[0]-coords[2])/(coords[1]-coords[3])
        m = coords[1] - k*coords[0]
        
        
    
    
    coords.append(k)
    coords.append(m)
   
    if p == 2:
        lines.append(coords)
    

def find_inter(line1, line2):
    inter = 0
    if (line2[5] != line1[5]):
        x_inter = (line1[4]-line2[4]) / (line2[5] - line1[5])
        if x_inter >= min(line1[0], line1[2]) and x_inter <= max(line1[0], line1[2]) and  x_inter >= min(line2[0], line2[2]) and x_inter <= max(line2[0], line2[2]):
            return [[x_inter, x_inter*line1[4] + line1[5]]]
    else:   
            res = []
            length =  min(line2[2], line1[2]) - line2[0]
            for i in range(0,length+1):
                x_inter = line2[0] + i
                res.append([x_inter,x_inter*line1[4] + line1[5]])
            
            return res
    
    return []
            

def find_points(line):
    res = []
    if line[4] == "hor":
        for x in range(min(line[0], line[2]), max(line[0], line[2])+1):
            res.append([x, line[1]])
    elif line[4] == "vert":
        for y in range(min(line[1], line[3]), max(line[1], line[3])+1):
            res.append([line[0], y])
    else:
        for x in range(min(line[0], line[2]), max(line[0], line[2])+1):
            res.append([x, int(x*line[4]+line[5])])
    return res
    
inters = {}

for line in lines:
    points = find_points(line)
    
    for point in points:
        string = ",".join(str(e) for e in point)
        if string in inters.keys():
            inters[string] = inters[string] + 1
        else:
            inters[string] = 1
res = 0
for k,v in inters.items():
    if v >= 2:
        res = res+1
# print(inters)
print(res)

    
matrix = []
for x in range(0,10):
    x_row = []
    for y in range(0,10):
        coord = str(y)+","+str(x)
        if coord in inters.keys():
            x_row.append(inters[coord])
        else:
            x_row.append(0)
    matrix.append(x_row)
    print(x_row)
    

        