# Recursion and Iteration
def factorial_iterative(n):
    fac = 1
    for i in range(1,n+1):
        fac = fac * i
    return fac
def factorial_recursive(n):
    if n<=1:
        return 1
    return n*factorial_recursive(n-1)
n = int(input("Enter the number whose factorial you want to calculate : "))
print("Factorial Iteratively : ",factorial_iterative(n))
print("Factorial Recursively : ",factorial_recursive(n))

def fibonacci(n):
    if(n<=1):
        return n
    return fibonacci(n-1)+fibonacci(n-2)
n = int(input("Which term of fibonacchi you want to get : "))
print("Fibonacchi Recursively : ",fibonacci(n))