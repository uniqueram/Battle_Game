from pkgutil import iter_modules
import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

from .magic import Spell
class Person:
    def __init__(self,hp,mp,atk,df,magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp 
        self.mp = mp
        self.atkl = atk-10
        self.atkh = atk+ 10
        self.df = df 
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Item"]


    def generate_damage(self):
        return random.randrange(self.atkl,self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i=1
        print("Action")
        for item in self.actions:
            print("    " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("magic")
        for Spell in self.magic:
            print("    " + str(i) + ":", Spell.name, "(cost:", str([Spell.cost]) + ")")
            i += 1
    

    def choose_item(self):
        i=1

        print(bcolors.OKGREEN + bcolors.BOLD + "Item:" + bcolors.ENDC)
        for item in self.items:
            print("    " + str(i) + ".", item["item"].name, ":", item["item"].description, "(x5)")
            i += 1
        




    
    



