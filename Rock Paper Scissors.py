import random

game_list = ['Rock', 'Paper', 'Scissors']
comp_win = 0
user_win = 0


def run_win():
    run_code = print(f"Computer chose: {computer_choice}")
    print(f"You Chose: {user_choice}")
    print("You win!")
    return run_code


def run_loose():
    run_code = print(f"Computer chose: {computer_choice}")
    print(f"You Chose: {user_choice}")
    print("You loose!")
    return run_code


def run_draw():
    run_code = print(f"Computer chose: {computer_choice}")
    print(f"You Chose: {user_choice}")
    print("It's a Draw")
    return run_code


while True:
    computer_choice = random.choice(game_list)
    computer_choice = computer_choice.lower()
    user_choice = input("Rock, Paper, Scissors: ")
    user_choice = user_choice.lower()
    if computer_choice == 'rock' and user_choice == 'paper':
        run_win()
        user_win += 1
    elif computer_choice == 'scissors' and user_choice == 'rock':
        run_win()
        user_win += 1
    elif computer_choice == 'paper' and user_choice == 'scissors':
        run_win()
        user_win += 1
    elif computer_choice == 'scissors' and user_choice == 'paper':
        run_loose()
        comp_win += 1
    elif computer_choice == 'paper' and user_choice == 'rock':
        run_loose()
        comp_win += 1
    elif computer_choice == 'rock' and user_choice == 'scissors':
        run_loose()
        comp_win += 1
    elif computer_choice == user_choice:
        run_draw()
    elif user_choice == 'score':
        print(f"Current Score: User-{user_win}, Computer-{comp_win}")
    elif user_choice == 'quit':
        print("Game Over")
        print(f"The Final Score: User-{user_win}, Computer-{comp_win}")
        break
    else:
        print("Wrong Command")
