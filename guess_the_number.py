import random

print("Welcome to guess the number game!!")
while True:
    attempts=0
    computer_input=random.randint(1,10)

    while True:
            user_input=int(input("Guess the number!"))
            if user_input==computer_input:
                print("you have correctly guessed the number.\n"+ f"Your attempts:{attempts}")
                break
            
            elif user_input > computer_input:
                print("Your guessing is too high!")
                attempts+=1
                continue
            elif user_input < computer_input:
                print("Your guessing is too low!")
                attempts+=1
                continue
            
    play_again=input("Do you want to play again?(y/n)").lower()
    if play_again == 'y':
        continue
    else:
         print("Thanks for playing the game!")

        
