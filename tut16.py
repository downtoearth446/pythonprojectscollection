op = input("Enter operator : ")
inp1 = int(input("Enter first number : "))
inp2 = int(input("Enter second number : "))
ans = 0
if inp1==45 and inp2==3 and op=="*":
    print(555)
elif inp1==3 and inp2 == 45 and op=="*":
    print(555)
elif inp1==56 and inp2 == 9 and op=="+":
    print(77)
elif inp1==9 and inp2 == 56 and op=="+":
    print(77)
elif inp1==56 and inp2 == 6 and op=="/":
    print(4)
elif op == "+":
    print(inp1+inp2)
elif op == "-":
    print(inp1-inp2)
elif op == "*":
    print(inp1*inp2)
elif op == "/" and inp2 != 0:
    print(inp1/inp2)
else:
    print("Invalid operation")
