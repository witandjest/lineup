
HEADERS = {'User-Agent': 'Mozilla/5.0'}
GET_ROSTER_URL = 'https://www.fleaflicker.com/api/FetchRoster?sport=NHL&league_id=12086&team_id=62837&season=2019'

import requests
import json

class Roster:

    # id = False
    # name = ''
    # team = ''
    # positions = []

    playerList = []

    def __init__ (self):
        self.buildRoster();

    def buildRoster(self):
        rosterJSON = self.fetchRosterJSON()
        self.loadPlayersFromJSON(rosterJSON)


    def fetchRosterJSON(self):
        return requests.Session().get(url=GET_ROSTER_URL, headers=HEADERS).content


    def loadPlayersFromJSON(self, rosterJSON):
        data = json.loads(rosterJSON)

        rawStartingPlayerData = data['groups'][0]['slots']
        rawBenchPlayerData = data['groups'][1]['slots']
        rawInjuredPlayerData = data['groups'][2]['slots']

        for playerData in rawStartingPlayerData:
            self.addPlayerFromPlayerData(playerData)

        for playerData in rawBenchPlayerData:
            self.addPlayerFromPlayerData(playerData)

        print(self.playerList)
        # print(roster.keys())
        # print(roster['groups'][1]['slots'][0])

        # print(json.dumps(roster, indent=4, sort_keys=True))
    

    def addPlayerFromPlayerData(self, playerData):

        rosterSlotIsEmpty = 'leaguePlayer' not in playerData
        if (rosterSlotIsEmpty):
            return
        
        newPlayer = {}

        playerInfo = playerData['leaguePlayer']['proPlayer']
        positionInfo = playerData['leaguePlayer']['rankFantasy']['positions']

        newPlayer['id'] = playerInfo['id']
        newPlayer['name'] = playerInfo['nameFull']
        newPlayer['team'] = playerInfo['proTeamAbbreviation']
        
        newPlayer['positions'] = []
        for position in positionInfo:
            newPlayer['positions'].append(position['position']['label'])

        self.playerList.append(newPlayer)

    # def getPositionEligibilityMap():




