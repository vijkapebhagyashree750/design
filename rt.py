from colorama import Fore, Style, init

init(autoreset=True)

for i in range(6):
    for j in range(7):
        if (i == 0 and j % 3 != 0) or \
           (i == 1 and j % 3 == 0) or \
           (i - j == 2) or \
           (i + j == 8):
            
            # Change colors dynamically
            if i % 2 == 0:
                print(Fore.RED + "❤", end=" ")
            else:
                print(Fore.MAGENTA + "❤", end=" ")
        else:
            print(" ", end=" ")
    print()

