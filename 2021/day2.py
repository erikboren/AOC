with open("day2 input.txt") as my_file:
    data = my_file.read().splitlines()


pos = [0,0]

directions = {"forward": [0,1],
              "down": [1,0],
              "up": [-1,0]}


for line in data:
    direction, amp  = line.split(" ")
    direction = directions[direction]
    amp = int(amp)
    pos = [pos[0]+amp*direction[0], pos[1]+direction[1]*amp]

print(pos[0]*pos[1])

aim = 0
pos = [0,0]


for line in data:
    direction, amp  = line.split(" ")
    amp =int(amp)
    if direction == "up":
        aim = aim - amp
    elif direction == "down":
        aim = aim + amp
    elif direction == "forward":
        pos[0] = pos[0] + aim*amp
        pos[1] = pos[1] + amp

print(pos[0]*pos[1])