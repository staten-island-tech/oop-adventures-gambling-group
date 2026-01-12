import random
import time
class Roulette:
    def __init__(self, balance):
        self.balance = balance
    def home_page(self):
        intro = print(f"Welcome to Roulette! Your balance is currently ${self.balance}.")
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
        if self.balance <= 1:
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
            if bet > self.balance or bet < 1:
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
            self.balance += bet * 35
            print(f"Congrats! You bet ${bet} and won ${bet * 35}")
        else:
            print(f"Unfortunately you lost ${bet}")
            self.balance -= bet
        self.broke()
        while True:
            again_ask = input(f"""Your balance is now ${self.balance}, choose an option:
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
            if bet > self.balance or bet < 1:
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
            self.balance += bet * 17
            print(f"Congrats! You bet ${bet} and won ${bet * 17}")
        else:
            print(f"Unfortunately you lost ${bet}")
            self.balance -= bet
        self.broke()
        while True:
            again_ask = input(f"""Your balance is now ${self.balance}, choose an option:
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
            if bet > self.balance or bet < 1:
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
            self.balance += bet * 11
            print(f"Congrats! You bet ${bet} and won ${bet * 11}")
        else:
            print(f"Unfortunately you lost ${bet}")
            self.balance -= bet
        self.broke()
        while True:
            again_ask = input(f"""Your balance is now ${self.balance}, choose an option:
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
            if bet > self.balance or bet < 1:
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
            self.balance += bet * 8
            print(f"Congrats! You bet ${bet} and won ${bet * 8}")
        else:
            print(f"Unfortunately you lost ${bet}")
            self.balance -= bet
        self.broke()
        while True:
            again_ask = input(f"""Your balance is now ${self.balance}, choose an option:
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
            if bet > self.balance or bet < 1:
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
            self.balance += bet * 6
            print(f"Congrats! You bet ${bet} and won ${bet * 6}")
        else:
            print(f"Unfortunately you lost ${bet}")
            self.balance -= bet
        self.broke()
        while True:
            again_ask = input(f"""Your balance is now ${self.balance}, choose an option:
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
            if bet > self.balance or bet < 1:
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
            self.balance += bet * 5
            print(f"Congrats! You bet ${bet} and won ${bet * 5}")
        else:
            print(f"Unfortunately you lost ${bet}")
            self.balance -= bet
        self.broke()
        while True:
            again_ask = input(f"""Your balance is now ${self.balance}, choose an option:
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
            if bet > self.balance or bet < 1:
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
            self.balance += bet * 2
            print(f"Congrats! You bet ${bet} and won ${bet * 2}")
        else:
            print(f"Unfortunately you lost ${bet}")
            self.balance -= bet
        self.broke()
        while True:
            again_ask = input(f"""Your balance is now ${self.balance}, choose an option:
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
            if bet > self.balance or bet < 1:
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
            self.balance += bet
            print(f"Congrats! You bet ${bet} and won ${bet}")
        else:
            print(f"Unfortunately you lost ${bet}")
            self.balance -= bet
        self.broke()
        while True:
            again_ask = input(f"""Your balance is now ${self.balance}, choose an option:
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
            if bet > self.balance or bet < 1:
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
            self.balance += bet
            print(f"Congrats! You bet ${bet} and won ${bet}")
        else:
            print(f"Unfortunately you lost ${bet}")
            self.balance -= bet
        self.broke()
        while True:
            again_ask = input(f"""Your balance is now ${self.balance}, choose an option:
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
            if bet > self.balance or bet < 1:
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
            self.balance += bet
            print(f"Congrats! You bet ${bet} and won ${bet}")
        else:
            print(f"Unfortunately you lost ${bet}")
            self.balance -= bet
        self.broke()
        while True:
            again_ask = input(f"""Your balance is now ${self.balance}, choose an option:
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


game = Roulette(10000)            
game.home_page()
            
        

    


















# Bet Types:
#    Single number bet: pays 35 to 1. Also called “straight up.”
#    Double number bet: pays 17 to 1. Also called a “split.” 
#    Three number bet: pays 11 to 1. Also called a “street.”
#    Four number bet: pays 8 to 1. Also called a “corner bet.”
#    Five number bet: pays 6 to 1. Only one specific bet which includes the following numbers: 0-00-1-2-3.
#    Six number bets: pays 5 to 1. Example: 7, 8, 9, 10, 11, 12. Also called a “line.”
#    Twelve numbers or dozens: (first, second, third dozen) pays 2 to 1.
#    Column bet (12 numbers in a row): pays 2 to 1. 
#    18 numbers (1-18): pays even money. 
#    18 numbers (19-36): pays even money. 
#    Red or black: pays even money. 
#    Odd or even: bets pay even money.
"""     def buy_chips(self):
        casino_chips = [
            "White = $1",
            "Red = $5",
            "Blue/Brown/Orange = $10",
            "Green = $25",
            "Black = $100",
            "Purple = $500",
            "Yellow = $1000",
            "Orange = $5000"
        ]
        for chip in casino_chips:
            print(chip)
        chips = input("what type of chip would you like")
        if chips.lower() == "white":
            if self.balance >= 1:
                quantity = input("How many?") """