#1/usr/bin/env python3

import socket

HOST = '127.0.0.1' #Standard loopbacback interface address (localhost)
PORT = 9999      #Posrt to listen on

with socket.socjet(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn,addr = s.accept()
    with conn:
         print('Server is connected with address',addr)
         while True:
             data = conn.recv(2048) #default byte stream size
             if not data:
                 break
             conn.sendall(data)