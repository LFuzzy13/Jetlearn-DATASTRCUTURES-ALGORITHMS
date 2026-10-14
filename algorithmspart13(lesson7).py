text = input("Enter A String: ")

stack =[]

for char in text:
    stack.append(char)

reversed_text = ""

while len(stack)>0:
    reversed_text = reversed_text + stack.pop()

print("Original String:", text)
print("Reversed String:", reversed_text)
