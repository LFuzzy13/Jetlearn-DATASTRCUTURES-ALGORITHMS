def fibonacci(n):
    if n == 0 or n == 1:# these are the base cases
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) # recursion part


for i in range(25):#how many times the sequence happens
    print(fibonacci(i))