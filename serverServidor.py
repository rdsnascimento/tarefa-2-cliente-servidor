from socket import *
serverPort = 120
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('192.168.0.108',serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
while True:
        con, cliente = serverSocket.accept()
        print 'Conectado por', cliente
        while True:
                msg3 = con.recv(1024)
                if not msg3: break
                msg1 = con.recv(1024)
                msg2 = con.recv(1024)
                if msg3 == '1':
                        print 'Resultado ', msg1, '+', msg2, ' enviado para cliente'
                        con.send(str(int(msg1)+int(msg2)))
                        pass
                elif msg3 == '2':
                        print 'Resultado ', msg1, '-', msg2, ' enviado para cliente'
                        con.send(str(int(msg1)-int(msg2)))
                        pass
                elif msg3 == '3':
                        print 'Resultado ', msg1, '*', msg2, ' enviado para cliente'
                        con.send(str(int(msg1)*int(msg2)))
                        pass
                elif msg3 == '4':
                        print 'Resultado ', msg1, '/', msg2, ' enviado para cliente'
                        con.send(str(int(msg1)/int(msg2)))
                        pass
                else:
                        con.send('Erro: opera��o inv�lida')
                        pass
                        break
        print 'Finalizada a conex�o'
        break
serverSocket.close()
