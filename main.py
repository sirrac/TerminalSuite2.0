from WeatherLookup import *
import questionary
from plumbum import *
from journal import *
    
if __name__ == '__main__':
    
    introPrinter("Welcome to the Terminal Suite!")
   
    main_choices = questionary.select(
        "What app would you like to use?",
        choices=[
            'The Weather App',
            'Journal',
            'Quit',
        ]).ask()
    
    match main_choices:
            case 'The Weather App':
                 WeatherApp()
            case 'Journal':
                 GJournal()
            case 'Quit':
                 print('Bye!')
