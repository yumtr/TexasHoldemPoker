class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.N = 0

    def inHand(self):
        return self.N

    def addCard(self, c):
        self.cards.append(c)
        self.N += 1

    def reset(self):
        self.N = 0
        self.cards.clear()

    # ace는 1혹은 11로 모두 사용 가능
    # 일단 11로 계산한 후 21이 넘어가면 1로 정정
    def value(self):
        total = 0
        ace = 0
        for i in range(self.N):
            total += self.cards[i].getValue()
            if self.cards[i].getValue() == 1:
                total += 10
                ace += 1
        while total > 21 and ace != 0:
            total -= 10
            ace -= 1
        return total
