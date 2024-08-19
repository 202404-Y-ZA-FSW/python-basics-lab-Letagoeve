import random

computer_number = random.randint(1, 100) # Generate a random number between 1 and 100
attempts=0

while True:
     # prompt the user to guess a number
    user_input = input("Guess a number between 1 and 100: ")

    if user_input.isdigit():
        user_input = int(user_input) #convert the user input to integer
        attempts += 1 #increment the attempt counter
        
        # provide feedback based on the user's guess
        if user_input < computer_number:
            print("Too low! Try again!")
        elif user_input > computer_number:
            print("Too high! Try again!")
        else:
            print(f"Congratulations! Numbers match! You guessed the number in {attempts} attempts.")   
            # exit the loop since the correct number was guessed        
            break
        
    else:
        #handle invalid input
        print("Invalid input. Please enter a valid number.")
