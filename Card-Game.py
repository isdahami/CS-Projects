""" cardGame.py
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
from random import *

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")

def main():
  clearDeck()

  for i in range(5):
    assignCard(PLAYER)
    assignCard(COMP)

  showDeck()
  showHand(PLAYER)
  showHand(COMP)

def clearDeck():
     #go through all the cards
     for cardNum in range(NUMCARDS):
        #set each location to DECK
        cardLoc[cardNum] = DECK

def showDeck():
    # go through all the cards
    for cardNum in range(NUMCARDS):
        # print card number, location of card
        print("{:3}: {:20} {}".format(cardNum, getCardName(cardNum), cardLoc[cardNum]))
    print()

def getCardName(cardNum):
    #given a card number
    # figure rank and suit
    suit = cardNum // 13
    rank = cardNum % 13

    # use them to create a string card name
    result = "{} of {}".format(rankName[rank], suitName[suit])
    # return card name
    return result

def assignCard(hand):
    # given a hand
    # while we have not picked a card
    keepGoing = True
    while (keepGoing):
        cardNum = randrange(NUMCARDS)
        # if that card is in deck
        if (cardLoc[cardNum] == DECK):
            # assign that card the location from hand
            cardLoc[cardNum] = hand
            keepGoing = False

def showHand(hand):
    # given a hand
    # go through all the cards
    for cardNum in range(NUMCARDS):
        # if card is in hand
        if cardLoc[cardNum] == hand:
        # print the card name
            print (getCardName(cardNum))

    print()


main()
