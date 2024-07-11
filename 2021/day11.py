with open("day11 input.txt") as my_file:
    data = my_file.read().splitlines()

rows1 = []
rows2 = []
for line in data:
    rows1.append([int(x) for x in line])
    rows2.append([int(x) for x in line])

flashes = 0

def step(rows, flashes):
    rows = [ [en +1 for en in row] for row in rows]

    go = True
    while go == True:
        go = False
        for y, row in enumerate(rows):
            for x, en in enumerate(row):
                
                if rows[y][x] > 9:
                    go = True
                    flashes += 1
                    for i in range(max(0,y-1),min(len(row),y+2)):
                        for j in range(max(0,x-1),min(len(row),x+2)):
                            if rows[i][j] <10 and rows[i][j] != 0:
                                rows[i][j] += 1
                   
                    
                    rows[y][x] = 0
                    
    check = set()            
    for y, row in enumerate(rows):
            for x, en in enumerate(row):
             check.add(en)       
    all_flash = False    
    
    if check == set([0]):
        all_flash = True    

    return rows, flashes, all_flash

for x in range(0,1000):
    rows1, flashes, all_flash = step(rows1, flashes)
    if all_flash:
        break

print(flashes)
print(x+1)
print(rows1)

