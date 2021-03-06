from home_admins import intAdmin

class AdminMenu:

    def Admin_mainMenu(self):
        print('\n\n\n\nWelcome to EventIt, Administrator.')
        running = True
        while running:
            try:
                print('\n\nPlease select a menu: \n1.- User managment \t2.- Event management \t3.- Admin management \t4.- Exit Program')
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
                print('Please enter a valid number.\n\n')

        
    def Admin_userMenu(self):
        print('\n\n\n\nUser managment.')
        user_menu = True
        while user_menu:
            try:
                print('\n\nPlease select an action: \n1.- Unblock user \t2.- Block user \t3.- Return to main menu')
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
                print('Please enter a valid number.\n\n')

    def Admin_eventMenu(self):
        print('\n\n\n\nEvent managment.')
        event_menu = True
        while event_menu:
            try:
                print('\n\nPlease select an action: \n1.- Accept Event \t2.- Deny Event \t3.- Return to main menu')
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
                print('Please enter a valid number.\n\n')

    def Admin_adminMenu(self):
        print('\n\n\n\nAdmin management.')
        admin_menu = True
        while admin_menu:
            try:
                print('\n\nPlease select an action: \n1.- Add administrator \t2.- Ban administrator \t3.- Return to main menu')
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
                print('Please enter a valid number.\n\n')



menu_admin = AdminMenu()