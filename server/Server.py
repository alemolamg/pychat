import socket
import threading

class Server:
    def __init__(self, host = "localhost", port = 3000):
        self.host = host    # Host IP
        self.port = port    # Port to listen
        self.clients = []   # List of Clients
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Socket connection
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print("Server listening on {}:{}".format(self.host, self.port))

    # Add client socket connection - INGLES
    def add_client(self, client_socket):
        while True:
            message = client_socket.recv(1024).decode()
            print("Received message:", message)
            for client in self.clients:
                client.send(message.encode())

    def start(self):
        while True:
                client_socket, client_address = self.server_socket.accept()
                print("Client connected:", client_address)
                self.clients.append(client_socket)
                client_thread = threading.Thread(target=self.add_client, args=(client_socket,))
                client_thread.start()

