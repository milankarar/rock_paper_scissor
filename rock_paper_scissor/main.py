import random

def play(user, computer):

    if user == computer:
        return "It's a tie"
    if is_win(user, computer):
        return 'You'
    else:
        return 'Computer'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r')\
        or (player == 's' and opponent == 'p'):
        return True
    else:
        return False

user = input("Choose a move: (r) for rock (p) for paper (s) for scissor ").lower()

computer = random.choice(['r', 'p', 's'])

result = play(user, computer)

user_move = None

computer_move = None


if user == 'r':
    user_move = 'rock'

elif user == 'p':
    user_move = 'paper'

elif user == 's':
    user_move = 'scissor'
    
else:
    print('Wrong Input')

if computer == 'r':
    computer_move = 'rock'

elif computer == 'p':
    computer_move = 'paper'

elif computer == 's':
    computer_move = 'scissor'

if result.startswith('Its') and user_move != None:
    print(f"You choosed {user_move} and the computer also choosed {computer_move} and {result}!!")

elif result.startswith('You') or result.startswith('Computer') and user_move != None:
    print(f"You choosed {user_move} and the computer choosed {computer_move} and {result} won!!")