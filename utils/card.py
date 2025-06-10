from typing import List

class Symbol:
    def __init__(self, icon) -> str:
        icon = ["♥", "♦", "♣", "♠"]
        color_dict = {"♦": "Red", "♥":'Red', "♣": "Black", "♠": "Black"}
        self.color = color_dict[icon]
        self.icon = icon
    
    def __str__(self):
        return f"{self.color} {self.icon}"

class Card(Symbol):
    def __init__(self, value, icon) -> str:
        #super.__init__(self, icon)
        #value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.value = value
        self.icon = icon
    
    def __str__(self):
        return f"The card received {self.value}, {self.color}, {self.icon}"
    