class HospitalQueue:
    def __init__(self):
        self.queue = []

    def add_patient(self):
        pid = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        symptoms = input("Enter Symptoms: ")
        self.queue.append({
            "ID": pid, "Name": name, "Symptoms": symptoms
        })
        print("Patient Added.")

    def display(self):
        if not self.queue:
            print ("No Patients Waiting.")
        for p in self.queue:
            print(p)

    def search(self):
        pid = input("Enter Patient ID: ")
        for p in self.queue:
            if p["ID"] == pid:
                print (p)
                return
        print ("Patient Not Found.")

    def update(self):
        pid = input("Enter Patient ID To Update: ")
        for p in self.queue:
            if p["ID"] ==pid:
                p["Name"] = input("New Name: ")
                p["Symptoms"] = input ("New Symptoms: ")
                print ("Patient Updated.")
                return
        print ("Patient Not Found.")

    def delete (self):
        pid = input("Enter Patient ID To Delete: ")
        for p in self.queue:
            if p["ID"] == pid:
                self.queue.remove(p)
                print("Patient Deleted.")
                return
        print("Patient Not Found.")

    def dequeue(self):
        if self.queue:
            print("Next Patient:", self.queue.pop(0))
        else:
            print("No Patients Remain In The Queue.")

    def peek(self):
        if self.queue:
            print("Next Patient:", self.queue[0])
        else:
            print("No Patients Are In The Queue.")
    def menu(self):
        while True:
            print("\n1.Add \n2.Display \n3.Search \n4.Update")
            print("5.Delete by ID \n6. Call Next \n7.Peek \n 8.Exit")
            choice = input("Enter Choice: ")

            if choice =="1":
                self.add_patient()
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
app = HospitalQueue()
app.menu()
        