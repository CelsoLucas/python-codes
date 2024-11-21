from colorama import Fore, Style, init, Back

init()
print(Fore.RED + "Vermelho")
print(Fore.GREEN + "Verde")
print(Fore.BLUE + "Azul")
print(Style.RESET_ALL + "Texto na cor padrão")
print(Back.MAGENTA + "Texto com cor no fundo")