import re
with open("day 3 input.txt") as my_file:
    data = my_file.readlines()

def extract_parts(line, line_nbr):
    # regex
    res = []
    hits = re.findall(r'\d+', line)

    for hit in hits:
        if hit == "9":
            print("9!")
        part = dict()
        part["part"] = int(hit)
        part["x"] = list(range(line.index(hit),line.index(hit)+len(hit)))
        part["y"] = line_nbr

        res.append(part)
    
    return res



def extract_symbols(line, line_nbr):
    res = []
    line= line.split("\n")[0]
    for index, char in enumerate(line):
        if char != "." and (ord(char) < 48 or ord(char) >=58 ) and char != "\n":
            res.append({
                "x": index,
                "y" : line_nbr,
                "char": char
            })
    
    return res
    
    


parts = []
symbols = []
for line_nbr, line in enumerate(data):
    for part in extract_parts(line,line_nbr):
        parts.append(part)
    for symbol in extract_symbols(line,line_nbr):
        symbols.append(symbol)



engine_parts_sum = 0
pairs = []
def evaluate_pair(part, symbol):
    x_dist = min([abs(x-symbol["x"]) for x in part["x"]])
    y_dist = abs(symbol["y"]-part["y"])

    if (y_dist == 0 and x_dist == 1) or( y_dist == 1 and x_dist == 0) or (y_dist == 1 and x_dist == 1):
        return True
    else:
        return False
    

used_parts = []

for part in parts:
    for symbol in symbols:
        if evaluate_pair(part, symbol):
            engine_parts_sum = engine_parts_sum + part["part"]
            used_parts.append(part["part"])
            pairs.append({
                    "part": part,
                    "symbol": symbol
            })
            

print(engine_parts_sum)
# print(used_parts)
# print(sum(used_parts))
# print(len(used_parts))