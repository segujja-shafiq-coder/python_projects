import random


def roll_die():
    return random.randint(1,6)



def play_turn(player_name):
    total_score= 0
    print(f'\nplayer {player_name}`s turn') 
    while True:
        roll= roll_die()
        print(f'you rolled a {roll}')
        if roll == 1:
            return 0    
        total_score+=roll
        question=input('Do you want to roll again ? (y/n): ').lower
        if question!='y':
            return total_score

def main():
    scores= [0,0]
    current_player=0
    while True:
       player_name= int(current_player+1)
       total_score=play_turn(player_name) 
       scores[current_player]+=total_score 
       print(f'\n you scored {total_score} points this turn')
       print(f'current scores: player 1 : {scores[0]} and player 2 : {scores[1]}')
    
       if scores[current_player]>=100:
           print(f'{player_name} wins')
           break
       current_player=1 if current_player==0 else 0
    
if  __name__=='__main__':
    main()