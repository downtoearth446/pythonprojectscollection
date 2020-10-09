# time module
# using time module to calculate the execution time of a program
# for loop and while loop are equally efficient
# time() returns the time
import time
initial = time.time()
print("Initial time : ",initial)
i = 0
initial = time.time()
while i<50:
    print(i)
    i+=1
print("While loop ran in : ",time.time()-initial)
initial1 = time.time()
for i in range(50):
    print(i)
print("For loop ran in : ",time.time()-initial1)
print(time.asctime(time.localtime(time.time())))
print(time.localtime(time.time()))
# time fxn gives time
# local time gives localtime in tuple format
# asctime converts it into readable format
for i in range(50):
    time.sleep(2)
    print(time.asctime(time.localtime(time.time())))
# sleep function gives you the required delay
# such as a delay of 2 seconds as given above