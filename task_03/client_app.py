import socket
import sys

def start_client(host, port, mode, topic=None):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to server")

    # Send the client mode (PUBLISHER or SUBSCRIBER) to the server
    client_socket.sendall(mode.encode())

    if mode.upper() == "SUBSCRIBER":
        if topic:
            # If the client is a subscriber and a topic is provided, send the topic to the server
            topic = f',{topic}'
            client_socket.sendall(topic.encode())
        else:
            print("Please provide a topic for the subscriber.")
            client_socket.close()
            return

        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print("Received message:", data.decode())

    elif mode.upper() == "PUBLISHER":
        if topic:
            # If the client is a publisher and a topic is provided, send the topic to the server
            topic_to_send = f',{topic}'
            client_socket.sendall(topic_to_send.encode())
        else:
            print("Please provide a topic for the publisher.")
            client_socket.close()
            return

        while True:
            message = input("Enter message: ")
            prepare_for_send = f'{topic}:{message}'
            client_socket.sendall(prepare_for_send.encode())
            if message.lower() == "terminate":
                break

    # Close the socket and end the connection
    client_socket.close()
    print("Disconnected from server")

if __name__ == '__main__':
    if len(sys.argv) < 4 or len(sys.argv) > 5:
        print("Usage: python client_app.py <host> <port> <mode (PUBLISHER or SUBSCRIBER)> [<topic>]")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    mode = sys.argv[3]
    topic = sys.argv[4] if len(sys.argv) == 5 else None

    start_client(host, port, mode, topic)
