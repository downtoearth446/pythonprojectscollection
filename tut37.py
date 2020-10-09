# lambda functions
minus = lambda x,y: x-y
print(minus(3,2))

# sort function takes a key
# key takes a function 
a = [[1,2],[-2,100],[20,0]]

a_first = lambda a : a[1]
a.sort(key = a_first)
print(a)
