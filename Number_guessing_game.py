import random
    

number = random.randint(1,100)
while True:
    try:
        choice= int(input('Guess any number between 1 and 100 : '))
        if choice>number:
            print('Too high!')
        elif choice<number:
            print( 'Too low!')
        else:
            print('congratulations , you guessed the number')
            break  
    except ValueError:
        print('please enter a valid number')

    