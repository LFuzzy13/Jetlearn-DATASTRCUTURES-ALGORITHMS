def countdown(n):

    if n == 0: 
        print("Lift Off!")
        return
    print (n)

    countdown(n-1)

countdown(10)
