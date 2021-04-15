""" Create a program that allows the user to play a "High-Low"game.
This will allow the user to input any number and the output displayed will tell
the user whether or not the input was too high or too low or if they have
guessed the number correctly.  When the user gets the number correct,
the program will stop and will say that the user has
guessed the number correctly. """

#print text describing the game and how it works
print ("HELLO, WELCOME TO THE HIGH-LOW GAME")
print ("I'M THINKING OF A NUMBER BETWEEN 1 AND 100." )
print ("GUESS A NUMBER, AND I'LL TELL YOU IF YOU'RE TOO HIGH, TOO LOW, OR GOT IT RIGHT.")
print ("GOOD LUCK :)")
#first step is to generate random number
import random
ran_num = random.randrange(1,100)
#start the counter
count = 1
#get number or input from user
user_num = int(input("ENTER A NUMBER BETWEEN 1-100: "))
#create a while loop to check number
while user_num != ran_num:
#count +1
    count += 1
#if the number is > than the ran num then print TOO HIGH
    if user_num > ran_num:
        print("TOO HIGH!")
#get user input again
        user_num = int(input("ENTER A NUMBER BETWEEN 1-100: "))
#if the number is less than the ran num then print TOO LOW
    elif user_num < ran_num:
        print("TOO LOW!")
        user_num = int(input("ENTER A NUMBER BETWEEN 1-100: "))
#ask user input again
#if correct then print correct
    else:
        print("correct")

#print how many tries it took
print("IT TOOK YOU {} TRIES".format(count))