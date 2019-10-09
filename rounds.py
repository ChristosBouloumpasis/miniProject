#!/usr/bin/env python3
class Round:
    #constructor
    def __init__(self, creatorsName):
        self.statusActive = True
        self.orders = {}
        self.creatorName = creatorsName

    def inputPreference(self,preference):
        self.orders[preference.getPerson()] = preference.getDrink()

    def getRoundItems(self):
        return self.orders

    def getRoundStatus(self):
        return self.statusActive

    def getRound(self):

        return {
            "Creator": self.creatorName,
            "Round": self.orders
        }
