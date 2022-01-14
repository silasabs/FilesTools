from contextlib import nullcontext
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
                path = load_path()
                organizer(path)
            
            except Exception as error:
                print(f'Error found {error.__cause__}')
            
            else: 
                print('Organized directory !')
        
        elif option == 2:
            print('Select the file you want to generate the Hash')
            path = load_file()

            SHA256 = hash(path)
            print('Hash generated SHA256: ', SHA256)

        elif option == 3:
            print('Select the directory you want to compress')
            
            try:
                PATH = load_path()
                compression(PATH)           
            
            except Exception as error:
                print(f'Error found {error.__cause__}')
            
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
                # Checks if the file is .txt and if any file was selected.
                if checkExtension(path_file, 'txt') == True:
                    print('Select your public key.')
                    path_key = load_file()
                    # Checks the key extension and if true the file is encrypted.
                    if checkExtension(path_key, 'pem') == True:
                        encryptTextFile(path_key, path_file)
                        print('The file was encrypted.')
                else:
                    print('Unable to perform encryption.')
                    
            except Exception as error:
                print(f'Error found {error.__cause__}')          
            
            finally:
                print('Thanks for using FilesTool !')
        
        elif option == 6:
            
            try:
                print('Select your private key')
                path_key = load_file()
                # Checks if the file is .pem and if any file was selected.
                if checkExtension(path_key, 'pem') == True:
                    print('Select the file to be decrypted')
                    path_file = load_file()
                    # Checks the key extension and if true the file is decrypted.
                    if checkExtension(path_file, 'bin') == True:
                        decryptTextFile(path_key, path_file)
                        print('The file has been decrypted.')              
                else:
                    print('Unable to decrypt the file.')
            
            except Exception as error:
                print(f'error found {error.__cause__}')
            
            finally:
                print('Thanks for using FilesTool !')

        elif option == 7:
            break
        
        else:
            print('invalid option')
        
        clear_display()

if __name__ == '__main__':
    main()