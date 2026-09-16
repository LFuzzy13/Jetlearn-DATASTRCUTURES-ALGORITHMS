def sumOfNumber(n):
    print(f"calling sumofnumber({n})")

    if n==0 or n ==1: #base case

        print("base case reached with n =", n)
        return n
    else:
        result = n +sumOfNumber(n-1)
        print(f"returning {result} for n =",n) #recursion
        return result

print("final answer:", sumOfNumber(50))
