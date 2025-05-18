import random 


# generate  a random number between 0 - 100
num = random.randint(0, 100)

while True:
    # get user input as an int
    try:
        imp =int(input("guess a number: "))
    except:
        print("thats not a number")
        continue


    # check if input is greater than the random number
    if imp > num:
        print ("guess lower")
    # check if input is less than the random number
    elif imp < num:
        print("guess higher")
    # if it isent greater or less than then it has to be equal
    else:
        print("you win!")

        # check if user wishes to play again
        i = input("do you wish to play again? (y,n)")
        # if user answers yes
        if i == 'y':
            # generate  a random number between 0 - 100
            num = random.randint(0, 100)
            print("--------------------------")
            continue
        # if user answers no
        else:
            # ends the loop so the program terminates
            break




