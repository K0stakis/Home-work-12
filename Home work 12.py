# 1)Напишіть гру "rock-paper-scissors-lizard-Spock".
# Ввід даних гравцем - ченез input
# Рекомендую подумати над такими класами як Player, GameFigure, Game.
# Памʼятайте про чистоту і простоту коду (DRY, KISS), коментарі та докстрінги.
import random

def computer_random_number():
    return random.randint(1, 5)

computer_number = computer_random_number()

def cycle_user_input():
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        try:
            user_input = input(
                'Enter a number from 1 to 5.\nWhere:\n1 - scissors \n2 - paper \n3 - stone \n4 - lizard \n5 - Spock\n ')

            if user_input.isdigit():
                user_input = int(user_input)

                if 1 <= user_input <= 5:
                    return user_input
                else:
                    print('Wrong! Enter a number between 1 and 5.')
                    attempts += 1
            else:
                print('Wrong! Enter a NUMBER!')
            attempts += 1
            remaining_attempts = max_attempts - attempts
            print(f"Remaining attempts: {remaining_attempts}")

        except ValueError:
            print("Enter a valid number from 1 to 5")
    print("Exceeded maximum attempts")
    exit()

user_number = cycle_user_input()

def comparison_loop(computer_number, user_input):
    while computer_number == user_input:
        print("You and your opponent chose the same numbers. You need to make a choice again.")
        user_input = cycle_user_input()
        computer_number = computer_random_number()
    return game(computer_number=computer_number, user_input=user_number)

def game(computer_number, user_input):
    if computer_number == user_number:
        comparison_loop(computer_number=computer_number, user_input=user_number)
    elif computer_number == 1 and user_number == 2:
        print("GAME OVER! You lost! Scissors cut the paper.")
        return None
    elif computer_number == 1 and user_number == 3:
        print("GAME OVER! You won! The stone broke the scissors.")
        return None
    elif computer_number == 1 and user_number == 4:
        print("GAME OVER! You lost! The scissors cut off the head of your Lizard.")
        return None
    elif computer_number == 1 and user_number == 5:
        print("GAME OVER! You won! Spock smashes scissors")
        return None
    elif computer_number == 2 and user_number == 1:
        print("GAME OVER! You won! Your scissors cut the paper.")
        return None
    elif computer_number == 2 and user_number == 3:
        print("GAME OVER! You lost! Your stone was covered with your opponent's paper.")
        return None
    elif computer_number == 2 and user_number == 4:
        print("GAME OVER! You won! Your Lizard has eaten your opponent's paper.")
        return None
    elif computer_number == 2 and user_number == 5:
        print("GAME OVER! You lost! Paper disproves Spock.")
        return None
    elif computer_number == 3 and user_number == 1:
        print("GAME OVER! You lost! Your scissors were broken by your opponent's stone.")
        return None
    elif computer_number == 3 and user_number == 2:
        print("GAME OVER! Your choice brought you victory! The paper covers the stone.")
        return None
    elif computer_number == 3 and user_number == 4:
        print("GAME OVER! You won! Lizard eats paper.")
        return None
    elif computer_number == 3 and user_number == 5:
        print("GAME OVER! You won! Spock vaporizes rock.")
        return None
    elif computer_number == 4 and user_number == 1:
        print("GAME OVER! Your choice brings you victory! With your scissors you cut off the head of your opponent's Lizard.")
        return None
    elif computer_number == 4 and user_number == 2:
        print("GAME OVER! Your choice brought you defeat! The paper was eaten by an enemy Lizard.")
        return None
    elif computer_number == 4 and user_number == 3:
        print("GAME OVER! Your choice brought you victory! The stone crushed the Lizard.")
        return None
    elif computer_number == 4 and user_number == 5:
        print("GAME OVER! You lost! Lizard poisons Spock")
        return None
    elif computer_number == 5 and user_number == 1:
        print("GAME OVER! You lost! Spock smashes scissors.")
        return None
    elif computer_number == 5 and user_number == 2:
        print("GAME OVER! You won! Paper disproves Spock.")
        return None
    elif computer_number == 5 and user_number == 3:
        print("GAME OVER! You lost! Spock vaporizes rock.")
        return None
    elif computer_number == 5 and user_number == 4:
        print("GAME OVER! You won! Lizard poisons Spock.")
        return None

game(computer_number=computer_number, user_input=user_number)
