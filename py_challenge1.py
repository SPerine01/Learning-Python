# Write a small program to ask for a name and an age
# When both values have been entered, check if the person is the right age to go 
# must be over 18 and under 31
# If they're welcome, welcome them with a nice message, otherwise send them a polite message refusing their entry




name = input("What's your name? ")
age = int(input("How old are you? "))

if (age > 18) and (age < 31):
	print("Welcome " + name + ", enjoy our festive holiday")
else:
	print("Sorry friend, you're not the proper age for this event")