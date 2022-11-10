def print_hello():
    print('hello')


def get_name(name):
    print(f'your name is - {name}')


def calculate():
    print("lets see how much is 5 + 3.2:")
    print(5 + 3.2)


def sum(num1, num2):
    return num1 + num2


def str(str1, str2):
    return str1 + " " + str2


def check_age():
    while True:
        num = input('please tell me your age:')
        try:
            c = int(num)
            return int(c)
        except ValueError:
            print("You didn't enter a number please choose again")
            continue


def check_char():
    while True:
        try:
            char = input('please tell me your last name first letter:')
            int(char)
            print("You entered a number not char, please try again")
            continue
        except ValueError:
            if char == '' or char == ' ':
                print("You entered empty char, please try again")
                continue
            elif len(char) > 1:
                print("You entered too many chars, please try again")
                continue
            else:
                return char


def check_currency():
    while True:
        num = input('please tell me the Current shekels-dollar currency:')
        try:
            c = float(num)
            return c
        except ValueError:
            print("You didn't enter a number please choose again")
            continue


def check_tf():
    while True:
        tf = input('Did you fly abroad (true/false)?')
        try:
            c = float(tf)
            print("You didn't enter a number please choose again")
            continue
        except ValueError:
            if tf == 'true' or tf == 'True' or tf == 'TRUE' or tf == 'FALSE' or tf == 'false' or tf == 'False':
                return tf
            else:
                print("You didn't enter a True Or False please enter again")
                continue


def check_apt():
    while True:
        apt = input('please tell me your Your apartment number:')
        try:
            c = int(apt)
            if c <= 0:
                print("It can't be right, please try again:")
                continue
            else:
                return int(c)
        except ValueError:
            print("You didn't enter a number please choose again")
            continue

def check_num(num):
    while True:
        try:
            c = int(num)
            return False
        except ValueError:
            print("You didn't enter a number please choose again")
            return True
#######################################################################################
def first():
    print('1)')

    chk = True
    while chk:
        x = input('please enter first number\n')

        chk = check_num(x)
    chk = True
    while chk:
        y = input('please enter second number\n')
        chk = check_num(y)

    if int(x) > int(y):
        print('BIG')
        print('###################################')
    elif x == y :
        print('Its Equal!! ')
        print('###################################')
    else:
        print('small')
        print('###################################')


def second():
    print('2)')
    for loop in range(5):
        print(f'iteration number - {loop + 1}')
    print('###################################')


def third():
    print('3)')
    while True:
        try:
            x = int(input(f'Please enter numbers between 1 and 4: \n'))
            if 1 <= x <= 4:
                if x == 1:
                    print('summer')
                    print('###################################')
                    break
                elif x == 2:
                    print('winter')
                    print('###################################')
                    break
                elif x == 3:
                    print('fall')
                    print('###################################')
                    break
                else:
                    print('spring')
                    print('###################################')
                    break
        except ValueError:
            print("its not a number, please try again")
            continue


def forth():
    print('4)')
    print(''' count =1
while count <11:
print(count)
count = count + 1''')
    print('this loop will run 10 times (1-10)')
    print('the last print will be 10')
    print('-lets check - /n')

    count = 1
    while count < 11:
        print(count)
        count = count + 1

    print('###################################')


def five():
    print('5)')
    age = check_age()
    flname = check_char()
    currency = check_currency()
    fly = check_tf()
    apt = check_apt()
    var_dict = {'Age': age, 'First letter last name': flname, 'Current currency': currency, 'Did you fly': fly,
                'Apartment': apt}
    print('#####################')
    print('Your Details : ')
    print('#####################')

    for key, val in var_dict.items():
        #
        # var_dict.get(key, '')
        print(f'{key}:  {val}')

    print('\n')
    print(f'if we add {list(var_dict.keys())[0]} with {list(var_dict.keys())[2]} we will get :')
    print(
        f'{list(var_dict.values())[0]} + {list(var_dict.values())[2]} = {float(list(var_dict.values())[0]) + int(list(var_dict.values())[2])}')
    print('###################################')


def six():
    print('6)')
    pn = input('please tell me your Phone Number:')
    print(f'Phone Numeber: {pn}')
    print('###################################')


def seven():
    print('7)')
    print_hello()
    print('###################################')


def eight():
    print('8)')
    name = input('Please enter your name:')
    get_name(name)
    calculate()
    print('###################################')


def nine():
    print('9)')
    print(('Please enter two numbers to be summed'))

    chk = True
    while chk:
        x = input('please enter first number\n')
        chk = check_num(x)
    chk = True
    while chk:
        y = input('please enter second number\n')
        chk = check_num(y)
    sum_num = sum(int(x), int(y))
    print(f'here is the sum of the number you chose : {sum_num}')
    print(('***************************************** '))
    print(('Please enter two strings to be manipulate'))
    str1 = input('please enter first string\n')
    str2 = input('please enter second string \n')
    str_man = str(str1, str2)
    print(f'here new string -  {str_man}')
    print('###################################')

    #######################################
    ##        Assignment Lesson 2        ##
    #######################################

#
# first()
# second()
# third()
# forth()
# five()
# six()
# seven()
# eight()
nine()