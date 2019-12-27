import json

def getTeamAbbreviation(teamName):
    teamAbbreviationDict = {
        'Arizona Coyotes': 'ARZ',
        'Anaheim Ducks': 'ANH',
        'Boston Bruins': 'BOS',
        'Buffalo Sabres': 'BUF',
        'Calgary Flames': 'CGY',
        'Carolina Hurricanes': 'CAR',
        'Chicago Blackhawks': 'CHI',
        'Colorado Avalanche': 'COL',
        'Columbus Blue Jackets': 'CBJ',
        'Dallas Stars': 'DAL',
        'Detroit Red Wings': 'DET',
        'Edmonton Oilers': 'EDM',
        'Florida Panthers': 'FLA',
        'Los Angeles Kings': 'LA',
        'Minnesota Wild': 'MIN',
        'Montréal Canadiens': 'MTL',
        'Nashville Predators': 'NSH',
        'New Jersey Devils': 'NJ',
        'New York Islanders': 'NYI',
        'New York Rangers': 'NYR',
        'Ottawa Senators': 'OTT',
        'Philadelphia Flyers': 'PHI',
        'Pittsburgh Penguins': 'PIT',
        'San Jose Sharks': 'SJ',
        'St. Louis Blues': 'STL',
        'Tampa Bay Lightning': 'TB',
        'Toronto Maple Leafs': 'TOR',
        'Vancouver Canucks': 'VAN',
        'Vegas Golden Knights': 'VGK',
        'Washington Capitals': 'WSH',
        'Winnipeg Jets': 'WPG'
    }

    return teamAbbreviationDict[teamName]
           
def prettyPrint(dictionary):
    print(json.dumps(dictionary, sort_keys=False, indent=4))