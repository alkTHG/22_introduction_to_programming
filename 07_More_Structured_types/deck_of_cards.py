import math
import random


def generate_deck():
    suits = ('hearts', 'spades', 'diamonds', 'clubs')
    ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace')
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append([rank, suit])
    print('standard deck generated')
    return deck


def deal(players, cards, deck):
    game = []
    for i in range(players):
        game.append(i + 1)
        for j in range(cards):
            # game.append(deck.pop(math.floor(random.random() * len(deck))))
            game.append(deck.pop(random.randrange(0, len(deck))))
    print('\nplayers with cards delt', game)
    print('\ncards left in deck', deck)


deck = generate_deck()
deal(2, 25, deck)

