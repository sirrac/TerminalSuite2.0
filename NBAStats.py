import requests
from pprint import pp
import questionary
from plumbum import cli

def get_players():
    url = "https://www.balldontlie.io/api/v1/players"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    pp(response.text)

def get_team():
   
    url = "https://www.balldontlie.io/api/v1/teams"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    pp(response.text)
    
def get_individual_player(query):
    url = "https://www.balldontlie.io/api/v1/players/?search=" + query
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    pp(response.text)

class NBAStat(cli.Application):

    def main(self):
        choice = questionary.select(
        "What would you like to do?",
        choices = ['Total player data', 'Total team data','Individual player data', 'Individual team data', 'Quit']).ask()

        match choice:
            case 'Total player data':
                get_players()
            case 'Total team data':
                get_team()
            case 'Individual player data':
                your_player = questionary.text("Type player").ask()
                get_individual_player(your_player)
            case 'Individual team data': 
                pass
            case 'Quit':
                print('Bye!')

if __name__ == '__main__':
    NBAStat()