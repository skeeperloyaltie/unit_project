import random 
import time

lower_bound = 1
upper_bound = 100

def main():
    print("Welcome to Guess the Number - AI Edition!")
    print("Think of a number between", lower_bound, "and", upper_bound)
    time.sleep(2)
    print("I will try to guess the number you are thinking of.")
    time.sleep(1)
    print("You only need to respond with 'H' if the guess is too high, 'L' if it's too low, and 'C' if I guessed correctly.")
    time.sleep(2)
    print("Let's get started!")
