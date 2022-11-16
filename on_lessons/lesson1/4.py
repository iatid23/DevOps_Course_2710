# a.
first = 7
second = 44.3
sumNum = first + second
print(sumNum)
multi = first * second
print(multi)
dv = second / first
print(dv)

# b.
a = 8
a = 17
a = 9
b = 6
c = a + b
b = c + a
b = 8
print(a)
print(b)
print(c)
strU = f"a val is = {a}, b var is {b}, c val is {c}"

print(strU)

# c(1). Is there a difference between the two lines below? Why?
# name = “john”
# name = ‘john’

# in python no - in bash sure - however in python we can use it as string inside string

# c(2).
# my_number = 5+5
# print("result is: "+my_number)
# casting
my_number = str(5 + 5)
print("result is: " + my_number)

# d.
x = 5
y = 2.36
print(x + int(y))
# output = 7

# one more challenge
a = 8
b = "123"
c = (a + int(b))

print(c)
