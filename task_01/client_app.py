import socket
import sys

def start_client(host, port):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((host, port))
    print("Connected to server")

    while True:
        message = input("Enter message: ")

        # Encode the message to bytes and send it to the server
        client_socket.sendall(message.encode())

        if message.lower() == "terminate":
            break

    client_socket.close()
    print("Disconnected from server")

if __name__ == '__main__':
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python client_app.py <host> <port>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])

    start_client(host, port)

