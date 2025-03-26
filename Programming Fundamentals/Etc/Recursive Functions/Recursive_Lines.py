def recursive(n, i=1, up=True):
    print('*' * i)  # Print "*" (i) times
    # If counting up, add 1 for the next print statement
    if up:
        i += 1
    # If not counting up, subtract 1 for the next print statement #
    else:
        i -= 1
    # When (i) hits the given value (n) to count to, start counting down #
    if i == n:
        up = False
    # As long as (i) remains above 0, recursively call the function #
    if i != 0:
        recursive(n, i, up)


# Call the function #
recursive(3)
