from random import choice
from pip.decouple import config


def play_game():
    numbers = list(range(1, 11))
    money = config("MY_MONEY", cast=int, default=0)
    total_rounds = 0
    total_wins = 0
    total_losses = 0

    while True:
        print(f'Your current money is {money}$')
        sum = int(input('Enter your sum: '))
        bet = int(input('Choose a number from 1 to 10: '))
        total_rounds += 1
        if bet not in numbers:
            print("Invalid slot. Please choose a number between 1 and 10.")
            continue

        winning_slot = choice(numbers)
        if bet == winning_slot:
            money += (sum * 2)
            total_wins += 1
            print(f" You won {sum * 2}$!")
        else:
            money -= sum
            total_losses += 1
            print(f" you lost {sum}$.")

        play_again = int(input('Do you want to play again?(1-yes or 2-no): '))
        if play_again == 1:
            continue
        elif play_again == 2:
            print(f"Thanks for playing! Your score: rounds - {total_rounds}, "
                  f"wins - {total_wins}, losses - {total_losses}, money - {money}")
            break





