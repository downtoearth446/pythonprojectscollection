# global and local variables and global keyword
l = 10 # global variable
m = 20
def f1():
    l = 5 # local variable hence local is used m not re declared hence global variable is used
    n = "Local Variable not available outside the function f1 "
    print("Inside f1 l = ",l)
    print("Inside f1 m = ",m)
    print(n)
print("Before f1 l = ",l)
f1()
print("After f1 l = ",l)

# now how to change global variable inside the function
# using global keyword
a = 50
def f2():
    global a
    a = a+5
    print("Value of a inside f2 : ",a)
print("Value of a before calling f2 : ",a)
f2()
print("Value of a after calling f2 : ",a)

# note that in c/c++ we can call a function from another function but we can not define
# a function inside another function
# but in python we can define as well as call a function inside another function

def harry():
    x = 20 # local variable
    def rohan():
        global x # global variable
        x = 88
    print("Before Calling Rohan x = ", x)
    rohan()
    print("After Calling Rohan x = ", x)
# print("Before Calling Harry x = ",x) Error
harry()
print("After Calling Harry x = ",x)