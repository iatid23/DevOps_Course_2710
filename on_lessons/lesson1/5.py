# lesson 2 - 3/11/22

import importFile

name = 'itamar'
if name == 'itamar':
    print('your name is itamar')
elif name == 'at':
    print('you are at')
else:
    print('hi')

numbers = [1, 2, 4, 3, 5, 6, 4, 3]

is_male = False
print(numbers)
#
# if 4 in numbers:
#     print('yes')
# if type(is_male) == int:
#     if 4 in is_male:
#         print('yesssss')
# # how to check type of var - pre defined func
# print(type(is_male))


for i in numbers:
    print(i)

numbers2 = range(len(numbers))
print(numbers2)
print(type(numbers2))

for t in numbers2:
    print(numbers2[t])

listFromRange = [*numbers2]
print(listFromRange)

num = [*range(3, 20)]
print(num)
num2 = [*range(3, 20, 2)]
print(num2)

x = 0
while x < 30:
    x += 1
    if x == 6:
        continue
    if x == 3:
        pass
    else:
        print(f'its here {x}')

##7 boom!
# xcr = 0
# while xcr <= 100:
#     if (xcr % 7) == 0:
#         print('BOOM!!!!')
#     elif str(7) in str(xcr):
#         print(f'it Has A - 7  : {xcr}')
#     else:
#         print(f'number -  {xcr}')
#     xcr += 1
print('############################')


def seven_boom():
    xcr2 = range(1, 101)
    for num in xcr2:
        if (num % 7) == 0:
            print('BOOM!!!!')
        elif str(7) in str(num):
            print(f'it Has A - 7  : {num}')
        else:
            print(f'number -  {num}')
        num += 1


def seven_boom2(x):
    for num in x:
        if (num % 7) == 0:
            print('BOOM!!!!')
        elif str(7) in str(num):
            print(f'it Has A - 7  : {num}')
        else:
            print(f'number -  {num}')
        num += 1


seven_boom()
f =70
boom_range = range(1, f)
seven_boom2(boom_range)




importFile.something_boom(130, 3)
rng = input("Enter your range num:")
boom = input("Enter your boom num:")
importFile.something_boom(int(rng), int(boom))
