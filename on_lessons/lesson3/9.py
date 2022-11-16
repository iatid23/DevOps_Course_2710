import sys


def save_name():

    clean = input('if you wanna clean file first please enter clean:\n')
    if clean == 'clean':
        open('names3d.txt', 'w').close()
    else:
        pass
    names = open('names3.txt', mode='a+')
    chk = True
    while chk:
        print('Please add desired name:\n')
        print('when you wanna stop writing enter "stop"')
        name = input()
        if name == 'stop':
            break;
        names.write(f'\n{name}')
    names.close();


def read_names():
    names = open('names33''.txt')
    for name in names:
        print(name)
    names.seek(0, 0)


# try:
#     save_name()
# except BaseException as e:
#         print(f"There was an error - {e}")
# read_names()

def div_numbers(x, y):
    try:
        print(x/y)
    #except ZeroDivisionError as e:
    except BaseException as e:
        print(f"There was an error - {e}")
    # except: # catch *all* exceptions
    #     e = sys.exc_info()[0]
    #     #print(e)
    #     er = str(e)
    #
    #     c = sys.exc_info()[1]
    #    # print(c)
    #     s = str(e).find("'")+1
    #     cut = len(er)-2
    #     stre = er[int(s):int(cut)]
    #
    #     #print(stre)
    #    # raise Exception(stre)


    # except stre as ert:
    #     print(ert)


#div_numbers(12, 5)
#div_numbers(12, 0)
div_numbers(12, 'j')