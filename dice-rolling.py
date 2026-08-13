import random

while True:
    Question=input('Roll the dice (y/n): ').lower()
    if Question=='y':
        die_1=random.randint(1,6)
        die_2=random.randint(1,6)
        output=(f'{die_1},{die_2}')
    elif Question== "n":
        output='Thanks for playing!'
        break
    else:
        output='invalid choice!'
    print(output)
        
