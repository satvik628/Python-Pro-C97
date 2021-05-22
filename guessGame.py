#Random is a command which is used for generating a random number,string etc. or select randomly from strings given
import random

# Starting heading of app
print("Welcome to Guess the number game")
print("Rules : You have 5 chances to guess and enter your guess in box . Remember you have to guess between 1 to 9 ")

# Creating a random number making variable
numbers=random.randint(1,9)

# Coverting variable to string 
number=str(numbers)


# Creating chances variable and giving it a initial value
chance=0



# Setting condition to check whether chances are less than 5 or not
while chance<5:
    
    # Creating Input box where player can enter his/her guess
    guess=input("Enter your guessed number make sure its 1 to 9 :")

    # if condition for checking answer and if its correct result as
    if(guess==number):
        print("Congratulations ! You guess is exact and YOU WON !!")
        # Breaking to stop their only and restart
        break

    elif(guess<number):
        print("Oops ! Your answer is wrong but you are too close")
        # Break Command
        break
    else:
        print("Oh ! That's so much guess little smaller one")

    # Incrementing 1 chance after each guess   
    chance= +1
    

# Added if condition so if player's all 5 guesses are wrong so it prints a message
if chance==5:
    print("You lose because your chances are now over . The number was "+number)