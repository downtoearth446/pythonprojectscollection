try:
    magic_number = 200
    no_of_guesses = 5
    t = False
    while no_of_guesses :
        x = int(input("Guess the number between 0 to 500 : "))
        if x==magic_number:
            print("Wow !! You guessed it right in",5-no_of_guesses+1,"guesses")
            t = True
            break
        elif x>magic_number and no_of_guesses-1:
            print("Try a smaller number. You have",no_of_guesses-1,"guesses remaining")
        elif x<magic_number and no_of_guesses-1:
            print("Try a larger number. You have",no_of_guesses-1,"guesses remaining")
        no_of_guesses -= 1
    if no_of_guesses == 0 and not t:
        print("Game Over !!!")
except:
    print("Invalid Input")