import threading
import socket

host = '0.0.0.0' # accept all same network ips
port = 20598

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # af inet is internet, can use bluetooth and others
server.bind((host, port)) # only uses host and port
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024) # number of bytes to receive
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client) # remove client if it disconnects
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat\n".encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024)

        nicknames.append(nickname) # adds user to lists
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat\n".encode('ascii'))
        client.send('Connected to the server'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is running")
receive() # run server