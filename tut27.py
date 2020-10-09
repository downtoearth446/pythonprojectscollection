# dealing with reading of files
f = open("harry.txt")
# no mode given to open function so it opens file in it's default mode
# that is read mode with text ,"rt" mode
# open function returns a file pointer to the file after opening that file
# file opened now reading the file using file pointer
content = f.read()
print(content)
# now closing the file using file_pointer.close()
f.close()
# file ko close isliye karte hain taki jo bhi resources file ko kholne me lage hain
# vo resource release ho jaye aur agar koi aur program file ko read karna chahta hai
# to vo aaram se read kar sake us file ko

# the above code can be written like this too
f = open("harry.txt","rt")
content = f.read()
print(content)
f.close()

# we can also specify the number of characters that read function should read
f = open("harry.txt","rt")
print(f.read(3))# this reads the first 3 characters in file
print(f.read(2))# this reads the next 2 characters in file
f.close()

# if we exceed the limit then only the characters which are available are read
f = open("harry.txt","rt")
print("1st time",f.read(300))# since 300 > characters in file so only the characters available are read
print("2nd time",f.read(200))# no character remaining hence nothing is read
f.close()

# to print the content line by line we use the file pointer
print("Printing line by line =>")
f = open("harry.txt","rt")
for line in f:
    print(line,end="")
f.close()
# once you read a file the file pointer becomes empty hence nothing is obtained on reading it

# another way to read lines is to use readline function
print("\nReading using readline function")
f = open("harry.txt","rt")
print(f.readline(),end="")
print(f.readline(),end="")
f.close()

# readlines function creates a list of lines
f = open("harry.txt")
print(f.readlines())
f.close()