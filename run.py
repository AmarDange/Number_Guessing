# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import pyfiglet
from termcolor import colored


def Welcome():
    """
    Function to display home page
    """
    title = "Welcome  to  NUMBER  GUESSING  GAME "
    print(colored(pyfiglet.figlet_format(title), "green"))
Welcome()


def guess_number():
    random_number = random.randint(1, 20)
    player_name = input("Enter Your Name:  ")
    confirm_play = input("Would you like to start the game? (Enter yes/no): ")
    attempts = 0

    while confirm_play.lower() == "yes":

        guess = int(input("Guess any number between 1 to 50 : "))

        if guess < 1 or guess > 50:
            print("Please guess any number in the Range.")

        elif guess == random_number:
            print("@@@###$$$Congratulations ", player_name, 'You Win $$$###@@@')
            attempts +=1
            print("It took you ", attempts, "attempts to win this Game.")
            break
        elif guess > random_number:
            print("Hint: Please try with smaller number.")
            attempts +=1

        elif guess < random_number:
            print("Hint: Please try with larger number.")
            attempts +=1

    else:
        print("Thanks ", player_name, "for your Time.")

guess_number()

