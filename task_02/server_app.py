import socket
import sys
import threading

subscribers = [] 
publishers = []  

def handle_client(client_socket, address):
    # Receive client type (SUBSCRIBER or PUBLISHER) from the client
    client_type = client_socket.recv(1024).decode()

    if client_type.upper() == "SUBSCRIBER":
        subscribers.append(client_socket)
        print("Subscriber connected:", address)
    elif client_type.upper() == "PUBLISHER":
        publishers.append(client_socket)
        print("Publisher connected:", address)

    while True:
        # Receive data (up to 1024 bytes) from the client
        data = client_socket.recv(1024)
        if not data:
            break

        print("Received from client", address, ":", data.decode())
        if data.decode() == "terminate":
            break

        if client_type.upper() == "PUBLISHER":
            # Forward the data to all connected subscribers
            for subscriber in subscribers:
                subscriber.sendall(data)

    if client_type.upper() == "SUBSCRIBER":
        subscribers.remove(client_socket)
        print("Subscriber disconnected:", address)
    elif client_type.upper() == "PUBLISHER":
        publishers.remove(client_socket)
        print("Publisher disconnected:", address)

    # Close the connection with the client
    client_socket.close()

def print_subsandpubs():
    print("Subscribers:", subscribers)
    print("Publishers:", publishers)

def start_server(port):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the localhost and the specified port
    server_socket.bind(('localhost', port))

    # Listen for incoming connections with a backlog of 5 queued connections
    server_socket.listen(5)
    print("Server listening on port", port)

    while True:
        # Accept incoming connection from a client and get its socket and address
        client_socket, address = server_socket.accept()

        print("Client connected:", address)
        threading.Thread(target=handle_client, args=(client_socket, address)).start()

        # Start a new thread
        threading.Thread(target=print_subsandpubs).start()

if __name__ == '__main__':
    # Check if the correct number of arguments (port) is provided
    if len(sys.argv) != 2:
        print("Usage: python server_app.py <port>")
        sys.exit(1)

    port = int(sys.argv[1])
    start_server(port)
