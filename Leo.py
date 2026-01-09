import random
import time

class MC():
    def __init__(self, name, klass, health, defense, strength, mana, speed, money, level, inv, exp, attacktype, debt):
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
        self.attacktype = attacktype
        self.debt = debt

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
        print(f"Debt ~ {self.debt}")
        print(f"Inventory ~ {self.inv}")

    def lvup(self):
        Req = 100
        Lvtime = 0
        while self.exp >= Req:
            if self.exp > Req:
                self.level += 1
                self.exp -= Req
                Lvtime += 1
                Req += 5
        if Lvtime >= 1:
            print(f"You leveled up {Lvtime} times!")
            print(f"You're now level {self.level}")
        print(f"Exp: {self.exp}/{Req}")

    def loan(self):
        global interest
        print("Loan interest rates:")
        print("Loans less than 10k ~ 10% interest")
        print("Loans 10k or more ~ 15% interest")
        print("Loans 50k or more ~ 20% interest")
        print("Loans 100k or more ~ 25% interest")
        print("Loans 500k or more ~ 35% interest")
        LV = False
        while LV == False:
            loan = input("How much money do you want?")
            if not loan.isdigit():
                print("Invalid input! Input how much you want!")
            else:
                loan = int(loan)
                if loan <= 0:
                    print(f"Invalid amount!")
                elif loan < 10000:
                    interest = 1.1
                    LV = True
                elif 50000 > loan >= 10000:
                    interest = 1.15
                    LV = True
                elif 100000 > loan >= 50000:
                    interest = 1.2
                    LV = True
                elif 500000 > loan >= 100000:
                    interest = 1.25
                    LV = True
                else:
                    interest = 1.35
                    LV = True
            print(f"Okay, here you go.")
            self.money += loan
            time.sleep(1)
            print("Now go back and win your money!")
            self.debt += (loan * interest)
    

    def debtcheck(self):
        if self.money > self.debt:
            loans = False
            while loans == False:
                decision = input("You have enough to pay off your loan shark debt! Do you want to? (y/n)")
                if decision.lower() not in ["y","n"]:
                    print("Invalid input, (y/n)")
                elif decision.lower() == "y":
                    self.money -= self.debt
                    self.debt = 0
                else:
                    self.debt *= interest
                    print(f"Your debt is now {self.debt}! Should've paid it off sooner!")
                    

            


    def gamble(self):
        re = True
        while re == True:
            re = False
            CI = False
            while CI == False:
                gamble = input("How much money do you want to bet?")
                if not gamble.isdigit():
                    print("Invalid input! Input how much you want to bet.")
                else:
                    gamble = int(gamble)
                    if gamble > self.money or gamble <= 0:
                        print(f"Invalid amount! You have ${self.money}!")
                    else:
                        print(f"Okay, your bet is ${gamble}.")
                        CI = True
            win = False
            Tie = False
            a = 0
            YP = 0
            DP = 0
            done = False
            Deck = [
            "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
            "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
            "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
            "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC"]
            for i in range(3):
                print ("Shuffling..")
                time.sleep(0.25)
                random.shuffle(Deck)
                print ("Shuffling...")
                time.sleep(0.25)
                random.shuffle(Deck)

            time.sleep(0.25)
            Your_Hand = [Deck[0], Deck[1]]
            Dealer_Hand = [Deck[2]]
            for i in range(4):
                del Deck[0]
            print(f"Your hand: {Your_Hand}")
            print(f"Dealer's hand: {Dealer_Hand}")

            for cards in range(2):
                card=Your_Hand[cards][:-1]
                if card in ["10","J","Q","K"]:
                    YP += 10
                elif card == "A":
                    if YP+11 > 21:
                        YP += 1
                    else:
                        YP += 11
                        a += 1
                elif card in "23456789":
                    YP += int(card)
            
            Dcard=Dealer_Hand[0][:-1]
            if Dcard in ["10","J","Q","K"]:
                DP += 10
            elif Dcard == "A":
                if DP+11 > 21:
                    DP += 1
                else:
                    DP += 11
            elif Dcard in "23456789":
                DP += int(Dcard)
        
            print(f"Your points: {YP}")
            print(f"Dealer's points: {DP}")
        
            while done == False:
                Valid = False
                while Valid == False:
                    Choice = input("Do you want to hit or stand? (h/s)")
                    if Choice.lower() not in ["h","s"]:
                        print("Invalid input, (h/s)")
                    else:
                        Valid = True
                if Choice == "h":
                    Draw = Deck[0]
                    del Deck[0]
                    card=Draw[:-1]
                    if card in ["10","J","Q","K"]:
                        YP += 10
                    elif card == "A":
                        if YP+11 > 21:
                            YP += 1
                        else:
                            YP += 11
                    elif card in "23456789":
                        YP += int(card)
                    Your_Hand.append(Draw)
                    print(f"You drew a {Draw}")
                    if YP > 21:
                        done = True
                        print(f"Your points: {YP}... YOU BUST!")
                    elif YP < 21:
                        print(f"Your points: {YP}")
                    else:
                        print("Your points: 21")
                        done = True
                else:
                    done = True
                    print(f"Okay, you have {YP} points")
            while YP > DP and YP < 21:
                DDraw = Deck[0]
                del Deck[0]
                card=DDraw[:-1]
                if card in ["10","J","Q","K"]:
                    DP += 10
                elif card == "A":
                    if DP+11 > 21:
                        DP += 1
                    else:
                        DP += 11
                elif card in "23456789":
                    DP += int(card)
                Dealer_Hand.append(DDraw)
                print(f"The Dealer drew a {DDraw}")
                time.sleep(0.75)
                print(f"The dealer has {DP} points.")
                time.sleep(1)
            if done == False:
                print(f"The Dealer has {DP} points")
            time.sleep(1)
            if DP > 21:
                print(f"The dealer busts, you WIN ${gamble*(1+self.level*0.025)}!!!")
                win = True
            elif 21 > YP > DP or YP == 21 and DP != 21:
                time.sleep(1)
                print(f"YOU WIN {gamble*(1+self.level*0.025)}!!!")
                win = True
            elif 22 > DP > YP:
                time.sleep(1)
                print("YOU LOST!!! DEALER WINS!!!")
            elif DP == YP:
                time.sleep(1)
                print("PUSH!!! YOU TIE WITH THE DEALER!!!")
                Tie = True
            if win == True:
                self.money += (gamble*(1+self.level*0.025))
            elif Tie == True:
                print("No money lost, no money won")
            else:
                self.money -= gamble
            time.sleep(0.75)
            print(f"You now have ${self.money}.")
            time.sleep(0.75)

            if win == True:
                self.exp += 0.5*gamble
                print(f"You gained {(0.5*gamble)} exp!")
            elif Tie == True:
                self.exp += 0.25*gamble
                print(f"You gained {(0.25*gamble)} exp!")
            else:
                self.exp += 0.1*gamble
                print(f"You gained {(0.1*gamble)} exp!")

            ag = False
            while ag == False:
                again = input("Do you wanna go again? (y/n)")
                if again.lower() not in ["y","n"]:
                    print("Invalid input, (y/n)")
                else:
                    ag = True
            if again == "y" and self.money > 0:
                re = True
            elif again == "y" and self.money == 0:
                print("Bro you got no more money, maybe go to the loan sharks!")
                loans = False
                while loans == False:
                    loan = input("Do you want to go to the loan sharks? (y/n)")
                    if loan.lower() not in ["y","n"]:
                        print("Invalid input, (y/n)")
                    elif loan.lower() == "y":
                        loans = True
                        self.loan()
                    else:
                        loans = True
                    re == True
            else:
                re = False
            if self.debt() > 0:
                self.debtcheck()
            
                    
                




        
        
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
    attacktype = "Big bop"
print(f"Okay, your class is {klass}")
Name = input("Choose your name")
print(f"Okay, your name is {Name}")
you = MC(Name, klass, 100, 10, 10, 10, 10, 1000, 1, [], 0, "attacktypeph", 0)




you.gamble()

""" you.stats()
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


 """









