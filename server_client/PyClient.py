# -*- coding: utf-8 -*-

import os
from socket import *
from time import ctime


host="127.0.0.1"
port=13000
addr=(host,port)
UDPSock=socket(AF_INET,SOCK_DGRAM)
while True:
    data=input("Enter message to send or type 'exit':")
    UDPSock.sendto(('[%s] %s'%(ctime(),data)).encode(),addr)
    if data == 'exit':
        break
UDPSock.close()
os._exit(0)
