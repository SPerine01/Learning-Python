# splitting and joining strings

s = 'This is a string of words'
print(s.split())
# split() returns a list of splits, where the string separates on the whitespace

print('This    is    a    string   of       words'.split())
# it folds all the whitespace together, then it splits the words up in a list

print(s.split('i'))
# this returns a list and splits the words on the i chars

words = s.split()
print(words)
for w in words:
    print(w)

new = ':'.join(words)
print(new)
# joins the string back together with a colon : in place of a space

