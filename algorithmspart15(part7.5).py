class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, value):
        self.main_stack.append(value)

        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.main_stack:
            print("The stack is empty")
            return

        value = self.main_stack.pop()

        if value == self.min_stack[-1]:
            self.min_stack.pop()

    def get_min(self):
        if not self.min_stack:
            print("The stack is empty")
        else:
            return self.min_stack[-1]

    def display(self):
        print("Main Stack:", self.main_stack)


# Example usage
s = MinStack()

s.push(5)
s.push(2)
s.push(8)
s.push(1)

s.display()
print("Minimum:", s.get_min())

s.pop()

s.display()
print("Minimum:", s.get_min())