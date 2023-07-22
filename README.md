# Publish - Subscribe Middleware Architecture
SCS3203-Middleware-Architecture Assignment 01
Luminary Group-37

To use the application, follow the outlined steps:

## Clone this repository :
```console
git clone https://github.com/tharindugunawardhana99/Pub-Sub_Architecture.git
```

# Task - 01
Created a simple client-server architecture.

--Instructions to run the code

1. Run server.

    i. goto task_01 directory in a new terminal

    ```console
    cd task_01
    ```

    ii. Run the server_app.py file with the port number as an argument.

    ```console
    python server_app.py 5000
    ```

2. Run the client.

    i. goto task_01 directory in a new terminal

    ```console
    cd task_01
    ```

    ii. Run the client_app.py file with the server ip and port number as arguments in a new terminal.

    ```console
    python client_app.py localhost 5000
    ```

    iii. Enter the message to be sent to the server. 

    ```console
    Enter message: Hello Server
    ```

    iv. Terminate the publisher.

    ```console
    Enter message: terminate
    ```

# Task - 02

Enhanced client-server architecture to publisher-subscriber architecture.

1. Run server.

    i. goto task_02 directory in a new terminal

    ```console
    cd task_02
    ```

    ii. Run the server_app.py file with the port number as an argument.

    ```console
    python server_app.py 5000
    ```

2. Run the client as publisher.

    i. goto task_02 directory in a new terminal

    ```console
    cd task_02
    ```

    ii. Run the client_app.py file with the server IP, port number, and publisher as arguments in a new terminal.

    ```console
    python client_app.py localhost 5000 publisher
    ```

    iii. Enter the message to be sent to the server. 

    ```console
    Enter message: Hello Server
    ```

    iv. Terminate the publisher.

    ```console
    Enter message: terminate
    ```

3. Run the client as a subscriber.

    i. goto task_02 directory in a new terminal

    ```console
    cd task_02
    ```

    ii. Run the client_app.py file with the server IP, port number, and subscriber as arguments in a new terminal.

    ```console
    python client_app.py localhost 5000 subscriber
    ```

3. Run the client_app.py file with the server IP, port number, and subscriber or publisher as arguments.

```console
python client_app.py localhost 5000 publisher
```

4. Enter the message to be sent to the server. 

```console
Enter message: Hello Server
```

# Task - 03

Enhanced publisher-subscriber architecture to publisher architecture with channel filtering topic based.

1. Run server.

    i. goto task_03 directory in a new terminal

    ```console
    cd task_03
    ```

    ii. Run the server_app.py file with the port number as an argument.

    ```console
    python server_app.py 5000
    ```

2. Run the client as publisher.

    i. goto task_03 directory in a new terminal

    ```console
    cd task_03
    ```

    ii. Run the client_app.py file with the server IP, port number, publisher, and topic as arguments in a new terminal.

    ```console
    python client_app.py localhost 5000 publisher topic1
    ```

    iii. Enter the message to be sent to the server. 

    ```console
    Enter message: Hello Server
    ```

    iv. Terminate the publisher.

    ```console
    Enter message: terminate
    ```

3. Run the client as a subscriber.

    i. goto task_03 directory in a new terminal

    ```console
    cd task_03
    ```

    ii. Run the client_app.py file with the server IP, port number, subscriber, and topic as arguments in a new terminal.

    ```console
    python client_app.py localhost 5000 subscriber topic1
    ```
# Task -04

![Task4img](https://github.com/tharindugunawardhana99/Pub-Sub_Architecture/assets/89847807/03949b72-a2f1-46ee-8ee1-25b750c6f0f9)

Description-
In this architecture, the message broker is the central point of communication for publishers and subscribers. The message broker is responsible for storing messages in a durable storage and distributing them to subscribers.

To improve availability and reliability, the message broker should be deployed in a distributed manner. This means that there should be multiple instances of the message broker running in different locations. If one instance of the message broker fails, the other instances will continue to operate.

In addition, the message broker should be configured to replicate messages to multiple storage nodes. This will ensure that if one storage node fails, the messages will still be available in other storage nodes.

The following are some of the benefits of the distributed architecture for Pub/Sub:

1.Improved availability: The single server node's single point of failure is eliminated by the distributed design. The message broker's other instances will keep running even if one instance crashes.

2.Improved reliability: Even if one storage node fails, messages will still be available thanks to the distributed architecture's replication of messages to numerous storage nodes.

3.Scalability: More instances of the message broker and storage nodes can be added to grow the distributed architecture to handle more traffic. 
