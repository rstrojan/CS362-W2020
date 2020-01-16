# -*- coding: utf-8 -*-
"""
Created on Wed 01/15/2020

@author: suterr
"""

import Dominion
import random
import testUtility
from collections import defaultdict

#Get player names
player_names = ["*Ryan"]

#number of curses and victory cards
if len(player_names)>2:
    nV=12
else:
    nV=8
nC = -10 + 10 * len(player_names)


box = testUtility.GetBoxes(nV)

#Pick 10 cards from box to be in the supply.
supply = testUtility.pickCards(box, player_names, nV, nC)

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.makePlayers(player_names)

#Play the game
testUtility.playGame(supply, players,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)