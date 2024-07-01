with open("day7 input.txt") as my_file:
    data = my_file.read().splitlines()

crabs = []

for line in data:
    for crab in line.split(","):
        crabs.append(int(crab))
        

results1 = []
for pos in range(0,max(crabs)+1):
    res = 0
    for crab in crabs:
        res += abs(crab-pos)
    results1.append(res)
# print(results)
print(min(results1))


results2 = []
minres = 0
for pos in range(0, max(crabs)+1):
    res = 0
    if pos%100 == 0:
        print(pos)
    for crab in crabs:
        if len(results2) > 0 and res > minres:
            next
        
        dist = abs(crab-pos)
        res += sum(range(0,dist+1))
    
    results2.append(res)
    minres = res
print(min(results2))
    
    