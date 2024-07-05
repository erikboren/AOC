with open("day10 input.txt") as my_file:
    data = my_file.read().splitlines()
    
chars =["(", ")", "{", "}", "<", ">", "[", "]"]    
cres = []  
ires = []

cpoints = {")": 3,
          "]": 57,
          "}": 1197,
          ">": 25137}


ipoints = {")": 1,
          "]": 2,
          "}": 3,
          ">": 4}

for line in data:
    count = {}
    
    missing = ""
    corrupt = ""  
    open_chunks = ""
    last_open_chunk = ""
    counter = {}
    for char in chars:
        counter[char]  = 0
    
    for i, char in enumerate(line):
        index = chars.index(char)
        counter[char] += 1
        if index%2 == 0:
            open_chunks += char
            last_open_chunk = char
        else: 
            if last_open_chunk == chars[index-1]:
                pass
            else:
                # corrupt
                corrupt = char
                missing = chars[chars.index(last_open_chunk)+1]
                cres.append(corrupt)
            
            
            open_chunks = open_chunks[:len(open_chunks)-1]
            
            last_open_chunk = open_chunks[-1] if len(open_chunks) >0 else ""
            
    if corrupt == "":
        ires_line = 0
        for chunk in open_chunks[::-1]:
            ires_line = ires_line*5 + ipoints[chars[chars.index(chunk)+1]]
        
        ires.append(ires_line)
                    
ires.sort()

index = int(len(ires)/2 - 0.5)


p1 = sum([cpoints[x] for x in cres])

print(p1)
print(ires)
print(len(ires))
print(ires[index])