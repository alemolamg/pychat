# Client main
import sys
from Client import Client

if len(sys.argv) > 1:
    print("server name: " + sys.argv[1])
    client = Client(str(sys.argv[1]))
else:
    client = Client()

client.start()
