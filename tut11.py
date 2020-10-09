#Dictionary and it's function
#Dictionary is key value pairs
d = {}
print(type(d))
d = []
print(type(d))
d = ()
print(type(d))
d1 = {"Harry":"Burger","Rohan":"Fish","Shukla":"Roti"}
print(d1)
print(d1["Harry"])
# Dictionary inside dictionary
d2 = {"Harry":"Burger","Rohan":"Fish","Shukla":"Roti","Shubham":{"Breakfast":"Bread","Lunch":"Kheer","Dinner":"Maggi"}}
print(d2)
print(d2["Shubham"])
print(d2["Shubham"]["Lunch"])
# Adding elements in dictionary
d2["Subscriber"] = "Junk Food"
d2[420] = "Ganja"
print(d2["Subscriber"])
print(d2[420])
print(d2)
# deleting elements in d2
del d2[420]
print(d2)
del d2["Shubham"]
print(d2)

# copy
d3 = d2
del d3["Subscriber"]
print(d3)
print(d2)
# on changing d3 d2 is also changed
d3["raju"] = "Samosa"
print(d3)
print(d2)
# so in this case d3 = d2 a new dictionary is not created it refers to previous dish
# to create a new dictionary from the previous dictionary we need to use copy function
d4 = d2.copy()
d4["Chutki"] = "Barfi"
print(d4)
print(d2)
# on changing d4,d2 is not changed
# get function in dictionary
print(d4.get("Chutki"))
# update function in dictionary
d4.update({"Leena":"Toffee"})
print(d4["Leena"])
print(d4.keys())
print(d4.items())
print(d4.values())
