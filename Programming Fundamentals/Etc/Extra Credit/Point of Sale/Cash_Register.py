from RetailItem import RetailItem

class CashRegister:
    # Initialize with a list that can hold the item objects #
    def __init__(self):
        self.sale = []

    # Mutator Methods #
    def purchase_item(self, item):
        self.sale.append(item)

    def clear(self):
        self.sale.clear()
        print('Sales list cleared.')

    # Accessor Methods #
    def get_total(self):
        # Total is established each time get_total is called #
        self.total = 0.00
        for i in range(len(self.sale)):
            self.total += self.sale[i].get_price()
        return self.total

    def show_items(self):
        print('-----Items-----')
        for i in range(len(self.sale)):
            print(self.sale[i].get_description())



def main():
    # Creating item objects #
    jacket = RetailItem('Jacket', 12, 59.95)
    jeans = RetailItem('Designer Jeans', 40, 34.95)
    shirt = RetailItem('Shirt', 20, 24.95)

    # Create the register #
    register = CashRegister()

    # Add items to the register #
    register.purchase_item(jacket)
    register.purchase_item(jeans)
    register.purchase_item(shirt)

    # Print results #
    register.show_items()
    print('----------------')
    print('Total: $' + format(register.get_total(), '.2f'))


main()
