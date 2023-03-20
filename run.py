# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# import random
# import pyfiglet
# from termcolor import colored


# def Welcome():
#     """
#     Function to display home page
#     """
#     title = "Welcome  to  NUMBER  GUESSING  GAME "
#     print(colored(pyfiglet.figlet_format(title), "green"))
# Welcome()


# def guess_number():
#     random_number = random.randint(1, 20)
#     player_name = input("Enter Your Name:  ")
#     confirm_play = input("Would you like to start the game? (Enter yes/no): ")
#     attempts = 0

#     while confirm_play.lower() == "yes":

#         guess = int(input("Guess any number between 1 to 50 : "))

#         if guess < 1 or guess > 50:
#             print("Please guess any number in the Range.")

#         elif guess == random_number:
#             print("@@@###$$$Congratulations ", player_name, 'You Win $$$###@@@')
#             attempts +=1
#             print("It took you ", attempts, "attempts to win this Game.")
#             break
#         elif guess > random_number:
#             print("Hint: Please try with smaller number.")
#             attempts +=1

#         elif guess < random_number:
#             print("Hint: Please try with larger number.")
#             attempts +=1

#     else:
#         print("Thanks ", player_name, "for your Time.")

# guess_number()

print("Wellcome to quiz game !!")
print('NOTE: if your spelling is incorrect then it is considered as wrong answer')
score = 0
question_no = 0
playing = input('Do you want to play ? ').lower()
if playing == 'yes':
    question_no += 1
    ques = input(f'\n{question_no}. what does CPU stand for? ').lower()
    if ques == 'central processing unit':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> central processing unit')

# ------1
    question_no += 1
    ques = input(f'\n{question_no}. what does GPU stand for? ').lower()
    
    if ques == 'graphics processing unit':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> graphics processing unit')

# -----2
    question_no += 1
    ques = input(f'\n{question_no}. what does RAM stand for? ').lower()
    
    if ques == 'random access memory':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> random access memory')

# -----3
    question_no += 1
    ques = input(f'\n{question_no}. what does PSU stand for? ').lower()
    
    if ques == 'power supply unit':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> power supply unit')


# -----4
    question_no += 1
    ques = input(f'\n{question_no}. what does ROM stand for? ').lower()
    
    if ques == 'read only memory':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> read only memory')


# ------5 

else:
    print('thankyou you are out of a game.')
    quit()

print(f'\nnumber of question is {question_no}')
print(f'your score is {score}')
try:
    percentage = (score *100)/question_no
except ZeroDivisionError:
    print('0% quetions are correct')

print(f'{percentage}% questions are correct.')