# -*- coding: cp1252 -*-
from socket import *
serverName='192.168.0.108'
serverPort= 120
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
while True:
    msg = raw_input ('\nEscolha a operação\n1- Soma\n2- Subtracao\n3- Multiplicacao\n4- Divisao\n5- Sair\n*>> ' )
    if int(msg) > 4:
        break
        pass
    else:
        clientSocket.send (msg)
        pass
    msg = raw_input ('\nEntre com operando 1: ')
    clientSocket.send (msg)
    msg = raw_input ('Entre com operando 2: ')
    clientSocket.send (msg)
    msg = clientSocket.recv(1024)
    print 'Resultado: ', msg
clientSocket.close()
