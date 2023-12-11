import re
with open("day 2 input.txt") as my_file:
    data = my_file.readlines()

cubes = {
    'red' : 12,
    'green': 13,
    'blue': 14
}
# red, green, blue

def parse_line(line):
    colors = ["red", "green", "blue"]
    game_id = line.split(":")[0].split("Game ")[1]
    line = line.split(": ")[1].split("\n")[0]
    sub_sets = line.split("; ")
    game = dict()
    game["id"] = int(game_id)
    game["sets"] = list()
    for sub_set in sub_sets:
        nbrs= dict()
        

        for color in colors:
            if len(re.findall(r'\d+ ' + color, sub_set)) > 0:
                nbrs[color] = int(re.findall(r'\d+ ' + color, sub_set)[0].split(" " + color)[0])
                   

        game["sets"].append(nbrs)
        # for color in colors:
        #     # print(color)
    
    return game

def impossible_game(game, cubes, colors):
    for sub_set in game["sets"]:
        for color in colors:
            if color in sub_set.keys():
                if sub_set[color] > cubes[color]:
                    return 0
    
    return game["id"]


# Part 2


def game_power(game,colors):
    cubes = dict()
    for color in colors:
        cubes[color] =[]

    for sub_set in game["sets"]:
        for color in cubes.keys():
            if color in sub_set.keys():
                cubes[color].append(sub_set[color])
    
    power = 1
    for color in colors:
        if color in cubes.keys():
            power = power*max(cubes[color])
    
    return power

sum = 0
power_sum = 0
for line in data:
    game = parse_line(line)
    sum = sum + impossible_game(game, cubes, list(cubes.keys()))
    power_sum = power_sum + game_power(game, list(cubes.keys()))

print(sum)
print(power_sum)