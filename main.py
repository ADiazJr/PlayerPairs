import random

def RunGame():

    def CreateDeck():
        deck = []
        type_deck = ['1','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        for item in type_deck:
            amount_per_type = 0
            while amount_per_type != 3:
                deck.append(item)
                amount_per_type += 1
        return deck
    
    game_deck = CreateDeck()
    random.shuffle(game_deck)
    print(game_deck)

RunGame()