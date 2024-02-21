# Client main
import sys
from Client import Client

if len(sys.argv) != 3:
    client = Client()
else:
    client = Client(str(sys.argv[1]), int(sys.argv[2]))
client.start()
