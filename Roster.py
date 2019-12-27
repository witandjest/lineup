
HEADERS = {'User-Agent': 'Mozilla/5.0'}
GET_ROSTER_URL = 'https://www.fleaflicker.com/api/FetchRoster?sport=NHL&league_id=12086&team_id=62837&season=2019'
GET_SCHEDULE_URL = 'https://statsapi.web.nhl.com/api/v1/schedule'

import requests
import json

from datetime import datetime, timedelta

from uniqueHelpers import getTeamAbbreviation, prettyPrint

from DailyRoster import DailyRoster

class Roster:

    # id = False
    # name = ''
    # team = ''
    # positions = []

    playerList = []

    startOfWeek = ''
    endOfWeek = ''

    weeklySchedule = {}

    weeklyRoster = {}

    def __init__ (self):
        self.getWeeklySchedule()
        self.buildRoster()

        self.findRosterGaps()
        # self.getTeamsForRosterGaps()
        
    def findRosterGaps(self):
        for date, teams in self.weeklySchedule.items():
            print(date)  

            startingPlayers = self.getStartingPlayersForDay(teams)
            self.weeklyRoster[date] = DailyRoster(startingPlayers)
            
            print(self.weeklyRoster[date].rosterMap)
            
           
        
        print('-----')
        # self.prettyPrint(activePlayerList)

    def getStartingPlayersForDay(self, activeTeams):
        activePlayers = []
        for player in self.playerList:
            if (player['team'] in activeTeams and 'G' not in player['positions']): # temporarily excluding goalies
                activePlayers.append(player)
 
        return activePlayers

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

        # print(self.playerList)
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
    
    def populateCurrentWeek(self):
        today = datetime.today()
        last_monday = today - timedelta(days=today.weekday())
        next_sunday = last_monday + timedelta(days=6)

        self.startOfWeek = datetime.date(last_monday)
        self.endOfWeek = datetime.date(next_sunday)
 
    def getWeeklySchedule(self):
        self.populateCurrentWeek()

        startOfWeekString = self.startOfWeek.strftime('%Y-%m-%d')
        endOfWeekString = self.endOfWeek.strftime('%Y-%m-%d')

        weeklyScheduleURL = GET_SCHEDULE_URL + '?startDate=' + startOfWeekString + '&endDate=' + endOfWeekString
        rawRequestData =  json.loads(requests.Session().get(url=weeklyScheduleURL, headers=HEADERS).content);

        teamsPlayingPerDay = {}
       
        # print(rawRequestData['dates']);
        for date in rawRequestData['dates']:
            dateString = date['date']
            teamsPlaying = []
            for game in date['games']:
                #print(game['gameDate']);
                homeTeam = game['teams']['home']['team']['name']
                awayTeam = game['teams']['away']['team']['name']

                homeTeam = getTeamAbbreviation(homeTeam)
                awayTeam = getTeamAbbreviation(awayTeam)
                
                teamsPlaying.append(homeTeam)
                teamsPlaying.append(awayTeam)

            teamsPlayingPerDay[dateString] = teamsPlaying;

        self.populateWeekdays(teamsPlayingPerDay);


    def populateWeekdays(self, teamsPlayingPerDay):
        self.weeklySchedule['Monday'] = teamsPlayingPerDay[self.getIncrementedDateFromStartOfWeek(0)] if self.getIncrementedDateFromStartOfWeek(0) in teamsPlayingPerDay else []
        self.weeklySchedule['Tuesday'] = teamsPlayingPerDay[self.getIncrementedDateFromStartOfWeek(1)] if self.getIncrementedDateFromStartOfWeek(1) in teamsPlayingPerDay else []
        self.weeklySchedule['Wednesday'] = teamsPlayingPerDay[self.getIncrementedDateFromStartOfWeek(2)] if self.getIncrementedDateFromStartOfWeek(2) in teamsPlayingPerDay else []
        self.weeklySchedule['Thursday'] = teamsPlayingPerDay[self.getIncrementedDateFromStartOfWeek(3)] if self.getIncrementedDateFromStartOfWeek(3) in teamsPlayingPerDay else []
        self.weeklySchedule['Friday'] = teamsPlayingPerDay[self.getIncrementedDateFromStartOfWeek(4)] if self.getIncrementedDateFromStartOfWeek(4) in teamsPlayingPerDay else []
        self.weeklySchedule['Saturday'] = teamsPlayingPerDay[self.getIncrementedDateFromStartOfWeek(5)] if self.getIncrementedDateFromStartOfWeek(5) in teamsPlayingPerDay else []
        self.weeklySchedule['Sunday'] = teamsPlayingPerDay[self.getIncrementedDateFromStartOfWeek(6)] if self.getIncrementedDateFromStartOfWeek(6) in teamsPlayingPerDay else []

    def getIncrementedDateFromStartOfWeek(self, increment):
        return (self.startOfWeek + timedelta(days=increment)).strftime('%Y-%m-%d');





