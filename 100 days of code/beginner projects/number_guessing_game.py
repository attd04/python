import random

# comparing the number and the guess // gives output (too high / win)
def compare(num, ges):
        if num > ges:
            print("Too low.")
    
        if ges > num:
            print("Too high.")

        if ges == num:
            return f"\nYou guessed it! The number was {num}!"


print("Welcome to The Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.\n")
mode = input("Choose a difficulty. Type 'easy' or 'hard': ")

# determining how many lives
lives = 0
if mode == "easy":
    lives += 10
else:
    lives += 5

print(f"You have {lives} lives. Good luck!")

# randomly selected number
number = random.randint(1,100)

guess = int(input("\nMake a guess: "))

# compares numbers, reduces & prints lives, keeps guessing going
while number != guess:
    compare(number, guess)
    if lives != 1:
        print("Guess again.")
    
    if guess != number and lives != 0:
        lives = lives - 1

        if lives == 0:
            print("\nOut of lives! You lose.")
            quit()
        print("\n-------------------------")    
        print(f"You have {lives} lives left.")
        print("-------------------------\n")
        
    guess = int(input("Make a guess: "))
      
print(compare(number, guess))
