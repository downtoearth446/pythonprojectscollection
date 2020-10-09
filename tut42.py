# how to pass list and dictionary to a function (not necessary they are optional arguments)
# args and kwargs
# args and kwargs are optional arguments passed to a function
# the order of normal arguments args and kwargs must be same as given in this line
# else there will be a error
# the list is converted into tuple while passing in this way
# it is not necessary to name them as args and kwargs it is just a convention
# args has one * it is used to pass a list to a function list changes into tuple
# kwargs has ** it is used to pass a dictionary to a function dictionary remains a dictionary
# args can be used to pass tuple in the same way tuple remains a tuple


# Code 1
# def printfxn(normal,*args,**kwargs):
#     print("\n \n \n")
#     print(normal)
#     print(type(args))
#     print(type(kwargs))
#     for i in args:
#         print(i)
#     for key,value  in kwargs.items():
#         print(f"{key} is our {value}")
#
# students = ["Harry","Rohan","Meetu","Manu","Potter"]
# leaders = {
#     "Harry":"Coder",
#     "Rohan":"Leader",
#     "Meetu":"Cheater",
#     "Manu":"Gangster",
#     "Potter":"Looser"
# }
# n = "Pyare Pyare Bacche"
# printfxn(n)
# printfxn(n,*students)
# printfxn(n,*students,**leaders)


# same way to do as above
# Code 2
def printfxn(normal,args,kwargs):
    print("\n \n \n")
    print(normal)
    print(type(args))
    print(type(kwargs))
    for i in args:
        print(i)
    for key,value  in kwargs.items():
        print(f"{key} is our {value}")

students = ["Harry","Rohan","Meetu","Manu","Potter"]
leaders = {
    "Harry":"Coder",
    "Rohan":"Leader",
    "Meetu":"Cheater",
    "Manu":"Gangster",
    "Potter":"Looser"
}
n = "Pyare Pyare Bacche"
# printfxn(n)
# printfxn(n,students)
printfxn(n,students,leaders)