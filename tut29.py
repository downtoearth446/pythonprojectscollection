f = open("harry.txt","w") # text selected by default
f.write("Harry Bhai Bohot acche hain \n")
# agar file nahi bani hogi to ban jayegi
# aur agar bani hogi to uska content overwrite ho jayega
f.close()

# if we do not want to overwrite the content in the file then we will open the file in append mode

f = open("harry.txt","a")
f.write("Harry bhai bahut acche hain \n")
f.close()

# f.write returns the number of characters written in the file

f = open("harry.txt","a")
print(f.write("Hi Harry Bhai !!!\n"))
f.close()

# handle read and write both use r+

f = open("harry.txt","r+")
print(f.read())
f.write("You are a very good tutor harry bhai !!!\n")
f.close()