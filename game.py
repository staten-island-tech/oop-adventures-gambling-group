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
        super().__init__(name, money, useage, lost)
        self.stonks = gained

    def show_status(self):
        print(f"Name: {self.name}  Balance: {self.money}  Times Gambled: {self.times_used}  Money Earned: {self.stonks}  Money Lost: {self.moneygiven}")

class Slot_Machine(class_base):
    def __init__(self, name, money, useage, lost, probabilitytracker):
        super().__init__(name, money, useage, lost)
        self.win_chance = probabilitytracker

    def display_info(self): 
        print(f"{self.name} --- Times Used:{self.times_used}  Money Earned: {self.moneygiven}  Money Lost: {self.money}")

newgamblername = input("Name yourself: ")
balance = random.randint(45, 100)
Newgambler = Person(newgamblername, balance, 0, 0, 0)
print(f"{newgamblername} enters a casino with only ${balance} to their name.")
time.sleep(2.4)
print("In the casino, there are 3 slot machines. One on the left, one on the right, and one in the middle.")
time.sleep(2.87)
gamblechoice = input("What would you like to do? (Type 'L' to use the left machine, 'M' to use the one in the middle, 'R' to use the right machine, 'A' for additional options, and anything else (besides the additional options) to leave the casino.) ")


left_machine = Slot_Machine("Left Slot Machine", 0, 0, 0, random.randint(0, 34))
left_machine_win_money = 30
left_machine_win_rate = 35

middle_machine = Slot_Machine("Middle Slot Machine", 0, 0, 0, random.randint(0, 99))
middle_machine_win_money = 60
middle_machine_win_rate = 100

right_machine = Slot_Machine("Right Slot Machine", 0, 0, 0, random.randint(0, 9))
right_machine_win_money = 9
right_machine_win_rate = 10


while gamblechoice == "L" or gamblechoice == "M" or gamblechoice == "R" or gamblechoice == "A" or gamblechoice == "S" or gamblechoice == "LI" or gamblechoice == "MI" or gamblechoice == "RI":
    while Newgambler.money > 0:
        if left_machine.win_chance >= left_machine_win_rate:
            ICantStopWinning = 0.1
            if random.random() <= ICantStopWinning:
                Newgambler.money += left_machine_win_money
                Newgambler.stonks += left_machine_win_money
                left_machine.moneygiven += left_machine_win_money
                left_machine.win_chance -= left_machine_win_rate
                left_machine.win_chance / 2
                time.sleep(1)
                print(f"You won!!! You gained ${left_machine_win_money}. {Newgambler.name}'s wallet now has ${Newgambler.money}.")
            if random.random() > ICantStopWinning:
                ICantStopWinning += 0.125
                time.sleep(0.85)
                print(f"....You lost. {Newgambler.name}'s wallet did not change.")

        if middle_machine.win_chance >= middle_machine_win_rate:
            ICantStopWinning = 0.1
            if random.random() <= ICantStopWinning:
                Newgambler.money += middle_machine_win_money
                middle_machine.moneygiven += middle_machine_win_money
                middle_machine.win_chance -= middle_machine_win_rate
                middle_machine.win_chance / 2
                print(f"You won!!! You gained ${middle_machine_win_money}. {Newgambler.name}'s wallet now has ${Newgambler.money}.")
            elif random.random() > ICantStopWinning:
                ICantStopWinning += 0.125
                time.sleep(0.85)
                print(f"....You lost. {Newgambler.name}'s wallet did not change.")

        if right_machine.win_chance >= right_machine_win_rate:
            ICantStopWinning = 0.1
            if random.random() <= ICantStopWinning:
                Newgambler.money += right_machine_win_money
                right_machine.moneygiven += right_machine_win_money
                right_machine.win_chance -= right_machine_win_rate
                right_machine.win_chance / 2
                print(f"You won!!! You gained ${right_machine_win_money}. {Newgambler.name}'s wallet now has ${Newgambler.money}.")
            elif random.random() > ICantStopWinning:
                ICantStopWinning += 0.125
                time.sleep(0.85)
                print(f"....You lost. {Newgambler.name}'s wallet did not change.")

        if gamblechoice == "L":
            Newgambler.money -= 1
            Newgambler.moneygiven += 1
            left_machine.win_chance += 1
            left_machine.times_used += 1
            Newgambler.times_used += 1
            left_machine.money +=1
            print(f"You used the left slot machine. {Newgambler.name}'s balance is now {Newgambler.money}!")
            time.sleep(0.5)
            print(".")
            time.sleep(0.3)
            print("..")
            time.sleep(0.2)
            print("...")
            if left_machine.win_chance < left_machine_win_rate:
                time.sleep(0.85)
                print(f"....You lost. {Newgambler.name}'s wallet did not change.")
            gamblechoice = input("What would you like to do? (Type 'L' to use the left machine, 'M' to use the one in the middle, 'R' to use the right machine, 'A' for additional options, and anything else (besides the additional options) to leave the casino.) ")


        if gamblechoice == "M":
            Newgambler.money -= 1
            Newgambler.moneygiven += 1
            middle_machine.win_chance += 1
            middle_machine.times_used += 1
            Newgambler.times_used += 1
            middle_machine.money +=1
            print(f"You used the middle slot machine. {Newgambler.name}'s balance is now {Newgambler.money}!")
            time.sleep(0.5)
            print(".")
            time.sleep(0.3)
            print("..")
            time.sleep(0.2)
            print("...")
            if middle_machine.win_chance < middle_machine_win_rate:
                time.sleep(0.85)
                print(f"....You lost. {Newgambler.name}'s wallet did not change.")
            gamblechoice = input("What would you like to do? (Type 'L' to use the left machine, 'M' to use the one in the middle, 'R' to use the right machine, 'A' for additional options, and anything else (besides the additional options) to leave the casino.) ")

        if gamblechoice == "R":
            Newgambler.money -= 1
            Newgambler.moneygiven += 1
            right_machine.win_chance += 1
            right_machine.times_used += 1
            Newgambler.times_used += 1
            right_machine.money +=1
            print(f"You used the right slot machine. {Newgambler.name}'s balance is now {Newgambler.money}!")
            time.sleep(0.5)
            print(".")
            time.sleep(0.3)
            print("..")
            time.sleep(0.2)
            print("...")
            if right_machine.win_chance >= right_machine_win_rate:
                time.sleep(0.85)
                print(f"....You lost. {Newgambler.name}'s wallet did not change.")
            gamblechoice = input("What would you like to do? (Type 'L' to use the left machine, 'M' to use the one in the middle, 'R' to use the right machine, 'A' for additional options, and anything else (besides the additional options) to leave the casino.) ")

        if gamblechoice == "A":
            print("Type 'S' to check your stats, 'LI' to check the information of the left slot machine, 'MI' to check the middle slot machine's information, and 'RI' to check the right slot machine")
            time.sleep(3)
            gamblechoice = input("What would you like to do? (Type 'L' to use the left machine, 'M' to use the one in the middle, 'R' to use the right machine, 'A' for additional options, and anything else (besides the additional options) to leave the casino.) ")

        if gamblechoice == "S":
            Newgambler.show_status()
            time.sleep(2)
            gamblechoice = input("What would you like to do? (Type 'L' to use the left machine, 'M' to use the one in the middle, 'R' to use the right machine, 'A' for additional options, and anything else (besides the additional options) to leave the casino.) ")

        if gamblechoice == "LI":
            left_machine.display_info()
            time.sleep(0.9)
            gamblechoice = input("What would you like to do? (Type 'L' to use the left machine, 'M' to use the one in the middle, 'R' to use the right machine, 'A' for additional options, and anything else (besides the additional options) to leave the casino.) ")

        if gamblechoice == "MI":
            middle_machine.display_info()
            time.sleep(0.9)
            gamblechoice = input("What would you like to do? (Type 'L' to use the left machine, 'M' to use the one in the middle, 'R' to use the right machine, 'A' for additional options, and anything else (besides the additional options) to leave the casino.) ")

        if gamblechoice == "RI":
            right_machine.display_info()
            time.sleep(0.9)
            gamblechoice = input("What would you like to do? (Type 'L' to use the left machine, 'M' to use the one in the middle, 'R' to use the right machine, 'A' for additional options, and anything else (besides the additional options) to leave the casino.) ")

    if Newgambler.money == 0:
        print("Your balance reached 0. You are now broke!")
    if Newgambler.money < 0:
        print(f"Your balance reached {Newgambler.money}. You are in debt!")

    if gamblechoice != "L" and gamblechoice != "M" and gamblechoice != "R" and gamblechoice != "A" and gamblechoice != "S" and gamblechoice != "LI" and gamblechoice != "MI" and gamblechoice != "RI":
        gamblechoice = "test"
    if gamblechoice == "test":
        if Newgambler.money > 0:
            print(f"You were financially responsible! You left the casino with ${Newgambler.money}!")





