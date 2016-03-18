import socket
import sys

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
message = "GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n"
mysock.connect(('www.pythonlearn.com', 80))
mysock.sendto(message.encode(),('www.pythonlearn.com', 80))

while True:
    data = mysock.recv(512)

    if ( len(data) < 1 ) :
        break
    print (data)
    readable = data.decode("utf-8")
    readable.replace("\r\n", r"\n")
    print (readable)
mysock.close()