import platform
import socket

#fields
HOST = '127.0.0.1'      #host ip
PORT = 42069            #port
ADDR = (HOST, PORT)     #socket endpoint
MSG = ""

#gets message from user input
MSG = input("Type your message here:")

#creates socket and sends it to the server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(ADDR)
sock.sendall(bytes(MSG, "utf-8"))
data = sock.recv(4096)
print(data)