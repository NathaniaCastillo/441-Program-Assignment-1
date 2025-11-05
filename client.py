import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a client socket with same specifications as server 
#when connecting use public ip UNLESS you are connecting same network not via internet
client.connect(('127.0.0.1', 9999)) #using public ip and same port number

client.send("Hello From Client".encode()) #sending message to server
print(client.recv(1024).decode())