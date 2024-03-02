import math

with open("day3 input.txt") as my_file:
    data = my_file.read().splitlines()

length = len(data)

print(length)

rlength = len(data[0])

print(rlength)

most_common = []

sums = []


for line in data:
    for i in range(0,rlength):
        if len(sums) < i+1:
            sums.append(int(line[i]))
        else:
            sums[i] = sums[i] + int(line[i])

print(sums)

gamma =0 
epsilon =0
epsilons = []
for i,summ in enumerate(sums):
    if summ > length/2:
        epsilon = epsilon + math.pow(2,rlength-i-1)
        epsilons.append(1)
    else:
        gamma = gamma + math.pow(2,rlength-i-1)
        epsilons.append(0)
        

print(gamma*epsilon)
print(epsilons)

indexes = []

def scrub1(data, index=0):
    if index == rlength:
        return data[0]
    
    new_data = []
    summ = 0
    for line in data:
        summ = summ + int(line[index])
    
    if summ >= len(data)/2:
        for line in data:
            if line[index] == "1":
                new_data.append(line)
    else:
        for line in data:
            if line[index] == "0":
                new_data.append(line)
    index = index+1
    
    return scrub1(new_data,index)

print(scrub1(data))

def scrub2(data, index=0):
    if index == rlength or len(data) == 1:
        return data[0]
    
    new_data = []
    summ = 0
    for line in data:
        summ = summ + int(line[index])
    
    if summ >= len(data)/2:
        for line in data:
            if line[index] == "0":
                new_data.append(line)
    else:
        for line in data:
            if line[index] == "1":
                new_data.append(line)
    index = index+1
    


    return scrub2(new_data,index)

scrubs = [scrub1(data),scrub2(data)]

print(scrubs)

scrubs_dec = []

for scrub in scrubs:
    dec = 0
    for i,v in enumerate(scrub):
        dec = dec + int(v)*math.pow(2,len(scrub)-i-1)
    scrubs_dec.append(dec)

print(scrubs_dec[0]*scrubs_dec[1])