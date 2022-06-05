from curses.ascii import SP
from classes.game import Person, bcolors
from classes.magic import Spell

#create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("quake", 14, 140, "black")

#create white magic
cure = Spell ("Cure", 12, 120, "white")
cura = Spell ("Cura", 18 ,200, "white")


#Instantiate people
player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, quake])
enemy = Person(1200, 65, 45, 25, [cure, cura])

running = True
i = 0

print(bcolors.FAIL +bcolors.BOLD + "An enemy Attacks!" + bcolors.ENDC)

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
                magic_choice = int(input("choose magic:"))
                magic_dmg = player.generate_spell_damage(magic_choice)
                spell = player.get_spell_name(magic_choice)
                cost = player.get_spell_mp_cost(magic_choice)

                current_mp = player.get_mp()

                if cost > current_mp:
                        print(bcolors.FAIL + "\n Not enough MP\n" + bcolors.ENDC)
                        continue

                player.reduce_mp(cost)
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell + "deals", str(magic_dmg), "points of damage" + bcolors.ENDC)
                

        enemy_choice = 1

        enemy_dmg = enemy.generate_damage()
        player.take_damage(enemy_dmg)
        print("Enemy attacks for", enemy_dmg)

        print("------------------------------")

        print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp() + bcolors.ENDC))

        print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)

        print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)

        if enemy.get_hp() ==0:
                print(bcolors.OKGREEN + "you win!" + bcolors.ENDC)
                running = False
        elif player.get_hp() ==0:
                print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
                running = False
    
 

