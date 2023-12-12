import re

with open("day 3 input.txt") as my_file:
    data = my_file.read().splitlines()

def find_neighbours(y, x1, x2):
    
    if y >= 0 and y <= len(data)-1:
        xmax = len(data[y])
        return data[y][max(0,x1):min(x2,xmax)]
    else:
        return ""
    
parts = []
for y, line in enumerate(data):
    for hit in re.finditer(r'\d+', line):
        left = hit.start()
        right = hit.end()

        neighbours = find_neighbours(y-1,left-1,right+1) + find_neighbours(y,left-1, left) + \
                    find_neighbours(y, right, right+1) + find_neighbours(y+1, left-1,right+1)
        
        if set(neighbours) != {"."}:
            parts.append(int(hit.group()))
print(sum(parts))

    

