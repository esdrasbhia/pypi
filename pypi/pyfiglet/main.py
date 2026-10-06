import pyfiglet

texto = input ("digite uma palavra ou uma frase: ")
nome = pyfiglet.figlet_format(texto)
print(nome)