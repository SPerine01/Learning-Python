print("Something")
# print is a built in function, a function that comes with python

# custom functions are functions you create using the def method, they're reusable code. Referred to as just functions

def potatoCost(potatoPrice, amount, potatoType):
	cost = potatoPrice * amount
	print(potatoType)
	return(cost)

potatoCost(10, 10, 3.0)
