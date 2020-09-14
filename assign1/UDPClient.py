#imports that socket module that is needed for all network communication
from socket import *

#defines the server name and port
serverName = ''
serverPort = 12000

#creates a UDP client socket for a IPv4 network
clientSocket = socket(AF_INET, SOCK_DGRAM)

#message to be sent to the server
message = input("Input lowercase sentence:")

#sends the defined message to the serve after translating it from string to byte 
clientSocket.sendto(message.encode(), (serverName, serverPort))

#when a packet is recieved by the client it is saved to modifiedMessage
#the source ip address and port is stored in serverAddress
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

#converts bytes to strings and then  prints
print(modifiedMessage.decode())

#closes socket
clientSocket.close()
