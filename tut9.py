mystr = "Harry is a good boy"
print(mystr[6])
print(mystr[0:5]) # 0 to 4 not including 5 but including 0
print(len(mystr)) # gives length of string
#print(mystr[78]) gives error as 78 is out of range
print(mystr[0:78]) # error maaf ho gayi jitni hai utni le lo

print(mystr[0:5:2]) # har doosra character print hoga
# matlab ki ek character skip hoga in 0 to 5 excluding 5

print(mystr[0:]) # poora peeche tak lega
print(mystr[:5]) # shuru se le lega
print(mystr[:]) # poora le lega
print(mystr[::]) #last vale ko by default 1 le lega
print(mystr[::3]) # har 3rd character le lega means 2 character skip karega
print(mystr[::5559]) # think

# positive index starts from 0 from left to right
# negative index starts from -1 from right to left
#  H  a  r  r  y
#  0  1  2  3  4
# -5 -4 -3 -2 -1

print(mystr[-3:]) #till the end
print(mystr[-3:-1]) #not including -1 and including -3
print(mystr[::-1]) #string ko ulta kar dega
print(mystr[::-3]) #ulti string me skip karega pehle ulti karega
print(mystr.isalnum())#false due to spaces
print(mystr.isalpha())#false due to spaces
print(mystr.endswith('boy'))
print(mystr.count('b')) #counts number of b in mystr
mstr ="    jdgh      "
print(mstr.strip())
print(mstr.rstrip())
print(mstr.lstrip())
print(mystr.capitalize())
print(mystr.find('iss'))# finds and tells the index at which the given elemet is present
# if element is not present then prints -1
print(mstr.upper()) #converts each letter to upper case
print(mystr.lower()) #converts each letter to lower case
print(mystr.replace('is', 'are')) #replaces is with are
