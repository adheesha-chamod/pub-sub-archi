import socket
import sys
import threading

topic_subscribers = {}

def handle_client(client_socket, address):
    # Receive client type and topic from the client
    client_type = client_socket.recv(1024).decode()
    client_type, topic = client_type.split(',')
    
    if client_type.upper() == "SUBSCRIBER":
        # If the client is a subscriber, add it to the list of subscribers for the specified topic
        if topic not in topic_subscribers:
            topic_subscribers[topic] = []
        topic_subscribers[topic].append(client_socket)
        print("Subscriber connected:", address, "Topic:", topic)

    elif client_type.upper() == "PUBLISHER":
        # If the client is a publisher, add it to the list of publishers for the specified topic
        if topic not in topic_subscribers:
            topic_subscribers[topic] = []
        topic_subscribers[topic].append(client_socket)
        print("Publisher connected:", address, "Topic:", topic)

    while True:
        # Receive data (up to 1024 bytes) from the client
        data = client_socket.recv(1024)
        if not data:
            break

        incoming = data.decode()
        topic, message = incoming.split(':')
        print("Received from Publisher", address, ":", message, "| Topic:", topic)

        if data.decode().lower() == "terminate":
            break

        if client_type.upper() == "PUBLISHER":
            # If the client is a publisher, forward the data to all connected subscribers of the topic
            data = message.encode()
            if topic in topic_subscribers:
                subscribers = topic_subscribers[topic]
                for subscriber in subscribers:
                    subscriber.sendall(data)

    if client_type.upper() == "SUBSCRIBER":
        # If the client is a subscriber, remove it from the list of subscribers for the specified topic
        topic = client_socket.recv(1024).decode()
        if topic in topic_subscribers:
            topic_subscribers[topic].remove(client_socket)
            print("Subscriber disconnected:", address)
    elif client_type.upper() == "PUBLISHER":
        print("Publisher disconnected:", address)

    client_socket.close()

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

        # Print that a client has connected and start a new thread to handle the client
        print("Client connected:", address)
        threading.Thread(target=handle_client, args=(client_socket, address)).start()

if __name__ == '__main__':
    # Check if the correct number of arguments (port) is provided
    if len(sys.argv) != 2:
        print("Usage: python server_app.py <port>")
        sys.exit(1)

    port = int(sys.argv[1])
    start_server(port)
