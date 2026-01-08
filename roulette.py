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
""")
            if choose == "1":
                self.single_number()
                again5 = False
            elif choose == "2":
                self.double_number()
                again5 = False
            else:
                print("Invalid option, you must choose a number.")
                again5 = True
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
            if gamble < 0 or gamble > 36:
                print("Invalid number. Try again, 0-36.")
                continue
            break

        spins = random.randint(111,148)
        raterate = 1.00008
        rate = 1.01
        x = 0.07
        for i in range(spins):
            x *= rate
            rate *= raterate
            print(wheel[i % 37])
            time.sleep(x)
        number = wheel[(spins - 1) % 37]       
        if gamble == int(number[:-1]):
            self.balance += bet * 35
            print(f"Congrats! You bet ${bet} and won ${bet * 35}")
        else:
            print(f"Unfortunately you lost ${bet}")
            self.balance -= bet
        while True:
            again_ask = input(f"Your balance is now ${self.balance}, do you want to play again?")
            if again_ask.lower() == "yes" or again_ask.lower() == "yeah":
                break
            elif again_ask.lower() == "no":
                self.home_page()
                return
            else:
                print("Invalid input. (Yes/No)")
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
            if gamble < 0 or gamble > 36:
                print("Invalid number. Try again, 0-36.")
                continue
            if gamble in numbers:
                print("You already chose that number. Choose another.")
                continue
            numbers.append(gamble)
        spins = random.randint(111,148)
        raterate = 1.00005
        rate = 1.01
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
        while True:
            again_ask = input(f"Your balance is now ${self.balance}, do you want to play again?")
            if again_ask.lower() == "yes" or again_ask.lower() == "yeah":
                break
            elif again_ask.lower() == "no":
                self.home_page()
                return
            else:
                print("Invalid input. (Yes/No)")
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