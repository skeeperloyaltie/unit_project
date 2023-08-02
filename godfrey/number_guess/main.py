import random


def get_user_input(prompt, allowed_values=None):
    while True:
        user_input = input(prompt).strip().lower()
        if allowed_values is None or user_input in allowed_values:
            return user_input
        print("Invalid input. Please try again.")


def play_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Think of a number between a given range, and I will try to\
         guess it.")
    print("After each guess, provide feedback so I can improve my next guess.")
    
    # Get the range for the guessing game
    while True:
        try:
            min_value = int(input("Enter the minimum value of the range: "))
            max_value = int(input("Enter the maximum value of the range: "))
            if min_value < max_value:
                break
            print("Invalid range. The minimum value should be less than the\
                 maximum value.")
        except ValueError:
            print("Invalid input. Please enter valid integers for the range.")
    
    # AI's guessing loop
    while True:
        guess = random.randint(min_value, max_value)
        print(f"My guess is: {guess}")
        feedback = get_user_input("Is my guess correct, too high, or too low? \
            (Enter 'correct', 'high', or 'low'): ", 
                                  allowed_values=['correct', 'high', 'low'])
        
        if feedback == 'correct':
            print("Hooray! I guessed your number correctly!")
            break
        elif feedback == 'high':
            max_value = guess - 1
        else:  # feedback == 'low'
            min_value = guess + 1
        
        if min_value > max_value:
            print("Oops! It seems like you provided incorrect feedback.")
            print("Please make sure to provide accurate feedback.")
            break
    
    print("Thanks for playing the Number Guessing Game!")


if __name__ == "__main__":
    play_guessing_game()
