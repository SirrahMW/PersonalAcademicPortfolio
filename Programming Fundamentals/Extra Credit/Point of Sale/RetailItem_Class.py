from RetailItem import RetailItem

def main():
    jacket = RetailItem('Jacket', 12, 59.95)
    print(jacket.get_description())
    print(jacket.get_stock())
    print(jacket.get_price())

    jeans = RetailItem('Designer Jeans', 40, 34.95)
    print(jeans.get_description())
    print(jeans.get_stock())
    print(jeans.get_price())

    shirt = RetailItem('Shirt', 20, 24.95)
    print(shirt.get_description())
    print(shirt.get_stock())
    print(shirt.get_price())


main()
