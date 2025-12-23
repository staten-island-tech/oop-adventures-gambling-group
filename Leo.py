import random

class MC():
    def __init__(self, name, klass, health, defense, strength, mana, speed, money, level, inv, exp):
        self.klass = klass
        self.name = name
        self.health = health
        self.defense = defense
        self.strength = strength
        self.mana = mana
        self.speed = speed
        self.money = money
        self.level = level
        self.inv = inv
        self.exp = exp

    def stats(self):
        print("Your stats:")
        print(f"Name ~ {Name}")
        print(f"Class ~ {klass}")
        print(f"Health ~ {self.health*h}")
        print(f"Defense ~ {self.defense*d}")
        print(f"Strength ~ {self.strength*st}")
        print(f"Mana ~ {self.mana*mn}")
        print(f"Speed ~ {self.speed*spd}")
        print(f"Level ~ {self.level}")
        print(f"Money ~ {self.money}")
        print(f"Inventory ~ {self.inv}")

    def lvup(self):
        Lvtime = 0
        while self.exp >= 100:
            if self.exp > 100:
                self.level += 1
                self.exp -= 100
                Lvtime += 1
        if Lvtime >= 1:
            print(f"You leveled up {Lvtime} times!")
        
        
class enemy():
    def __init__(self, type, health, defense, strength, speed, level, attacktype):
        self.type = type
        self.klass = klass
        self.health = health
        self.defense = defense
        self.strength = strength
        self.speed = speed
        self.level = level
        self.attacktype = attacktype

    def fight(self):
        dead = False
        YSpd = you.speed
        EnSpd = self.speed
        if you.speed != self.speed:
            while dead == False:
                if YSpd > EnSpd:
                    print("you.attack supposed to be here")
                    EnSpd += self.speed
                elif EnSpd > YSpd:
                    self.atk()
                    YSpd += you.speed
                elif EnSpd == YSpd:
                    print(f"Your Speed ~ {YSpd} = Enemy Speed {EnSpd}. Round skip.")
                if self.health <= 0:
                    dead == True
                    print(f"You won! EXP gained: {18 + 2*self.level}")
                    you.exp += (18 + 2*self.level)
                    you.lvup()
        else:
            rotation = 0
            while dead == False:
                rotation += 1
                if rotation == 1:
                    print("you.attack supposed to be here")
                elif rotation == 2:
                    self.atk()
                    rotation = 0
                if self.health <= 0:
                    dead == True
                    print(f"You won! EXP gained: {18 + 2*self.level}")
                    you.exp += (18 + 2*self.level)
                    you.lvup()

    def dmg(self, dmgmod):
        you.health -= (self.strength*dmgmod)


    def atk(self):
        rngatk = random.randint(1,4)
        if rngatk == 1:
            print(f"{self.type} used tactical nuke for {self.strength*3} damage!")
            self.dmg(3)
        else:
            print(f"{self.type} used {self.attacktype} for {self.strength} damage!")
            self.dmg(1)




CC = False
while CC == False:
    print("Classes:")
    print("A) Mage ~ 5x mana, 0.2x strength, 0.5x hp, 1x defense")
    print("B) Warrior ~ 0x mana, 2x strength, 2x hp, 2x defense, 1.5x speed")
    print("C) Tank ~ 3x hp, 3x defense, 0.5x speed")
    klass = input("Choose your class")
    if klass.lower() == "a":
        klass = "Mage"
        CC = True
    elif klass.lower() == "b":
        klass = "Warrior"
        CC = True
    elif klass.lower() == "c":
        klass = "Tank"
        CC = True
    else:
        print("Please type A, B, or C to select class.")
CC = False
if klass == "Mage":
    h = 0.5
    d = 1
    st = 0.2
    mn = 5
    spd = 1
    weapon = "Rusty Scepter"
if klass == "Warrior":
    h = 1.5
    d = 1.5
    st = 1.5
    mn = 0
    spd = 1.5
    weapon = "Dull Blade"
if klass == "Tank":
    h = 3
    d = 3
    st = 1
    mn = 1
    spd =0.5
    weapon = "Huge Old Hammer"
print(f"Okay, your class is {klass}")
Name = input("Choose your name")
print(f"Okay, your name is {Name}")

you = MC(Name, klass, 100, 10, 10, 10, 10, 0, 1, [], 0)
you.stats()
print("You wake up to an empty house, your wife and kids have been stolen by the corrupt government")
print("Your main mission: Save your wife and kids by adventuring out and confronting Bart, the king")
print(f"Now, you go to your friend's home, and they give you a {weapon} to help you on this journey")
while CC == False:
    Gob = enemy("Goblin", 100, 10, 10, 10, 1, "stab")
    CC = False
    FE = input("As you now venture out into the plains, you encounter a green goblin by a chest, do you fight (a) or flee (b)?")
    if FE.lower() == "a":
        print("placeholderfight")
        Gob.fight()
        CC = True
    elif FE.lower() == "b":
        print("You fled for saftey, you coward!")
        CC = True
    else:
        print("Invalid Option!")












