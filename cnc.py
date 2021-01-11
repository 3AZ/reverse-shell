import socket
from colorama import Fore
import os

os.system("clear")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((("0.0.0.0"), 666))
s.listen(5)
print(Fore.CYAN + "[-] Waiting For Connection...")
clientsocket, addr = s.accept()
print("[+] New Connection From " + str(addr))
ans = input("[~]>: " + Fore.RED)
while True:
	clientsocket.send(bytes(ans.encode("utf-8")))
	ans = input(Fore.CYAN + "[~]>: " + Fore.RED)