# functions

# inbuilt function example
x = (9,4)
print(sum(x))

# press control and then click on the function to get it's documentation

# user defined functions
# declaration of function
def my_function():
    print("Hello you are in my_function")
# calling of function
my_function()

# function with parameters
def m_fun(a,b):
    print("The sum of a and b is :",a+b)
m_fun(5,6)

# function that returns some value
def mt_fun(a,b):
    """This is a docstring this is used to tell you about the functionality of our function this is the first line of function"""
    """This docstring is different from a normal comment notice the color"""
    return a+b
print("The sum of a and b is :",mt_fun(5,6))

print(str(mt_fun.__doc__)) # note the missing parenthesis