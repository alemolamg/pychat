import socket
import threading

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.username = input("Enter your username: ")

    def receive_messages(self):
        while True:
            message = self.client_socket.recv(1024).decode()
            if message:
                print(message)

    def send_message(self):
        while True:
            message = input()
            if message.lower() == "exit":
                break
            self.client_socket.send("{}: {}".format(self.username, message).encode())

    def start(self):
        self.client_socket.connect((self.host, self.port))
        print("Connected to server.")
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()
        send_thread = threading.Thread(target=self.send_message)
        send_thread.start()

if __name__ == "__main__":
    client = Client("localhost", 3000)
    client.start()
