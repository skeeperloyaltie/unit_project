import random
import time

def generate_guess(lower_bound, upper_bound):
    return random.randint(lower_bound, upper_bound)

def get_user_feedback():
    user_response = input("Is the guess correct? (H/L/C): ").upper()
    while user_response not in ["H", "L", "C"]:
        print("Invalid input. Please enter 'H', 'L', or 'C'.")
        user_response = input("Is the guess correct? (H/L/C): ").upper()
    return user_response

def main():
    lower_bound = 1
    upper_bound = 100

    print("Think of a number between", lower_bound, "and", upper_bound)
    time.sleep(1)

    while True:
        guess = generate_guess(lower_bound, upper_bound)
        print("AI's guess:", guess)
        user_response = get_user_feedback()

        if user_response == "H":
            upper_bound = guess - 1
        elif user_response == "L":
            lower_bound = guess + 1
        else:  # user_response == "C"
            print("AI guessed correctly! The number was:", guess)
            break

if __name__ == "__main__":
    main()
