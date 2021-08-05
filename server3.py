import socket
LOCALHOST='localhost'
PORT=8080
server=socket.socket(socket.AF_INET,
                     socket.SOCK_STREAM)
server.bind((LOCALHOST,PORT))
server.listen(1)
print('server started')
print('Waiting for client request...')
clientConnection, clientAddress=server.accept()
print('Connect client:',clientAddress)
msg=''
while True:
    in_data=clientConnection.recv(1024)
    msg=in_data.decode()
    if msg=='bye':
        break
    print("From Client:", msg)
    out_data=input("Enter server message:")
    clientConnection.send(bytes(out_data,'UTF-8'))
print('Client disconnected')
clientConnection.close()
