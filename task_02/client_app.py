import socket
import sys

def start_client(host, port, mode):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to server")

    # Encode the message to bytes and send it to the server
    client_socket.sendall(mode.encode())

    if mode.upper() == "SUBSCRIBER":
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print("Received message:", data.decode())

    elif mode.upper() == "PUBLISHER":
        while True:
            message = input("Enter message: ")
            client_socket.sendall(message.encode())
            if message.lower() == "terminate":
                break

    client_socket.close()
    print("Disconnected from server")

if __name__ == '__main__':
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python client_app.py <host> <port> <mode (PUBLISHER or SUBSCRIBER)>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    mode = sys.argv[3]

    start_client(host, port, mode)