with open("day1.txt") as my_file:
    data = my_file.read().splitlines()

left = []
right = []

for line in data:
    l, r = [int (x) for x in line.split("   ")]

    left.append(l)
    right.append(r)


left.sort()
right.sort()

dists = []

for i in range(len(left)):
    dists.append(abs(left[i]-right[i]))

print(sum(dists))

## Part 2

sim = []

for l in left:
    sims = 0
    for r in right:
        if r > l:
            break
        if r == l:
            sims = sims +1
    sim.append(sims*l)

print(sum(sim))