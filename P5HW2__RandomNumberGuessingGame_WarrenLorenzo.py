# CTI-110
# P5HW2: Random Number Guessing Game
# Lorenzo Warren
# April 22, 2018
#

# Use the random module
import random

# set constant values
secret = 55

def main():
    number = int(input('Guess what the secret number is ? '))
    for guess in range(number):
        # Guess the secret number
        secret = random.randint(1, 100)
        if secret > 55:
            print('Too high, try again')
        else:
            print('Too low, try again')
        if secret == 55:
            print('WOW congratulations you have guessed the corrent number')
        # Want to play again?
        again = input('Play again? (y = yes): ')
        number = int(input('Guess what the secret number is ? '))


# call the main function.
main()
