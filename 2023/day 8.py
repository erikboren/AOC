from math import gcd

with open("day 8 input.txt") as my_file:
    data = my_file.read().strip()

instructions , rest = data.split("\n\n")

elements = dict()   

for line in rest.split("\n"):
    elements[line.split(" =")[0]] = line.split("= ")[1][1:-1].split(", ")

pos = "AAA"
steps = 0

def find(start,part2=False):
    pos = start
    steps = 0
# part 1
    run = True
    while run:
        instruction = instructions[steps % len(instructions)] 

        if instruction == "L":
            k = 0
        elif instruction == "R":
            k = 1

        pos = elements[pos][k]
        steps = steps +1

        if part2:
            if pos[-1] == "Z":
                run = False
                return(steps)
        elif pos == "ZZZ":
            return steps

print(find("AAA"))

# Part2
steps2 = []

for key , value in elements.items():
    if key[-1] == "A":
        steps2.append(find(key,True))

# https://en.wikipedia.org/wiki/Chinese_remainder_theorem
res = 1
for x in steps2:
    res = (res*x)//gcd(x,res)

print(res)
    


