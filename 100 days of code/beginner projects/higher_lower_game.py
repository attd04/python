from replit import clear
import random
from art import logo
from art import vs

names = ["Christiano Ronaldo", "Nike", "Drake", "Will Smith", "Joe Biden", "Stephan Curry", "@dudewithsign", "Drew Barrymore", "Petsmart", "Starbucks", "Zendaya", "Kodak", "Valley", "COIN", "Chase Lawrence", "Bad Suns", "Madonna", "Eric Andre", "NY Knicks", "Bella Hadid", "Heconghc", "Gabby Douglas", "Autumn Tiede", "Troye Sivan", "Pewdiepie", "Emma Watson", "Priyanka Chopra Jonas", "9GAG", "Ronaldinho", "Maluma", "Camila Cabello"]

type = ["a Footballer", "a sportswear brand", "a rapper", "an actor, producer, comedian", "the U.S. President", "a professional basketball player", "a guy who holds up relatable cardboard signs in public spaces", "an actress", "a pet supplies store", "a chain coffee shop", "an actress", "a photography brand", "a pop, indie band", "an indie, alternative band", "lead singer of the band COIN", "an indie / rock band", "a musician", "a comedian", "a professional basketball team", "a super model", "a super model", "an olympic gymnast", "the programmer of this game", "a musician", "Youtuber","an actress", "an actress and musician", "social media platform", "Footballer", "a musician", "a musician"]

origin = ["Portugal", "United States", "Canada", "the United States", "the United States", "the United States", "the United States", "the United States", "the United States", "the United States", "the United States", "the United States", "Canada", "the United States", "the United States", "the United States", "the United States", "the United States", "the United States", "the United States", "China", "the United States", "the United States", "Australia", "Sweden", "Great Britain", "India", "China", "Brazil", "Colombia", "Cuba"]

followers = [5390000000, 264000000, 129000000, 62800000, 19300000, 48800000, 8000000, 16500000, 799000, 17900000, 165000000, 1000000, 74000, 175000, 44700, 100000, 18700000, 2500000, 3600000, 57100000, 159000, 1400000, 876, 13900000, 21700000, 69400000, 53000000, 52000000, 51000000, 50000000, 49000000]


# comparing followers, return true = right / false = incorrect
def compare(choice, followers, num_A, num_B, score):
    '''Compares followers, returns true if guess correct'''
    if choice == "A" and followers[num_A] > followers[num_B]:
        clear()
        return True
        
    elif choice == "B" and followers[num_A] > followers[num_B]:
        clear()
        return False
        
    elif choice == "A" and followers[num_B] > followers[num_A]:
        clear()
        return False
        
    elif choice == "B" and followers[num_B] > followers[num_A]:
        clear()
        return True

    elif choice == "A" or choice == "B" and followers[num_B] == followers[num_A]:
        clear()
        return True


def compare2(n_A, n_B, opt_A, opt_B, nms, typ, orig):
    if followers[n_A] > followers[n_B]:
        n_B = random.randint(0, 30)
        opt_B = f"{nms[n_B]}, {typ[n_B]} from {orig[n_B]}"
        
        if n_B == n_A:
            n_B = random.randint(0, 30)
            opt_B = f"{nms[n_B]}, {typ[n_B]} from {orig[n_B]}" 
    
        print(f"\nCompare A: {opt_A}")
        print(vs)
        print(f"Against B: {opt_B}")

    elif followers[n_A] < followers[n_B]: 
        n_A = random.randint(0, 30)
        opt_A = f"{nms[n_A]}, {typ[n_A]} from {orig[n_A]}"
        
        if n_A == n_B:
            n_A = random.randint(0, 30)
            opt_A = f"{nms[n_A]}, {typ[n_A]} from {orig[n_A]}"
    
        print(f"\nCompare A: {opt_A}")
        print(vs)
        print(f"Against B: {opt_B}")


        
# assigning options

num_A = random.randint(0, 30)
option_A = f"{names[num_A]}, {type[num_A]} from {origin[num_A]}"

num_B = random.randint(0, 30)
option_B = f"{names[num_B]}, {type[num_B]} from {origin[num_B]}"

while num_A == num_B:
    num_B = random.randint(0, 30)
    option_B = f"{names[num_B]}, {type[num_B]} from {origin[num_B]}"


# game starts
score = 0
print(logo)
print(f"\nCompare A: {option_A}")
print(vs)
print(f"Against B: {option_B}")
choice = input("\nWho has more ;pfollowers? Type 'A' or 'B?': ")

compare(choice, followers, num_A, num_B, score)


# adding score / continuing w game
while compare(choice, followers, num_A, num_B, score) == True:
    score += 1
    print(logo)
    print(f"You're right! Current score: {score}")
    compare2(num_A, num_B, option_A, option_B, names, type, origin)
    choice = input("\nWho has more followers? Type 'A' or 'B?': ")
    compare(choice, followers, num_A, num_B, score)
    

print(f"Sorry, that's wrong. Final score: {score}")
