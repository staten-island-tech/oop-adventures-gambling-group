import random
import time

class Person:
    def __init__(self, name, money):
        self.name = name
        self.__money = money

    def play(self, machinetype):
        self.__money += 10
        self.gamble = f"{self.name} used the {machinetype}. {self.name}'s balance is now {self.__money}!"
        print(self.gamble)

    def show_status(self):
        print(f"Name: {self.name}  Balance: {self.__money}")

Newgambler = Person("Cookie", random.randint(35, 100))
Newgambler.play("fetch")

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"

class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)  # Call the parent class constructor
        self.student_id = student_id
    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"

left_machine = 4
middle_machine = 9
right_machine = 3
quarterjar = 77
machinenumber = 1
timesplayed = 0
while quarterjar > 0:
    if left_machine == 35:
        quarterjar += 30
        left_machine -= 35
    if middle_machine == 100:
        quarterjar += 60
        middle_machine -= 100
    if right_machine == 10:
        quarterjar += 9
        right_machine -= 10
    if machinenumber == 1 and quarterjar > 0:
        quarterjar -= 1
        left_machine += 1
        timesplayed += 1
        machinenumber += 1
    if machinenumber == 2 and quarterjar > 0:
        quarterjar -= 1
        middle_machine += 1
        timesplayed += 1
        machinenumber += 1
    if machinenumber == 3 and quarterjar > 0:
        quarterjar -= 1
        right_machine += 1
        timesplayed += 1
        machinenumber -= 2
print(f"Martha plays {timesplayed} times before going broke.")










