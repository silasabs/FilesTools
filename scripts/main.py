from functions import *

def main():
    
    option = 0

    while option != 4:
        # initialize user instructions
        initialize()
        option = int(input('\nOption > '))

        if option == 1:
            print('Select the directory you want to organize')
            
            try:
                PATH = load_path()
                organizer(PATH)
            except Exception as error:
                print(f'error found {error.__cause__}')
            else: 
                print('Organized directory !')

            clear_display()
        
        elif option == 2:
            print('Select the file you want to generate the Hash')
            PATH = load_file()

            SHA256 = hash(PATH)
            print('Hash generated SHA256: ', SHA256)
            clear_display()

        elif option == 3:
            print('Select the directory you want to compress')
            
            try:
                PATH = load_path()
                compression(PATH)           
            except Exception as error:
                print(f'error found {error.__cause__}')
            else:
                print('The files have been compressed !')

            clear_display()
        
        elif option == 4:
            break
        
        else:
            clear_display()
            print('invalid option')

if __name__ == '__main__':
    main()