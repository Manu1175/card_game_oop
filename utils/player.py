from utils.card import Card
import random
from typing import List
import numpy as np

class Player:
    def __init__(self, name):
        self.cards = [] #cards in atribute as a List?
        turn_counts = 0 #turn_counts: int
        self.turn_counts = turn_counts
        number_of_cards = 0 #number_of_cards: int
        self.number_of_cards = number_of_cards
        #history = [Card()]
        self.history = [] #history: Card
        self.name = name
    
    def __str__(self) -> str:
        cards_str = [str[card] for card in self.cards]
        history_str = [str[card] for card in self.history]
        return f"{cards_str} {self.turn_counts} {history_str}"
    
    def play(self):
        if len(self.cards) == 0:
            print("no more cards to play")
        picked_card = random.shuffle(self.cards)
        self.cards.remove(picked_card)
        self.history.append(picked_card)
        self.turn_counts += 1
        #print(f"{PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}")
        print(f"{self.name}, turn: {self.turn_counts} played: {Card.value} {Card.icon}")
        return picked_card
    
    def update_cards(self, cards:List[Card]):
        self.cards = cards
    
class Deck:
    def __init__(self):
        self.cards = [] #cards: Card?
        
    def __str__(self) -> str:
        desc = f"{self.cards.value} {self.cards.color} {self.cards.icon}"
        return desc
        
    def fill_deck(self, players):
        #looping in value, color and icon, then assigning Card
        #Create list of cards value, cards icon
        list_card_values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        list_card_icon = ["♥", "♦", "♣", "♠"]
        
        cards = []
       
        for v in list_card_values:
            for i in list_card_icon:
                cards.append(Card(v, i))
        return cards
                   
    def shuffle(self):
        random.shuffle(self.cards)
            
    def distribute(self, players):
        #turn_count += 1
        #numb_cards = 52
        #numb_players = len(players)
        #remainder = numb_cards % numb_players
        
        cards_per_player = np.array_split(self.cards, len(players))
        self.shuffle()
        for s in self.cards:
            for p in cards_per_player:
                number_of_card += 1
                p.update_card(s)
                #card = Card(self.cards[s,p])
                #history = Card(self.cards[s,p])
                #players.append[card, turn_count, number_of_card, history]
            
                
        