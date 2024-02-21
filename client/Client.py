import socket
import threading

class Client:
    def __init__(self, host = "localhost", port = "12345"):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.username = input("Enter username: ")
        self.connected = False

    def receive_messages(self):
        try:
            while True:
                message = self.client_socket.recv(1024).decode()
                if message:
                    print(message)
        except:
            self.close_connection()

    def send_message(self):
        try:
            while True:
                message = input()
                if message.lower() == "exit":   # Exit from server
                    break
                if len(message) > 0:
                    self.client_socket.send("{}: {}".format(self.username, message).encode())
        except:
            self.close_connection()

    # Created not to repeat 
    def close_connection(self):
        print("Connection closed.")
        self.client_socket.close()
        raise SystemExit()

    # Start client
    def start(self):
        try:
            self.client_socket.connect((self.host, self.port)) # Connet to server
            self.connected = True
            print("Connected to server.")
            receive_thread = threading.Thread(target=self.receive_messages) # receive message thread
            receive_thread.start()
            send_thread = threading.Thread(target=self.send_message) # send message thread
            send_thread.start()
        except Exception as e:
            print("Error:", e)
            self.client_socket.close()
            raise SystemExit()  # Finaliza la ejecución del programa

if __name__ == "__main__":
    client = Client("localhost", 12345)
    client.start()
