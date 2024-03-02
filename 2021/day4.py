with open("day4 input.txt") as my_file:
    data = my_file.read().splitlines()



moves = data[0].split(",")

matrices = []
matrix = False

for line in data[1:]:
    if line and not matrix:
        matrix = True
        matrices.append([])
        matrices[-1].append(line.split())
    elif not line:
        matrix = False
    else: 
        matrices[-1].append(line.split())

marked = {}

for i,matrix in enumerate(matrices):
    marked[i]  = []


def check(marks):
    # horizontal and vertical conditons
    xset = set([ m[1] for m in marks])
    yset = set([ m[0] for m in marks])

    for x in xset:
        count = 0
        for mark in marks:
            if mark[1] == x:
                count = count +1
        if count == 5:
            return True
        
    for y in yset:
        count = 0
        for mark in marks:
            if mark[0] == y:
                count = count +1
        if count == 5:
            return True

    # diagonal condition
    # diag1 = 0
    # diag2 = 0

    # diag1 = len ([m for m in marks if int(m[0]) == int(m[1])])
    # diag2 = len ([m for m in marks if int(m[0])+int(m[1]) ==4])

    # if diag1 == 5 or diag2 == 5:
    #     return True

def loop(moves, matrices, marked):
    moves_comp = []
    for i, move in enumerate(moves):
        moves_comp.append(move)
        for m, matrix in enumerate(matrices):
            for r, row in enumerate(matrix):
                for c, nbr in enumerate(row):
                    if nbr == move:
                        marked[m].append([r,c])
                        if len(marked[m]) <= 5:
                            pass
                        else:
                            if check(marked[m]):
                                return matrix,moves_comp
                            
matrix, moves_comp = loop(moves,matrices,marked)
summ = 0
for row in matrix:
    for nbr in row:
        if nbr in moves_comp:
            pass
        else:
            summ = summ + int(nbr)

print(summ)

print(summ*int(moves_comp[-1]))


def loop2(moves, matrices, marked):
    moves_comp = []
    winning_boards = set()
    for i, move in enumerate(moves):
        moves_comp.append(move)
        for m, matrix in enumerate(matrices):
            for r, row in enumerate(matrix):
                for c, nbr in enumerate(row):
                    if nbr == move:
                        marked[m].append([r,c])
                        if len(marked[m]) <= 5:
                            pass
                        else:
                            if check(marked[m]):
                                winning_boards.add(m)
                                if len(winning_boards) == len(matrices):
                                    return matrix, moves_comp
                                
marked = {}

for i,matrix in enumerate(matrices):
    marked[i]  = []


matrix, moves_comp = loop2(moves,matrices,marked)
summ = 0
for row in matrix:
    for nbr in row:
        if nbr in moves_comp:
            pass
        else:
            summ = summ + int(nbr)

print(moves_comp)
print(summ)

print(summ*int(moves_comp[-1]))


