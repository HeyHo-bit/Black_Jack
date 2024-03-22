from hand import Chips



class Info:

    playing = True

    def hit(deck,hand):
        
        hand.add_card(deck.deal())
        hand.aces_case()

    def show_some(player,dealer):        
        print("\nDealer's Hand:")
        print(" <card hidden>")
        print('',dealer.cards[1])  
        print("\nPlayer's Hand:", *player.cards, sep='\n ')
        
    def show_all(player,dealer):
        print("\nDealer's Hand:", *dealer.cards, sep='\n ')
        print("Dealer's Hand =",dealer.value)
        print("\nPlayer's Hand:", *player.cards, sep='\n ')
        print("Player's Hand =",dealer.value)

    def player_busts(player,dealer,chips):
        print("Player busts!")
        Chips.lose_bet(chips)

    def player_wins(player,dealer,chips):
        print("Player wins!")
        Chips.win_bet(chips)

    def dealer_busts(player,dealer,chips):
        print("Dealer busts!")
        Chips.win_bet(chips)
        
    def dealer_wins(player,dealer,chips):
        print("Dealer wins!")
        Chips.lose_bet(chips)
        
    def push(player,dealer):
        print("Dealer and Player tie! It's a push.")