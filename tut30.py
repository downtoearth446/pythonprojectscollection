#Exercise 4
try:
    x = int(input("Enter a number : "))
    y = int(input("Enter 1 for True and 0 for False : "))
    i = 0
    if y==1 :
        while i<x:
            j = 0
            while j<=i:
                print("*",end=" ")
                j+=1
            print("\n",end="")
            i+=1
    elif y==0:
        i = x-1
        while i>=0:
            j = i
            while j>=0:
                print("*",end=" ")
                j-=1
            print("\n",end="")
            i-=1
    else:
        print("Invalid value for true/false")
except Exception as err:
    print(err)