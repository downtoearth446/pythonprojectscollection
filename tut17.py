list1 = [5,4,3,2,1]
for i in list1:
    print(i)
name_lollypop = [["Harry",5],["Larry",10],["Carry",20],["Marie",60]]
for i in name_lollypop:
    print(i)
for name,lollypop in name_lollypop:
    print(name,"eats",lollypop,"lollypop")
dictionary = dict(name_lollypop)
print(dictionary)
# iterating over keys in dictionary
for i in dictionary:
    print(i)
# do not give any output
# for name,lollypop in dictionary:
#     print(name,"eats",lollypop,"lollypop")

# correct way
print(dictionary.items())
for name,lollypop in dictionary.items():
     print(name,"eats",lollypop,"lollypop")


# quiz soln

my_list = ["name",'c',123,2,0,-100,100,0.30,60.30,'*',"Shikhar"]
for item in my_list:
    if str(item).isnumeric() and item > 6:
        print(item)