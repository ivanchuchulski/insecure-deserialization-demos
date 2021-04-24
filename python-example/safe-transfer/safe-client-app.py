# import socket, pickle, builtins, yaml
# from user import User

# HOST = "127.0.0.1"
# PORT = 9090



# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#     sock.connect((HOST,PORT))
#     sock.send(serialized_user.encode())

import socket
import sys
import yaml
from user import User

def send_to_server():
    HOST, PORT = "localhost", 9090

    user = User('spam', 'eggs')
    serialized_user = yaml.dump(user)
    data = serialized_user

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n", "utf-8"))

        received = str(sock.recv(1024), "utf-8")

    print("Sent:     {}".format(data))
    print("Received: {}".format(received))

if __name__ == "__main__":
    send_to_server()