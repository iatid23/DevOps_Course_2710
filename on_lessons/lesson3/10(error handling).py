#run time error

def print_number():
    print(10/0)
    for number in range(10):
        print(number)

def call_to_print_number():
    print_number()


call_to_print_number()