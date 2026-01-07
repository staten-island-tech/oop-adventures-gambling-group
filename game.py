import random
import time

class class_base:
    def __init__(self, name, money, useage, lost):
        self.name = name
        self.money = money
        self.times_used = useage
        self.moneygiven = lost

class Person(class_base):
    def __init__(self, name, money, useage, lost, gained):
        super().__init__(name, money, useage, lost, gained)
        self.stonks = gained

    def play(self, machinetype):
        self.money += 10
        self.gamble = f"{self.name} used the {machinetype}. {self.name}'s balance is now {self.money}!"
        print(self.gamble)

    def show_status(self):
        print(f"Name: {self.name}  Balance: {self.money}  Times Gambled: {self.times_used}  Money Earned: {self.stonks}  Money Lost: {self.moneygiven}")

class Slot_Machine(class_base):
    def __init__(self, name, money, useage, lost):
        super().__init__(name, money, useage, lost)

    def display_info(self): 
        print(f"{self.name} --- Times Used:{self.times_used}, Money Earned: {self.moneygiven}, Money Lost: {self.money}")

newgamblername = input("Name yourself: ")
balance = random.randint(45, 100)
Newgambler = Person(newgamblername, balance, 0, 0, 0)
Newgambler.play("fetch")
print(f"{newgamblername} enters a casino with only ${balance} to their name.")
time.sleep(3.2)
print("In the casino, there are 3 slot machines. One on the left, one on the right, and one in the middle.")
time.sleep(3)
gamblechoice = input("What would you like to do? (Type 'L' to use the left machine, 'M' to use the one in the middle, 'R' to use the right machine, 'A' for additiopnal options, and anything else (besides the additional options) to leave the casino.)")


left_machine = Slot_Machine("Left Slot Machine", 0, random.randint(0, 34), 0)
middle_machine = Slot_Machine("Middle Slot Machine", 0, random.randint(0, 99), 0)
right_machine = Slot_Machine("Right Slot Machine", 0, random.randint(0, 9), 0)

machinenumber = 1
timesplayed = 0

while gamblechoice == "L" or gamblechoice == "M" or gamblechoice == "R" or gamblechoice == "A" or gamblechoice == "B" or gamblechoice == "LI" or gamblechoice == "MI" or gamblechoice == "RI":
    while Newgambler.money > 0:
        if left_machine.times_used >= 35:
            ICantStopWinning = 0.1
            if random.random() <= ICantStopWinning:
                Newgambler.money += 30
                Newgambler.stonks += 30
                left_machine.moneygiven += 30
                if left_machine.times_used > 35:
                    left_machine.times_used -= 35
                    left_machine.times_used / 2
                elif left_machine.times_used == 35:
                    left_machine.times_used -= 35
            if random.random() > ICantStopWinning:
                ICantStopWinning += 0.125
        if middle_machine.times_used >= 100:
            ICantStopWinning = 0.1
            if random.random() <= ICantStopWinning:
                Newgambler.money += 60
                middle_machine.moneygiven += 60
                if middle_machine.times_used > 100:
                    middle_machine.times_used -= 100
                    middle_machine.times_used / 2
                elif middle_machine.times_used == 100:
                    middle_machine.times_used -= 100
            elif random.random() > ICantStopWinning:
                ICantStopWinning += 0.125
        if right_machine.times_used >= 10:
            ICantStopWinning = 0.1
            if random.random() <= ICantStopWinning:
                Newgambler.money += 9
                right_machine.moneygiven += 9
                if right_machine.times_used > 10:
                    right_machine.times_used -= 10
                    right_machine.times_used / 2
                elif right_machine.times_used == 10:
                    right_machine.times_used -= 10
            elif random.random() > ICantStopWinning:
                ICantStopWinning += 0.125
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
        if gamblechoice == "A":
            print("")
        if gamblechoice == "B":
            Newgambler.show_status()
        if gamblechoice == "LI":
            left_machine.display_info()








        gamblechoice = input("What would you like to do? (Type 'L' to use the left machine, 'M' to use the one in the middle, 'R' to use the right machine, 'A' for additiopnal options, and anything else (besides the additional options) to leave the casino.)")

if Newgambler.money == 0:
    print("Your balance reached 0. You are now broke!")
if Newgambler.money < 0:
    print(f"Your balance reached {Newgambler.money}. You are in debt!")
if Newgambler.money > 0:
    if gamblechoice != "L" and gamblechoice != "M" and gamblechoice != "R" and gamblechoice != "A" and gamblechoice != "B" and gamblechoice != "LI" and gamblechoice != "MI" and gamblechoice != "RI":
        print(f"You were financially responsible!. You left the casino with ${Newgambler.money}!")





