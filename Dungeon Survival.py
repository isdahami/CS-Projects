#import random
import random

print("""-------------------------------------------------------------------
-------------------------------------------------------------------
██████╗░██╗░░░██╗███╗░░██╗░██████╗░███████╗░█████╗░███╗░░██╗
██╔══██╗██║░░░██║████╗░██║██╔════╝░██╔════╝██╔══██╗████╗░██║
██║░░██║██║░░░██║██╔██╗██║██║░░██╗░█████╗░░██║░░██║██╔██╗██║
██║░░██║██║░░░██║██║╚████║██║░░╚██╗██╔══╝░░██║░░██║██║╚████║
██████╔╝╚██████╔╝██║░╚███║╚██████╔╝███████╗╚█████╔╝██║░╚███║
╚═════╝░░╚═════╝░╚═╝░░╚══╝░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚══╝

░██████╗██╗░░░██╗██████╗░██╗░░░██╗██╗██╗░░░██╗░█████╗░██╗░░░░░
██╔════╝██║░░░██║██╔══██╗██║░░░██║██║██║░░░██║██╔══██╗██║░░░░░
╚█████╗░██║░░░██║██████╔╝╚██╗░██╔╝██║╚██╗░██╔╝███████║██║░░░░░
░╚═══██╗██║░░░██║██╔══██╗░╚████╔╝░██║░╚████╔╝░██╔══██║██║░░░░░
██████╔╝╚██████╔╝██║░░██║░░╚██╔╝░░██║░░╚██╔╝░░██║░░██║███████╗
╚═════╝░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝
-------------------------------------------------------------------
-------------------------------------------------------------------""")

print(""" OBJECTIVE: The objective to this game is to survive
            as long as possible to achieve the highest score!
-------------------------------------------------------------------
------------------------------------------------------------------- """)


#class selection w/ attributes
class warrior (object):
    health = 30
    strength = 10
    defense = 8
    magic = 1

class mage (object):
    health = 25
    strength = 3
    defense = 6
    magic = 10

class paladin (object):
    health = 25
    strength = 7
    defense = 10
    magic = 6

class cleric (object):
    health = 25
    strength = 4
    defense = 8
    magic = 9

class peasant (object):
    health = 10
    strength = 2
    defense = 1
    magic = 0

# Enemy Classes w/ attributes

class skeleton (object):
    name = "Skeleton"
    health = 15
    strength = 2
    defense = 2
    loot = random.randint(0,2)

class goblin (object):
    name = "Goblin"
    health = 20
    strength = 3
    defense = 3
    loot = random.randint(0,2)

class bandit (object):
    name = "Bandit"
    health = 22
    strength = 3
    defense = 2
    loot = random.randint(0,2)

class troll (object):
    name = "Cave Troll"
    health = 30
    strength = 5
    defense = 2
    loot = random.randint(0,2)

# function to choose class
def classSelect():
    print("Select your character!")
#ask user to input as to what class they are going to choose
    choice = input("1. Warrior \n2. Mage \n3. Paladin \n4. Cleric \n5. Peasant \n")
    if choice == "1":
        character = warrior
        print("You have chosen the WARRIOR...")
        print("Health - ", character.health)
        print("Strength - ", character.strength)
        print("Defense - ", character.defense)
        print("Magic - ", character.magic)
        return character
    elif choice == "2":
        character = mage
        print("You have chosen the MAGE...")
        print("Health - ", character.health)
        print("Strength - ", character.strength)
        print("Defense - ", character.defense)
        print("Magic - ", character.magic)
        return character
    elif choice == "3":
        character = paladin
        print("You have chosen the PALADIN...")
        print("Health - ", character.health)
        print("Strength - ", character.strength)
        print("Defense - ", character.defense)
        print("Magic - ", character.magic)
        return character
    elif choice == "4":
        character = cleric
        print("You have chosen the CLERIC...")
        print("Health - ", character.health)
        print("Strength - ", character.strength)
        print("Defense - ", character.defense)
        print("Magic - ", character.magic)
        return character
    elif choice == "5":
        character = peasant
        print("You have chosen the PEASANT...")
        print("Health - ", character.health)
        print("Strength - ", character.strength)
        print("Defense - ", character.defense)
        print("Magic - ", character.magic)
        return character
    else:
        print("ONLY PRESS 1, 2, 3, 4, or 5")
        classSelect()

# enemy select generator
# this function randomly generates an enemy
def enemyselect(skeleton, goblin, bandit, troll):
# enemy list -> 0 = skeleton 1 = goblin 2 = bandit 3 = troll
    enemyList = [skeleton, goblin, bandit, troll]
    # chance rate
    chance = random.randint(0,3)
    enemy = enemyList[chance]
    return enemy

# this function allows for loot to be randomly dropped
def loot():
# loot list -> 0 = potion 1 = sword 2 = shield
    loot = ["potion", "sword", "shield"]
    lootChance = random.randint(0,2)
    lootDrop = loot[lootChance]
    return lootDrop
 # this function changes attributes based on loot drop
def lootStatus(lootDrop, character):
    if lootDrop == "potion":
        character.health = character.health + 20
        print ("YOUR HEALTH INCREASED BY 20!")
        print ("YOUR HEALTH IS NOW", character.health)
        return character

    elif lootDrop == "sword":
        character.strength = character.strength + 2
        print("YOUR STRENGTH INCREASED BY 2!")
        print("YOUR STRENGTH IS NOW", character.strength)
        return character

    elif lootDrop == "shield":
        character.defense = character.defense + 2
        print("YOUR DEFENSE INCREASED BY 2!")
        print("YOUR DEFENSE IS NOW", character.defense)
        return character




def battlestate(score):
    enemy = enemyselect(skeleton, goblin, bandit, troll)
    print("A", enemy.name, "has appeared!")
    print("You have 3 options...")
    while enemy.health > 0:
        choice = input("1. Sword \n2. Magic \n3. RUN! \n")
        #c hoice 1 if statement
        if choice == "1":
            print("You swing your sword, attacking the", enemy.name)
            hitchance = random.randint(0,10)
            # lower number = more likely to hit
            if hitchance > 3:
                enemy.health = enemy.health - character.strength
                print("YOU HIT THE ENEMY, THEIR HEALTH IS NOW...", enemy.health)
                # enemies hit chance to hit the character if health is > 0
                # based on the defense
                if enemy.health > 0:
                    character.health = character.health - (enemy.strength / character.defense)
                    print("THE", enemy.name, "TAKES A SWING AND HITS YOU LEAVING", character.health)
                    gameOver(character, score)

                else:
                    # resets enemies health
                    # resets bc we face the same enemies several times
                    # also adds score
                    if enemy.name == "Skeleton":
                        enemy.health = 15
                        score = score + 10

                    elif enemy.name == "Goblin":
                        enemy.health = 20
                        score = score + 15

                    elif enemy.name == "Bandit":
                        enemy.health = 22
                        score = score + 20

                    elif enemy.name == "Cave Troll":
                        enemy.health = 30
                        score = score + 25

                    print("YOU HAVE DEFEATED THE", enemy.name)
                    lootDrop = loot()
                    print("YOU'VE RECIEVED A", lootDrop)
                    lootStatus(lootDrop, character)
                    return score
                    # break back to while loop
                    break
            else:
                # missed attack and enemy attacks user
                print("YOU MISSED!!!")
                print("THE", enemy.name, "HITS YOU FOR FULL DAMAGE")
                # take health away from user
                character.health = character.health - enemy.strength
                print("YOU NOW ONLY HAVE", character.health, "REMAINING")
                gameOver(character, score)

        # choice number 2 elif statement
        # magic choice
        elif choice == "2":
            print("You cast a spell, attacking the", enemy.name)
            hitchance = random.randint(0,10)
            # lower number = more likely to hit
            if hitchance > 3:
                enemy.health = enemy.health - character.magic
                print("YOU HIT THE ENEMY, THEIR HEALTH IS NOW...", enemy.health)
                # enemies hit chance to hit the character if health is > 0
                # based on the defense
                if enemy.health > 0:
                    character.health = character.health - (enemy.strength / character.defense)
                    print("THE", enemy.name, "TAKES A SWING AND HITS YOU LEAVING", character.health)
                    gameOver(character, score)

                else:
                    # resets enemies health
                    # resets bc we face the same enemies several times
                    # keeps track of score
                    if enemy.name == "Skeleton":
                        enemy.health = 15
                        enemy = score + 10

                    elif enemy.name == "Goblin":
                        enemy.health = 20
                        enemy = score + 15

                    elif enemy.name == "Bandit":
                        enemy.health = 22
                        enemy = score + 20

                    elif enemy.name == "Cave Troll":
                        enemy.health = 30
                        enemy = score + 25

                    print("YOU HAVE DEFEATED THE", enemy.name)
                    lootDrop = loot()
                    print("YOU'VE RECIEVED A", lootDrop)
                    lootStatus(lootDrop, character)
                    return score
                    # break back to while loop
                    break
            else:
                # missed attack and enemy attacks user
                print("YOU MISSED!!!")
                print("THE", enemy.name, "HITS YOU FOR FULL DAMAGE")
                # take health away from user
                character.health = character.health - enemy.strength
                print("YOU NOW ONLY HAVE", character.health, "REMAINING")
                gameOver(character, score)

        # RUN choice
        elif choice == "3":
            print("YOU ATTEMPT TO RUN...")
            # generate run chance
            runchance = random.randint(1,10)
            if runchance > 4:
                print("YOU GOT AWAY SAFE!")
                break
            else:
                print("THERE'S NO WHERE TO RUN...")
                print("THE ENEMY HITS YOU FOR FULL DAMAGE...")
                character.health = character.health - enemy.strength
                print("YOUR HEALTH IS NOW", character.health)
                gameOver(character, score)

        else:
            print("NUMBER NOT ALLOWED...PLEASE TYPE ONLY 1, 2, OR 3.")

# Game over function
def gameOver(character, score):
    if character.health < 1:
        print("YOU HAVE NO HEALTH LEFT")
        print("GAME OVER!")
        print("YOU HAVE SCORED...", score)
        name = input("Type your name...")
        writeScore(score,name)
        # opens file and reads
        file=open("score.txt","r")
        # prints out name and score
        for line in file:
            splitline = line.split(",")
            print(splitline[0], splitline[1])



# Write score to score.txt
def writeScore(score, name):
    file = open("score.txt", "a")
    file.write(str(name))
    file.write(",")
    file.write(str(score))
    file.write(",")
    file.write("\n")
    file.close()


score = 0
character = classSelect()
score = battlestate(score)
print("SCORE OF...", score)
score = battlestate(score)
print("SCORE OF...", score)
score = battlestate(score)
print("SCORE OF...", score)
score = battlestate(score)
print("SCORE OF...", score)
score = battlestate(score)
print("SCORE OF...", score)







