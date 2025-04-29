import random
import Player
import json


# Ideas to add in future 
## Logos
## Club History
## Club nickname
## Stadium data
path_club_names = "data/club_names.json"

def load_club_name():
    with open(path_club_names) as file:
        club_data = json.load(file)
    return club_data

def generate_club_name():
    return random.choice([key for key, val in load_club_name])

def get_stadium_name(club_name):
    return load_club_name()[club_name]

class Team:
    def __init__(self, name=None, stadium_name=None):
        self.name = generate_club_name()
        self.stadium_name = get_stadium_name(name)
       
       
Team().hello 
print(hello)