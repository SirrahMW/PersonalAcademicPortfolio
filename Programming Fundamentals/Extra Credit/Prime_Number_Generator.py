# This program takes a user's input and decides if it is prime and shows all
# prime numbers that come before the number

def main():
    # User input #
    n = int(input('Enter a whole number greater than 1: '))
    while n <= 1:
        n = int(input('Enter a whole number greater than 1: '))

    # Lists #
    allNums = []
    allPrimes = []

    # Add all numbers up to n into a list #
    for i in range(2, n):
        allNums.append(i)

    # Pick the primes out of that list #
    for x in allNums:
        if is_prime(x):
            allPrimes.append(x)

    # Print whether n is prime #
    if is_prime(n):
        print(n, 'is prime!')
    else:
        print(n, 'is not prime!')

    # Print all primes up to n #
    print(allPrimes)

# Function to more easily determine a prime number #
def is_prime(n):
    prime = True
    for i in range(2, n):
        if (n % i) == 0:
            prime = False
    return prime


main()
