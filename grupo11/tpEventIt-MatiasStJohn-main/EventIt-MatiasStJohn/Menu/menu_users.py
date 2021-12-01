from Menu.home_usuarios import intUser


class UserMenu:

    def User_mainMenu(self):
        print(f'\n\nWelcome to EventIt, {intUser.currentUser}')
        running = True
        while running:
            try:
                print('\n\nPlease select a menu: \n1.- Event menu \n2.- Contacts \n3.- Exit Program')
                menu_input = input('Enter a menu number: ')
                if menu_input == '1':
                    UserMenu.User_eventMenu(self)
                elif menu_input == '2':
                    UserMenu.User_contactMenu(self)
                elif menu_input == '3':
                    print('logging off. Exiting program.')
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Please enter a valid number.\n')

    def User_eventMenu(self):
        print(f'\n\nEvent menu.')
        running = True
        while running:
            try:
                print('\nPlease select an action: \n1.-Report Event \n2.-Return to main menu')
                menu_input = input('Enter a menu number: ')
                if menu_input == '1':
                    intUser.reportEvent()
                elif menu_input == '2':
                    print('logging off. Exiting program.')
                    running = False
                else:
                    raise ValueError
            except ValueError:
                print('Please enter a valid number.\n')

    def User_contactMenu(self):
        print(f'\n\nContact menu.')
        running = True
        while running:
            try:
                print(
                    '\nPlease select an action: \n1.-Enviar solicitud \n2.-Ver solicitudes \n3.-Return to main menu')
                menu_input = input('Enter a menu number: ')
                if menu_input == '1':
                    intUser.contactoDeInteres()
                elif menu_input == '2':
                    intUser.check_requests()
                elif menu_input == '3':
                    running = False
                else:
                    raise ValueError
            except ValueError:
                print('Please enter a valid number.\n')


menu_user = UserMenu()
