#creating the parent class

class Product:

    def __init__(self,name,price,quantity):

        #different properties
        self.name = name
        self.price = price
        self.quantity = quantity

    #calculating the total

    def calculate_total(self):
        return self.price * self.quantity

    #displaying the product in the output
    def display_product(self):
        print("\nProduct:", self.name)
        print("Price:",self.price)
        print("Quantity:",self.quantity)
        print("Total Price:",self.calculate_total())

#creating the child class (discounted product)

class DiscountedProduct(Product):

    #properties
    def __init__ (self,name,price,quantity,discount):
        super().__init__(name,price,quantity)
        self.discount = discount

    #calculating discounted total
    def calculate_total(self):
        total = super().calculate_total()
        discount_amount = total * self.discount / 100
        return total - discount_amount

#displaying the discount
    def display_discount(self):
        print("Discount:",self.discount,"%")
#the item itself
product = DiscountedProduct(
    "Backpack",
    350,
    1,
    20,
)


#displaying the final output
product.display_product()
product.display_discount()

    
        


    