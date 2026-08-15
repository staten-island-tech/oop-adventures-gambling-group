import random
import time
print("Welcome to Sean's casino!")
choose = input("""What do you want to play?"
1. Roulette
2. BlackJack
3. Slots
""")
class Player:
    def __init__(self, name, balance):
        self.balance = balance  
        self.name = name
player = Player("Leo", 10000)

class Roulette:
    def __init__(self, balance):
        self.balance = balance
    def home_page(self):
        print(f"Welcome to Roulette! Your balance is currently ${player.balance}.")
        again5 = True
        while again5 == True:
            choose = input("""Choose what you want to play(1,2,etc.):
1. Single number bet
2. Double number bet
3. Triple number bet
4. Four number bet
5. Five number bet
6. Six number bet
7. Dozen bet
8. Red/Black
9. 18 number bet
10. Odd/Even bet                                                                                                        
""")
            if choose == "1":
                self.single_number()
                again5 = False
            elif choose == "2":
                self.double_number()
                again5 = False
            elif choose == "3":
                self.triple_number()
                again5 = False
            elif choose == "4":
                self.four_numbers()
                again5 = False
            elif choose == "5":
                self.five_numbers()
                again5 = False
            elif choose == "6":
                self.six_numbers()
                again5 = False       
            elif choose == "7":
                self.dozen_bet()
                again5 = False         
            elif choose == "8":
                self.red_black()
                again5 = False
            elif choose == "9":
                self.half_numbers()
                again5 = False
            elif choose == "10":
                self.odd_even()
                again5 = False
            else:
                print("Invalid option, you must choose a number.")
                again5 = True
    

    def broke(self):
        if player.balance <= 1:
            print("""Your balance is $0. You will be redirected to the home page.
             
             
             
             
             
             
             
             
            """)
            time.sleep(1.5)
            self.home_page()


    def single_number(self):
        wheel = [
                "0G",
                "1R", "2B", "3R", "4B", "5R", "6B",
                "7R", "8B", "9R", "10B", "11B", "12R",
                "13B", "14R", "15B", "16R", "17B", "18R",
                "19R", "20B", "21R", "22B", "23R", "24B",
                "25R", "26B", "27R", "28B", "29B", "30R",
                "31B", "32R", "33B", "34R", "35B", "36R"
                ]
        while True:
            bet = input("How much do you want to bet? ")
            if not bet.isdigit():
                print("Error. Invalid input, must be an integer. Try again")
                continue
            bet = int(bet)
            if bet > player.balance or bet < 1:
                print("Invalid bet amount")
                continue
            break
        while True:
            gamble = input("Choose a number: ")
            if not gamble.isdigit():
                print("Error. Invalid input, must be an integer. Try again")
                continue
            gamble = int(gamble)
            if gamble < 1 or gamble > 36:
                print("Invalid number. Try again, 0-36.")
                continue
            break

        spins = random.randint(74,111)
        raterate = 1.00005
        rate = 1.0075
        x = 0.07
        for i in range(spins):
            x *= rate
            rate *= raterate
            print(wheel[i % 37])
            time.sleep(x)
            if i >= spins - 6:
                raterate *=1.08
        number = wheel[(spins - 1) % 37]       
        if gamble == int(number[:-1]):
            player.balance += bet * 35
            print(f"Congrats! You bet ${bet} and won ${bet * 35}")
        else:
            print(f"Unfortunately you lost ${bet}")
            player.balance -= bet
        self.broke()
        while True:
            again_ask = input(f"""Your balance is now ${player.balance}, choose an option:
1. Play again
2. Play a different game
""")
            if again_ask == "1":
                return self.single_number()
            elif again_ask.lower() == "2":
                self.home_page()
                return
            else:
                print("Invalid option. (1/2)")
                continue


    def double_number(self):
        wheel = [
                "0G",
                "1R", "2B", "3R", "4B", "5R", "6B",
                "7R", "8B", "9R", "10B", "11B", "12R",
                "13B", "14R", "15B", "16R", "17B", "18R",
                "19R", "20B", "21R", "22B", "23R", "24B",
                "25R", "26B", "27R", "28B", "29B", "30R",
                "31B", "32R", "33B", "34R", "35B", "36R"
                ]
        while True:
            bet = input("How much do you want to bet? ")
            if not bet.isdigit():
                print("Error. Invalid input, must be an integer. Try again")
                continue
            bet = int(bet)
            if bet > player.balance or bet < 1:
                print("Invalid bet amount")
                continue
            break
        numbers = []
        while len(numbers) < 2:
            gamble = input(f"Choose number #{len(numbers) + 1}: ")
            if not gamble.isdigit():
                print("Error. Invalid input, must be an integer. Try again")
                continue
            gamble = int(gamble)
            if gamble < 1 or gamble > 36:
                print("Invalid number. Try again, 0-36.")
                continue
            if gamble in numbers:
                print("You already chose that number. Choose another.")
                continue
            numbers.append(gamble)
        spins = random.randint(111,148)
        raterate = 1.00005
        rate = 1.0075
        x = 0.07
        for i in range(spins):
            x *= rate
            rate *= raterate
            print(wheel[i % 37])
            time.sleep(x)
            if i >= spins - 6:
                raterate *=1.08
        number = wheel[(spins - 1) % 37]       
        if number[:-1] in numbers:
            player.balance += bet * 17
            print(f"Congrats! You bet ${bet} and won ${bet * 17}")
        else:
            print(f"Unfortunately you lost ${bet}")
            player.balance -= bet
        self.broke()
        while True:
            again_ask = input(f"""Your balance is now ${player.balance}, choose an option:
1. Play again
2. Play a different game
""")
            if again_ask == "1":
                return self.double_number()
            elif again_ask == "2":
                self.home_page()
                return
            else:
                print("Invalid option. (1/2)")
                continue


    def triple_number(self):
        wheel = [
                "0G",
                "1R", "2B", "3R", "4B", "5R", "6B",
                "7R", "8B", "9R", "10B", "11B", "12R",
                "13B", "14R", "15B", "16R", "17B", "18R",
                "19R", "20B", "21R", "22B", "23R", "24B",
                "25R", "26B", "27R", "28B", "29B", "30R",
                "31B", "32R", "33B", "34R", "35B", "36R"
                ]
        while True:
            bet = input("How much do you want to bet? ")
            if not bet.isdigit():
                print("Error. Invalid input, must be an integer. Try again")
                continue
            bet = int(bet)
            if bet > player.balance or bet < 1:
                print("Invalid bet amount")
                continue
            break
        numbers = []
        while len(numbers) < 3:
            gamble = input(f"Choose number #{len(numbers) + 1}: ")
            if not gamble.isdigit():
                print("Error. Invalid input, must be an integer. Try again")
                continue
            gamble = int(gamble)
            if gamble < 1 or gamble > 36:
                print("Invalid number. Try again, 0-36.")
                continue
            if gamble in numbers:
                print("You already chose that number. Choose another.")
                continue
            numbers.append(gamble)
        spins = random.randint(111,148)
        raterate = 1.00005
        rate = 1.0075
        x = 0.07
        for i in range(spins):
            x *= rate
            rate *= raterate
            print(wheel[i % 37])
            time.sleep(x)
            if i >= spins - 6:
                raterate *=1.08
        number = wheel[(spins - 1) % 37]       
        if number[:-1] in numbers:
            player.balance += bet * 11
            print(f"Congrats! You bet ${bet} and won ${bet * 11}")
        else:
            print(f"Unfortunately you lost ${bet}")
            player.balance -= bet
        self.broke()
        while True:
            again_ask = input(f"""Your balance is now ${player.balance}, choose an option:
1. Play again
2. Play a different game
""")
            if again_ask == "1":
                return self.triple_number()
            elif again_ask.lower() == "2":
                self.home_page()
                return
            else:
                print("Invalid option. (1/2)")
                continue
        

    def four_numbers(self):
        wheel = [
                "0G",
                "1R", "2B", "3R", "4B", "5R", "6B",
                "7R", "8B", "9R", "10B", "11B", "12R",
                "13B", "14R", "15B", "16R", "17B", "18R",
                "19R", "20B", "21R", "22B", "23R", "24B",
                "25R", "26B", "27R", "28B", "29B", "30R",
                "31B", "32R", "33B", "34R", "35B", "36R"
                ]
        while True:
            bet = input("How much do you want to bet? ")
            if not bet.isdigit():
                print("Error. Invalid input, must be an integer. Try again")
                continue
            bet = int(bet)
            if bet > player.balance or bet < 1:
                print("Invalid bet amount")
                continue
            break
        numbers = []
        while len(numbers) < 4:
            gamble = input(f"Choose number #{len(numbers) + 1}: ")
            if not gamble.isdigit():
                print("Error. Invalid input, must be an integer. Try again")
                continue
            gamble = int(gamble)
            if gamble < 1 or gamble > 36:
                print("Invalid number. Try again, 0-36.")
                continue
            if gamble in numbers:
                print("You already chose that number. Choose another.")
                continue
            numbers.append(gamble)
        spins = random.randint(111,148)
        raterate = 1.00005
        rate = 1.0075
        x = 0.07
        for i in range(spins):
            x *= rate
            rate *= raterate
            print(wheel[i % 37])
            time.sleep(x)
            if i >= spins - 6:
                raterate *=1.08
        number = wheel[(spins - 1) % 37]       
        if number[:-1] in numbers:
            player.balance += bet * 8
            print(f"Congrats! You bet ${bet} and won ${bet * 8}")
        else:
            print(f"Unfortunately you lost ${bet}")
            player.balance -= bet
        self.broke()
        while True:
            again_ask = input(f"""Your balance is now ${player.balance}, choose an option:
1. Play again
2. Play a different game
""")
            if again_ask == "1":
                return self.four_numbers()
            elif again_ask.lower() == "2":
                self.home_page()
                return
            else:
                print("Invalid option. (1/2)")
                continue


    def five_numbers(self):
        wheel = [
                "0G",
                "1R", "2B", "3R", "4B", "5R", "6B",
                "7R", "8B", "9R", "10B", "11B", "12R",
                "13B", "14R", "15B", "16R", "17B", "18R",
                "19R", "20B", "21R", "22B", "23R", "24B",
                "25R", "26B", "27R", "28B", "29B", "30R",
                "31B", "32R", "33B", "34R", "35B", "36R"
                ]
        while True:
            bet = input("How much do you want to bet? ")
            if not bet.isdigit():
                print("Error. Invalid input, must be an integer. Try again")
                continue
            bet = int(bet)
            if bet > player.balance or bet < 1:
                print("Invalid bet amount")
                continue
            break
        numbers = []
        while len(numbers) < 5:
            gamble = input(f"Choose number #{len(numbers) + 1}: ")
            if not gamble.isdigit():
                print("Error. Invalid input, must be an integer. Try again")
                continue
            gamble = int(gamble)
            if gamble < 1 or gamble > 36:
                print("Invalid number. Try again, 0-36.")
                continue
            if gamble in numbers:
                print("You already chose that number. Choose another.")
                continue
            numbers.append(gamble)
        spins = random.randint(111,148)
        raterate = 1.00005
        rate = 1.0075
        x = 0.07
        for i in range(spins):
            x *= rate
            rate *= raterate
            print(wheel[i % 37])
            time.sleep(x)
            if i >= spins - 6:
                raterate *=1.08
        number = wheel[(spins - 1) % 37]       
        if number[:-1] in numbers:
            player.balance += bet * 6
            print(f"Congrats! You bet ${bet} and won ${bet * 6}")
        else:
            print(f"Unfortunately you lost ${bet}")
            player.balance -= bet
        self.broke()
        while True:
            again_ask = input(f"""Your balance is now ${player.balance}, choose an option:
1. Play again
2. Play a different game
""")
            if again_ask == "1":
                return self.five_numbers()
            elif again_ask.lower() == "2":
                self.home_page()
                return
            else:
                print("Invalid option. (1/2)")
                continue


    def six_numbers(self):
        wheel = [
                "0G",
                "1R", "2B", "3R", "4B", "5R", "6B",
                "7R", "8B", "9R", "10B", "11B", "12R",
                "13B", "14R", "15B", "16R", "17B", "18R",
                "19R", "20B", "21R", "22B", "23R", "24B",
                "25R", "26B", "27R", "28B", "29B", "30R",
                "31B", "32R", "33B", "34R", "35B", "36R"
                ]
        while True:
            bet = input("How much do you want to bet? ")
            if not bet.isdigit():
                print("Error. Invalid input, must be an integer. Try again")
                continue
            bet = int(bet)
            if bet > player.balance or bet < 1:
                print("Invalid bet amount")
                continue
            break
        numbers = []
        while len(numbers) < 6:
            gamble = input(f"Choose number #{len(numbers) + 1}: ")
            if not gamble.isdigit():
                print("Error. Invalid input, must be an integer. Try again")
                continue
            gamble = int(gamble)
            if gamble < 1 or gamble > 36:
                print("Invalid number. Try again, 1-36.")
                continue
            if gamble in numbers:
                print("You already chose that number. Choose another.")
                continue
            numbers.append(gamble)
        spins = random.randint(111,148)
        raterate = 1.00005
        rate = 1.075
        x = 0.07
        for i in range(spins):
            x *= rate
            rate *= raterate
            print(wheel[i % 37])
            time.sleep(x)
            if i >= spins - 6:
                raterate *=1.08
        number = wheel[(spins - 1) % 37]       
        if number[:-1] in numbers:
            player.balance += bet * 5
            print(f"Congrats! You bet ${bet} and won ${bet * 5}")
        else:
            print(f"Unfortunately you lost ${bet}")
            player.balance -= bet
        self.broke()
        while True:
            again_ask = input(f"""Your balance is now ${player.balance}, choose an option:
1. Play again
2. Play a different game
""")
            if again_ask == "1":
                return self.six_numbers()
            elif again_ask.lower() == "2":
                self.home_page()
                return
            else:
                print("Invalid option. (1/2)")
                continue


    def dozen_bet(self):
        wheel = [
                "0G",
                "1R", "2B", "3R", "4B", "5R", "6B",
                "7R", "8B", "9R", "10B", "11B", "12R",
                "13B", "14R", "15B", "16R", "17B", "18R",
                "19R", "20B", "21R", "22B", "23R", "24B",
                "25R", "26B", "27R", "28B", "29B", "30R",
                "31B", "32R", "33B", "34R", "35B", "36R"
                ]
        while True:
            bet = input("How much do you want to bet? ")
            if not bet.isdigit():
                print("Error. Invalid input, must be an integer. Try again")
                continue
            bet = int(bet)
            if bet > player.balance or bet < 1:
                print("Invalid bet amount")
                continue
            break
        numbers = []
        while True:
            gamble = input("""Choose your dozen:
1. 1-12
2. 13-24
3. 25-36""")
            if gamble == "1":
                numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
            elif gamble == "2":
                numbers = [13,14,15,16,17,18,19,20,21,22,23,24]
            elif gamble == "3":
                numbers = [25,26,27,28,29,30,31,32,33,34,35,36]
            else:
                print("Invalid option, you must choose a number.")
                continue
            break
        spins = random.randint(111,148)
        raterate = 1.00005
        rate = 1.0075
        x = 0.07
        for i in range(spins):
            x *= rate
            rate *= raterate
            print(wheel[i % 37])
            time.sleep(x)
            if i >= spins - 6:
                raterate *=1.08
        number = wheel[(spins - 1) % 37]       
        if number[:-1] in numbers:
            player.balance += bet * 2
            print(f"Congrats! You bet ${bet} and won ${bet * 2}")
        else:
            print(f"Unfortunately you lost ${bet}")
            player.balance -= bet
        self.broke()
        while True:
            again_ask = input(f"""Your balance is now ${player.balance}, choose an option:
1. Play again
2. Play a different game
""")
            if again_ask == "1":
                return self.dozen_bet()
            elif again_ask.lower() == "2":
                self.home_page()
                return
            else:
                print("Invalid option. (1/2)")
                continue


    def red_black(self):
        wheel = [
                "0G",
                "1R", "2B", "3R", "4B", "5R", "6B",
                "7R", "8B", "9R", "10B", "11B", "12R",
                "13B", "14R", "15B", "16R", "17B", "18R",
                "19R", "20B", "21R", "22B", "23R", "24B",
                "25R", "26B", "27R", "28B", "29B", "30R",
                "31B", "32R", "33B", "34R", "35B", "36R"
                ]
        while True:
            bet = input("How much do you want to bet? ")
            if not bet.isdigit():
                print("Error. Invalid input, must be an integer. Try again")
                continue
            bet = int(bet)
            if bet > player.balance or bet < 1:
                print("Invalid bet amount")
                continue
            break
        while True:
            gamble = input("Red or Black?")
            if gamble.lower() == "red":
                color = "R"
                break
            elif gamble.lower() == "black":
                color = "B"
                break
            else:
                print("Invalid option, choose again.")
                continue
        spins = random.randint(111,148)
        raterate = 1.00005
        rate = 1.0075
        x = 0.07
        for i in range(spins):
            x *= rate
            rate *= raterate
            print(wheel[i % 37])
            time.sleep(x)
            if i >= spins - 6:
                raterate *= 1.08
        number = wheel[(spins - 1) % 37]       
        if color in number:
            player.balance += bet
            print(f"Congrats! You bet ${bet} and won ${bet}")
        else:
            print(f"Unfortunately you lost ${bet}")
            player.balance -= bet
        self.broke()
        while True:
            again_ask = input(f"""Your balance is now ${player.balance}, choose an option:
1. Play again
2. Play a different game
""")
            if again_ask == "1":
                return self.red_black()
            elif again_ask.lower() == "2":
                self.home_page()
                return
            else:
                print("Invalid option. (1/2)")
                continue
    def half_numbers(self):
        wheel = [
                "0G",
                "1R", "2B", "3R", "4B", "5R", "6B",
                "7R", "8B", "9R", "10B", "11B", "12R",
                "13B", "14R", "15B", "16R", "17B", "18R",
                "19R", "20B", "21R", "22B", "23R", "24B",
                "25R", "26B", "27R", "28B", "29B", "30R",
                "31B", "32R", "33B", "34R", "35B", "36R"
                ]
        while True:
            bet = input("How much do you want to bet? ")
            if not bet.isdigit():
                print("Error. Invalid input, must be an integer. Try again")
                continue
            bet = int(bet)
            if bet > player.balance or bet < 1:
                print("Invalid bet amount")
                continue
            break
        numbers = []
        while True:
            gamble = input("""Choose your half:
1. 1-18
2. 19-36
""")
            if gamble == "1":
                numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
            elif gamble == "2":
                numbers = [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
            else:
                print("Invalid option, you must choose a number.")
                continue
            break
        spins = random.randint(111,148)
        raterate = 1.00005
        rate = 1.0075
        x = 0.07
        for i in range(spins):
            x *= rate
            rate *= raterate
            print(wheel[i % 37])
            time.sleep(x)
            if i >= spins - 6:
                raterate *=1.08
        number = wheel[(spins - 1) % 37]       
        if int(number[:-1]) in numbers:
            player.balance += bet
            print(f"Congrats! You bet ${bet} and won ${bet}")
        else:
            print(f"Unfortunately you lost ${bet}")
            player.balance -= bet
        self.broke()
        while True:
            again_ask = input(f"""Your balance is now ${player.balance}, choose an option:
1. Play again
2. Play a different game
""")
            if again_ask == "1":
                return self.half_numbers()
            elif again_ask.lower() == "2":
                self.home_page()
                return
            else:
                print("Invalid option. (1/2)")
                continue

    def odd_even(self):
        wheel = [
                "0G",
                "1R", "2B", "3R", "4B", "5R", "6B",
                "7R", "8B", "9R", "10B", "11B", "12R",
                "13B", "14R", "15B", "16R", "17B", "18R",
                "19R", "20B", "21R", "22B", "23R", "24B",
                "25R", "26B", "27R", "28B", "29B", "30R",
                "31B", "32R", "33B", "34R", "35B", "36R"
                ]
        while True:
            bet = input("How much do you want to bet? ")
            if not bet.isdigit():
                print("Error. Invalid input, must be an integer. Try again")
                continue
            bet = int(bet)
            if bet > player.balance or bet < 1:
                print("Invalid bet amount")
                continue
            break
        while True:
            gamble = input("""Choose Odd or Even
""")
            if gamble.lower() == "even":
                break
            elif gamble.lower() == "odd":
                break
            else:
                print("Invalid option, you must choose odd or even")
                continue
        spins = random.randint(111,148)
        raterate = 1.00005
        rate = 1.0075
        x = 0.07
        for i in range(spins):
            x *= rate
            rate *= raterate
            print(wheel[i % 37])
            time.sleep(x)
            if i >= spins - 6:
                raterate *=1.08
        number = wheel[(spins - 1) % 37]
        if number == "0G":
            win = False
        else:
            value = int(number[:-1])
            num = value % 2
            if num == 1 and gamble.lower() == "odd":
                win = True
            elif num == 0 and gamble.lower() == "even":
                win = True
            else:
                win = False

        if win == True:
            player.balance += bet
            print(f"Congrats! You bet ${bet} and won ${bet}")
        else:
            print(f"Unfortunately you lost ${bet}")
            player.balance -= bet
        self.broke()
        while True:
            again_ask = input(f"""Your balance is now ${player.balance}, choose an option:
1. Play again
2. Play a different game
""")
            if again_ask == "1":
                return self.odd_even()
            elif again_ask.lower() == "2":
                self.home_page()
                return
            else:
                print("Invalid option. (1/2)")
                continue
class class_base:
    def __init__(self, name, useage, lost):
        self.name = name
        self.times_used = useage
        player.balancegiven = lost

    def show_status(self):
        print(f"Name: {self.name}  Balance: {player.balance}  Times Gambled: {self.times_used}  Money Earned: {self.stonks}  Money Lost: {player.balancegiven}")

class Slot_Machine(class_base):
    def __init__(self, name, money, useage, lost, probabilitytracker):
        super().__init__(name, money, useage, lost)
        self.win_chance = probabilitytracker

    def display_info(self): 
        print(f"{self.name} --- Times Used:{self.times_used}  Money Earned: {player.balancegiven}  Money Lost: {player.balance}")
    def play(self, player):
        newgamblername = input("Name yourself: ")
        balance = random.randint(45, 100)
        print(f"{newgamblername} enters a casino with only ${balance} to their name.")
        time.sleep(2.15)
        print("In the casino, there are 3 slot machines. One on the left, one on the right, and one in the middle.")
        time.sleep(2.87)
        gamblechoice = input("What would you like to do? (Type 'L' to use the left machine, 'M' to use the one in the middle, 'R' to use the right machine, 'A' for additional options, and anything else (besides the additional options) to leave the casino.) ")

        left_machine = Slot_Machine("Left Slot Machine", 0, 0, 0, random.randint(0, 34))
        left_machine_win_money = 30
        left_machine_win_rate = 65

        middle_machine = Slot_Machine("Middle Slot Machine", 0, 0, 0, random.randint(0, 99))
        middle_machine_win_money = 60
        middle_machine_win_rate = 250

        right_machine = Slot_Machine("Right Slot Machine", 0, 0, 0, random.randint(0, 9))
        right_machine_win_money = 9
        right_machine_win_rate = 25
        while player.balance > 0:
            while gamblechoice == "L" or gamblechoice == "M" or gamblechoice == "R" or gamblechoice == "A" or gamblechoice == "S" or gamblechoice == "LI" or gamblechoice == "MI" or gamblechoice == "RI":
                if left_machine.win_chance >= left_machine_win_rate:
                    ICantStopWinning = 0.1
                    if random.random() <= ICantStopWinning:
                        player.balance += left_machine_win_money
                        Newgambler.stonks += left_machine_win_money
                        left_machine.moneygiven += left_machine_win_money
                        left_machine.win_chance -= left_machine_win_rate
                        left_machine.win_chance / 2
                        time.sleep(1)
                        print(f"You won!!! You gained ${left_machine_win_money}. {player.name}'s wallet now has ${player.balance}.")
                    if random.random() > ICantStopWinning:
                        ICantStopWinning += 0.125
                        time.sleep(0.85)
                        print(f"....You lost. {player.name}'s wallet did not change.")

                if middle_machine.win_chance >= middle_machine_win_rate:
                    ICantStopWinning = 0.1
                    if random.random() <= ICantStopWinning:
                        player.balance += middle_machine_win_money
                        middle_machine.moneygiven += middle_machine_win_money
                        middle_machine.win_chance -= middle_machine_win_rate
                        middle_machine.win_chance / 2
                        print(f"You won!!! You gained ${middle_machine_win_money}. {player.name}'s wallet now has ${player.balance}.")
                    elif random.random() > ICantStopWinning:
                        ICantStopWinning += 0.125
                        time.sleep(0.85)
                        print(f"....You lost. {player.name}'s wallet did not change.")

                if right_machine.win_chance >= right_machine_win_rate:
                    ICantStopWinning = 0.1
                    if random.random() <= ICantStopWinning:
                        player.balance += right_machine_win_money
                        right_machine.moneygiven += right_machine_win_money
                        right_machine.win_chance -= right_machine_win_rate
                        right_machine.win_chance / 2
                        print(f"You won!!! You gained ${right_machine_win_money}. {player.name}'s wallet now has ${player.balance}.")
                    elif random.random() > ICantStopWinning:
                        ICantStopWinning += 0.125
                        time.sleep(0.85)
                        print(f"....You lost. {player.name}'s wallet did not change.")

                if gamblechoice == "L":
                    player.balance -= 1
                    player.balancegiven += 1
                    left_machine.win_chance += 1
                    left_machine.times_used += 1
                    Newgambler.times_used += 1
                    left_machine.money +=1
                    print(f"You used the left slot machine. {player.name}'s balance is now {player.balance}!")
                    time.sleep(0.5)
                    print(".")
                    time.sleep(0.3)
                    print("..")
                    time.sleep(0.2)
                    print("...")
                    if left_machine.win_chance < left_machine_win_rate:
                        time.sleep(0.85)
                        print(f"....You lost. {player.name}'s wallet did not change.")
                    gamblechoice = input("What would you like to do? (Type 'L' to use the left machine, 'M' to use the one in the middle, 'R' to use the right machine, 'A' for additional options, and anything else (besides the additional options) to leave the casino.) ")


                if gamblechoice == "M":
                    player.balance -= 1
                    player.balancegiven += 1
                    middle_machine.win_chance += 1
                    middle_machine.times_used += 1
                    Newgambler.times_used += 1
                    middle_machine.money +=1
                    print(f"You used the middle slot machine. {player.name}'s balance is now {player.balance}!")
                    time.sleep(0.5)
                    print(".")
                    time.sleep(0.3)
                    print("..")
                    time.sleep(0.2)
                    print("...")
                    if middle_machine.win_chance < middle_machine_win_rate:
                        time.sleep(0.85)
                        print(f"....You lost. {player.name}'s wallet did not change.")
                    gamblechoice = input("What would you like to do? (Type 'L' to use the left machine, 'M' to use the one in the middle, 'R' to use the right machine, 'A' for additional options, and anything else (besides the additional options) to leave the casino.) ")

                if gamblechoice == "R":
                    player.balance -= 1
                    player.balancegiven += 1
                    right_machine.win_chance += 1
                    right_machine.times_used += 1
                    Newgambler.times_used += 1
                    right_machine.money +=1
                    print(f"You used the right slot machine. {player.name}'s balance is now {player.balance}!")
                    time.sleep(0.5)
                    print(".")
                    time.sleep(0.3)
                    print("..")
                    time.sleep(0.2)
                    print("...")
                    if right_machine.win_chance >= right_machine_win_rate:
                        time.sleep(0.85)
                        print(f"....You lost. {player.name}'s wallet did not change.")
                    gamblechoice = input("What would you like to do? (Type 'L' to use the left machine, 'M' to use the one in the middle, 'R' to use the right machine, 'A' for additional options, and anything else (besides the additional options) to leave the casino.) ")

                if gamblechoice == "A":
                    print("Type 'S' to check your stats, 'LI' to check the information of the left slot machine, 'MI' to check the middle slot machine's information, and 'RI' to check the right slot machine")
                    time.sleep(3)
                    gamblechoice = input("What would you like to do? (Type 'L' to use the left machine, 'M' to use the one in the middle, 'R' to use the right machine, 'A' for additional options, and anything else (besides the additional options) to leave the casino.) ")

                if gamblechoice == "S":
                    self.show_status()
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

            if gamblechoice != "L" and gamblechoice != "M" and gamblechoice != "R" and gamblechoice != "A" and gamblechoice != "S" and gamblechoice != "LI" and gamblechoice != "MI" and gamblechoice != "RI":
                gamblechoice = "test"
            if gamblechoice == "test" and player.balance > 0 and player.balance != 0:
                print(f"You were financially responsible! You left the casino with ${player.balance}!")
                gamblechoice = "est"
                player.balance = -1
            if player.balance == 0:
            print("Your balance reached 0. You are now broke!")
            if player.balance < 0 and gamblechoice != "est":
            print(f"Your balance reached {player.balance}. You are in debt!")

class MC():
    def __init__(self, money, level, exp, debt):
        player.balance = money
        self.level = level
        self.exp = exp
        self.debt = debt

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
            player.balance += loan
            time.sleep(1)
            print("Now go back and win your money!")
            self.debt += (loan * interest)
    

    def debtcheck(self):
        if player.balance > self.debt:
            loans = False
            while loans == False:
                decision = input("You have enough to pay off your loan shark debt! Do you want to? (y/n)")
                if decision.lower() not in ["y","n"]:
                    print("Invalid input, (y/n)")
                elif decision.lower() == "y":
                    player.balance -= self.debt
                    self.debt = 0
                else:
                    self.debt *= interest
                    print(f"Your debt is now {self.debt}! Should've paid it off sooner!")
                    

            


    def gamble(self):
        re = True
        while re == True:
            re = False
            while True:
                gamble = input("How much money do you want to bet?")
                if not gamble.isdigit():
                    print("Invalid input!")
                    continue
                else:
                    gamble = int(gamble)
                    if gamble > player.balance or gamble <= 0:
                        print(f"Invalid amount! You have ${player.balance}!")
                        continue
                    else:
                        print(f"Okay, your bet is ${gamble}.")
                break
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
                player.balance += (gamble*(1+self.level*0.025))
            elif Tie == True:
                print("No money lost, no money won")
            else:
                player.balance -= gamble
            time.sleep(0.75)
            print(f"You now have ${player.balance}.")
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

            while True:
                again = input("Do you wanna go again? (y/n)")
                if again.lower() not in ["y","n"]:
                    print("Invalid input, (y/n)")
                    continue
                else:
                    break
            if again == "y" and player.balance > 0:
                re = True
            elif again == "y" and player.balance == 0:
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
            if self.debt > 0:
                self.debtcheck()
            
                    
                




        
        
""" 

you = MC(player.balance, 1, 0, 0)
you.gamble()
 """
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