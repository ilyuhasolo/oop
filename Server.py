import socket
import datetime
import random
from Treatment import Treatment


server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server.bind(('localhost', 7777))
server.listen()


def Writer(message: str):
    print(str(datetime.datetime.now()) + ": " + message)


print("Server started")
while True:
    sock, addr = server.accept()
    print(str(datetime.datetime.now()) + ': Connection from ' + str(addr))
    worker = Treatment(socket=sock, id=random.randrange(1, 1000), callback=Writer)
    worker.start()
