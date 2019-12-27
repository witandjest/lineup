import requests
import json

from datetime import datetime, timedelta

from uniqueHelpers import getTeamAbbreviation, prettyPrint

class DailyRoster:

    # id = False
    # name = ''
    # team = ''
    # positions = []

    activePlayers: {}
    rosterGaps: {}

    eligiblePositions = {
        'C': ['C', 'F', 'F/D'],
        'LW': ['LW', 'F', 'F/D'],
        'RW': ['RW', 'F', 'F/D'],
        'D': ['D', 'F/D'],
    }

    def __init__ (self, activePlayers):
        # potentially this becomes startedRoster at some point?
        self.rosterMap = {
            'C': 1,
            'LW': 2,
            'RW': 2,
            'F': 1,
            'D': 4,
            'F/D': 1
        }

        self.populateActivePlayers(activePlayers)
        self.findRosterGaps()
        # self.getTeamsForRosterGaps()

    def populateActivePlayers(self, activePlayers):
        self.activePlayers = activePlayers

        
    def findRosterGaps(self):
        singlePositionPlayers = []
        multiPositionPlayers = []

        unstartedPlayers = []

        for player in self.activePlayers:
            if (len(player['positions']) == 1):
                singlePositionPlayers.append(player)
            else: 
                multiPositionPlayers.append(player)

        for player in singlePositionPlayers:
            if (self.startPlayer(player) == False):
                unstartedPlayers.append(player)

        #print(singlePositionPlayers)
        #prettyPrint(self.rosterMap)

        for player in multiPositionPlayers:
            if (self.startPlayer(player) == False):
                unstartedPlayers.append(player)

        #print(multiPositionPlayers)
        #prettyPrint(self.rosterMap)

        prettyPrint(unstartedPlayers)

        #for player in self.activePlayers:
            #print(player['name'])
            #print(self.isSpace(player['positions'][0], rosterMap))

    
            # find a way to handle multi positional players being optimally placed - easiest way might be to put the single position players where they go first
        
        # we also want to find an excess player list to see if we need to drop anyone
        
        # self.prettyPrint(activePlayerList)

        self.rosterGaps = ['nothing here']

    def startPlayer(self, player):
        positions = player['positions']

        for playerPosition in positions:
            for potentialPosition in self.eligiblePositions[playerPosition]:
                if (self.rosterMap[potentialPosition] > 0):
                    self.rosterMap[potentialPosition] -= 1 
                    return True

        return False
    
    def isSpace(self, position, rosterMap):
        for position in self.eligiblePositions[position]:
            if (rosterMap[position] > 0) :
                return True

        return False


    def getStartingPlayersForDay(self, activeTeams):
        activePlayers = []
        for player in self.playerList:
            if (player['team'] in activeTeams and 'G' not in player['positions']): # temporarily excluding goalies
                activePlayers.append(player)
 
        return activePlayers





