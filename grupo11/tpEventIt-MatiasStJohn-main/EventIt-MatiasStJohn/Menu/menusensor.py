from Classes.map import enter_map
from Classes.sensor import currentPico, listaPicos


class SensorMenu:

    def sensor_mainMenu(self, sensor):
        print('\n\nWelcome to the program')
        running = True
        while running:
            try:
                print('\nPlease select a menu: \n1.-Show top 3 zones\n2.-Show info\n3.-last peak\n4.-Tablero Picos\n5.-Open map\n6.-Exit')
                menu_input = input('Enter menu number: ')
                if menu_input == '1':
                    print(sensor.top3())
                elif menu_input == '2':
                    sensor.getInfo()
                elif menu_input == "3":
                    print(currentPico())
                elif menu_input == "4":
                    print(listaPicos())
                elif menu_input == '5':
                    enter_map()
                elif menu_input == "6":
                    print('Logging off. Exiting program.')
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Please enter a valid number.\n')


senMenu = SensorMenu()
