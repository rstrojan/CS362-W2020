from unittest import TestCase
import testUtility
import Dominion
import random
import testUtility
from collections import defaultdict

class TestCard(TestCase):

    def setUp(self):
        # Get player names
        self.player_names = ["*Ryan", "*Janie"]

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

        # Costruct the Player objects
        self.players = testUtility.makePlayers(self.player_names)

        # Final score
        testUtility.finalScore([Dominion.Player(self.players)])

    def test_react(self):
        self.fail()
