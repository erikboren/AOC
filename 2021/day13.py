with open("day13 sample.txt") as my_file:
    data = my_file.read().splitlines()


points = set()

folds = []

for line in data:
    if len(line) > 0:
        if line[0] == "f":
            folds.append(line.split('fold along ')[1].split("="))
            continue
            
        points.append([int(x) for x in line.split(",")])

print(folds)

def fold(points, loc, dirxy):
    
    if dirxy == "x":
        
    
    for i, point in enumerate(points):
        
        