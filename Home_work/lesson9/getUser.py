import getpass

def get_username():
    return getpass.getuser()

if __name__ == '__main__':
    print("User Name:", get_username())