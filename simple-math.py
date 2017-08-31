# ========================= Simple math
num = 5
print(num + 5)
print(num * 5)
print(num - 2)
print(num / 3)
# divison, answer will be a float

print(num // 3)
# floor division, ans will be an integer

print(num % 3)
# modulo, ans will be division remainer

print(divmod(5, 3))
# divmod function returns floor division ans and the remainder together


# print(num += 1)
# simplistic way of saying num = num + 1
# print(num -= 1)
# print(num *= 5)
# print(num //= 5)

# =========================


# ========================= Comparing values

print(num < 6)  # True
print(num > 6) # False
print(num >= 8) # False
print(num <= 5) # True
print(num == 5) # True
print(num != 10) # True
print(num != 5) # False

x, y = 5, 6
print(id(x))
print(id(y))
print(x is y) # False, different ids in memory
print(x is not y) # True

y = 5
print(id(y)) # now y has the same id as x since it was assigned to 5
print(x is y) # True, since both are 5 and 5 points to a specific id

x, y = [5], [5]
print(id(x))
print(id(y))
# lists are mutable, so they'll point to different ids in memory
print(x == y) # True, they have the same value
print(x is y) # False, they have different ids

# ========================= Operating on Boolean values

print(5 == 5)
print(7 < 5)
print(type(True))
print(True and False) #comparing both True and False together will make it False
print(True and True)
print(True or False)
print(False or False) #comparing Falso or False, when they're the same, is False
#and / or operators are Boolean operators
print(True & True) #this is bitwise arithmetic, not Boolean. It will print True

a, b = 0, 1
m, n = "zero", "one"
print(a < b) # prints True
print(m < n) # prints False

if (a < b) and (m < n):
    print('yes')
else:
    print('no')
# prints no


if (a < b) or (m < n):
    print('yes')
else:
    print('no')
# prints yes