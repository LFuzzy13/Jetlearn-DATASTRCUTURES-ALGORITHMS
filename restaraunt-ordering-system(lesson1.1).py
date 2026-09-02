class Order:

    def __init__(self,customer):
        self.customer = customer
        self.items = []
        self.total = 0

    def add_item(self,item,price):
        self.items.append((item,price))
        self.total +=price

    def display_bill(self,price):
        print("\nCustomer:",self.customer)

        print("Ordered Items :")
        for item in self.items:
            print(item,"£",price)
        print("Total: £",self.total)

order1 = Order("John Johnson")

order1.add_item("Hamburger ", 5.50)
order1.add_item("Hamburger ", 5.50)
order1.add_item("Fries ", 2.75)
order1.add_item("Soft Drink ", 5.99)
order1.add_item("Ice Cream ", 5)
order1.add_item("Strawberry Milkshake", 7.25)
order1.add_item("Chicken Nuggets", 3.99)

order1.display_bill()