#!/usr/bin/env python3
class Round:
    #constructor
    def __init__(self, creatorsName):
        self.statusActive = True
        self.orders = {}
        self.creatorName = creatorsName


    def inputChoice(self,drink, name):
        self.orders[name] = drink

    def getRound(self):

        return {
            "Creator": self.creatorName,
            "Round": self.orders
        }

    def getRoundStatus(self):
        return self.statusActive


