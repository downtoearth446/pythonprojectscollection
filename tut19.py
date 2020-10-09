# break and continue
i = 0
while True:
    if i == 45:
        break
    print(i,end=" ")
    i += 1
i = 0;
print("\n")
while True:
    if i < 5:
        i = i+1
        continue # take me to the top of the loop skipping the bottom portion
    if i == 45:
        break
    print(i,end=" ")
    i += 1

print("\n")
while True:
    x = int(input("Enter a number greater than hundred : "))
    if x<=100:
        continue
    print("Congratulations !!! You entered a number greater than hundred ")
