import random

first_names = ["James", "Luis", "Marco", "Lucas", "Andrei", "Nicolas", "Kaito", "Omar", "Ivan", "Leo"]
last_names = ["Anderson", "García", "Rossi", "Smith", "Silva", "Müller", "Wang", "Hernandez", "Ivanov", "Khan"]

PlAYER_POSITIONS = ["GK", "DEF", "MID", "ATT"]
GK_ROLES = ["Sweeper Keeper", "Shot Stopper", "Ball Playing Keeper"]
DEF_ROLES = ["Ball Playing Defender", "Stopper", "Full Back"]
MID_ROLES = ["Box to Box", "Playmaker", "Winger"]
ATT_ROLES = ["Poacher"]


def generate_random_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_random_position():
    return random.choice(PlAYER_POSITIONS)

def generate_random_role(position):
    if position == "GK":
        return random.choice(GK_ROLES)
    elif position == "DEF":
        return random.choice(DEF_ROLES)
    elif position == "MID":
        return random.choice(MID_ROLES)
    elif position == "ATT":
        return random.choice(ATT_ROLES)
    else:
        raise Exception('Position is Invalid')

class Player:
    def __init__(self, name=None, position=None, role=None, skill=None):
        self.name = generate_random_name()
        self.position = generate_random_position()
        self.role = generate_random_role(self.position)
        self.skill = random.randint(50, 100)
        self.experience = max(random.randint(0, 100), 1)
        self.injury = False
        self.injury_duration = 0
        self.injury_type = None
        self.morale = random.randint(0, 100)
        self.form = random.randint(0, 100)
        self.fitness = random.randint(0, 100)
        self.age = random.randint(18, 40)
        self.value = (self.experience * self.skill * self.fitness * self.morale) 