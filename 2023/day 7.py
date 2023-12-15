class hand:
    def types(self,counts):
        if len(counts) == 0: #Special case for when hand is "JJJJJ"
            return 7
        if counts[0] == 5:
            return 7
        elif counts[0] == 4:
            return 6
        elif counts[0] == 3 and counts[1] == 2:
            return 5
        elif counts[0] == 3:
            return 4
        elif counts[0] == 2 and counts[1] == 2:
            return 3
        elif counts[0] == 2:
            return 2
        else:
            return 1
    def handToString(self,hand):
        unis = set([*hand])
        
        counts = []

        for nbr in unis:
            counts.append(hand.count(nbr))
        
        counts.sort(reverse = True)

        self.type= self.types(counts)

        order = "AKQJT98765432"

        hexhand = ""

        for card in hand:
            hexhand += hex(len(order)-order.index(card)).split("0x")[1]

        self.string =  "0x" + str(self.type) + hexhand

    def handToStringTwo(self, hand):
        unis = set([*hand])
        counts = []

        for nbr in unis:
            if nbr != "J":
                counts.append(hand.count(nbr))
        
        counts.sort(reverse = True)
        jcount = hand.count("J")
        
        if len(unis) != 0:
            while jcount >0 and jcount != 5:
                for i, count in enumerate(counts):
                    if count < 5:
                        counts[i] += 1
                        jcount -= 1
                        break
        
        self.type2 = self.types(counts)
        order = "AKQT98765432J"
        hexhand = ""

        for card in hand:
            hexhand += hex(len(order)-order.index(card)).split("0x")[1]

        self.stringTwo =  "0x" + str(self.type2) + hexhand

    def __init__(self, hand, bet):
        self.bet = bet
        self.handToString(hand)
        self.handToStringTwo(hand)

with open("day 7 input.txt") as my_file:
    data = my_file.read().splitlines()
hands = []

for line in data:
    handstr, bet = line.split()
    hands.append(hand(handstr, int(bet)))


hands.sort(key=lambda x: int(x.string,0), reverse=True)

winnings = [x.bet*(len(hands)-i) for i,x in enumerate(hands)]

print(sum(winnings))


hands.sort(key=lambda x: int(x.stringTwo,0), reverse=True)

winnings = [x.bet*(len(hands)-i) for i,x in enumerate(hands)]
# print([x.stringTwo for x in hands])
print(sum(winnings))