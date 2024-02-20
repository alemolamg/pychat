import socket
import threading


# Server Class
class Server:
    def __init__(self, host="localhost", port=12345):
        self.host = host  # Host IP
        self.port = port  # Port to listen
        self.clients = []  # List of Clients
        self.server_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM
        )  # Socket connection
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print("Server listening on {}:{}".format(self.host, self.port))

    # Remove client and close connection
    def remove_client(self, client):
        if client in self.clients:
            client.close()  # Close socket connection
            self.clients.remove(client)  # Remove client from client list

    # Send message to clients
    def broadcast_message(self, message, sender):
        for client in self.clients:
            if client != sender:  # Not sender client
                try:
                    client.send(message.encode())
                except:
                    self.remove_client(client)

    # Save message on logs file
    def save_message(self, message):
        log_file = open("chat_history.log", "a")  # Open file
        log_file.write(message + "\n")  # Add last message
        log_file.flush()  # Save file

    # Add client socket connection
    def add_client(self, client_socket):
        try:
            while True:
                message = client_socket.recv(1024).decode()  # get client's message
                if message:
                    print("Received message:", message)
                    self.save_message(message)  # Save message on logs file
                    self.broadcast_message(
                        message, client_socket
                    )  # Send message to other clients
                else:
                    self.remove_client(client_socket)  # Client is out of server
                    break
        except:
            self.remove_client(client_socket)

    # Start client
    def start(self):
        while True:
            client_socket, client_address = (
                self.server_socket.accept()
            )  # accept client connection
            print("Client connected:", client_address)
            self.clients.append(client_socket)  # Add client to
            client_thread = threading.Thread(
                target=self.add_client, args=(client_socket,)
            )
            client_thread.start()
