with open("day6 input.txt") as my_file:
    data = my_file.read().splitlines()


init_fish = [0,0,0,0,0,0,0,0,0]
for line in data:
    for k in line.split(","):
        init_fish[int(k)] += 1
    
print(init_fish)
days = []
days.append(init_fish)
        

def pass_day(day):
    next_day = [0,0,0,0,0,0,0,0,0]
    
    for i, nbr in enumerate(day):
        if i == 0:
            next_day[6] += nbr
            next_day[8] += nbr
        else: 
            next_day[i-1] += nbr
    
    return next_day

for i in range(1,257):
    days.append(pass_day(days[-1]))
    print(str(i) + " days: " + str(days[-1]))
    
print(sum(days[-1]))