year = 2012
realYear = 2017

if year == realYear:
	print("Yup, this is the year!")
else:
	print("Nope, that's not it")

# print is a built in function
# custom functions are functions you create using the def method, they're reusable code

def potatoCost(potatoPrice, amount, potatoType):
	cost = potatoPrice * amount
	print(potatoType)
	return(cost)

potatoCost(10, 10, 3.5)