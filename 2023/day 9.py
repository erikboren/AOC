def diflist(v):
    difs = [x-v[i-1] for i,x in enumerate(v)]
    if len(difs) > 1:
        return difs[1:]
    else: 
        return [0]

def makeTree(v):
    if set(v[-1]) == {0}:
        return v
    
    v.append(diflist(v[-1]))
    return makeTree(v)

def predict(tree):
    for level in range(len(tree)-1,-1,-1):
        if set(tree[level]) == {0}:
            tree[level].append(0)
            tree[level].insert(0,0)
        else: 
            tree[level].append(tree[level][-1]+tree[level+1][-1])
            tree[level].insert(0,tree[level][0]-tree[level+1][0])
    
    return tree

with open("day 9 input.txt") as my_file:
    data = my_file.read().splitlines()
res = []
res2 = []
predictions = []
for line in data:
    tree = makeTree([[int(x) for x in line.split()]])
    prediction = predict(tree)
    res.append(prediction[0][-1])
    res2.append(prediction[0][0])
    predictions.append(prediction)

print(sum(res))
print(sum(res2))


