
MAX_BET = 10000
MIN_BET = 1

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

    def aces_case(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 


class Chips:
    
    def __init__(self,amount,amount_bet):
        self.total = amount 
        self.bet = amount_bet
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

    def deposit():
        while True:
                amount = input("How much would you like to deposit? $")
                if amount.isdigit():
                    amount=int(amount)
                    if amount > 0:
                        break
                    else:
                        print("Amount can't be 0.")
                else:
                    print("Please enter a number.")     

        return amount
        
    def get_bet():
        while True:
            amount_bet = input("How much would you like to bet? $")
            if amount_bet.isdigit():
                amount_bet=int(amount_bet)
                if MIN_BET <= amount_bet <= MAX_BET:
                    break
                else:
                    print(f"Amount can be between ${MIN_BET} - ${MAX_BET}.")
            else:
                print("Please enter a number.")

        return amount_bet