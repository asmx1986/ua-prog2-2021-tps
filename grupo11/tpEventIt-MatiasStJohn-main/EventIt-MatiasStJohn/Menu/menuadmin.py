from Menu.homeadmins import intAdmin


class AdminMenu:

    def Admin_mainMenu(self):
        print('\n\nWelcome to EventIt, Administrator.')
        running = True
        while running:
            try:
                print(
                    '\n\nPlease select a menu: \n1.-User managment \n2.-Event management \n3.-Admin management \n4.-Exit')
                menu_input = input('Enter menu number: ')
                if menu_input == '1':
                    AdminMenu.Admin_userMenu(self)
                elif menu_input == '2':
                    AdminMenu.Admin_eventMenu(self)
                elif menu_input == '3':
                    AdminMenu.Admin_adminMenu(self)
                elif menu_input == '4':
                    print('Logging off. Exiting program.')
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Please enter a valid number.\n')

    def Admin_userMenu(self):
        print('\n\nUser managment.')
        user_menu = True
        while user_menu:
            try:
                print('\n\nPlease select an action: \n1.-Unblock user \n2.-Block user \n3.-Return to main menu')
                menu_input = input('Enter action number: ')
                if menu_input == '1':
                    intAdmin.unblockUser()
                elif menu_input == '2':
                    intAdmin.blockUser()
                elif menu_input == '3':
                    user_menu = False
                else:
                    raise ValueError
            except ValueError:
                print('Please enter a valid number.\n')

    def Admin_eventMenu(self):
        print('\n\nEvent managment.')
        event_menu = True
        while event_menu:
            try:
                print('\nPlease select an action: \n1.-Accept Event \n2.-Deny Event \n3.-Return to main menu')
                menu_input = input('Please enter action number: ')
                if menu_input == '1':
                    intAdmin.acceptEventRequest()
                elif menu_input == '2':
                    intAdmin.denyEventRequest()
                elif menu_input == '3':
                    event_menu = False
                else:
                    raise ValueError
            except ValueError:
                print('Please enter a valid number.\n')

    def Admin_adminMenu(self):
        print('\n\nAdmin management.')
        admin_menu = True

        while admin_menu:
            try:
                print('\nPlease select an action: \n1.-Add administrator \n2.-Ban administrator \n3.-Return to main menu')
                menu_input = input('Please enter action number: ')
                if menu_input == '1':
                    intAdmin.addAdmin()
                elif menu_input == '2':
                    intAdmin.banAdmin()
                elif menu_input == '3':
                    admin_menu = False
                else:
                    raise ValueError
            except ValueError:
                print('Please enter a valid number.\n')


menu_admin = AdminMenu()
