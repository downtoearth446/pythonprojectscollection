# tell function tells us the position of file pointer in our file
f = open("harry.txt")
print(f.tell())
print(f.readline(),end="")
print(f.tell())
print(f.readline(),end="")
print(f.tell())

# to change the position of file pointer we use seek function
f.seek(5)
print(f.tell())
print(f.readline(),end="")
print(f.tell())
print(f.readline(),end="")
print(f.tell())

f.close()