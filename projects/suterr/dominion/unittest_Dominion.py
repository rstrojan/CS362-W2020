from unittest import TestCase
import Dominion
import random
import testUtility
from collections import defaultdict

class TestCard(TestCase):

    def setUp(self):
        # Get player names
        self.player_names = ["*Ryan", "*Janie"]
        self.players = testUtility.makePlayers(self.player_names)

        # number of curses and victory cards
        if len(self.player_names) > 2:
            self.nV = 12
        else:
            self.nV = 8
        self.nC = -10 + 10 * len(self.player_names)

        self.box = testUtility.GetBoxes(self.nV)

        # Pick 10 cards from box to be in the supply.
        self.supply = testUtility.pickCards(self.box, self.player_names, self.nV,self. nC)

        # initialize the trash
        self.trash = []

        self.player = Dominion.Player('Annie')

        #play the game
        #testUtility.playGame(self.supply, self.players, self.trash)

        # Final score
        #testUtility.finalScore(self.players)

    def test_init(self):
        self.setUp()
        cost = 1
        buypower = 5

        card = Dominion.Coin_card(self.player.name, cost, buypower)

        self.assertEqual('Annie', card.name)
        self.assertEqual(buypower, card.buypower)
        self.assertEqual(cost, card.cost)
        self.assertEqual("coin", card.category)
        self.assertEqual(0, card.vpoints)

    def test_react(self):
        pass