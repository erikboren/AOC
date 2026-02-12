with open("day4.txt") as my_file:
    data = my_file.read().splitlines()

def findAll(loc):
    
    directions = [[1,1], [1,0], [1,-1], [-1,-1], [-1,0], [-1,1], [0,1], [0,-1]]

    possible = []
    count = 0
    for dir in directions:
        if loc[0] + dir[0]*3 >=0 and loc[0] + dir[0]*3 <= len(data[0]) - 1  and loc[1] + 3*dir[1] >= 0 and loc[1] + 3*dir[1] <= len(data) -1:
            rem = []
            for i in range(1,4):
                rem.append(data[loc[0] + i * dir[0]][loc[1] + i * dir[1]])
            if rem == ["M","A","S"]:
                count = count + 1
    return count
                
                
   
    
    
count = 0
for y, row in enumerate(data):
    for x, char in enumerate(row):
        if char == "X":
           count = count + (findAll([x,y]))

print(count)

