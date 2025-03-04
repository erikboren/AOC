with open("day2.txt") as my_file:
    data = my_file.read().splitlines()

lines = []

for line in data:
    lines.append([int(x) for x in line.split(" ")])

def check_line1(line):
    gap = 0
    for i in range(len(line)-1):
        if i == 0:
            gap = line[i+1]-line[i]
            if abs(gap) >3 or abs(gap) < 1:
                return [False,i]
        else:
            new_gap = line[i+1]-line[i]

            if new_gap*gap < 0 or abs(new_gap) >3 or abs(new_gap) == 0:
                return [False,i]
            # This If-statement was a bit tricky. gaps need to be the same sign, abs(new_gap) less then equal to 3 and greater than equal to 1
            
            gap = new_gap
        
    return [True,0]

safe_counter = 0

for line in lines:
    if check_line1(line)[0]:
        safe_counter = safe_counter + 1

print(safe_counter)

def check_line2(line):
    check1_results = check_line1(line)
    if check1_results[0]:
        return check1_results
    i = check1_results[1]
    
    # Try to remove i
    
    for i in range(len(line)):
        sub_line = line[:i] + line[i+1:]
        check1_results = check_line1(sub_line)
        if check1_results[0]:
            return check1_results

    return check1_results          

safe_counter = 0

for line in lines:
     if check_line2(line)[0]:
        safe_counter = safe_counter + 1

print(safe_counter)

check_line1([40, 41, 44, 45,42])