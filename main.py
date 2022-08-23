import random
def create_deck():
    deck = []
    type_deck = ['1','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    for item in type_deck:
        amount_per_type = 0
        while amount_per_type != 3:
            deck.append(item)
            amount_per_type += 1
    return deck

def randomize_deck(created_deck):
    random.shuffle(created_deck)
    return created_deck


def deal_cards(shuffled_deck, player_count):
    player_one = []
    player_two = []
    player_three = []
    player_four = []
    if player_count == '2':
        players = [player_one, player_two]
        deal_number = 11
        while deal_number != 21:
            for player in players:
                card = shuffled_deck.pop(1)
                player.append(card)
                deal_number += 1
    if player_count == '3':
        players = [player_one, player_two, player_three]
        deal_number = 6
        while deal_number != 21:
            for player in players:
                card = shuffled_deck.pop(1)
                player.append(card)
                deal_number += 1
    if player_count == '4':
        players = [player_one, player_two, player_three, player_four]
        deal_number = 1
        while deal_number != 21:
            for player in players:
                card = shuffled_deck.pop(1)
                player.append(card)
                deal_number += 1

    return (players)

def check_pairs(players):
    player_one_pairs = 0
    player_two_pairs = 0
    player_three_pairs = 0
    player_four_pairs = 0
    if len(players) == 2:
        list_of_player_pairs = [player_one_pairs, player_two_pairs]
    elif len(players) == 3:
        list_of_player_pairs = [player_one_pairs, player_two_pairs, player_three_pairs]
    elif len(players) == 4:
        list_of_player_pairs = [player_one_pairs, player_two_pairs, player_three_pairs, player_four_pairs]
    index_number = 0
    for player in players:
        for string in range(len(player)):
            if player[string] == player[string-1] or player[string] == player[string-2] or player[string] == player[string-3] or player[string] == player[string-4]:
                list_of_player_pairs[index_number] +=1
            if string == 4:
                list_of_player_pairs[index_number] /= 2
                index_number += 1
    return list_of_player_pairs

def check_winner(list_of_pairs):
    check_number = 1
    player_winner_number = []
    if len(list_of_pairs) == 2:
        for pair_number in range(len(list_of_pairs)):
            if list_of_pairs[pair_number] <= (list_of_pairs[pair_number-1]-1) or list_of_pairs[pair_number] <= (list_of_pairs[pair_number -2]-1):
                check_number += 1
            else:
                player_winner_number.append(check_number)
                check_number += 1
        return player_winner_number
    elif len(list_of_pairs) == 3:
        for pair_number in range(len(list_of_pairs)):
            if list_of_pairs[pair_number] <= (list_of_pairs[pair_number-1]-1) or list_of_pairs[pair_number] <= (list_of_pairs[pair_number -2]-1):
                check_number += 1
            else:
                player_winner_number.append(check_number)
                check_number += 1
        return player_winner_number
    elif len(list_of_pairs) == 4:
        for pair_number in range(len(list_of_pairs)):
            if list_of_pairs[pair_number] <= (list_of_pairs[pair_number-1]-1) or list_of_pairs[pair_number] <= (list_of_pairs[pair_number -2]-1) or list_of_pairs[pair_number] <= (list_of_pairs[pair_number -3]-1):
                check_number += 1
            else:
                player_winner_number.append(check_number)
                check_number += 1
        return player_winner_number

def check_for_tie(winner):
    if len(winner) >= 2:
        (print(f"There was a tie between Players: {winner}"))
    else:
        print(f"The winner is Player:{winner}")

def run_game():
    game_deck = create_deck()
    shuffled_deck = randomize_deck(game_deck)
    player_count = input("Welcome to the Player Pairs, where the most pairs win! You will get 5 cards. How many players?:")
    players = deal_cards(shuffled_deck, player_count)
    pairs = check_pairs(players)
    if player_count == '2':
        print(f"""These are the results!
Player 1's hand:
{players[0]}
Player Pairs: {pairs[0]}
Player 2's hand:
{players[1]}
Player Pairs: {pairs[1]}""")
    elif player_count == '3':
        print(f"""Welcome to the Player Pairs, where the most pairs win! You will get 5 cards.
Player 1's hand:
{players[0]}
Player Pairs: {pairs[0]}
Player 2's hand:
{players[1]}
Player Pairs: {pairs[1]}
Player 3's hand:
{players[2]}
Player Pairs: {pairs[2]} """)
    elif player_count == '4':
         print(f"""Welcome to the Player Pairs, where the most pairs win! You will get 5 cards.
Player 1's hand:
{players[0]}
Player Pairs: {pairs[0]}
Player 2's hand:
{players[1]}
Player Pairs: {pairs[1]}
Player 3's hand:
{players[2]}
Player Pairs: {pairs[2]}
Player 4's hand:
{players[3]} 
Player Pairs:{pairs[3]} """)
    winner = check_winner(pairs)
    check_for_tie(winner)

run_game()
