from WeatherLookup import *
import questionary
from plumbum import *
from journal import *
from NBAStats import *
    
if __name__ == '__main__':
    
    introPrinter("Welcome to the Terminal Suite!")
   
    main_choices = questionary.select(
        "What app would you like to use?",
        choices=[
            'The Weather App',
            'Journal',
            'NBA Stat Explorer',
            'Quit',
        ]).ask()
    
    match main_choices:
            case 'The Weather App':
                 WeatherApp()
            case 'Journal':
                 GJournal()
            case 'NBA Stat Explorer':
                 NBAStat()
            case 'Quit':
                 print('Bye!')
            