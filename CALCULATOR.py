print('whenever we use the prompt input python converts it into a string')
a=input('enter 1 no')
b=input('enter 2 no')
c=a+b
print(c)
print('so here it is clear that\n on using prompt input python treats it as a string\n'
      'and not as a number')
print(' this can be corrected as follows ')
a=input("enter 1 no")
b=input('enter 2 no')
c=int(a)+int(b)
print(c)
print(' but even this has a drawback that only integers are valid here')
print('the command float can be used for integers as well as decimal nos ')
a=input('enter 1st no')
b=input('enter 2nd no')
c=float(a)+float(b)
print(c)
d=input("press ENTER to exit")



