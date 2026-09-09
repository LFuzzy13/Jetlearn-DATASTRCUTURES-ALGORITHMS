#parent class
class BankAccount:

    #creating the properties
    def __init__(self,account_number,holder_name,balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    #how much is being deposited
    def deposit(self, amount):
        self.balance += amount
        print ("£", amount, "deposited successfully")
    #withdrawing money
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance += amount
            print ("£", amount, "withdrawn successfully")
        else:
            print("insuffient funds")
    #showing balance
    
    def show_balance(self):
        print("\nAccount Holder:", self.holder_name)
        print("Balance : £", self.balance)
#creating the child class

class PremiumAccount(BankAccount):

    #basic properties
    def __init__ (self,account_number,holder_name,balance):
        super().__init__(account_number,holder_name,balance)
        self.cashback_rate = 7.5

    #amount of cashback
    def cashback (self,amount):
        cashback = amount * self.cashback_rate / 100
        self.balance += cashback

        print ("Cashback Recieved : £", cashback)

    #showing premium benefits

    def show_premium_benefits(self):
        print("Cashback Rate",self.cashback_rate, "%")


#accounts

#account 1
account1 = PremiumAccount(
    "ACC7423",
    "John Johnson",
    1200
)

account1.show_balance()
account1.withdraw(700)
account1.cashback(700)
account1.deposit(1350)
account1.show_premium_benefits()
account1.show_balance()


#account 2
account2 = PremiumAccount(
"ACC3503",
"Brian Brianson",
2300
)

account2.show_balance()
account2.withdraw(275)
account2.cashback(275)
account2.deposit(827)
account2.show_premium_benefits()
account2.show_balance()
    
