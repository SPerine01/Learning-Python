# name = input("What's your name?: ")
# age = input("How old are you, {0}? ".format(name))
# print(age)
# # input function returns a string datatype

# name = input("What's your name?: ")
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)

# if age >= 18:
# 	print("You're old enough to vote")
# 	print("Please vote in the next election!")
# else:
# 	print("Please come back in {0} years.".format(18 - age))

print("Let's play! Guess a number between 1 - 10")
guess = int(input())

# if guess < 4:
# 	print("That's not it. Guess a little higher")
# 	guess = int(input())
# 	if guess == 4:
# 		print("You got it! Whoo hoo!")
# 	else:
# 		print("Sorry, that's wrong")
# elif guess > 4:
# 	print("That's a little too high.")
# 	guess = int(input())
# 	if guess == 4:
# 		print("You got it! Yay!")
# 	else:
# 		print("Nope, that's not it.")
# else:
# 	print("You got it right on the first try! Whoohoo!")


# make the if else statement leaner
if guess != 4:
	if guess < 4:
		print("That's not it. Guess a little higher")
	else: # guess must be greater than 5
		print("Nope. Guess a little lower")

	guess = int(input())
	if guess == 4:
		print("You got it! Yay!")
	else:
		print("Sorry, that's not it.")
else:
	print("You got it right on the first try! Whoohoo!")
