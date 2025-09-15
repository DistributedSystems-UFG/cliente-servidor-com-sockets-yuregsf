from socket  import *
from constCS import *

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
msg = s.recv(1024)
print(msg.decode())
ponto = int(input())
s.send(str(ponto).encode())
table = s.recv(1024)
print(table.decode())
s.close()
