# Server Class
import socket
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime


class Server:
    def __init__(self, host="localhost", port=12345):
        self.host = host  # Host IP
        self.port = port  # Port to listen
        self.clients = []  # List for connect clients
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(4)  # Start to listen, max 4 connections
        print("Server listening on {}:{}".format(self.host, self.port))
        self.executor = ThreadPoolExecutor(max_workers=10)

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
        timestamp = datetime.now().strftime("%d-%m-%YT%H:%M:%S")  # get timestand
        log_file = open("chat_history.log", "a")  # Open file
        log_file.write("{} - {}\n".format(timestamp, message))  # Add last message
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
        try:
            while True:
                # accept client connection
                client_socket, client_address = self.server_socket.accept()
                print("Client connected:", client_address)

                self.clients.append(client_socket)
                self.executor.submit(self.add_client, client_socket)
        except KeyboardInterrupt:
            print("Shutting down server.")
            self.executor.shutdown()
            self.server_socket.close()
            raise SystemExit()
