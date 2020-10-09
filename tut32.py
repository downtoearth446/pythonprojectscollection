# another way to open and close a file
with open("harry.txt") as f:
    print(f.tell())
    print(f.readline())
    print(f.tell())
    print(f.readlines())
    print(f.tell())
    # file is closed after this block
f = open("harry.txt")
print(f.readlines())
f.close()