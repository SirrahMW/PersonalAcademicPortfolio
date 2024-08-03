class RetailItem:
    # Initialization #
    def __init__(self, description, inStock, price):
        self.description = description
        self.inStock = inStock
        self.price = price

    # Mutator Methods #
    def set_price(self, price):
        self.price = price
        
    def set_description(self, description):
        self.description = description
    
    def set_stock(self, inStock):
        self.inStock = inStock

    # Accessor Methods #
    def get_price(self):
        return self.price

    def get_description(self):
        return self.description

    def get_stock(self):
        return self.inStock
