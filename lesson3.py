#########################################
###        Asignment lesson 3         ###
#########################################
import flasky

def one():
    print('one')
    print('a = 1/0')
    try:
        a = 1/0
    except ZeroDivisionError as e:
        print(f'We have a problem - {e}')
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n')




def two():
    print('two')
    print('''try:
    x = 1
finally:
    print("finally")''')
    print('Yes It iS lEGAL - SEE:')
    try:
        x = 1
    finally:
        print("finally")
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n')


def three():
    print('three')
    print('''except:
                print("found an error")''')
    print('This Exception can caught any exception that will be thrown -  IT IS GENERAL ')
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n')


def four():
    print('four')
    print('the last execution is too general there for we cannot know the expect exception - that is what wrong with it ')
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n')


def five():
    print('five')
    print('a. except IOError')
    print('will catch exception that come from working with files - like trying to write to file without permission   ')
    print('b. except ZeroDivisionError')
    print('will catch exception that come from dividing number in Zero')
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n')


def six():
    print('six')
    print('Create a text file named “words.txt” programmatically')
    name = input('Please Enter A Name to write into file\n')
    try:
        file = open('words.txt', 'w+')
        file.write(f'{name}\n')
        file.close()
    except BaseException as e:
        print(f'There is a Problem - {e}')
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n')


def seven():
    print('seven')
    print('Lets Read THE FILE WE MADE EARLIER')
    try:
        file = open('words.txt', 'r')
        for name in file:
            print(name)
        file.seek(0, 0)
    except BaseException as e:
        print(f'There is a Problem - {e}')
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n')


def eight():
    print('eight')
    print('Lets Write Hebrew into THE FILE WE MADE EARLIER')
    print('First Lets Clean It')
    try:
        file = open('words.txt', 'w+', encoding='utf-8')
        file.truncate(0)
        file.write('וואו אנחנו כותבים עברית\n')
        seven()
        # will print te file
    except BaseException as e:
        print(f'There is a Problem - {e}')
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n')


def nine():
    print('nine')
    print('Lets Flask')


def ten():
    print('10.Create an image from code (png file) Hint: use Pillow')

one()
two()
three()
four()
five()
six()
seven()
eight()
nine()
