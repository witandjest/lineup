INITIATE_SESSION_URL = 'https://www.fleaflicker.com/nhl/leagues/12086/players/confirm?toAddPlayerId=331'
ADD_PLAYER_URL = 'https://www.fleaflicker.com/nhl/leagues/12086/players/add';

LOGIN_URL = 'https://www.fleaflicker.com/nfl/login'
LOGIN_INFO = {'email':'witjest@gmail.com','password':'somethingunique@94', 'keepMe':'true'}

HEADERS = {'User-Agent': 'Mozilla/5.0'}

import requests
import bs4

class FleaflickerConnection:

    session = False

    def __init__ (self):
        self.connect();

    def connect(self):
        self.session = requests.Session()
        response = self.session.get(url=INITIATE_SESSION_URL, headers=HEADERS)

        cookies = requests.utils.cookiejar_from_dict(requests.utils.dict_from_cookiejar(self.session.cookies))
        loginRequest = self.session.post(LOGIN_URL, headers=HEADERS, data=LOGIN_INFO, cookies=cookies)

        return True

    def addPlayer(self, playerID):
        playerData = {'toAddPlayerId':playerID,'toDropPlayerId':''}
        addPlayerResponse = self.session.post(url = ADD_PLAYER_URL, headers=HEADERS, data=playerData)

        parsedResponse = bs4.BeautifulSoup(addPlayerResponse.content, 'html.parser')  
        return parsedResponse

    