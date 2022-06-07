from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

#create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("quake", 14, 140, "black")

#create white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18 ,200, "white")


#Create some Items
potion = Item("potion", "potion", "Heals 50 Hp", 50)
hi_potion = Item("Hi-potion", "potion", "Heals for 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hi_elixer = Item("MegaElixer", "elixer", "Fully resoters party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_magic = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{"item":potion, "quantity": 15}, {"item":hi_potion, "quantity": 5}, 
                {"item":superpotion, "quantity": 10},
                {"item":elixer, "quantity":20}, {"item":hi_elixer, "quantity":25}]
#Instantiate people
player = Person(460, 65, 60, 34, player_magic, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

running = True
i = 0

print(bcolors.FAIL + "An enemy Attacks!" + bcolors.ENDC)

while running:
        print("=======================")
        player.choose_action()
        choice = input("Choose Action:")
        index = int(choice) - 1

        if index == 0:
                dmg = player.generate_damage()
                enemy.take_damage(dmg)
                print("you attacked for", dmg, "points of damage.")
        elif index == 1:
                player.choose_magic()
                magic_choice = int(input("choose magic:"))-1

                if magic_choice == -1:
                        continue

                Spell = player.magic[magic_choice]
                magic_dmg = Spell.generate_damage()

                current_mp = player.get_mp()

                if Spell.cost > current_mp:
                        print(bcolors.FAIL + "\n Not enough MP\n" + bcolors.ENDC)
                        continue

                if Spell.type == "white":
                        player.heal(magic_dmg)
                        print(bcolors.OKBLUE + "\n" + Spell.name + "heals for", str(magic_dmg), "HP." + bcolors.ENDC)
                elif Spell.type == "black":         
                        enemy.take_damage(magic_dmg)
                        print(bcolors.OKBLUE + "\n" + Spell.name + "deals", str(magic_dmg), "points of damage" + bcolors.ENDC)
        elif index == 2:
                player.choose_item()
                item_choice = int(input("Choose item:")) -1

                if item_choice == -1:
                        continue

                item = player.items[item_choice]["item"]
                if player.items[item_choice]["quantity"] == 0:
                        print(bcolors.FAIL + "\n" + "None left...." + bcolors.ENDC)
                        continue

                player.items[item_choice]["quantity"] -= 1
          
                if item.type == "potion":
                        player.heal(item.prop)
                        print(bcolors.OKGREEN + "\n" + item.name + "heals for", str(item.prop), "HP", bcolors.ENDC)
                elif item.type == "elixer":
                        player.hp = player.maxhp
                        player.mp = player.maxmp
                        print(bcolors.OKGREEN + "\n" + item.name + "fully restores HP/MP" + bcolors.ENDC)
                elif item.type == "attack":
                        enemy.take_damage(item.prop)
                        print(bcolors.FAIL + "\n" + item.name + "deals", str(item.prop), "points of damage" + bcolors.ENDC) 

        enemy_choice = 1

        enemy_dmg = enemy.generate_damage()
        player.take_damage(enemy_dmg)
        print("Enemy attacks for", enemy_dmg)

        print("------------------------------")

        print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)

        print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)

        print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)

        if enemy.get_hp() ==0:
                print(bcolors.OKGREEN + "you win!" + bcolors.ENDC)
                running = False
        elif player.get_hp() ==0:
                print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
                running = False
    
 

