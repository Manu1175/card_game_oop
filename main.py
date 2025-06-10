from utils.game import Board
from utils.card import Card
from utils.player import Player, Deck

names = ['Charlie', 'David', 'Charlotte', 'Vanessa']
players = []
for name in names:
    players.append(name)
b = Board(players)
print(b)
d = Deck()
b.start_game(d)
while not b.game_over:
    b.play_turn()