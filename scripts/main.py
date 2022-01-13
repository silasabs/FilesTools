from FileSystem import *
from EncryptFiles import *
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

        if option == 1:
            print('Select the directory you want to organize')
            
            try:
                PATH = load_path()
                organizer(PATH)
            except Exception as error:
                print(f'error found {error.__cause__}')
            else: 
                print('Organized directory !')
        
        elif option == 2:
            print('Select the file you want to generate the Hash')
            PATH = load_file()

            SHA256 = hash(PATH)
            print('Hash generated SHA256: ', SHA256)

        elif option == 3:
            print('Select the directory you want to compress')
            
            try:
                PATH = load_path()
                compression(PATH)           
            except Exception as error:
                print(f'error found {error.__cause__}')
            else:
                print('The files have been compressed !')

        elif option == 4:
            print('Select the directory where you want to store your keys')
            generate_key()
            print('your keys have been generated.')

        elif option == 5:
            try:              
                print('Select the file you want to encrypt [.txt]')
                path_file = load_file()
                print('select your public key.')
                path_key = load_file()

                encryptTextFile(path_key, path_file)

            except Exception as error:
                print(f'error found {error.__cause__}')          
            
            else:
                print('the file was encrypted.')
        
        elif option == 6:
            try:
                print('Select your private key')
                path_key = load_file()
                print('Select the file to be decrypted')
                path_file = load_file()

                decryptTextFile(path_key, path_file)
            
            except Exception as error:
                print(f'error found {error.__cause__}')
            
            else:
                print('The file has been decrypted.')

        elif option == 7:
            break
        
        else:
            print('invalid option')
            clear_display()
        
        clear_display()

if __name__ == '__main__':
    main()