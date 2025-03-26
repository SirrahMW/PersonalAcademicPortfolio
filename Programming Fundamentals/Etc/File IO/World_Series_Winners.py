# Function to create the year and which team won #
def year_winner(datafile):
    # Empty dictionary for the file contents #
    d = {}
    # Starting year #
    year = 1903

    # Assign year as the key and the team as the value in dict #
    for line in datafile:
        d[year] = line.rstrip()
        # Add 1 to year for next iteration #
        year += 1

    # Return dict to call point #
    return d


# Function to create a dict with the team name : num of wins #
def win_count(d):
    # Empty dictionary for counting wins for each team #
    w = {}

    # Iterate over every key and value in the years list #
    for key, value in d.items():
        # If the team name is not present in the wins list, add it #
        if value not in w:
            w[value] = 1  # Initial win #
        # If the team name is already present, add 1 to it #
        elif value in w:
            w[value] += 1  # Additional wins #

    # Return dict to call point #
    return w


# Function to get user input and return information #
def get_results(d, w):
    print('Enter a year between 1903-2009 to see what team won that year:')

    # Get user input #
    try:
        search = int(input())

        # Validate user input #
        while search < 1903 or search > 2009:
            search = int(input('Please enter a valid year in range 1903-2009: '))

    # Try again if input is not integer value #
    except ValueError:
        print('ERROR: Please enter an integer value:')
        search = int(input())

    # Assign winner and total wins to an object #
    winner = d[search]
    totals = w[winner]

    # If the year entered has this string, then no series was played #
    if 'World Series Not Played' in winner:
        print('No World Series was played in', search)

    # Print results #
    else:
        print(search, 'Winner:', winner)
        print(winner, 'won', totals, 'World Series through 2009')


# Main function #
def main():
    with open('WorldSeries.txt', 'r') as datafile:
        years = year_winner(datafile)
        wins = win_count(years)
        get_results(years, wins)


# Call on main function #
main()

