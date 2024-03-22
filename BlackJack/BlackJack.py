from deck import Deck
from hand import Hand,Chips
from gameinfo import Info

if __name__ == '__main__':

    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')

    playing = True
    amount = Chips.deposit()

    def hit_or_stand(deck,hand):       
        global playing
        while True:
            x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
            
            if x[0].lower() == 'h':
                Info.hit(deck,hand)  # hit() function defined above

            elif x[0].lower() == 's':               
                print("Player stands. Dealer is playing.")        
                playing = False
                
            else:
                print("Sorry, please try again.")
                continue
            break

while (True):

    
    amount_bet =  Chips.get_bet()
    # Create & shuffle the deck, deal two cards to each player

    game_info = Info()
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    # Set up the Player's chips
    player_chips = Chips(amount,amount_bet) # remember the default value is 100    
 
    # Show cards (but keep one dealer card hidden)
    Info.show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        
        # Show cards (but keep one dealer card hidden)
        Info.show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            Info.player_busts(player_hand,dealer_hand,player_chips)
            break        


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            Info.hit(deck,dealer_hand)    
    
        # Show all cards
        Info.show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            Info.dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            Info.dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            Info.player_wins(player_hand,dealer_hand,player_chips)

        else:
            Info.push(player_hand,dealer_hand)        
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break


    # Prompt the Player for their bet
    
   