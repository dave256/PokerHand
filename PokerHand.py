#!/usr/bin/env python3

# ----------------------------------------------------------------------
# PokerHand.py
# Dave Reed
# 08/14/2020
# ----------------------------------------------------------------------

from typing import List
from CardDeck import Card

class PokerHand:

    # Poker value of hands in increasing order so they can be compared
    # in methods refer to as PokerHand.HIGH_CARD, etc.
    HIGH_CARD = 0
    TWO_OF_A_KIND = 1
    TWO_PAIRS = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8

    # hand names for printing the card names
    # in methods refer to as PokerHand.HAND_NAMES
    HAND_NAMES = ('High Card', 'Two of a Kind', 'Two Pairs', 'Three of a Kind',
                  'Straight', 'Flush', 'Full House', 'Four of a Kind',
                  'Straight Flush')

    # ------------------------------------------------------------------

    def __init__(self):
        """initialize empty hand"""
        self.cards: List[Card] = []

    # ------------------------------------------------------------------

    def clear(self):
        """remove all cards from hand"""
        self.cards = []

    # ------------------------------------------------------------------

    def addCards(self, cards: List[Card]):
        """add a list of cards to the hand"""
        self.cards.extend(cards)

    # ------------------------------------------------------------------

    def addCard(self, card: Card):
        """add a single card to the hand"""
        self.cards.append(card)

    # ------------------------------------------------------------------

    def evaluateHand(self):
        """determine the value of the hand and the constant for the hand and the name of the hand
        for example, it might return PokerHand.STRAIGHT_FLUSH, PokerHand.HAND_NAMES[PokerHand.STRAIGHT_FLUSH]

        :return: two values, the int constant for the hand and the str name of the hand
        """
        # important bug fix
        pass

# ----------------------------------------------------------------------


def main():
    pass

main()