# Request URL: https://www.fleaflicker.com/nhl/leagues/12086/players/add?toAddPlayerId=4723
# Request Method: GET

#import selenium
#from selenium import webdriver

#driver = webdriver.Chrome()
#driver.get('https://www.fleaflicker.com/nhl/leagues/12086/players')

# https://www.fleaflicker.com/nhl/leagues/12086/players/add?toAddPlayerId=4723
# https://www.fleaflicker.com/nhl/leagues/12086/players/confirm?toAddPlayerId=331


# ADD REQUEST (POST)
# https://www.fleaflicker.com/nhl/leagues/12086/players/add
# toAddPlayerId
# toDropPlayerId

#print(loginRequest.content)
#print(BeautifulSoup(loginRequest.content, 'html.parser').prettify())
#print('=====================')

#playerData = {'toAddPlayerId':'331','toDropPlayerId':''}
#r = session.post(url = addPlayerURL, headers=headers, data=playerData)

#print(r.content);

#parsedResponse = BeautifulSoup(r.content, 'html.parser')    # stored as HTML
#prettyResponse = parsedResponse.prettify()                  # stored as string
#print(prettyResponse[8000:16000])


# if alert exists, keep trying? something to that effect
# alertList = parsedResponse.select('.alert-danger')



import requests
import time
import json

from FleaflickerConnection import FleaflickerConnection
from Roster import Roster

addPlayerURL = 'https://www.fleaflicker.com/nhl/leagues/12086/players/add'
HEADERS = {'User-Agent': 'Mozilla/5.0'}

# request object? has methods like: hasError(), printError(), 


def getWeeklySchedule():

    return False


def getCurrentRoster():

    roster = Roster();





def connectAndAdd():
    connection = FleaflickerConnection()

    playerIDs = ['2789']

    targetPlayerID = playerIDs[0];
    addResponse = connection.addPlayer(targetPlayerID)

    alertList = addResponse.select('.alert-danger')

    timeoutCount = 0
    while (len(alertList) > 0 and timeoutCount < 180):
        addResponse = connection.addPlayer(targetPlayerID)
        alertList = addResponse.select('.alert-danger')

        if(len(alertList) > 0):
            print(alertList[0].text)
        else:
            print('Player added successfully: ' + playerID)
            for playerID in playerIDs[1:]:
                connection.addPlayer(playerID)
                print('Player added successfully: ' + playerID)

        time.sleep(0.5)
        timeoutCount += 1
        
    print(addResponse.status_code)


getCurrentRoster();


# Next Steps:

# create a fake league with 4 teams so that you can test adds
# refresh until a player becomes available
# try running at 8am for a few days, then attach to a cron when it works (AWS Lambda)

# for each player, try to add - check response?
# or spam requests every 10 seconds <--