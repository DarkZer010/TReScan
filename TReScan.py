'''
all for Knowledge

NetExploit
'''

# importa a biblioteca socket e colorama
import socket
from colorama import init, Fore, Style
import os
import datetime
import pyfiglet
import time

init()

os.system("clear")

text = "TReScan"
logo = pyfiglet.figlet_format(text)
print(logo)

try:
    # ip do alvo
    alvo = input(Fore.BLUE+"digite url ou ip do alvo: "+Style.RESET_ALL).lower()
    print("\n")
except KeyboardInterrupt:
    print(Fore.RED+"você saiu de forma errada, user o comando sair"+Style.RESET_ALL)
    exit()

if not alvo:
    print(Fore.CYAN+"url ou ip incorreto!"+Style.RESET_ALL)
elif alvo == "sair":
    print(Fore.RED+"saindo..."+Style.RESET_ALL)
    time.sleep(1)
    exit()

print(Fore.YELLOW+"procurando portas..."+   Style.RESET_ALL)
time.sleep(5)

print(Fore.BLUE+f"alvo: {alvo}\n"+Style.RESET_ALL)		

try:
    # varre das portas 1 até 1025
    for porta in range(1, 1025):
    	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cria um socket para conexão tcp

	    # define o tempo de conexão
    	sock.settimeout(1)

    	# verifica as portas abertas
    	if sock.connect_ex((alvo, porta)) == 0:
    		print(Fore.GREEN + f"portas abertas: {porta}" + Style.RESET_ALL) # imprime as portas abertas
except Exception as e:
 	print(Fore.RED+f"ERRO!"+Style.RESET_ALL)
 	
 	sock.close() # fecha o socket

'''

desenvolved by DarkZero

Group NetExploit

'''
