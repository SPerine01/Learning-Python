age = int(input("How old are you? "))

# using and/or
if (age < 16) or (age > 65):
	print("Enjoy your free time")
else:
	print("Have a good day at work")


x = input("Please enter some text: ")
if x:
	print("You entered '{}' ".format(x))
else:
	print("You didn't enter anything, that sucks")


# using not
print(not False)
print(not True)


new_age = int(input("How old are you? "))
if not(new_age < 18):
	print("You're old enough to vote")
	print("Cast you ballot")
else:
	print("You're only {0}, come back in {1} years".format(new_age, 18 - new_age))


# using in
parrot = "African Grey"

letter = input("Enter a character: ")

if letter in parrot:
	print("That's what we're looking for {}, good job".format(letter))
else:
	print("No, that's not it")


# using not & in
parrot = "African Grey"

letter = input("Enter a character: ")

if letter not in parrot:
	print("No, that's not it")
else:
	print("That's what we're looking for {}, good job".format(letter))
