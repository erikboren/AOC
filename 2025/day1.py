filename = "2025/day1_input.txt"

with open(filename, 'r') as f:
	# dial = f.readlines()
	data = f.read().splitlines()

dial = 50

data = [int(line[1:]) if line[0] == "R" else -int(line[1:]) for line in data]


turns = 0
zeros = 0
turns2 = 0
x= 50

for rot in data:
	dturns = abs(rot) // 100
	rem = int(abs(rot)%100*rot/abs(rot))
	
	if dial + rem not in range(1,100) and dial != 0:
		dturns += 1
		
	dial = (dial+rem)%100 
	
	if dial == 0:
		zeros += 1
	
	turns += dturns

	turn_str = f' and turns {dturns} times' if dturns > 0 else ""
	print(f'Dial turns {rot} to {dial}{turn_str}')

print(zeros)
print(turns)

