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
    
    def randomize_deck(created_deck):
        random.shuffle(created_deck)
        return created_deck

    shuffled_deck = randomize_deck(game_deck)

    def deal_cards(shuffled_deck):
        player_one = []
        player_two = []
        player_three = []
        player_four = []
        players = [player_one, player_two, player_three, player_four]
        deal_number = 1
        while deal_number != 21:
            for player in players:
                card = shuffled_deck.pop(1)
                player.append(card)
                print(player)
                deal_number += 1
        return (players)
    players = deal_cards(shuffled_deck)
    print(players)
RunGame()