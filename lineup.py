# Request URL: https://www.fleaflicker.com/nhl/leagues/12086/players/add?toAddPlayerId=4723
# Request Method: GET

#import selenium
#from selenium import webdriver

#driver = webdriver.Chrome()
#driver.get('https://www.fleaflicker.com/nhl/leagues/12086/players')

# https://www.fleaflicker.com/nhl/leagues/12086/players/add?toAddPlayerId=4723
# https://www.fleaflicker.com/nhl/leagues/12086/players/confirm?toAddPlayerId=331


import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup

addPlayerURL = 'https://www.fleaflicker.com/nhl/leagues/12086/players/confirm?toAddPlayerId=331'
loginURL = 'https://www.fleaflicker.com/nfl/login';

headers = {'User-Agent': 'Mozilla/5.0'}
payload = {'email':'witjest@gmail.com','password':'ferrari@767', 'keepMe':'true'}


session = requests.Session()
r = session.get(url = addPlayerURL, headers=headers)

cookies = requests.utils.cookiejar_from_dict(requests.utils.dict_from_cookiejar(session.cookies))

loginRequest = session.post(loginURL,headers=headers,data=payload, cookies=cookies)

#print(loginRequest.content)
#print(BeautifulSoup(loginRequest.content, 'html.parser').prettify())
#print('=====================')


r = session.get(url = addPlayerURL, headers=headers)

#print(r.content);

print(BeautifulSoup(r.content, 'html.parser').prettify())

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