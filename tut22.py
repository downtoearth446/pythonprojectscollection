# operators in python

# arithmetic operators
a = 20
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) # gives rounded value after division
print(a**b) # a ki power b exponentiation
print(a%b) # gives remainder

# assignment operators
x = 5
print(x)
x += 10
print(x)
x -= 10
print(x)
x *= 5
print(x)
x /= 6
print(x)
x = 10
x %= 3
print(x)

# identity operators
x = 10
y = 5
print(x is y)
print(x is not y)
x = 5
print(x is y)
print(x is not y)

# membership operators
my_list = [1,2,3,4,5,6]
print(2 in my_list)
print(2 not in my_list)
print(7 in my_list)
print(7 not in my_list)

# Bitwise Operators
print(1 & 2)
print(1 | 2)