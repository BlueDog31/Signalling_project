import socket
import numpy

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind("https://github.com/BlueDog31/Signalling_project.git")
serverSocket.listen(1)
clientSocket, clientAdress = serverSocket.accept()
print(Definition: f"Tilkoblet fra: {client_address}")
while True:
    # Motta data fra klienten (opptil 1024 bytes) og dekod til tekst
    data = client_socket.recv(1024).decode('utf-8')
    if not data or data.lower() == 'hade':
        print("Klienten koblet fra.")
        break
    print(f"Klienten sier: {data}")
    
    # Svar klienten
    svar = input("Svar til klienten: ")
    client_socket.send(svar.encode('utf-8'))

# 6. Lukk forbindelsene
client_socket.close()
server_socket.close()
