import random

ROCK='r'
PAPERS='p'
SCISSORS='s'

options ={ROCK:'Rock',PAPERS:'papers',SCISSORS:'Scissors'}
choices=tuple(options.keys())

def get_user_choice():
    while True:
        user_choice=input('rock ,papers or scissors (r,p,s): ').lower()
        
        if user_choice  in choices:
            return user_choice
        else:
            print('invalid choice')
            
def display_choices(user_choice,computer_choice):
     print(f'computer chose , {options[computer_choice]}')
     print(f'You chose , {options[user_choice]}')
     
def determine_winner(user_choice, computer_choice):
    if user_choice==computer_choice:
        output="It's a Tie"
    elif(
        (user_choice ==ROCK and computer_choice==SCISSORS) or
        (user_choice==SCISSORS and computer_choice==PAPERS) or
        (user_choice==PAPERS and computer_choice==ROCK)):
        output='you Win'
    else:
        output='you lose'
    print(output)   
        
def play_game():
    while True:
        computer_choice= random.choice(choices)
        
        user_choice=get_user_choice()
        
        display_choices(user_choice,computer_choice)
        
        determine_winner(user_choice, computer_choice)
        
        continuity= input('do you want to continue? (y/n): ').lower()
        if continuity== 'n':
            break
play_game()