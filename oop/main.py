import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    
    def __init__(self, name:str, price:float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod # Add a decorator
    def instantiate_from_csv(cls):
        # Use a context manager to read the csv file
        with open('oop/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # Count out floats that are point zero e.g. 5.0
        if isinstance(num, float):
            # Count out floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity} )"



print(Item.is_integer(6.9))


