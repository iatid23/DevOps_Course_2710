a = "itamar"
b = "a"
print(a + " " + b)

c = 7
print(a + " " + str(c))

# one more way for connecting strings in python
# string interpolation
# f -string - the "F" tells the interpreter it's an injection string
print(f"{a} {b}")
print("{a} {b}")
# one more way for connecting strings in python
print("{} {}".format(a, b))
# one more way for connecting strings in python
print("%s %s" % (a, b))
# we let the print decide how to show it - it add space by itself
print(a, b)
# so:
dd = a + " " + b
print(dd)

er = 'itamar'
ee = "a"
et = 'hh "ita"'
print(et)

# better way
et = " itamar \" at\""
print(et)

# special notes
# \n => newline

et = " itamar \n \" at\""
print(et)

g = ''' lkhdfjkhsjjjjjjjjjjjj

jjj {a}'''
print(g)
