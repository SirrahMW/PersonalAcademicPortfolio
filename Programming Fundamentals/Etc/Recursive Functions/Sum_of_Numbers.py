def sum_all(n, v=0):  # Contain a value of zero to add to
    print(v)  # First, print the current value we are at
    if n > 0:  # While the given value is not zero
        v += n  # Add the value of the given number to our current value
        sum_all(n - 1, v)  # Recurse with one less than the given number

# Call the function #
sum_all(10)
