from calendar import c
from ctypes.wintypes import PUSHORT
from re import X
from plumbum import cli
from plumbum import colors, cli
from pyfiglet import Figlet
import yaml, ruamel.yaml
import os, fnmatch
import questionary
from questionary import prompt
from datetime import datetime
import textwrap
    
def print_banner(text):
    with colors['LIGHT SEA GREEN']:
        print(Figlet(font='slant').renderText(text))
        
author = ""
journal_name = ""


def load_config(filename):
    global author, journal_name
    if not os.path.exists(filename):
        save_config(filename, {
            "author": '',
            "journal_name": ''
        })

    with open(filename, "r") as file:
        data = yaml.safe_load(file)
    author = data['author']
    journal_name = data['journal_name']

def save_config(filename, config):
    yaml = ruamel.yaml.YAML()
    
    with open(filename, "w") as file:
        yaml.dump(config, file)
 
def init_folder(folder_name):
    try:
        os.makedirs(folder_name)
    except:
        print(f"Creating the directory {folder_name} has failed.")
    os.chdir(journal_name)
    add_page()
    
def create_journal():
    global author, journal_name
    author = ruamel.yaml.scalarstring.DoubleQuotedScalarString(questionary.text("What is your name?").ask())
    
    journal_name = ruamel.yaml.scalarstring.DoubleQuotedScalarString(author + "-Journal")
    
    my_dict = dict(author=author, journal_name=journal_name)

    save_config("config.yaml", my_dict)
    init_folder(journal_name)
def open_journal():
    today_entry = str(datetime.today().strftime('%Y-%m-%d')) + ".txt"
    os.chdir(journal_name)
    journal_list = os.listdir()
    if not journal_list:
        add_page()
    for entry in journal_list:
        if fnmatch.fnmatch(entry, today_entry):
            add_content(today_entry)
        else:
            add_page()

def add_page():
    today_entry = str(datetime.today().strftime('%Y-%m-%d'))+ ".txt"
    open(today_entry, 'x')
    print(f"Created Entry: {today_entry}")
    add_content(today_entry)
        
def add_content(title):
    with open(title, "a") as entry:
        writing = questionary.text("Write entry here:").ask()
        prettier_writing = textwrap.fill(writing) + "\n"
        entry.write(prettier_writing)

def read_entries():

    os.chdir(journal_name)
    journal_list = os.listdir()
    question = [{
        "type": "select",
        "name": "select_entry",
        "message": "Choose an entry to read",
        "choices": journal_list
    },]
    entry = prompt(question)['select_entry']
    with open(entry, 'r') as e:
        print(e.read())
 
def edit_entries():
    os.chdir(journal_name)
    journal_list = os.listdir()
    

def delete_entries():
    os.chdir(journal_name)
    journal_list = os.listdir()
    question = [{
        "type": "select",
        "name": "select_entry",
        "message": "Choose an entry to delete.. warning, can't be recovered!",
        "choices": journal_list
    },]
    removal = prompt(question)['select_entry']
    os.remove(removal)


class GJournal(cli.Application):
    
    def main(self):
        global journal_name, author
        
        load_config("config.yaml")
        print_banner("Welcome to the Journal!")
        
        choice = questionary.select(
        "Your options...",
        choices = [
             "Journal",
             "Read Entries",
             "Delete Entries",
             "Exit"
        ]).ask()
        
        if choice == 'Journal':
            if journal_name == "":
                create_journal()
            else:
                open_journal()
        elif choice == 'Read Entries':
            read_entries()
        elif choice == 'Delete Entries':
            delete_entries()
        elif choice == "Exit":
            print("Bye!")
        
    
        
if __name__=="__main__":
    GJournal()
    