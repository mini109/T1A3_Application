import time
import user_interface
import coffee_selection
import colorama
from colorama import Fore
colorama.init(autoreset=True)

# Represents the coffee machine


class CoffeeMachine:
    def __init__(self):
        # supplies held by the coffee machine
        self.water = 500
        self.coffee_beans = 250
        self.milk = 300

    def supplies_report(self):
        user_interface.clear()
        # print a report of the machine's supplies and each level
        print(f'\n The machine\'s supply levels are: ')
        if self.water < 100:
            print(
                f'\n {(Fore.RED + 'Water: ' + '\033[39m')}{self.water}ml / 500ml')
        elif self.water <= 250:
            print(f'\n {(Fore.YELLOW + 'Water: ' +
                  '\033[39m')}{self.water}ml / 500ml')
        else:
            print(f'\n {(Fore.GREEN + 'Water: ' +
                  '\033[39m')}{self.water}ml / 500ml')

        if self.coffee_beans < 50:
            print(
                f'\n {(Fore.RED + 'Coffee: ' + '\033[39m')}{self.coffee_beans}g / 250g')
        elif self.coffee_beans <= 120:
            print(f'\n {(Fore.YELLOW + 'Coffee: ' +
                  '\033[39m')}{self.coffee_beans}g / 250g')
        else:
            print(f'\n {(Fore.GREEN + 'Coffee: ' +
                  '\033[39m')}{self.coffee_beans}g / 250g')

        if self.milk < 100:
            print(
                f'\n {(Fore.RED + 'Milk: ' + '\033[39m')} {self.milk}ml / 300ml')
        elif self.milk <= 200:
            print(f'\n {(Fore.YELLOW + 'Milk: ' +
                  '\033[39m')} {self.milk}ml / 300ml')
        else:
            print(
                f'\n {(Fore.GREEN + 'Milk: ' + '\033[39m')} {self.milk}ml / 300ml')
        time.sleep(2)

    def cleaning_cycle(self):
        # reduce the machine's water supply by 50ml
        if self.water > 50:
            print(f'\n {Fore.YELLOW}Initiating cleaning cycle - please standby')
            time.sleep(3)
            self.water -= 50
            print(f'\n {Fore.GREEN}The cleaning cycle is now complete. The machine is ready for use')
            time.sleep(2)
        else:
            print(f'\n {Fore.RED}Unable to complete the cleaning cycle. \n There is an insufficient amount of water available. Please refill the machine')
            time.sleep(2)

    def refill_machine(self):
            print('\n Which supply would you like to refill:')
            print(f'\n{(Fore.YELLOW + '[1]' + '\033[39m')} Water')
            print(f'\n{(Fore.YELLOW + '[2]' + '\033[39m')} Coffee Beans ')
            print(f'\n{(Fore.YELLOW + '[3]' + '\033[39m')} Milk ')
            print(f'\n{(Fore.YELLOW + '[4]' + '\033[39m')} All')
            print(f'\n{(Fore.YELLOW + '[5]' + '\033[39m')} None')

            refill_selection = input('\n:')
            match refill_selection:
                case '1':
                    self.water = 500
                    self.supplies_report()
                case '2':
                    self.coffee_beans = 250
                    self.supplies_report()
                case '3':
                    self.milk = 400
                    self.supplies_report()
                case '4':
                    self.water = 500
                    self.coffee_beans = 250
                    self.milk = 400
                    self.supplies_report()
                case '5':
                    print(f'\n {Fore.CYAN} No supplies have been refilled')
                    time.sleep(2)
                case _:
                    user_interface.clear()
                    print(
                    f"\n{Fore.RED}Sorry [{refill_selection}] is not a valid option - please select a valid option"
                    )
                    self.refill_machine()

    def make_coffee(self):
        # function which takes the users selection from coffeeselection class and determins if there are enough supplies to make the selection
        if (self.water >= coffee_selection.choice['water']) and (self.milk >= coffee_selection.choice['milk']) and (self.coffee_beans >= coffee_selection.choice['coffee']):
            self.water -= coffee_selection.choice['water']
            self.coffee_beans -= coffee_selection.choice['coffee']
            self.milk -= coffee_selection.choice['milk']
            user_interface.clear()
            print(f'\n Your coffee is being made now - please wait ')
            time.sleep(2)
            user_interface.clear()
            print(f'''\n Here is your{Fore.YELLOW} {
                  coffee_selection.choice['name']}''')
            print(f'\n {Fore.MAGENTA} Enjoy!')
            time.sleep(2)
            user_interface.clear()
        else:
            user_interface.clear()
            print(f'''\n{Fore.RED}Sorry there are not enough supplies in the machine to make a {
                  coffee_selection.choice['name']}. Please refill the machine.''')
            time.sleep(3)
