from colorama import Fore, Style

def notify_print(string):
    print(Fore.RED + "/!\\ /!\\ /!\\ /!\\ /!\\ /!\\ /!\\ /!\\ /!\\")
    print(Style.RESET_ALL)
    print(string)
    print(Fore.RED + "/!\\ /!\\ /!\\ /!\\ /!\\ /!\\ /!\\ /!\\ /!\\")
    print(Style.RESET_ALL)
