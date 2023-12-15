with open("day 5 input.txt") as my_file:
    data = my_file.read().splitlines()


seeds = []
maps = []
   
#parsing input into seeds and maps   
for i, line in enumerate(data):
    if line.split(":")[0] == "seeds":
        seeds_list = line.split(": ")[1].split()
        for seed in seeds_list:
            seeds.append([int(seed)])
    
    if "map:" in line.split():
        map_name = line.split("map")[0]
        current_map = {
            "name": map_name,
            "dsrs": []
        }
        maps.append(current_map)
        for map_line_str in data[i+1:]:
            if map_line_str == "":
                break
            
            dsr = [int(x) for x in map_line_str.split() ]

            current_map["dsrs"].append(dsr) 

def use_map(seed_loc, maap):
    for dsr in maap["dsrs"]:
        if seed_loc <= dsr[1]+dsr[2] and seed_loc >= dsr[1]: 
            return seed_loc - dsr[1] + dsr[0 ]
    return seed_loc

for current_map in maps:
    for seed in seeds:
        seed.append(use_map(seed[-1], current_map))

print(min([(seed[-1]) for seed in seeds]))
seeds_list = [x[0] for x in seeds]


# part2
def calculate_range(R, maap):
    A = []

    for dsr in maap["dsrs"]:
        dest, src, sz = dsr
        src_end = src + sz
        dest_end = dest + sz
        new_range = []
        
        while R:
            hit = False 
            (start, end) = R.pop()

            before = (start, min(end, src))
            inter = (max(start,src), min(src_end, end))
            after = (max(src_end, start), end)

            if before[1]>before[0]:
                new_range.append(before)
                
            if inter[1] > inter[0]:
                A.append((inter[0]-src+dest, inter[1]-src+dest))
                
            if after[1] > after[0]:
                new_range.append(after)
                
            assert len(A)+len(new_range) > 0

        R = new_range
    assert len(A+R) >0
    return A+R

part2 = []
pairs = list(zip(seeds_list[::2], seeds_list[1::2]))
# for st, sz in pairs:
#     seed_range = [(st,sz+st)]
#     for maap in maps:
#         seed_range = calculate_range(seed_range,maap)
    
#     part2.append(min(seed_range[0]))

for st, sz in pairs:
    R = [(st, sz+st)]
    for maap in maps:
        R = calculate_range(R,maap)
        # print(R)
    part2.append(min(R)[0])



print(min(part2))





