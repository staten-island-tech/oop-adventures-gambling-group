import random
import time

class class_base:
    def __init__(self, name, money):
        self.name = name
        self.money = money

class Person(class_base):
    def __init__(self, name, money):
        super().__init__(name, money)

    def play(self, machinetype):
        self.money += 10
        self.gamble = f"{self.name} used the {machinetype}. {self.name}'s balance is now {self.money}!"
        print(self.gamble)

    def show_status(self):
        print(f"Name: {self.name}  Balance: {self.money}")

class Slot_Machine(class_base):
    def __init__(self, name, money, useage):
        super().__init__(name, money)
        self.times_used = useage

    def display_info(self): 
        print(f"Times Used:{self.times_used}, Money Earned: {self.times_used}, Money Lost: {self.subject}")

newgamblername = input("Name yourself: ")
balance = random.randint(35, 100)
Newgambler = Person(newgamblername, balance)
Newgambler.play("fetch")
print(f"{newgamblername} enters a casino with only ${balance} to their name.")
time.sleep(3.2)
print("In the casino, there are 3 slot machines. One on the left, one on the right, and one in the middle.")
time.sleep(3)
gamblechoice = input("What would you like to do? (Type 'L' to use the left machine, 'M' to use the one in the middle, 'R' to use the right machine, 'A' for additiopnal options, and anything else (besides the additional options) to leave the casino.)")


left_machine = 4
middle_machine = 9
right_machine = 3

machinenumber = 1
timesplayed = 0

while gamblechoice == "L" or gamblechoice == "M" or gamblechoice == "R" or gamblechoice == "A" or gamblechoice == "B" or gamblechoice == "LI" or gamblechoice == "MI" or gamblechoice == "RI":
    while Newgambler.money > 0:
        if left_machine == 35:
            quarterjar += 30
            left_machine -= 35
        if middle_machine == 100:
            quarterjar += 60
            middle_machine -= 100
        if right_machine == 10:
            quarterjar += 9
            right_machine -= 10
        if gamblechoice == "L":
            quarterjar -= 1
            left_machine += 1
            timesplayed += 1
            machinenumber += 1
        if gamblechoice == "M":
            quarterjar -= 1
            middle_machine += 1
            timesplayed += 1
            machinenumber += 1
        if gamblechoice == "R":
            quarterjar -= 1
            right_machine += 1
            timesplayed += 1
            machinenumber -= 2
        if gamblechoice == "B":

        gamblechoice = input("What would you like to do? (Type 'L' to use the left machine, 'M' to use the one in the middle, 'R' to use the right machine, 'A' for additiopnal options, and anything else (besides the additional options) to leave the casino.)")

if Newgambler.money == 0:
    print("Your balance reached 0. You are now broke!")
if Newgambler.money < 0:
    print(f"Your balance reached {Newgambler.money}. You are in debt!")
if Newgambler.money > 0:
    if gamblechoice != "L" and gamblechoice != "M" and gamblechoice != "R" and gamblechoice != "A" and gamblechoice != "B" and gamblechoice != "LI" and gamblechoice != "MI" and gamblechoice != "RI":
        print(f"You were financially responsible!. You left the casino with ${Newgambler.money}!")


print(f"Martha plays {timesplayed} times before going broke.")




