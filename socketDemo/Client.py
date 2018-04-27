# coding:utf-8

import socketDemo
s = socketDemo.socket(socketDemo.AF_INET, socketDemo.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))

print('--->>>' + s.recv(1024).decode('utf-8'))

s.send(b'Hello, I am a client')
print('--->>>' + s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()












