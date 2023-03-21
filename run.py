# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import pyfiglet
from termcolor import colored


def Welcome(message):
    """
    Show a Welcome message.
    """
    # title = "Welcome  to  NUMBER  GUESSING  GAME "
    print(colored(pyfiglet.figlet_format(message), "yellow"))

Welcome("Welcome  to  Brain  Refreshing  GAME ")


def game():
    welcome("Welcome to Brain Refreshment Game\n")
    player_name = input("Enter Your Name: ").strip()

    print("\n")
    print("option [1] Guess_Number")
    print("option [2] Computer_Quiz")
    print("option [0] Exit the Brain Refershment Game.")
    print("\n")

    # In this case we don't actually care about option being an int
    # "1" is just as good as 1 as we're not performing any mathematical
    # operations on it.
    option = input("Enter your Game Option : ").strip()

    while option != "0":
        if option == "1":
            welcome("Welcome  to  NUMBER  GUESSING  GAME ")

            # We got the player name centrally above, but it's needed in the
            # actual game functions, so pass it in as a parameter.
            guess_number(player_name)
            
        elif option == "2":
            welcome("Welcome  to  Ask Question  GAME ")

            quiz(player_name)
            
        else:
            print("Invalid option")

        print("\n")
        continue_playing = input(
            "Enter yes to play again or anything else to exit: ").strip()

        if continue_playing.lower() != "yes":
            print("Thanks for using the programm. Goodbye")
            quit()

game()




def guess_number(player_name):
    random_number = random.randint(1, 50)
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

def ask_question(question, correct_answer):
    user_answer = input(question).strip()
    question_score = 0
    
    # Make sure the answer is not case sensitive, so that, for example
    # ""central processing unit" and "Central Processing Unit" grade the same.
    if user_answer.lower() == correct_answer.lower():
        print('Correct')
        question_score = 1
    else:
        print('Incorrect')

    return question_score

def quiz(player_name):
    score = 0
    score += ask_question(
        "Is the coding language Python, named after a snake? ", "no")
    score += ask_question(
        "What does CPU stand for? ", "central processing unit")
    score += ask_question("What does RAM stand for? ", "random access memory") 


questions = [
    {
        "question": "Is the coding language Python, named after a snake? ",
        "answer": "no"
    },
    {
        "question": "What does CPU stand for? ",
        "answer": "central processing unit"
    },
    {
        "question": "What does RAM stand for? ",
        "answer": "random access memory"
    }
]

def ask_question(question, correct_answer):
    user_answer = input(question).strip()
    question_score = 0
    
    # Make sure the answer is not case sensitive, so that, for example
    # ""central processing unit" and "Central Processing Unit" grade the same.
    if user_answer.lower() == correct_answer.lower():
        print('Correct')
        question_score = 1
    else:
        print('Incorrect')

    return question_score

def quiz():
    score = 0
    for question in questions:
        score += ask_question(question["question"], question["answer"])

    print("Your score is: " + str(score) + "/" + str(len(questions)))



# def quiz():
#     # We defined this already.
#     # Add the welcome message and continue playing prompt here like in
#     # guess_number()
#     pass

# def game():
#     welcome("Welcome to Brain Refreshment Game\n")
#     player_name = input("Enter Your Name: ").strip()

#     print("\n")
#     print("option [1] Guess_Number")
#     print("option [2] Computer_Quiz")
#     print("option [0] Exit the Brain Refershment Game.")
#     print("\n")

#     # In this case we don't actually care about option being an int
#     # "1" is just as good as 1 as we're not performing any mathematical
#     # operations on it.
#     option = input("Enter your Game Option : ").strip()

#     while option != "0":
#         if option == "1":
#             welcome("Welcome  to  NUMBER  GUESSING  GAME ")

#             # We got the player name centrally above, but it's needed in the
#             # actual game functions, so pass it in as a parameter.
#             guess_number(player_name)
            
#         elif option == "2":
#             welcome("Welcome  to  COMPUTER  QUIZ  GAME ")

#             quiz(player_name)
            
#         else:
#             print("Invalid option")

#         print("\n")
#         continue_playing = input(
#             "Enter yes to play again or anything else to exit: ").strip()

#         if continue_playing.lower() != "yes":
#             print("Thanks for using the programm. Goodbye")
#             quit()

# game()

# print("Wellcome to quiz game !!")
# print('NOTE: if your spelling is incorrect then it is considered as wrong answer')
# score = 0
# question_no = 0
# playing = input('Do you want to play ? ').lower()
# if playing == 'yes':
#     question_no += 1
#     ques = input(f'\n{question_no}. what does CPU stand for? ').lower()
#     if ques == 'central processing unit':
#         score +=1
#         print('correct! you got 1 point')
        
#     else:
#         print('Incorrect!')
#         print(f'current answer is --> central processing unit')

# # ------1
#     question_no += 1
#     ques = input(f'\n{question_no}. what does GPU stand for? ').lower()
    
#     if ques == 'graphics processing unit':
#         score +=1
#         print('correct! you got 1 point')
        
#     else:
#         print('Incorrect!')
#         print(f'current answer is --> graphics processing unit')

# # -----2
#     question_no += 1
#     ques = input(f'\n{question_no}. what does RAM stand for? ').lower()
    
#     if ques == 'random access memory':
#         score +=1
#         print('correct! you got 1 point')
        
#     else:
#         print('Incorrect!')
#         print(f'current answer is --> random access memory')

# # -----3
#     question_no += 1
#     ques = input(f'\n{question_no}. what does PSU stand for? ').lower()
    
#     if ques == 'power supply unit':
#         score +=1
#         print('correct! you got 1 point')
        
#     else:
#         print('Incorrect!')
#         print(f'current answer is --> power supply unit')


# # -----4
#     question_no += 1
#     ques = input(f'\n{question_no}. what does ROM stand for? ').lower()
    
#     if ques == 'read only memory':
#         score +=1
#         print('correct! you got 1 point')
        
#     else:
#         print('Incorrect!')
#         print(f'current answer is --> read only memory')


# # ------5 

# else:
#     print('thankyou you are out of a game.')
#     quit()

# print(f'\nnumber of question is {question_no}')
# print(f'your score is {score}')
# try:
#     percentage = (score *100)/question_no
# except ZeroDivisionError:
#     print('0% quetions are correct')

# print(f'{percentage}% questions are correct.')