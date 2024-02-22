import socket
from concurrent.futures import ThreadPoolExecutor


class Client:
    def __init__(self, host="localhost", port=12345):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.username = input("Enter username: ")
        self.executor = ThreadPoolExecutor(max_workers=3)

    def receive_messages(self):
        try:
            while True:
                message = self.client_socket.recv(1024).decode()
                if message:
                    print(message)
        except ConnectionResetError:
            self.close_connection()

    def send_message(self):
        try:
            while True:
                message = input()
                if message.lower() == "exit":  # Exit from server
                    break
                if len(message) > 0:
                    self.client_socket.send("{}: {}".format(self.username, message).encode())
        except ConnectionError:
            self.close_connection()

    # Created not to repeat
    def close_connection(self):
        print("Connection closed.")
        self.client_socket.close()
        raise SystemExit()

    # Start client
    def start(self):
        try:
            self.client_socket.connect((self.host, self.port))  # Connet to server
            print("Connected to server.")

            self.executor.submit(self.receive_messages)
            self.executor.submit(self.send_message)

        except Exception as e:
            print("Error:", e)
            self.close_connection()

if __name__ == "__main__":
    client = Client()
    client.start()