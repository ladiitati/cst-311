#imports that socket module that is needed for all network communication
from socket import *

#defines the server port
serverPort = 12000

#creates a UDP client socket for a IPv4 network
serverSocket = socket(AF_INET, SOCK_DGRAM)

#Binds the defined port number to the socket
serverSocket.bind(('', serverPort))

print("The server is ready to receive")

while True:
    #When a packet arrives thpacket of data is stored to message
    #and the client's IP address and port number are stored in clientAddress
    message, clientAddress = serverSocket.recvfrom(2048)

    #converts message from bytes to string and make upper case
    modifiedMessage = message.decode().upper()

    #will convert data from string to byte and send packet to the server socket to be delievered
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
