from Menu.login import menuLogin
class Menu:
    def mainMenu(self):
        print('\n\nWelcome to the program')
        running = True
        while running:
            try:
                print('\nPlease select a menu: \n1.-Register \n2.-Login as user \n3.-Login as Admin \n4.-Enter as Sensor \n5.-Exit')
                menu_input = input('Enter menu number: ')
                if menu_input == '1':
                    menuLogin.Register()
                elif menu_input == '2':
                    menuLogin.Login()
                elif menu_input == '3':
                    menuLogin.LoginAdmin()
                elif menu_input == '4':
                    menuLogin.LoginSensor()
                elif menu_input == '5':
                    print('Logging off. Exiting program.')
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Please enter a valid number.\n')
    

