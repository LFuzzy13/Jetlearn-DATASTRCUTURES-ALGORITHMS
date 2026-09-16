def factorial(n):

    if n == 1:
        print("Reaced Base Case") #when reaches 1 program stops (base case)
        return 1
    else:
        print (f"Calling factorial({n-1})") #recursion case
        return n * factorial(n-1)

print(factorial(999)) # how many times


