import re

with open("day 3 input.txt") as my_file:
    data = my_file.read().splitlines()
# Part 1

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

def find_parts(y,x):
    def check(y,x):
        parts = []
        for hit in re.finditer(r'\d+', data[y]):
            if abs(hit.start()-x) <= 1 or abs(hit.end()-x-1) <= 1:
                parts.append(int(hit.group()))
        return parts
    
    possible_ys = [-1, 0, 1]
    parts = []
    for possible_y in possible_ys:
        for part in check(y+possible_y,x):
            if part != None:
             parts.append(part)
    assert len(parts) <= 2, f" Lenght is {len(parts)}"
    if len(parts) == 2:
            return parts[0]*parts[1]
    else: 
        return 0



           
parts2 = []

for y, line in enumerate(data):
    
    for hit in re.finditer(r'\*',line):
        x = hit.start()
        parts2.append(find_parts(y,x))

print(sum(parts2))


 