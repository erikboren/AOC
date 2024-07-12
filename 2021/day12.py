with open("day12 input.txt") as my_file:
    data = my_file.read().splitlines()

p = 2
from collections import deque
import copy
# BFS

conns = {}

for line in data:
    pair = line.split("-")
    
    for node1 in pair:
        for node2 in pair:
            if node1 != node2:
                if node1 not in conns.keys():
                    conns[node1] = set([node2])
                else:
                    conns[node1].add(node2)
                    
for k,v in conns.items():
    print(k , v)


counter = 0

queue = deque([['start']])

paths = []

while len(queue) > 0:
    path = queue.popleft()
    
    if path[-1] == 'end':
        paths.append(path)
        continue
        

    node_conns = conns[path[-1]]
    
    for node in node_conns:
        if node.islower():
            if p == 1 and node not in path:
                new_path = copy.copy(path)
                new_path.append(node)
                queue.append(new_path)
            elif node != 'start':
                path_ls = [x for x in path if x.islower()]
                if len(path_ls) <= len(set(path_ls)) +1:
                    new_path = copy.copy(path)
                    new_path.append(node)
                    queue.append(new_path)
        else:
            new_path = copy.copy(path)
            new_path.append(node)
            queue.append(new_path)
            
print(len(paths))

