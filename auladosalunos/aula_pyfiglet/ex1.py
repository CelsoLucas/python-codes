import pyfiglet
from colorama import Fore, init
init()

lista_palavras = ["Hello", "Celso", "Você", "é", "Lindo"]

print(Fore.RED + lista_palavras[0])
print(Fore.GREEN + lista_palavras[1])
print(Fore.BLUE + lista_palavras[2])
print(Fore.YELLOW + lista_palavras[3])
print(Fore.MAGENTA + lista_palavras[4])