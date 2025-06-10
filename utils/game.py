from utils.card import Card
from utils.player import Player, Deck
from typing import List

class Board:
    def __init__(self, players: List[Player]):
        self.players = players #list of Players
        self.turn_count = 0
        self.active_cards = List[Card] #the last card played by each player.
        self.history_cards = List[Card] #all the cards played since the start of the game, except for active_cards.
        self.game_over = False
    
    def __str__(self):
        active_cards_str = [str(card) for card in self.active_cards]
        history_cards_str = [str(card) for card in self.history_cards]
        
        return f"Board with {len(self.players)} players, turn count {self.turn_count} with active: {active_cards_str}, history: { history_cards_str}"
    
    def start_game(self, d: Deck):
        d.fill_deck(self.players)
        d.distribute(self.players)
    
    def play_turn(self):
        for player in self.players:
            picked_card = player.play()
            if picked_card:
                self.active_cards.append(picked_card)
                self.history_cards.append(picked_card)
            else:
                self.game_over = True
                break
            if not self.game_over:
                self.turn_count += 1
                self.active_cards = []
                print(f"{self}")
        
        