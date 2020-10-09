# error handling in python
# try catch in c/c++
# try except in python
x = input("Enter number 1 : ")
y = input("Enter number 2 : ")
try:
    print("The sum of 2 numbers is :",int(x)+int(y))
except Exception as myerr:
    print(myerr)
print("Rest of the code runs !!!")