import random as r
import math

#Greeting
print("Are you bored? Let's play a guessing game. You enter a range of numbers and the system chooses one arbitrarily. You gotta guess that number in minimum number of trials!")

#Collecting the domain of numbers to be guessed as user input 
minRange = int(input("Enter the minimum number: "))
maxRange = int(input("Enter the maximum number: "))

#instantiating the counter for number of guesses
numberOfGuesses = 0
#The 'ideal' number of guesses to be made by the user to win the game
minimumNumberOfGuesses = int(math.log2(maxRange - minRange + 1))

#The number to be guessed
systemChosenNumber = r.randint(minRange, maxRange)
print(systemChosenNumber)

#Checks the accuracy of the number guessed by the user
while(True):
    userGuess = int(input("Your guess: "))
    #Ensures that the user's guess is inside his/her provided range. Not considered as a guess so counter isn't bumped up
    if (userGuess > maxRange or userGuess < minRange):
        print("Out of range! Please try again.")
    elif (userGuess > systemChosenNumber):
        print("The number you chose is too high!")
        numberOfGuesses += 1
    elif (userGuess < systemChosenNumber):
        print("The number you chose is too low!")
        numberOfGuesses += 1
    else:
        print("Right guess!") 
        numberOfGuesses += 1
        #Checks if user won or lost
        print("Ideal number of guesses: " + str(minimumNumberOfGuesses))
        print("Number of guesses by you: " + str(numberOfGuesses))
        if (numberOfGuesses <= minimumNumberOfGuesses):
            print("Congratulations! You got it in minimal trials")
        else:
            print("Better luck next time!")
        break





    


