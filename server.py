import threading
import socket
import time

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
            message = client.recv(1024).decode('ascii') # number of bytes to receive
            comparison = message.lower()
            if "weather" in comparison:
                response = message + " -> " + "Partly Cloudy, 63 Degrees Fahrenheit"
                broadcast(response.encode('ascii')) 
            elif "time" in comparison:
                current_time = time.strftime("%H:%M:%S")
                response = message + " -> " + current_time
                broadcast(response.encode('ascii'))
            elif "users" in comparison:
                response = message + " -> " + str(len(nicknames))
                broadcast(response.encode('ascii'))
            elif "help" in comparison:
                response = message + " -> " + "weather, time, users, help"
                broadcast(response.encode('ascii'))
            else:
                broadcast(message.encode('ascii'))
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

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')

        nicknames.append(nickname) # adds user to lists
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat\n".encode('ascii'))
        client.send('Connected to the server'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is running")
receive() # run server