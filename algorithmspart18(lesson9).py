class Orderprocessor:
    def __init__(self):
        self.queue = []

    def add_order(self):
        pid = input("Enter Order ID: ")
        name = input("Enter Customer Name: ")
        symptoms = input("Enter Order: ")
        self.queue.append({
            "ID": pid, "Name": name, "Order": symptoms
        })
        print("Order Added.")

    def display(self):
        if not self.queue:
            print ("No Orders Queueing.")
        for p in self.queue:
            print(p)

    def search(self):
        pid = input("Enter Order ID: ")
        for p in self.queue:
            if p["ID"] == pid:
                print (p)
                return
        print ("Order Not Found, this order may have been completed already.")

    def update(self):
        pid = input("Enter Order ID To Update: ")
        for p in self.queue:
            if p["ID"] ==pid:
                p["Name"] = input("New Name: ")
                p["Order"] = input ("New Order: ")
                print ("Order Updated.")
                return
        print ("Order Not Found.")

    def delete (self):
        pid = input("Enter Order ID To Delete a completed or canceled order.: ")
        for p in self.queue:
            if p["ID"] == pid:
                self.queue.remove(p)
                print("Order Deleted.")
                return
        print("Order Not Found, have you completed this already?")

    def dequeue(self):
        if self.queue:
            print("Next Order:", self.queue.pop(0))
        else:
            print("No Customers Remain In The Queue.")

    def peek(self):
        if self.queue:
            print("Next Order:", self.queue[0])
        else:
            print("No Customers Are In The Queue.")
    def menu(self):
        while True:
            print("\n1.Add \n2.Read Pending Orders \n3.Search \n4.Update")
            print("5.Delete by ID \n6. Call Next Order \n7.Look at current order \n 8.Exit")
            choice = input("Enter Choice: ")

            if choice =="1":
                self.add_order()
            elif choice == "2":
                self.display()
            elif choice == "3":
                self.search()
            elif choice == "4":
                self.update()
            elif choice == "5":
                self.delete()
            elif choice == "6":
                self.dequeue()
            elif choice == "7":
                self.peek()
            elif choice == "8":
                break
            else:
                print("Invalid Choice, Please Try Again.")
app = Orderprocessor ()
app.menu()
        