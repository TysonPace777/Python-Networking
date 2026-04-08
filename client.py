import socket
import threading
import os
from dotenv import load_dotenv

load_dotenv()

local_ip = os.getenv('local_ip')

nickname = input("Choose your nickname: ")

# declare same connections that server uses
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((local_ip, 20598))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
