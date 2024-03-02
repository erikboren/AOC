
with open("day1 input.txt") as my_file:
    data = my_file.readlines()

counter = -1
last_depth = 0

for i,line in enumerate(data):
    data[i] = int(line)

for line  in data:
    if int(line) > last_depth:
        counter = counter + 1
    last_depth = int(line)

print(counter)

last = 0
counter = -1
for i,line  in enumerate(data[:-2]):
    current = sum(data[i:i+3])
    if current > last:
        counter = counter + 1
    last = current

print(counter)
