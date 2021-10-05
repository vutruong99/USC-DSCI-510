#Try to execute the following flow
try:
	#Get the user's input in inches
	uInput = int(input("Enter the inches input: "))
	
	#Create a dictionary to store the values for the units
	dictionary = dict()

	#Calculate how many miles are there in the input (1 mile = 63360 inches)
	if (uInput // 63360 > 1):
		dictionary["miles"] = uInput // 63360
	else:
		dictionary["mile"] = uInput // 63360

	#Re-calculate the input after calculating the value for miles
	uInput = uInput % 63360
	
	#Calculate how many yards are there in the input (1 yard = 36 inches)
	if (uInput // 36 > 1):
		dictionary["yards"] = uInput // 36
	else:
		dictionary["yard"] = uInput // 36

	#Re-calculate the input after calculating the value for yards
	uInput = uInput % 36

	#Calculate how many feet are there in the input (1 foot = 12 inches)
	if (uInput // 12 > 1):
		dictionary["feet"] =  uInput // 12
	else:
		dictionary["foot"] = uInput // 12

	#Re-calculate the input after calculating the value for feet
	uInput = uInput % 12

	#The remainder is the value for inches
	if (uInput > 1):
		dictionary["inches"] = uInput
	else:
		dictionary["inch"] = uInput

	#Loop through the dictionary and print values and keys that are not zero
	print("You entered")
	for key in dictionary:
		if dictionary[key] !=0 :
		
			print(dictionary[key], key)

#If something is wrong, print the error
except:
	print("Invalid input")
