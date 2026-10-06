from colorama import Fore, Back, Style, init

init(autoreset=True) 

print(Fore.RED + 'eu suspiro em vermelho')
print(Back.GREEN + 'eu venco em verde')
print(Style.BRIGHT + 'eu sou um texto fraco')
print(Fore.YELLOW + Back.BLUE + 'eu sou um texto amarelo com fundo azul')

print('texto sem formatação')