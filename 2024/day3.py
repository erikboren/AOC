## REGEX mul\([0-9]+\,[0-9]+\)

import re

with open("day3.txt") as my_file:
    data = my_file.read().splitlines()

muls = []

def calculateMul(mul):
    factors = [int(x) for x in mul]
    return factors[0]*factors[1]

sum1 = 0

for line in data:
    mulsfound = [x[3:][1:-1].split(",") for x in re.findall("mul\([0-9]+\,[0-9]+\)",line)]
    for mul in mulsfound:
        sum1 = sum1 + calculateMul(mul)

print(sum1)

sum2 = 0
inputString = ""
for line in data:
    inputString = inputString+line

# starts enabled
enable = True
run = True
while run:
    if enable:
        splitlist = inputString.split("don't()",1)
        section = splitlist[0]
        if len(splitlist) == 2:
            inputString = splitlist[1]
        else:
            run = False
        enable = False
        mulsfound = [x[3:][1:-1].split(",") for x in re.findall("mul\([0-9]+\,[0-9]+\)",section)]
    for mul in mulsfound:
        sum2 = sum2 + calculateMul(mul)
    else:
        splitlist = inputString.split("do()",1)
        section = splitlist[0]
        if len(splitlist) == 2:
            inputString = splitlist[1]
        else:
            run = False
        enable = True

print(sum2)





