# Exercise 5
# Health Management System
def getdate():
    import datetime
    return datetime.datetime.now()
def enter():
    name = input("Enter client name : ")
    try:
        work = int(input("Enter 1 for Workout 2 for Diet : "))
        if name == "Harry" and work == 1:
            with open("HarryWorkout.txt","a") as f:
                inp = input("Enter the Name of Exercise : ")
                f.write("[ "+str(getdate())+" ] "+inp+"\n")
        elif name == "Harry" and work == 2:
            with open("HarryDiet.txt","a") as f:
                inp = input("Enter the Name of Dish : ")
                f.write("[ "+str(getdate())+" ] "+inp+"\n")
        elif name == "Rohan" and work == 1:
            with open("RohanWorkout.txt","a") as f:
                inp = input("Enter the Name of Exercise : ")
                f.write("[ "+str(getdate())+" ] "+inp+"\n")
        elif name == "Rohan" and work == 2:
            with open("RohanDiet.txt","a") as f:
                inp = input("Enter the Name of Dish : ")
                f.write("[ "+str(getdate())+" ] "+inp+"\n")
        elif name == "Hammad" and work == 1:
            with open("HammadWorkout.txt","a") as f:
                inp = input("Enter the Name of Exercise : ")
                f.write("[ "+str(getdate())+" ] "+inp+"\n")
        elif name == "Hammad" and work == 2:
            with open("HammadDiet.txt","a") as f:
                inp = input("Enter the Name of Dish : ")
                f.write("[ " + str(getdate()) + " ] " + inp + "\n")
        else:
            print("You are not a valid client !!")
    except Exception as err:
        print("Invalid Input !!")
def result():
    name  = input("Enter the name of client : ")
    try:
        work = int(input("Enter 1 for Workout 2 for Diet : "))
        if name == "Harry" and work == 1:
            with open("HarryWorkout.txt","a+") as f:
                f.seek(0)
                for i in f:
                    print(i,end="")
        elif name == "Harry" and work == 2:
            with open("HarryDiet.txt","a+") as f:
                f.seek(0)
                for i in f:
                    print(i,end="")
        elif name == "Rohan" and work == 1:
            with open("RohanWorkout.txt","a+") as f:
                f.seek(0)
                for i in f:
                    print(i,end="")
        elif name == "Rohan" and work == 2:
            with open("RohanDiet.txt","a+") as f:
                f.seek(0)
                for i in f:
                    print(i,end="")
        elif name == "Hammad" and work == 1:
            with open("HammadWorkout.txt","a+") as f:
                f.seek(0)
                for i in f:
                    print(i,end="")
        elif name == "Hammad" and work == 2:
            with open("HammadDiet.txt","a+") as f:
                f.seek(0)
                for i in f:
                    print(i,end="")
        else:
            print("You are not a valid client !!")
    except:
        print("Invalid Input !!!")
while(True):
    try:
        x = int(input("To Enter data press 1 , To Print data press 2 , To Exit press 3 : "))
        if x == 1:
            enter()
        elif x==2:
            result()
        elif x==3:
            break
        else:
            print("Invalid Input !!")
    except:
        print("Invalid Input !!!")