# Server Main
import sys
from Server import Server

# if len(sys.argv) != 3:
#     server = Server()
# else:
#     server = Server(str(sys.argv[1]), int(sys.argv[2]))

server = Server()
server.start()
