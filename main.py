import random


class Deck:
    def __init__(self):
        Ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        Suits = ['♥', '♦', '♣', '♠']
        self.Ranks = Ranks
        self.Suits = Suits
        self.deck = []
        for r in self.Ranks:
            for s in self.Suits:
                self.deck.append((r, s))
        random.shuffle(self.deck)

    def draw(self):
        return self.deck.pop()


class Game:
    players = []
    dealer = {
        'name': 'Jesus',
        'hand': [],
        'handsum': 0
    }
    players.append(dealer)

    def getplayers(self):  # push all the players into their list.
        while len(self.players) < 7:
            join = input('I see you, child, would you like to join? y/n')
            if join == 'y':
                name = False
                while not name:
                    try:
                        name = str(input('Hello my child, please provide your name'))
                    except ValueError:
                        print('ENTER YOUR NAME CHILD')
                player = {'name': name, 'hand': [], 'handsum': 0}
                self.players.append(player)
            elif join == 'n':
                break

    def pcard(self):
        print("┌───────┐")
        print("| {:<2}    |".format(self.rank))
        print("|       |")
        print("|   {}   |".format(self.suit))
        print("|       |")
        print("|    {:>2} |".format(self.rank))
        print("└───────┘")

deck = Deck()
