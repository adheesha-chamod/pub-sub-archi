# Publish - Subscribe Middleware Architecture
SCS3203-Middleware-Architecture Assingment 01
Luminary Group-37

To use the application, follow the outlined steps:

## Clone this repository :
```console
git clone https://github.com/tharindugunawardhana99/Pub-Sub_Architecture.git
```

## Task-01
Created a simple client server architecture.

--Instructions to run the code

1. Run server.

    i. goto Task_01 directory in a new terminal

    ```console
    cd Task_01
    ```

    ii. Run the server.py file with the port number as an argument.

    ```console
    python server.py 5000
    ```

2. Run the client.

    i. goto Task_01 directory in a new terminal

    ```console
    cd Task_01
    ```

    ii. Run the client.py file with the server ip and port number as arguments in a new terminal.

    ```console
    python client.py localhost 5000
    ```

    iii. Enter the message to be sent to the server. 

    ```console
    Enter message: Hello Server
    ```

    iv. Terminate the publisher.

    ```console
    Enter message: terminate
    ```

## Task-02

Enhanced client server architecture to publisher subscriber architecture.

1. Run server.

    i. goto Task_01 directory in a new terminal

    ```console
    cd Task_01
    ```

    ii. Run the server.py file with the port number as an argument.

    ```console
    python server.py 5000
    ```

2. Run the client as publisher.

    i. goto Task_01 directory in a new terminal

    ```console
    cd Task_01
    ```

    ii. Run the client.py file with the server ip, port number and publisher as arguments in a new terminal.

    ```console
    python client.py localhost 5000 publisher
    ```

    iii. Enter the message to be sent to the server. 

    ```console
    Enter message: Hello Server
    ```

    iv. Terminate the publisher.

    ```console
    Enter message: terminate
    ```

3. Run the client as subscriber.

    i. goto Task_01 directory in a new terminal

    ```console
    cd Task_01
    ```

    ii. Run the client.py file with the server ip, port number and subscriber as arguments in a new terminal.

    ```console
    python client.py localhost 5000 subscriber
    ```

3. Run the client.py file with the server ip, port number and subscriber or publisher as arguments.

```console
python client.py localhost 5000 publisher
```

4. Enter the message to be sent to the server. 

```console
Enter message: Hello Server
```

## Task -03

Enhanced publisher subscriber architecture to publisher architecture with channel filtering topic based.

1. Run server.

    i. goto Task_01 directory in a new terminal

    ```console
    cd Task_01
    ```

    ii. Run the server.py file with the port number as an argument.

    ```console
    python server.py 5000
    ```

2. Run the client as publisher.

    i. goto Task_01 directory in a new terminal

    ```console
    cd Task_01
    ```

    ii. Run the client.py file with the server ip, port number, publisher and topic as arguments in a new terminal.

    ```console
    python client.py localhost 5000 publisher topic1
    ```

    iii. Enter the message to be sent to the server. 

    ```console
    Enter message: Hello Server
    ```

    iv. Terminate the publisher.

    ```console
    Enter message: terminate
    ```

3. Run the client as subscriber.

    i. goto Task_01 directory in a new terminal

    ```console
    cd Task_01
    ```

    ii. Run the client.py file with the server ip, port number, subscriber and topic as arguments in a new terminal.

    ```console
    python client.py localhost 5000 subscriber topic1
    ```

# Task -04

![Picture1](https://github.com/tharindugunawardhana99/Pub-Sub_Architecture/assets/89847807/56de285c-c124-41b7-86a1-9043dfc7d02c)
