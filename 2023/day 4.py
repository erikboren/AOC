with open("day 4 input.txt") as my_file:
    data = my_file.read().splitlines()

def score(nbr):
    if nbr > 0:
        return pow(2,nbr-1)
    else:
        return 0

def parse(line):
    line = line.split(":")[1]
    winners, numbers = line.split(" | ")
    winners = set(winners.split())
    numbers = set(numbers.split())
    res = len(winners) + len(numbers) -  len(winners | numbers)
    if res != None:
        return res
    else:
        return 0
    
sump1 = []
matches = []
for line in data:
    sump1.append(score(parse(line)))
    matches.append(parse(line))
print(sum(sump1))

# part 2
cards = [1] * len(data)
for i, score in enumerate(matches):
    for k in range(1,score+1):
        cards[i+k] = cards[i+k] + cards[i]

print(sum(cards))
