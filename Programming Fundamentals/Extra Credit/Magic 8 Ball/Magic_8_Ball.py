# This program simulates a magic 8 ball
from random import randint

def main():
    # List to hold potential responses #
    responses = []
    # Append all responses from .txt to list #
    with open('8_Ball.txt', 'r') as r:
        for line in r:
            responses.append(line)
    # Variable for triggering another prompt #
    another = 'Y'
    while another.upper() == 'Y':
        # User input/question #
        print('Ask me a yes or no question:')
        q = input('')
        # Select response #
        a = responses[randint(0, 11)]
        # Print response #
        print(a)
        # Again? #
        another = input('Ask again? (Y/N): ')


# Call main #
main()
