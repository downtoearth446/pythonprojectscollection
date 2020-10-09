s = set()
print(type(s))

# making a set from list
s = set([1, 2, 3, 4])
print(s)

# or the same thing can be done like this
l = [1,2,3,4]
r = set(l)
print(r)

# set has unique values in it
p = set([1,1,2,3,4,4])
print(p)

# set also arranges the values in sorted order really not sure about this line
p = set([4,2,2,1,3])
print(p)

# adding values in set
p.add(5)
p.add(6)
p.add(5)
print(p)

# union of set p with another set
p1 = p.union({6,7,8})
print(p,p1)

t = set([10,11,12])
p2 = p1.union(t)
print(p1,p2)

# intersetion of one set with another set
x = p2.intersection(t)
print(p2,x)

# basic functions
print(len(t))
print(min(t))
print(max(t))

# is dijoint set
print(x.isdisjoint(t))
print(x.isdisjoint({1,2,3}))

# removing element from set
x.remove(10)
print(x)