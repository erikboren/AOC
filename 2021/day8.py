with open("day8 input.txt") as my_file:
    data = my_file.read().splitlines()
    
sps = []
ovs = []
for line in data:
    line_sp = line.split(" | ")[0].split(" ")
    sps.append(line_sp)
    
    line_ov = line.split(" | ")[1].split(" ")
    ovs.append(line_ov)
counter = 0
lenghts = [2, 3, 4, 7]
for ov in ovs:
    for pos in ov:
      if len(pos) in lenghts:
          counter += 1
          
print(counter)

# p2

# known numbers

section_scores = {
                "a": 8,
                "b": 6,
                "c": 8,   
                "d": 7,     
                "e": 4,     
                "f": 9,    
                "g": 7,  
                }

digit_scores = {
                1: 17,
                2: 8+8+7+4+7,
                3: 8+8+7+9+7,
                4: 6+8+7+9,
                5: 8+6+7+9+7,
                6: 8+6+7+4+9+7,
                7: 8+8+9,
                8: 8+6+8+7+4+9+7,
                9: 8+6+8+7+9+7,
                0: 8+6+8+4+9+7
                }
scores_digit = dict((v, k) for k, v in digit_scores.items())
print(digit_scores)
ov_sum = 0
for row, spsrow in enumerate(sps):
    all_freq = {}
    for sp in spsrow:
        for char in sp:
            if char in all_freq:
                all_freq[char] +=1
            else: 
                all_freq[char] = 1
    number_string = ""    
    for ov in ovs[row]:
        freq_sum = 0
        
        for char2 in ov:
            freq_sum += all_freq[char2]
        number_string = number_string + str(scores_digit[freq_sum])
        
    ov_sum += int(number_string)
    
print(ov_sum)