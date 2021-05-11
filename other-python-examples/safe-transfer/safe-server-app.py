

# HOST = "127.0.0.1"
# PORT = 9090

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     print("server started, waiting for client")

    
#     connection, address = s.accept()

#     print("client connected")

#     with connection:
#         print("My friend at ", address, " sent me some data")
#         received_data = connection.recv(1024).decode()
#         received_user = yaml.safe_load(received_data)
#         print(received_user)

import socketserver
import yaml
from user import User

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).decode().strip()
        received_user = yaml.safe_load(self.data)

        print("{} wrote:".format(self.client_address[0]))
        print(received_user)

        # response
        self.request.sendall(bytes(received_user.__str__().upper() + '\n', "utf-8"))

def start_server():
    HOST, PORT = "localhost", 9090

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

if __name__ == "__main__":
    start_server()
