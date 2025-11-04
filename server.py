import socket

server = socket. socket(socket.AF_INET, socket.SOCK_STREAM) #specifying type of socket with internet, working with TCP sock as asked
# just a server for accepting connections

#Reminder that TP connection is when you actually have a connection and exchange messages over that connection vs UDP send and recieve without maintaing a connection

#when hosting, use private ip
server.bind(('0.0.0.0', 9999)) #binding with local IP address and specifying server port as 9999
server.listen(3) #specifying max connections as 3

while True:
    # to actually talk with the server we need to have another socket (client) that comunicatews with te other socket
    client, addr = server.accept() #while true constantly accept connects, this will include client, 
    print(client.recv(1024).decode())
    client.send ("Hello from the server side".encode()) #message that will be sent to the client, not sure if this should be done yet