import random
import time


#Types (element) of wizard: Agressive, Defensive, 



class Wizard:
    def __init__(self, health, armour, agility, spell1, spell2):
        self.health = health
        self.armour = armour
        self.agility = agility
        self.spell1 = spell1
        self.spell2 = spell2
    
class Steven(Wizard):
    def __init__(self):
        super().__init__(200, 0.2, 0.1, "Fire", "Lightning")
        
class John(Wizard):
    def __init__(self):
        super().__init__(300, 0.4, 0.2, "Punch", "Shield")

class Dave(Wizard):
    def __init__(self):
        super().__init__(225, 0.3, 0.2, "Air", "Rock")

class Shaniquous(Wizard):
    def __init__(self):
        super().__init__(250, 0.25, 0.15, "Water", "Heal")


#Types of spell: fire, water, lightning, poison, heal, punch, air, rocks
class Spell:

    def __init__(self, damage, critChance, missChance, debuff): 
        self.damage = damage
        self.critChance = critChance
        self.missChance = missChance
        self.debuff = False

class WaterSpell(Spell): # water spell
    
    def __init__(self, waterBlock):
        super().__init__(40,0.5,0.1,False)
        self.waterBlock = 0.3
 

class LightningSpell(Spell): # lightning spell
    
    def __init__(self, stunChance):
        super().__init__(80,0.05,0.35,True)
        self.stunChance = 0.1


class FireSpell(Spell): # fire spell

    def __init__(self, fireDamagePercentage):
        super().__init__(50,0.15,0.3,True)
        self.fireDamagePercentage = 0.15


class HealSpell(Spell): # heal
    
    def __init__(self):
        super().__init__(-40,0,0.05,False)
    

class PunchSpell(Spell): # punch
    
    def __init__(self):
        super().__init__(55,0.5,0.35,False)
    
class AirSpell(Spell): # air
    
    def __init__(self, airMissDebuff):
        super().__init__(30,0.3,0.05,True)
        self.airMissDebuff = 0.25
        
class RockSpell(Spell): # rock
    
    def __init__(self):
        super().__init__(60,0.3,0.3,False)

class ShieldSpell(Spell):
    def __init__(self):
        super().__init__(-50,0,0.1,False)



def mainProgram():
    menu()

def menu(): 
    print("1. Play Wizard Game")
    print("2. End Game")
    choice = int(input("Enter Choice: "))
    while choice < 1 or choice > 2:
        print("Select 1 or 2!")
        choice = int(input("Enter Choice: "))
    if choice == 1:
        play()
    if choice == 2:
        print("Thanks for playing!")
        
        
def play():
    global wizardDict
    wizardDict = {
        1: "Steven",
        2: "John",
        3: "Dave",
        4: "Shaniquous"

    }
    global wizardChoicePlayer1
    global wizardChoicePlayer2
    objects()
    print("\n\n\n")
    print("Welcome to the Wizard game")
    print("PLAYER 1")
    print("Choose Your Wizard!")
    print("1. Steven: A powerful and agressive wizard")
    print("2. John: A defensive but mildly irrational wizard")
    print("3. Dave: A wizard who controls the elements")
    print("4. Shaniquous: Shaniquous")    
    wizardChoicePlayer1 = int(input("Enter Wizard: "))
    while (wizardChoicePlayer1>4 or wizardChoicePlayer1<1):
        print("Not a valid wizard: ")
        wizardChoicePlayer1 = int(input("Enter Wizard: "))
    if wizardChoicePlayer1 == 1:
        print("Player 1 has chosen Steven!")
    elif wizardChoicePlayer1 == 2:
        print("Player 1 has summoned John!")
    elif wizardChoicePlayer1 == 3:
        print("Player 1 has picked Dave!")
    elif wizardChoicePlayer1 == 4:
        print("Shaniquous.")

    print("\n\n\n\n\n")
    print("PLAYER 2")
    print("Choose Your Wizard!")
    print("1. Steven: A powerful and agressive wizard")
    print("2. John: A defensive but mildly irrational wizard")
    print("3. Dave: A wizard who controls the elements")
    print("4. Shaniquous: Shaniquous")   
    wizardChoicePlayer2 = int(input("Enter Wizard: "))
    while (wizardChoicePlayer2>4 or wizardChoicePlayer2<1):
        print("Not a valid wizard: ")
        wizardChoicePlayer2 = int(input("Enter Wizard: "))
    if wizardChoicePlayer2 == 1:
        print("Player 2 has chosen Steven!")
    elif wizardChoicePlayer2 == 2:
        print("Player 2 has summoned John!")
    elif wizardChoicePlayer2 == 3:
        print("Player 2 has picked Dave!")
    elif wizardChoicePlayer2 == 4:
        print("Shaniquous.")
    print("Player 1 will go first")
    fight()

def objects():
    global StevenPlayer1
    global StevenPlayer2
    global JohnPlayer1
    global JohnPlayer2
    global DavePlayer1
    global DavePlayer2
    global ShaniquousPlayer1
    global ShaniquousPlayer2
    global WaterPotion
    global FirePotion
    global LightningPotion
    global HealPotion
    global PunchPotion
    global AirPotion
    global RockPotion
    global ShieldPotion

    StevenPlayer1 = Steven()
    StevenPlayer2 = Steven()
    JohnPlayer1 = John()
    JohnPlayer2 = John()
    DavePlayer1 = Dave()
    DavePlayer2 = Dave()
    ShaniquousPlayer1 = Shaniquous()
    ShaniquousPlayer2 = Shaniquous()
    WaterPotion = WaterSpell(0)
    LightningPotion = LightningSpell(0)
    FirePotion = FireSpell(0)
    HealPotion = HealSpell()
    PunchPotion = PunchSpell()
    AirPotion = AirSpell(0)
    RockPotion = RockSpell()
    ShieldPotion = ShieldSpell()


def fight():
    pointer = 1
    print("\n\n")
    if wizardChoicePlayer1 == 1:
        print("Player 1, Steven has access to the following spells: ", StevenPlayer1.spell1, "and", StevenPlayer1.spell2)
        healthPlayer1 = StevenPlayer1.health
    elif wizardChoicePlayer1 == 2:
        print("Player 1, John has access to the following spells: ", JohnPlayer1.spell1 , "and", JohnPlayer1.spell2)
        healthPlayer1 = JohnPlayer1.health
    elif wizardChoicePlayer1 == 3:
        print("Player 1, Dave has access to the following spells: ", DavePlayer1.spell1 , "and", DavePlayer1.spell2)
        healthPlayer1 = DavePlayer1.health
    elif wizardChoicePlayer1 == 4:
        print("Player 1, Shaniquous has access to the following spells: ", ShaniquousPlayer1.spell1 , "and", ShaniquousPlayer1.spell2)
        healthPlayer1 = ShaniquousPlayer1.health
        
    if wizardChoicePlayer2 == 1:
        print("Player 2, Steven has access to the following spells: ", StevenPlayer2.spell1, "and", StevenPlayer2.spell2)
        healthPlayer2 = StevenPlayer2.health
    elif wizardChoicePlayer2 == 2:
        print("Player 2, John has access to the following spells: ", JohnPlayer2.spell1 , "and", JohnPlayer2.spell2)
        healthPlayer2 = JohnPlayer2.health
    elif wizardChoicePlayer2 == 3:
        print("Player 2, Dave has access to the following spells: ", DavePlayer2.spell1 , "and", DavePlayer2.spell2)
        healthPlayer2 = DavePlayer2.health
    elif wizardChoicePlayer2 == 4:
        print("Player 2, Shaniquous has access to the following spells: ", ShaniquousPlayer2.spell1 , "and", ShaniquousPlayer2.spell2)
        healthPlayer2 = ShaniquousPlayer2.health
    print("\n\n")

    print("Player 1 will start first")
    shieldCounterPlayer1 = 0
    healCounterPlayer1 = 0
    shieldCounterPlayer2 = 0
    healCounterPlayer2 = 0
    missChanceIncreasePlayer1 = False
    missChanceIncreasePlayer2 = False
    while healthPlayer1 > 0 and healthPlayer2 > 0:
        pointerChange = True
        if pointer == 1:
            print("Player 1 it is your turn!")
            if wizardChoicePlayer1 == 1: #add pointer to 2
                if missChanceIncreasePlayer1 == True:
                    LightningPotion.missChance = LightningPotion.missChance * 1.5
                    FirePotion.missChance = FirePotion.missChance * 1.5
                    missChanceIncreasePlayer1 = False
                print("Player 1, what spell do you want to use? ")
                spellChoicePlayer1 = input("Enter a spell: ")
                while spellChoicePlayer1 not in ["Fire", "Lightning"]:
                    print("You can only choose Fire or Lightning.")
                    spellChoicePlayer1 = input("Enter a spell: ")
                if spellChoicePlayer1 == "Fire": #Fire
                    print("Player 1 uses the Fire Spell!")
                    if random.randint(1,100) <= (FirePotion.missChance * 100):
                        print("\n")
                        print("...")
                        time.sleep(1)
                        print("You missed your Fire Spell!")
                    else:
                        healthPlayer2 = healthPlayer2 - FirePotion.damage
                        if random.randint(1,100) <= (FirePotion.fireDamagePercentage * 100):
                            print("...")
                            time.sleep(1)
                            print("Your opponent has been burned")
                            fireDamageTaken = healthPlayer2 * 0.1
                            healthPlayer2 = healthPlayer2 - fireDamageTaken

                        print("\n")
                        print("Player 2 now has,", healthPlayer2 , "health")
                        if healthPlayer2 < 0:
                            print("Your opponent has perished! Congratulations")
                if spellChoicePlayer1 == "Lightning": #Lightning
                    print("Player 1 uses Lightning spell!")
                    if random.randint(1,100) <= (LightningPotion.missChance * 100):
                        print("\n")
                        print("...")
                        time.sleep(1)
                        print("You missed your Lightning potion!")
                    else:
                        healthPlayer2 = healthPlayer2 - (LightningPotion.damage)
                        if random.randint(1,100) <= (LightningPotion.stunChance * 100):
                            print("...")
                            time.sleep(1)
                            print("Player 2 has been stunned and cannot move!")
                            pointerChange = False
                        print("\n")
                        print("Player 2 now has,", healthPlayer2 , "health")
                        if healthPlayer2 < 0:
                            print("Your opponent has perished! Congratulations")
  
                FirePotion.missChance = 0.3
                LightningPotion.missChance = 0.35
            elif wizardChoicePlayer1 == 2: # need to add pointers to 2
                if missChanceIncreasePlayer1 == True:
                    ShieldPotion.missChance = ShieldPotion.missChance * 1.5
                    PunchPotion.missChance = PunchPotion.missChance * 1.5
                    missChanceIncreasePlayer1 = False
                print("Player 1, what spell do you want to use?  ") 
                spellChoicePlayer1 = input("Enter a spell, you can only use Shield Twice: ")
                while spellChoicePlayer1 not in ["Shield", "Punch"]:
                    print("You can only choose Punch or Shield. You can only use shield twice")
                    spellChoicePlayer1 = input("Enter a spell: ")
                if shieldCounterPlayer1 == 2:
                    print("You are out of shield potions! Automatically using Punch Spell")
                    spellChoicePlayer1 = "Punch"
                if spellChoicePlayer1 == "Shield":
                    print("Player 1 used Shield!")
                    if random.randint(1,100) <= (ShieldPotion.missChance * 100):
                        print("\n")
                        print("...")
                        time.sleep(1)
                        print("You missed your shield potion!")
                    else:
                        healthPlayer1 = (healthPlayer1 - ShieldPotion.damage)
                        print("Player 1, your health is now,", healthPlayer1)
                        print("\n")
                        shieldCounterPlayer1 = shieldCounterPlayer1 + 1
                if spellChoicePlayer1 == "Punch":
                    print("Player 1 uses Punch!")
                    if random.randint(1,100) <= (PunchPotion.missChance * 100):
                        print("\n")
                        print("...")
                        time.sleep(1)
                        print("You missed your Punch!")
                    else:
                        healthPlayer2 = healthPlayer2 - PunchPotion.damage
                        print("\n")
                        print("Player 2 now has,", healthPlayer2 , "health")
                        if healthPlayer2 < 0:
                            print("Your opponent has perished! Congratulations")
                PunchPotion.missChance = 0.35
                ShieldPotion.missChance = 0.1     
            elif wizardChoicePlayer1 == 3:
                if missChanceIncreasePlayer1 == True:
                    AirPotion.missChance = AirPotion.missChance * 1.5
                    RockPotion.missChance = RockPotion.missChance * 1.5
                    missChanceIncreasePlayer1 = False
                print("Player 1, what spell do you want to use? ")
                spellChoicePlayer1 = input("Enter a spell: ")
                while spellChoicePlayer1 not in ["Air", "Rock"]:
                    print("You can only choose Air or Rock.")
                    spellChoicePlayer1 = input("Enter a spell: ")
                if spellChoicePlayer1 == "Air":
                    print("Player 1 uses Air Spell!")
                    if random.randint(1,100) <= (AirPotion.missChance * 100):
                        print("\n")
                        print("...")
                        time.sleep(1)
                        print("You missed your Air Potion!")
                    else:
                        if random.randint(1,100) <= (AirPotion.airMissDebuff * 100):
                            print("\n")
                            print("...")
                            time.sleep(1)
                            print("You increased your opponent's chance to miss on the next turn!")
                            missChanceIncreasePlayer2 = True
                        healthPlayer2 = healthPlayer2 - (AirPotion.damage)
                        print("\n")
                        print("Player 2 now has,", healthPlayer2 , "health")
                        if healthPlayer2 < 0:
                            print("Your opponent has perished! Congratulations")
                
                if spellChoicePlayer1 == "Rock":
                    print("Player 1 uses Rock Spell!")
                    if random.randint(1,100) <= (RockPotion.missChance * 100):
                        print("\n")
                        print("...")
                        time.sleep(1)
                        print("You missed your Rock Potion!")
                    else:
                        if random.randint(1,100) <= (RockPotion.critChance * 100):
                            print("You landed a critical hit!")
                            critDamage = (RockPotion.damage * 1.5)
                            healthPlayer2 = healthPlayer2 - critDamage
                        else:
                            healthPlayer1 = healthPlayer2 - RockPotion.damage
                        print("\n")
                        print("Player 2 now has,", healthPlayer2 , "health")
                        if healthPlayer2 < 0:
                            print("Your opponent has perished! Congratulations")
                AirPotion.missChance = 0.05
                RockPotion.missChance = 0.3
            elif wizardChoicePlayer1 == 4:
                if missChanceIncreasePlayer1 == True:
                    WaterPotion.missChance = WaterPotion.missChance * 1.5
                    HealPotion.missChance = HealPotion.missChance * 1.5
                    missChanceIncreasePlayer1 = False
            
                print("Player 1, what spell do you want to use? ")
                spellChoicePlayer1 = input("Enter a spell, you can only use heal twice: ")
                while spellChoicePlayer1 not in ["Water","Heal"]:
                    print("You can only choose Water or Heal.")
                    spellChoicePlayer1 = input("Enter a spell, you can only use heal twice: ")
                if healCounterPlayer1 == 2:
                    print("You are out of heal potions! Automatically using Water Spell")
                    spellChoicePlayer1 = "Water"
                if spellChoicePlayer1 == "Water":
                    print("Player 1 uses Water Spell!")
                    if random.randint(1,100) <= (WaterPotion.missChance * 100):
                        print("\n")
                        print("...")
                        time.sleep(1)
                        print("You missed your Water Potion!")
                    else:
                        healthPlayer2 = healthPlayer2 - (WaterPotion.damage)
                        print("\n")
                        print("Player 2 now has,", healthPlayer2 , "health")
                        if healthPlayer2 < 0:
                            print("Your opponent has perished! Congratulations")
                if spellChoicePlayer1 == "Heal":
                    print("Player 1 used Heal!")
                    if random.randint(1,100) <= (ShieldPotion.missChance * 100):
                        print("\n")
                        print("...")
                        time.sleep(1)
                        print("You missed your Heal potion!")
                    else:
                        healthPlayer1 = (healthPlayer1 - HealPotion.damage)
                        print("Player 1, your health is now,", healthPlayer1)
                        print("\n")
                        healCounterPlayer1 = healCounterPlayer1 + 1
                HealPotion.missChance = 0.05
                WaterPotion.missChance = 0.1

            if pointerChange == True:
                pointer = 2
            else: 
                pointer = 1
            continue

        if pointer == 2:
            print("Player 2 it is your turn!")
            if wizardChoicePlayer2 == 1:
                if missChanceIncreasePlayer2 == True:
                    LightningPotion.missChance = LightningPotion.missChance * 1.5
                    FirePotion.missChance = FirePotion.missChance * 1.5
                    missChanceIncreasePlayer2 = False
                print("Player 2, what spell do you want to use? ")
                spellChoicePlayer2 = input("Enter a spell: ")
                while spellChoicePlayer2 not in ["Fire", "Lightning"]:
                    print("You can only choose Fire or Lightning.")
                    spellChoicePlayer2 = input("Enter a spell: ")
                if spellChoicePlayer2 == "Fire": #Fire
                    print("Player 2 uses the Fire Spell!")
                    if random.randint(1,100) <= (FirePotion.missChance * 100):
                        print("\n")
                        print("...")
                        time.sleep(1)
                        print("You missed your Fire Spell!")
                    else:
                        healthPlayer1 = healthPlayer1 - FirePotion.damage
                        if random.randint(1,100) <= (FirePotion.fireDamagePercentage * 100):
                            print("...") 
                            time.sleep(1)
                            print("Your opponent has been burned")
                            fireDamageTaken = healthPlayer1 * 0.1
                            healthPlayer1 = healthPlayer1 - fireDamageTaken
                        print("\n")
                        print("Player 1 now has,", healthPlayer1 , "health")
                        if healthPlayer1 < 0:
                            print("Your opponent has perished! Congratulations") 
                if spellChoicePlayer2 == "Lightning": #Lightning
                    print("Player 2 uses Lightning spell!")
                    if random.randint(1,100) <= (LightningPotion.missChance * 100):
                        print("\n")
                        print("...")
                        time.sleep(1)
                        print("You missed your Lightning potion!")
                    else:
                        healthPlayer1 = healthPlayer1 - (LightningPotion.damage)
                        if random.randint(1,100) <= (LightningPotion.stunChance * 100):
                            print("...")
                            time.sleep(1)
                            print("Player 1 has been stunned and cannot move!")
                            pointerChange = False
                        print("\n")
                        print("Player 1 now has,", healthPlayer1 , "health")
                        if healthPlayer1 < 0:
                            print("Your opponent has perished! Congratulations")
                FirePotion.missChance = 0.3
                LightningPotion.missChance = 0.35
            elif wizardChoicePlayer2 == 2:
                if missChanceIncreasePlayer2 == True:
                    ShieldPotion.missChance = ShieldPotion.missChance * 1.5
                    PunchPotion.missChance = PunchPotion.missChance * 1.5
                    missChanceIncreasePlayer2 = False
                print("Player 2, what spell do you want to use?  ") 
                spellChoicePlayer2 = input("Enter a spell, you can only use Shield Twice: ")
                while spellChoicePlayer2 not in ["Shield", "Punch"]:
                    print("You can only choose Punch or Shield. You can only use shield twice")
                    spellChoicePlayer2 = input("Enter a spell: ")
                if shieldCounterPlayer2 == 2:
                    print("You are out of shield potions! Automatically using Punch Spell")
                    spellChoicePlayer2 = "Punch"
                if spellChoicePlayer2 == "Shield":
                    print("Player 2 used Shield!")
                    if random.randint(1,100) <= (ShieldPotion.missChance * 100):
                        print("\n")
                        print("...")
                        time.sleep(1)
                        print("You missed your shield potion!")
                    else:
                        healthPlayer2 = (healthPlayer2 - ShieldPotion.damage)
                        print("Player 2, your health is now,", healthPlayer2)
                        print("\n")
                        shieldCounterPlayer2 = shieldCounterPlayer2 + 1
                if spellChoicePlayer2 == "Punch":
                    print("Player 2 uses Punch!")
                    if random.randint(1,100) <= (PunchPotion.missChance * 100):
                        print("\n")
                        print("...")
                        time.sleep(1)
                        print("You missed your Punch!")
                    else:
                        healthPlayer1 = healthPlayer1 - PunchPotion.damage
                        print("\n")
                        print("Player 1 now has,", healthPlayer1 , "health")
                        if healthPlayer1 < 0:
                            print("Your opponent has perished! Congratulations")
                PunchPotion.missChance = 0.35
                ShieldPotion.missChance = 0.1            
            elif wizardChoicePlayer2 == 3:
                if missChanceIncreasePlayer2 == True:
                    AirPotion.missChance = AirPotion.missChance * 1.5
                    RockPotion.missChance = RockPotion.missChance * 1.5
                    missChanceIncreasePlayer2 = False
                print("Player 2, what spell do you want to use? ")
                spellChoicePlayer2 = input("Enter a spell: ")
                while spellChoicePlayer2 not in ["Air", "Rock"]:
                    print("You can only choose Air or Rock.")
                    spellChoicePlayer2 = input("Enter a spell: ")
                if spellChoicePlayer2 == "Air":
                    print("Player 2 uses Air Spell!")
                    if random.randint(1,100) <= (AirPotion.missChance * 100):
                        print("\n")
                        print("...")
                        time.sleep(1)
                        print("You missed your Air Potion!")
                    else:
                        if random.randint(1,100) <= (AirPotion.airMissDebuff * 100):
                            print("\n")
                            print("...")
                            time.sleep(1)
                            print("You increased your opponent's chance to miss on the next turn!")
                            missChanceIncreasePlayer1 = True
                        healthPlayer1 = healthPlayer1 - (AirPotion.damage)
                        print("\n")
                        print("Player 1 now has,", healthPlayer1, "health")
                        if healthPlayer1 < 0:
                            print("Your opponent has perished! Congratulations")
                
                if spellChoicePlayer2 == "Rock":
                    print("Player 2 uses Rock Spell!")
                    if random.randint(1,100) <= (RockPotion.missChance * 100):
                        print("\n")
                        print("...")
                        time.sleep(1)
                        print("You missed your Rock Potion!")
                    else:
                        if random.randint(1,100) <= (RockPotion.critChance * 100):
                            print("You landed a critical hit!")
                            critDamage = (RockPotion.damage * 1.5)
                            healthPlayer1 = healthPlayer1 - critDamage
                        else:
                            healthPlayer1 = healthPlayer1 - RockPotion.damage
                        print("\n")
                        print("Player 1 now has,", healthPlayer1 , "health")
                        if healthPlayer1 < 0:
                            print("Your opponent has perished! Congratulations")
                AirPotion.missChance = 0.05
                RockPotion.missChance = 0.3
            elif wizardChoicePlayer2 == 4:
                if missChanceIncreasePlayer2 == True:
                    WaterPotion.missChance = WaterPotion.missChance * 1.5
                    HealPotion.missChance = HealPotion.missChance * 1.5
                    missChanceIncreasePlayer2 = False

                print("Player 2, what spell do you want to use? ")
                spellChoicePlayer2 = input("Enter a spell, you can only use heal twice: ")
                while spellChoicePlayer2 not in ["Water","Heal"]:
                    print("You can only choose Water or Heal.")
                    spellChoicePlayer2 = input("Enter a spell, you can only use heal twice: ")
                if healCounterPlayer2 == 2:
                    print("You are out of heal potions! Automatically using Water Spell")
                    spellChoicePlayer2 = "Water"
                if spellChoicePlayer2 == "Water":
                    print("Player 2 uses Water Spell!")
                    if random.randint(1,100) <= (WaterPotion.missChance * 100):
                        print("\n")
                        print("...")
                        time.sleep(1)
                        print("You missed your Rock Potion!")
                    else:
                        healthPlayer1 = healthPlayer1 - (WaterPotion.damage)
                        print("\n")
                        print("Player 1 now has,", healthPlayer1 , "health")
                        if healthPlayer2 < 0:
                            print("Your opponent has perished! Congratulations")
                if spellChoicePlayer2 == "Heal":
                    print("Player 2 uses Heal!")
                    if random.randint(1,100) <= (HealPotion.missChance * 100):
                        print("\n")
                        print("...")
                        time.sleep(1)
                        print("You missed your Heal potion!")
                    else:
                        healthPlayer2 = (healthPlayer2 - HealPotion.damage)
                        print("Player 2, your health is now,", healthPlayer2)
                        print("\n")
                        healCounterPlayer2 = healCounterPlayer2 + 1
                HealPotion.missChance = 0.05
                WaterPotion.missChance = 0.1
            if pointerChange == True:
                pointer = 1
            else:
                pointer = 2
            continue



mainProgram()
