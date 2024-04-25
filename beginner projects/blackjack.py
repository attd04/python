import random
from replit import clear



def deal_card():
    ''' Deals a random card // returns the card value'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calc_score(cards):
    '''Calculated score for desired team // returns sum of cards'''

    if sum(cards) == 21 and len(cards) == 2:
        return 0
        
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)  
        
    
    

def compare(user_score, com_score):
    if user_score == com_score:
        print("\nDraw.")

    elif com_score == 0:
        print("\nComputer has Blackjack! You lose.")

    elif user_score == 0:
        print("\nBlackjack! You win!!")

    elif user_score > 21:
        print("\nBust! You lose.")

    elif com_score > 21:
        print("\nComputer busts! You win!!")

    elif user_score > com_score:
        print("\nYou win!!")

    else:
        print("\nComputer wins!")

        

def blackjack():    
    user_cards = []
    com_cards = []
    
    
    
    
    game_over = False
    
    
    for _ in range(2):
        user_cards.append(deal_card())
        com_cards.append(deal_card())
    
    
    while not game_over:
        
        user_score = calc_score(user_cards)
        com_score = calc_score(com_cards)
        
        
        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {com_cards[0]}")
        
        
        if user_score == 0 or user_score > 21 or com_score == 0:
            game_over = True
        else: 
            draw_another = input("\nDo you want to draw another card? y or n: ")
            print("--------------------------------------")
            
            if draw_another == "y":
                user_cards.append(deal_card())
            
            else: 
                game_over = True
    
            
        
    while com_score != 0 and com_score < 17:
        com_cards.append(deal_card())
        com_score = calc_score(com_cards)
    
    
    print(f'\nYour final cards: {user_cards}, final score: {user_score}')
    print(f'Computers final cards: {com_cards}, final score: {com_score}\n')
    
    compare(user_score, com_score)
    
while input("\n\n Do you want to play Blackjack? y or n: ") == "y":
    clear()
    blackjack()

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
