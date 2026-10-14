class Stack:

    def __init__(self,n):
        self.stack = []
        self.n = n

    def push (self,k):
        if len (self.stack) < self.n:
            self.stack.append(k)
        else:
            print("The Stack Is Full")

    def pop(self):
        if len(self.stack) == 0:
            print ("the stack is empty")
        else:
            self.stack.pop(-1)

    def top(self):
        if len(self.stack) == 0 :
            print("the stack is empty")
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def display(self):
        print(self.stack)

n = int(input("Enter The Total Amount Of Elements: "))
s = Stack(n)

while True:

    print ("\n --Stack Menu--")
    print ("1 : Push")
    print ("2 : Pop")
    print ("3 : Top")
    print ("4 : Size")
    print ("5 : Display")
    print ("6 : Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        k = input("Enter The Value To Add: ")
        s.push(k)

    elif choice == "2":
        s.pop()

    elif choice == "3":
        s.top()

    elif choice == "4":
        s.size()

    elif choice == "5":
        s.display()

    elif choice == "6":
        print ("Program Ended")
        break

    else:
        print ("Invalid Entry, Try Again")