import socket
import threading



client =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1",8080))

nickname = input("chose a nickname : ")

def receive () :
    while True:
        try:
            massage = client.recv(200).decode("ascii")
            if massage == "NICK" :
                client.send(nickname.encode("ascii"))
            else:
                print(massage)
        except:
            print("server was shut down")
            client.close()
            break
def write():
    while True :
        message = f"{nickname}: {input('')}"
        client.send(message.encode("ascii"))

receive_thread = threading.Thread(target=receive)
receive_thread.start()


write_thread =threading.Thread(target=write)

write_thread.start()
