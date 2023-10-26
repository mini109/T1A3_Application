import time
import os
import colorama
from colorama import Fore

colorama.init(autoreset=True)


def welcome_greeting():
    clear()
    with open("welcome_banner.txt", "r") as file:
        welcome = file.read()
    print(welcome)
    print(f"\n {Fore.CYAN}Hello there!")
    time.sleep(1)


def goodbye_message():
    with open("quit_banner.txt", "r") as file:
        goodbye = file.read()
    print(goodbye)
    time.sleep(1)
    print(f"\n {Fore.RED}TURNING OFF")
    time.sleep(1)


def user_menu():
    print("\n Please select an option:")
    print(f'\n{(Fore.YELLOW + '[1]' + '\033[39m')} Make A Coffee')
    print(f'\n{(Fore.YELLOW + '[2]' + '\033[39m')} Refill the Machine ')
    print(f'\n{(Fore.YELLOW + '[3]' + '\033[39m')} View Supply Levels ')
    print(f'\n{(Fore.YELLOW + '[4]' + '\033[39m')} Clean the Machine ')
    print(f'\n{(Fore.YELLOW + '[5]' + '\033[39m')} Turn Off')


def clear():
    os.system("cls" if os.name == "nt" else "clear")
