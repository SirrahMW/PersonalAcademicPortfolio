def create_deck():
    # Create a dictionary with each card and its value
    # stored as key-value pairs.
    deck = {'Ace of Spades': 1, '2 of Spades': 2, '3 of Spades': 3,
            '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6,
            '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9,
            '10 of Spades': 10, 'Jack of Spades': 10,
            'Queen of Spades': 10, 'King of Spades': 10,

            'Ace of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3,
            '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6,
            '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9,
            '10 of Hearts': 10, 'Jack of Hearts': 10,
            'Queen of Hearts': 10, 'King of Hearts': 10,

            'Ace of Clubs': 1, '2 of Clubs': 2, '3 of Clubs': 3,
            '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6,
            '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9,
            '10 of Clubs': 10, 'Jack of Clubs': 10,
            'Queen of Clubs': 10, 'King of Clubs': 10,

            'Ace of Diamonds': 1, '2 of Diamonds': 2, '3 of Diamonds': 3,
            '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6,
            '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9,
            '10 of Diamonds': 10, 'Jack of Diamonds': 10,
            'Queen of Diamonds': 10, 'King of Diamonds': 10}

    # Return the deck.
    return deck


def draw_card(deck):
    # Popitem was not correctly pulling a random card, so I used choice from 
    # the random module to correctly acquire a random card
    from random import choice
    card = choice(list(deck))
    value = deck.pop(card)

    # Print the card that was pulled
    print('[', card, ']')

    # Allow player to select what the value of the ace is
    if value == 1:
        print('You got an Ace, should it be valued at 1 or 11?')
        ace = int(input('Enter 1 or 11: '))
        while ace != 1 and ace != 11:
            ace = int(input('Enter 1 or 11: '))
        value = ace

    return value


def blackjack(deck):
    # Initialize player card values
    hand = [draw_card(deck), draw_card(deck)]

    print('Cards total:', sum(hand))
    print(str(hand).strip('[]'))

    again = input('\nDraw? (Y/N): ')

    while again.upper() == 'Y' and sum(hand) < 21:
        hand.append(draw_card(deck))
        print('Cards total:', sum(hand))
        print(str(hand).strip('[]') + '\n')
        if sum(hand) < 21:
            again = input('Draw? (Y/N): ')

    return sum(hand)


def determine_winner(player1, player2):
    if player1 > 21 and player2 > 21:
        print('Draw!')
    elif player1 > 21 >= player2:
        print('Player 2 wins!')
    elif player2 > 21 >= player1:
        print('Player 1 wins!')
    elif player1 > player2:
        print('Player 1 wins!')
    elif player2 > player1:
        print('Player 2 wins!')
    elif player1 == player2:
        print('Draw!')


def main():
    deck = create_deck()

    print('\n---Player 1---')
    player1 = blackjack(deck)
    print('\n---Player 2---')
    player2 = blackjack(deck)

    determine_winner(player1, player2)


main()
