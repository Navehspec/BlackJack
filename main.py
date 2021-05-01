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
    def __init__(self):
        self.players = []
        dealer = {
            'name': 'Jesus',
            'hand': [],
            'handsum': 0
        }
        self.players.append(dealer)
        self.deck = Deck()
        self.getplayers()
        self.losers = []
        self.wieners = []

    def getplayers(self):  # push all the players into their list.
        join = 'y'
        while len(self.players) < 7 and join != 'n':
            join = input('I see you, child, would you like to join? y/n\n')
            if join == 'y':
                name = False
                while not name:
                    try:
                        name = str(input('Hello my child, please provide your name\n'))
                    except ValueError:
                        print('ENTER YOUR NAME CHILD')
                player = {'name': name, 'hand': [], 'handsum': 0}
                self.players.append(player)
            elif join == 'n':
                break

    def deal(self):
        self.deck = Deck()
        for player in self.players:
            player['hand'].append(self.deck.draw())
            player['hand'].append(self.deck.draw())

    def handval(self, player):
        acecounter = 0
        player['handsum'] = 0
        for card in player['hand']:
            rank, _ = card
            if rank == 'A':
                acecounter += 1
            elif rank == 'Jack' or rank == 'Queen' or rank == 'King':
                player['handsum'] += 10
            else:
                player['handsum'] += int(rank)
        while acecounter > 0:
            if player['handsum'] <= 10:
                player['handsum'] += 11
                acecounter -= 1
            else:
                player['handsum'] += 1
                acecounter -= 1

    def playersturn(self):
        for player in self.players[1:]:
            self.handval(player)
            print(f"Remember, One of the Lord's Cards are: {self.players[0]['hand'][0]}")
            while (draw := input(f"{player['name']}, Your hand is: {player['hand']}, and you hand value is: {player['handsum']}.\nDraw another? y/n")) == 'y':
                player['hand'].append(self.deck.draw())
                self.handval(player)
                if player['handsum'] > 21:
                    print(f"{player['name']}, You've been SMITTEN, You're Out!")
                    print(f"You're new bad hand is: {player['hand']}")
                    self.losers.append(player['name'])
                    break

    def dealerturn(self):
        self.handval(self.players[0])
        while self.players[0]['handsum'] < 17:
            self.players[0]['hand'].append(self.deck.draw())
            self.handval(self.players[0])

    def conc(self):
        if self.players[0]['handsum'] > 21:
            for player in self.players[1:]:
                if player['name'] not in self.losers:
                    self.wieners.append(player['name'])
            print(f"------------GAME OVER-------------")
            print(f"The Lord's Hand is:\n{self.players[0]['hand']}")
            print(f"Jesus Has LOST! The Winners ARE:\n{self.wieners}\n and the losers are:\n{self.losers}")
        else:
            for player in self.players[1:]:
                if player['name'] not in self.losers:
                    if player['handsum'] > self.players[0]['handsum']:
                        self.wieners.append(player['name'])
                    elif player['handsum'] == self.players[0]['handsum']:
                        continue
                    else:
                        self.losers.append(player['name'])
            print(f"------------GAME OVER-------------")
            print(f"The Lord's Hand is:\n{self.players[0]['hand']}")
            print(f"The Winners ARE:\n{self.wieners}\n and the losers are:\n{self.losers}")










game = Game()
game.deal()
game.playersturn()
game.dealerturn()
game.conc()



# def pcard(self):
#    print("┌───────┐")
#    print("| {:<2}    |".format(self.rank))
#    print("|       |")
#    print("|   {}   |".format(self.suit))
#    print("|       |")
#    print("|    {:>2} |".format(self.rank))
#    print("└───────┘")
