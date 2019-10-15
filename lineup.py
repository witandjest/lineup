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


import requests
import time
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup


def addPlayer(session, playerID):
    playerData = {'toAddPlayerId':playerID,'toDropPlayerId':''}
    r = session.post(url = addPlayerURL, headers=headers, data=playerData)

    parsedResponse = BeautifulSoup(r.content, 'html.parser')  
    
    return parsedResponse



getSessionURL = 'https://www.fleaflicker.com/nhl/leagues/12086/players/confirm?toAddPlayerId=331'

addPlayerURL = 'https://www.fleaflicker.com/nhl/leagues/12086/players/add'
loginURL = 'https://www.fleaflicker.com/nfl/login';

headers = {'User-Agent': 'Mozilla/5.0'}
payload = {'email':'witjest@gmail.com','password':'ferrari@767', 'keepMe':'true'}


session = requests.Session()
r = session.get(url = getSessionURL, headers=headers)

cookies = requests.utils.cookiejar_from_dict(requests.utils.dict_from_cookiejar(session.cookies))

loginRequest = session.post(loginURL,headers=headers,data=payload, cookies=cookies)

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





playerID = '331'
addResponse = addPlayer(session, playerID)

alertList = addResponse.select('.alert-danger')

timeoutCount = 0
while (len(alertList) > 0 and timeoutCount < 10):
    addResponse = addPlayer(session, playerID)
    alertList = addResponse.select('.alert-danger')

    print(alertList[0].text)

    time.sleep(0.5)
    timeoutCount += 1


print(r.status_code)

player_ids = ['4723', '3474']

for player in player_ids:
    print(player)


# Next Steps:

# create a fake league with 4 teams so that you can test adds
# refresh until a player becomes available
# try running at 8am for a few days, then attach to a cron when it works (AWS Lambda)







# for each player, try to add - check response?
# or spam requests every 10 seconds <--