import socket
import sys

def start_server(port):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the localhost and the specified port
    server_socket.bind(('localhost', port))

    server_socket.listen(1)

    print("Server is running on port:", port)

    while True:
        # Accept incoming connection from a client and get its socket and address
        client_socket, address = server_socket.accept()

        print("Client connected on '", address, "' successfully.")

        while True:
            # Receive data (up to 1024 bytes) from the client
            data = client_socket.recv(1024)

            print("Client says:", data.decode())

            if data.decode() == "terminate":
                break

        # Close the connection with the client
        client_socket.close()

        # Display a message indicating the client has disconnected
        print("Client disconnected.")

if __name__ == '__main__':
    # Check if the correct number of arguments (port) is provided
    if len(sys.argv) != 2:
        print("Usage: python server_app.py <port>")
        sys.exit(1)

    port = int(sys.argv[1])

    start_server(port)
