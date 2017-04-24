# iterating through values

# using the for loop to iterate through a list, you can use it everytime you want to iterate through a list

filelist = [2015, 2017, 2019]

for item in filelist:
	print(item)

# prints each item in the list


for item in range(2015, 2030, 2):
	print(item)
# prints every other item in range, by a step of 2 (2015, 2017, 2019...)

for item in range(2015, 2030, 2):
	if item == 2025:
		print(item)
# prints 2025
