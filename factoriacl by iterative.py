def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact * i
    return fact
n=int(input("Enter a number to find its factoriacl:"))
c=factorial(n)
print("factorial of number=",c)
