from core import *
from asymmetrical import *
import pyfiglet

def initialize():
    """
    Function responsible for initializing user instructions.
    """
    title = pyfiglet.figlet_format("Files Tool")
    # instructions.
    print(title, '''
    Organize your directories\n
        1. Organize directory
        2. Hash a file
        3. Compress directory

    Make your data more secure\n
        4. Generate asymmetric key pair
        5. Encrypt File Text
        6. Decrypt File Text
        7. Exit\n''')

def main():  
    option = 0

    while option != 7:
        # initialize user instructions
        initialize()
        option = int(input('Option > '))

if __name__ == '__main__':
    main()