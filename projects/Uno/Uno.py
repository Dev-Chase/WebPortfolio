from Player import Player
from Deck import Deck
from random import seed, randint
from AI import *
import time
seed(randint(0, 9999999999999999))
# DECK_SIZE = 108
suits = ['R', 'G', 'B', 'Y']
# is_player_turn = True
# is_game_over = False
# is_player_winner = False
deck = Deck("deck")
deck.fill_new(suits)
deck.shuffle()
pile = ['','']

deck_return_switch = {
    "R": "Red",
    "G": "Green",
    "B": "Blue",
    "Y": "Yellow",
    "+": "",
    "W": "",
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "@": "+2",
    "r": "Reverse",
    "S": "Skip",
    "$": "+4",
    "C": "Wildcard"
}
is_wild_switcher = {
    "C": True,
    "$": True
}
def show_situation(player, computer, pile, is_player_turn):
    print("---------------------------------------------")
    print(f"The Computer has {len(computer.cards)} Cards.")
    print("The Current Card is a: ", deck_return_switch.get(pile[0], "Error"), deck_return_switch.get(pile[1], "Error"))
    print(f"You have {len(player.cards)} Cards: ", end="")
    for i in range(len(player.cards)):
        print(deck_return_switch.get(player.cards[i, 0], "Error"), deck_return_switch.get(player.cards[i, 1], "Error"), end="   ")
    if is_player_turn == True:
        print("\n", "It's your turn.")
    else:
        print("\n", "It's the computers turn.")
    print("---------------------------------------------")

def get_user_input(pile, player, other_player, is_player_turn):
    user_in = input("What card would you like to play?(Number of Card from left to right, 0=draw): ")
    try:
        int(user_in)
        if not int(user_in) > player.size_of_hand and int(user_in) != 0:
            card = [player.cards[int(user_in)-1, 0], player.cards[int(user_in)-1, 1]]
            colour_choice = "B"
            
            wild_switcher = {
                "+": True,
                "W": True
            }
            is_wild = wild_switcher.get(card[0], False)
            if is_wild:
                colour_choice = input("What colour would you like to play?(R,B,G,Y): ")
            is_player_turn = player.play_card(card, int(user_in), other_player, is_wild, colour_choice, pile, is_player_turn, deck)
            return is_player_turn
        elif int(user_in) == 0:
            player.add_card(deck)
            return True if player.can_player_play(pile) else False
    except ValueError:
        print("Invalid Input, try again.")
        time.sleep(1)
        return True

def new_game():
    seed(randint(0, 9999999999999999))
    DECK_SIZE = 108
    suits = ['R', 'G', 'B', 'Y']
    is_player_turn = True
    is_game_over = False
    # is_player_winner = False
    deck = Deck("deck")
    deck.fill_new(suits)
    deck.shuffle()
    pile = ['','']
    while deck.arr[DECK_SIZE-1, 0] == '+' or deck.arr[DECK_SIZE-1, 0] == 'W' or deck.arr[DECK_SIZE-1, 1] == '@' or deck.arr[DECK_SIZE-1, 1] == 'r' or deck.arr[DECK_SIZE-1, 1] == 'S':
        deck.shuffle()
    pile = deck.get_next_card()
    Chase = Player()
    Computer = Player()
    for i in range(7):
        Chase.add_card(deck)
        Computer.add_card(deck)
    show_situation(Chase, Computer, pile, is_player_turn)
    while is_game_over != True:
        
        if is_player_turn:
            is_player_turn = get_user_input(pile, Chase, Computer, is_player_turn)
            show_situation(Chase, Computer, pile, is_player_turn)
            if len(Chase.cards) == 0:
                is_game_over = True
                return True
            time.sleep(0.3)
        elif not is_player_turn:
            if Computer.can_player_play(pile):
                available_cards = get_available_cards(Computer, pile)
                get_card_colours(Computer)
                get_card_cata(Computer, available_cards)
                highest_value_card_ind = get_card_values(Computer, pile, available_cards)
                card = [Computer.cards[highest_value_card_ind, 0], Computer.cards[highest_value_card_ind, 1]]
                print("Computer is playing a:", deck_return_switch.get(Computer.cards[highest_value_card_ind, 0], "Error"), deck_return_switch.get(Computer.cards[highest_value_card_ind, 1], "Error"))
                is_player_turn = Computer.play_card(card, highest_value_card_ind+1, Chase, is_wild_switcher.get(card[1], False), Computer.pick_ideal_colour(), pile, is_player_turn, deck)
                show_situation(Chase, Computer, pile, is_player_turn)
                time.sleep(1)
            else:
                print("Computer is drawing.")
                Computer.add_card(deck)
                is_player_turn = False if Computer.can_player_play(pile) else True
                show_situation(Chase, Computer, pile, is_player_turn)
                time.sleep(1)
        if len(Computer.cards) == 0:
            is_game_over = True
            return False
while True:
    if new_game() == True:
        print("-------------------------------")
        print("-------------------------------")
        print("-------Congrats! You won!------")
        print("-------------------------------")
        print("-------------------------------")
    else:
        print("-------------------------------")
        print("-------------------------------")
        print("--------Sorry. You lost.-------")
        print("-------------------------------")
        print("-------------------------------")
    time.sleep(1.5)