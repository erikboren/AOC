from functools import reduce
with open("day 6 input.txt") as my_file:
    data = my_file.read().splitlines()

times = data[0].split(":")[1].split()
times = [int(x) for x in times]

dists = data[1].split(":")[1].split()
dists = [int(x) for x in dists]


def findways(time,dist):
    maxtime = time/2 + pow(pow(time/2,2)-dist, 1/2)
    if maxtime % 1 == 0:
        maxtime = maxtime -1
    else:
        maxtime = maxtime - maxtime % 1
    
    mintime = time/2 - pow(pow(time/2,2)-dist, 1/2)

    if mintime % 1 != 0:
        mintime = 1 + mintime - mintime % 1
    else: mintime = mintime + 1 

    return int(maxtime-mintime +1) 

res = []
for i, time in enumerate(times):
    res.append(findways(time,dists[i]))

ansp1 = reduce(lambda x, y: x*y, res)
print(int(ansp1))

#part2
p2time = ""
p2dist = ""
for time in times:
    p2time = p2time + str(time)
for dist in dists:
    p2dist = p2dist + str(dist)


print(findways(int(p2time), int(p2dist)))