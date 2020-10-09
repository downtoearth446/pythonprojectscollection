# using modules
import random
import math

# let us study about random module
random_number = random.randint(0,5)
# this generates a random integer between 0 and 5 including 0 and 5
print(random_number)

x = random.random()
# this generates a random number (fraction too) between 0 and 1
print(x)

friends = ["Harry","Hermoine","Ron","Ginny","Neville"]
y = random.choice(friends)
# this chooses a random element from friends list
print(y)

# to install any module use command pip install module_name
# type the command in terminal (also available in pycharm)

# use math module
x = math.sin(30)
print(x)
y = math.sin(math.pi/6)
print(y)
