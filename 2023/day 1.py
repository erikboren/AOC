# part 1

with open("day 1 part 1 input.txt") as my_file:
    data = my_file.readlines()

res = list()
for line in data:
    nbrs = list()
    for  char in line:
        try:
            nbrs.append(int(char))
        except:
            pass
    
    res.append(10*nbrs[0] + nbrs[-1])


sum = 0

for nbr in res:
    sum = sum + nbr

print(f"Part 1: {sum}")

# part 2

def find_nbr_alpha(sub_line,nbr_alpha,alpha_index):
    # This function is too complicated. Would have been sufficient just to replace all nbr_alpha with numbers instead and re use part 1
    # dumb
    try:
        res = []
        count = line.count(nbr_alpha)
        if count >1:
            pass
        while count > 0:
            line_index = sub_line.index(nbr_alpha)
            if len(res) >0:
                res.append ((alpha_index+1,line_index+res[-1][1]+len(nbr_alpha), "alpha"))
            else:
                res.append ((alpha_index+1,line_index, "alpha"))
            sub_line = sub_line[line_index+len(nbr_alpha):]
            count = count -1
        return res
    except:
        pass
       

def find_numbers(line):
    nbrs = list()
    nbrs_alpha = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for alpha_index, nbr_alpha in enumerate(nbrs_alpha):
        items = find_nbr_alpha(line, nbr_alpha, alpha_index)
        if items != None:
            for item in items:
                nbrs.append(item)
    
    index = 0
    for index, char in enumerate(line):
        if ord(char) <= 57 and ord(char) >=48:
            nbrs.append((int(char), index, "num"))
    first_index = len(line)
    last_index = -1

    first_nbr = None
    last_nbr = None

    for nbr_tup in nbrs:
        if nbr_tup[1] <= first_index:
            first_index = nbr_tup[1]
            first_nbr = nbr_tup[0]
        
        if nbr_tup[1] >= last_index:
            last_index = nbr_tup[1]
            last_nbr = nbr_tup[0]

    
    res = first_nbr*10 + last_nbr
    return res



sum2 = 0
results = list()
for line in data:
    to_add = find_numbers(line)
    sum2 = sum2 + to_add
    results.append([line,to_add])

print(f"Part 2: {sum2}")

