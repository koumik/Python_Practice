# 5) To find factorial of a number. Function Accepts number as an arguments.


def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
n=int(input("Enter a Number : "))
print(factorial(n))
