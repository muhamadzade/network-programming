import socket
server='localhost'
PORT=8080
client=socket.socket(socket.AF_INET,
                     socket.SOCK_STREAM)
client.connect((server,PORT))
client.sendall(bytes("This is from client",
                     'UTF-8'))
while True:
    in_data=client.recv(1024)
    print("From Server:", in_data.decode())
    out_data=input("Enter client message:")
    client.sendall(bytes(out_data,'UTF-8'))
    msg=in_data.decode()
    if out_data=='bye':
        break
client.close()
