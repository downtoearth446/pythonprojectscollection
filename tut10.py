# list tutorial
grocery = ["Harpic", "Vim bar", "Deodrant", "Bhindi", "Lolly pop", 56]
print(grocery)
print(grocery[2])
numbers = [8, 5, 2, 3, 4, 9, 6, 7]
numbers.sort()# it do not return a list it changes old list
print(numbers)
numbers.reverse()# it do not return a list it changes old list
print(numbers)

# note that slicing functions return a new list they do not modify the old list
print(numbers[1:5])
print(numbers[:5])
print(numbers[5:])
print(numbers[1:5:2])
print(numbers[::3])

# negative slicing me -1 se jyada nahi lena
# for more details see video

print(numbers[::-1])
print(max(numbers))# finds maximum number in list
print(min(numbers))# finds minimum number in list
print(sum(numbers))# finds sum of all numbers in list
print(len(numbers))# prints length of list
numbers.append(20)# adds 20 at the end of list
print(numbers)

my_list = []# creates an empty list
my_list.append(10)
my_list.append(20)
my_list.append(30)
print(my_list)

my_num_list =list() # creates an empty list
my_num_list.append(10)
my_num_list.append(10)
my_num_list.append(20)
my_num_list.append(30)
print(my_num_list)

my_num_list.insert(1, 5) # inserts 5 at index no 1
print(my_num_list)

my_num_list.remove(10) # removes only 1st instance of given number
print(my_num_list)

my_num_list.pop() # removes lat element in list
print(my_num_list)

# mutable => can change
# immutable => can not change
# list is mutable eg :-
my_num_list[0] = 4
print(my_num_list)

# tuple is immutable eg :-
tp = (1, 2, 3)
print(tp)
# tp[0] = 4 this line gives error as tuple is immutable

# ek element ka tuple banane ke liye () ke sath ,
# bhi lagana padega nahi to tuple nahi banega

# swapping of two numbers in python
a = 5
b = 4
a, b = b, a
print(a, b)