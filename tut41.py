# Snake Water Gun
import random
print("Snake Water Gun")
print("The one who wins more in 10 times will be the winner")
comp = 0
user = 0
lst = ["s","w","g"]
i = 0
while i< 10:
    user_choice = input("Enter s for snake , w for water , g for gun : ").lower()
    computer_choice = random.choice(lst)
    if(computer_choice == user_choice):
        print(f"{i+1} Round Draw ")
        print(f"You : {user}")
        print(f"Opponent : {comp}")
    elif ((computer_choice == "s" and user_choice == "w") or (computer_choice == "w" and user_choice == "g") or (computer_choice == "g" and user_choice == "s") ):
        print(f"{i + 1} Round Opponent Wins")
        comp+=1
        print(f"You : {user}")
        print(f"Opponent : {comp}")
    elif ((computer_choice == "w" and user_choice == "s") or (computer_choice == "g" and user_choice == "w") or (computer_choice == "s" and user_choice == "g")):
        print(f"{i + 1} Round You Win")
        user += 1
        print(f"You : {user}")
        print(f"Opponent : {comp}")
    else:
        print("Invalid input !!! Try Again")
        i = i-1
    i += 1
if user>comp:
    print("You Win !!!")
elif user<comp:
    print("Better Luck Next Time !!!")
else:
    print("Draw !!!")