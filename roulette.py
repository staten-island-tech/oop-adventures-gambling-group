import random
import time
class Roulette:
    def __init__(self, balance):
        self.balance = balance
    def single_number(self):
        while again == True:
            wheel = [
                    "0G",
                    "1R", "2B", "3R", "4B", "5R", "6B",
                    "7R", "8B", "9R", "10B", "11B", "12R",
                    "13B", "14R", "15B", "16R", "17B", "18R",
                    "19R", "20B", "21R", "22B", "23R", "24B",
                    "25R", "26B", "27R", "28B", "29B", "30R",
                    "31B", "32R", "33B", "34R", "35B", "36R"
                    ]
            bet = input("How much do you want to bet?")
            if bet > self.balance:
                print("You don't have enough money in your balance as of right now.")
                again == True
            gamble = input("Choose a number")
            spins = random.randint(72,96)
            for i in range(spins):
                print(wheel[i % 37])
                time.sleep(0.05)
            number = wheel[spins % 37]       
            if gamble == number:
                balance += bet * 35
                print(f"Congrats! You bet ${bet} and won ${bet * 35}")
            else:
                print(f"Unfortunately you lost ${bet}")
                balance -= bet
            again = input(f"Your balance is now {self.balance}, do you want to play again?")
            if again.lower() == "yes":
                again == True
            else:
                again == False
            

            
        

    


















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