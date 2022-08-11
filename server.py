import datetime
import socket

#fields
HOST = '127.0.0.1'      #host ip
PORT = 42069            #port
ADDR = (HOST, PORT)     #socket endpoint
MSG = b""               #blank message

#functionality for opening socket
def openSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(ADDR)
    s.listen(10)
    print("Listening on " + str(ADDR))
    return s

#creates socket and listens for message from client
def createSocket():
    s = openSocket()
    conn, addr = s.accept()
    MSG = conn.recv(4096)
    print(str(datetime.datetime.now().strftime("%c")) + " : " + MSG.decode())
    #conn.sendall(MSG)
    s.close()

while True:
    createSocket()
