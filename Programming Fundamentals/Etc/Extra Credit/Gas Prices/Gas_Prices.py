# Global constants for the starting and ending year
START_YEAR = 1993
END_YEAR = 2013


# This function simply translates an int 1-12 to a month name
def month_num_to_text(month):
    if month == 1:
        return 'January'
    elif month == 2:
        return 'February'
    elif month == 3:
        return 'March'
    elif month == 4:
        return 'April'
    elif month == 5:
        return 'May'
    elif month == 6:
        return 'June'
    elif month == 7:
        return 'July'
    elif month == 8:
        return 'August'
    elif month == 9:
        return 'September'
    elif month == 10:
        return 'October'
    elif month ==11:
        return 'November'
    elif month == 12:
        return 'December'
    else:
        return 'Error, month number outside normal month range (1-12).'


# Function that calculates and returns the average price of a given year
def average_price_per_year(getYear, data):
    # Total is used to calculate average
    total = []
    # For each line, strip \n and pass to a function that pulls the price and year
    # from the line.
    for line in data:
        line = line.rstrip()
        price, year = get_price_year(line)
        # If the year we pass to the function is on this line, add the price to total
        if getYear == year:
            total.append(price)
    # Return the calculated average, formatted to 3 decimal places
    return format((sum(total) / len(total)), '.3f')


# Function that calculates and returns the average price of a given month
def average_price_per_month(getMonth, data):
    # Total is used to calculate average
    total = []
    # rstrip every line, and get the price and the month from each line
    for line in data:
        line = line.rstrip()
        price, month = get_price_month(line)
        # If the month is one we are looking for, append to total
        if getMonth == month:
            total.append(price)
    # Return calculated average, formatted to 3 decimal places
    return format((sum(total) / len(total)), '.3f')


# This function pulls the year and price from a line
def get_price_year(line):
    # Split the line using ":" as delimiter
    splitLine = line.split(':')     # This separates int values and float values
    # Change the price into a floating point value
    price = float(splitLine[1])
    # Split again, but only the date part of the line
    fullDate = splitLine[0].split('-')
    # Pull the year from that new list, and make it an integer
    year = int(fullDate[2]) 
    # Return both values
    return price, year


# This function pulls the month and price from a line
def get_price_month(line):
    # Split the line using ":" as a delimiter
    splitLine = line.split(':')
    # Change price into a floating point value
    price = float(splitLine[1])
    # Split again, but only the dates
    fullDate = splitLine[0].split('-')
    # Pull the month out of the full date
    month = int(fullDate[1])
    # Return both values
    return price, month


# This function does the processing for printing the annual prices
def get_average_annual_price():
    # Open the file and readlines
    with open('GasPrices.txt', 'r') as text:
        data = text.readlines()
    # Loop from starting to ending year, calling the average_price_per_year func each time
    print('---Average Annual Gas Prices---')
    for year in range(START_YEAR, END_YEAR + 1):
        print(year, ': $', average_price_per_year(year, data), sep='')


# This function does the processing for printing the monthly prices
def get_average_monthly_price():
    # Open the file and readlines
    with open('GasPrices.txt', 'r') as text:
        data = text.readlines()
    # Loop from 1-12 for each month and print the average price for each
    print('---Average Monthly Gas Prices---')
    for month in range(1,13):
        print(month_num_to_text(month), ': $', average_price_per_month(month, data), sep='')


# This function gets the date of the highest price
def get_highest_price():
    # Open the file and readlines
    with open('GasPrices.txt', 'r') as text:
        data = text.readlines()
    # Separate date and price into two separate lists
    dates = []
    prices = []
    # Pull the needed data from each line
    for line in data:
        line = line.rstrip()
        date, price = get_date_price(line)
        # Append to the two lists
        dates.append(date)
        prices.append(price)

    print('---Highest Price---')
    # Setting the value of the highest price
    highest = max(prices)
    for i in range(len(dates)):
        # When the index of the highest value is found, print the dates[i] string
        if prices[i] == highest:
            print(dates[i], ' has the highest price: $', prices[i], sep='')


# This function gets the date of the lowest price
def get_lowest_price():
    # Open the file and readlines
    with open('GasPrices.txt', 'r') as text:
        data = text.readlines()
    # Separate date and price into two separate lists
    dates = []
    prices = []
    # Pull the needed data from each line
    for line in data:
        line = line.rstrip()
        date, price = get_date_price(line)
        # Append to the two lists
        dates.append(date)
        prices.append(price)

    print('---Lowest Price---')
    # Setting the value of the lowest price
    lowest = min(prices)
    for i in range(len(dates)):
        # When the index of the lowest value is found, print the dates[i] string
        if prices[i] == lowest:
            print(dates[i], ' has the lowest price: $', prices[i], sep='')


# This function gets the date as a string and the price as a float from the line
def get_date_price(line):
    # Separate the line into date, and price
    splitLine = line.split(':')
    # Convert price into a float
    price = float(splitLine[1])
    # Leave date as a single string
    date = splitLine[0]
    # Return the values
    return date, price


# This function creates a .txt of the records ordered by price (high-low)
def make_high_to_low():
    with open('GasPrices.txt', 'r') as text:
        data = text.readlines()

    dates = []
    prices = []
    for line in data:
        date, price = get_date_price(line)
        dates.append(date)
        prices.append(price)

    with open('GasPrices_HighToLow.txt', 'w') as newText:
        newLine = ''
        for i in range(len(dates)):
            high = max(prices)
            search = prices.index(high)
            newLine = dates[search] + ':' + str(prices[search]) + '\n'

            prices.remove(prices[search])
            dates.remove(dates[search])

            newText.write(newLine)


# This function creates a .txt of the records ordered by price (low-high)
def make_low_to_high():
    with open('GasPrices.txt', 'r') as text:
        data = text.readlines()

    dates = []
    prices = []
    for line in data:
        date, price = get_date_price(line)
        dates.append(date)
        prices.append(price)

    with open('GasPrices_LowToHigh.txt', 'w') as newText:
        newLine = ''
        for i in range(len(dates)):
            low = min(prices)
            search = prices.index(low)
            newLine = dates[search] + ':' + str(prices[search]) + '\n'

            prices.remove(prices[search])
            dates.remove(dates[search])

            newText.write(newLine)


def main():
    get_average_annual_price()
    get_average_monthly_price()
    get_highest_price()
    get_lowest_price()
    make_low_to_high()
    make_high_to_low()


main()
