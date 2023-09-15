from calendar import c
from distutils.cygwinccompiler import check_config_h
from xml.dom.expatbuilder import ParseEscape
from pyfiglet import Figlet
from plumbum import colors, cli 
from configparser import ConfigParser
import questionary
import urllib 
from urllib import request, parse
import json
import pprint 
from pprint import pp

    
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q="

def introPrinter(text):
    with colors['RED']:
        print(Figlet(font='big').renderText(text))
        
def get_api():
    
    config = ConfigParser()
    config.read("secret.ini")
    return config["openweather"]["key"]
    
def get_weather(url_to_analyze):
    
    reply = request.urlopen(url_to_analyze)
    data = reply.read()
    return json.loads(data)
    
def test():
    pass

def urlLookUp(input):
    try:
        weather = get_weather(input)
        pp(weather)
            
    except urllib.error.HTTPError: 
        print("City not found!")
        
        
class WeatherApp(cli.Application):
    
    def main(self):
        
        global choice 
        
        introPrinter("Welcome to the Weather Service!")
           
        choice = questionary.select(
        "What would you like to do?",
        choices=[
            'Current weather search',
            'Forecast search',
            'Config',
            'Quit'
        ]).ask()
        
        match choice:
            case 'Current weather search':
                 city = questionary.text("What city would you like to see today?").ask()
                 url = BASE_URL + city + "&appid=" + get_api()  
                 urlLookUp(url)
            case 'Forecast search':
                 city = questionary.text("What city would you like to see the forecast for today?").ask()
                 url = "http://api.openweathermap.org/data/2.5/forecast?q=" + city + "&appid=" + get_api()
                 urlLookUp(url)
            case 'Quit':
                 pass
            
       

