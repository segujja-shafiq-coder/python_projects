import random
from termcolor import cprint

QUESTION = 'question'
OPTIONS = 'options'
ANSWER = 'answer'



def ask_question(index,question, options):
    print(f'Question {index} : {question}')
    for option in options:
        print(option)
        
    return input('your answer: ').upper().strip()  

def run_question(Quiz):
  
    random.shuffle(Quiz)

    score = 0

    for index , item in enumerate(Quiz ,1):
        user_choice=ask_question(index, item[QUESTION],item[OPTIONS])
        if user_choice==item[ANSWER]:
            cprint('Correct!', 'green')
            score+=1
        else:
            cprint(f'Wrong, the correct answer is {item[ANSWER]}','red')
    print(f'Quiz over! , Your final score is {score} out of {len(Quiz)}')
    
def main():
    Quiz = [
        {
            QUESTION : 'What is the capital of uganda?',
            OPTIONS : ['A. kampala', 'B. Arua', 'C. mukono','D. Mbarara'],
            ANSWER : 'A'
        },
        {
            QUESTION : 'Which planet is known as the red planet?',
            OPTIONS : ['A. Earth', 'B. Jupiter', 'C. Mars','D. Saturn'],
            ANSWER : 'C'
        },
        {
            QUESTION : 'What is the largest ocean on Earth?',
            OPTIONS : ['A. Indian', 'B. Atlantic', 'C. Arctic','D. Pacific'],
            ANSWER : 'D'
        }
          ]

    run_question(Quiz)
         
if __name__ == '__main__':
    main()