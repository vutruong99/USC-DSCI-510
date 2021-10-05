#Import the random library
from random import randint

#Initialize a random number between 1 and 10
random_number = randint(1,10)

#Initialize the count value to keep track of the number of guesses
count = 1

#Try to execute the following flow
try:
	#Prompt the user for a guess
	guess = int(input("Guess the secret number: "))

	#While the user's guess is not correct
	while(guess != random_number):
		
		#Increase count by one
		count += 1

		#If the guess is greater than the number
		if (guess > random_number):

			#Print a hint saying that it is greater, also prompt a new guess
			guess = int(input("Your guess is higher than the secret number, try again: "))
		
		#If not
		else:

			#Print a hint saying that it is less, also prompt a new guess
			guess = int(input("Your guess is less than the secret number, try again: "))

	#Once the while loop finishes, the guess is equal to the random number, so print Correct! and the number of tries
	if count > 1:
		print("Correct! It takes you", count, "tries to get the number!")
	else:
		print("Correct! It takes you only", count, "try to get the number!")

#If the input is invalid, print error message
except:
	print("Invalid input")


