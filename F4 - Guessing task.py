from random import randint

print("Welcome to the random number guessing game!\n")
print("You hav to enter an integer (whole) number to guess\n")
print("The game will tell you if you guess too high or too low!\n")

def guessing_game():
    answer = randint(1,100)
    guess = int(input("Guess the number: "))

    while guess != answer:
        
        if guess < answer:
            print("That's too low, try again")
            guess = int(input("Guess the number: "))
            
        elif guess > answer:
            print("That's too high, try again")
            guess = int(input("Guess the number: "))
    
    print("\nWell done, that's right!")    
    
    rerun()

def rerun():

    run_again = input("\nWould you like to guess again?\nPlease Type Y for Yes or N for No: ")
      
    if run_again.upper() == "Y":
        guessing_game()

    elif run_again.upper() == "N":
        print("Good Luck!")
        quit()

    else:
        rerun()

guessing_game()

input("\nPress ENTER to exit program")

