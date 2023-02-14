# CS361: Character Selector for League of Legends

## Communication Contract

A) How to REQUEST data from microservice:
  
    The microservices makes use of a Python library calls ZeroMQ. In order to request data, a client file is needed.
    The client file sends the requests to the server file, which then selects what to send back depending on the request.
    The matching criterias for the REQUEST and what will get send back will be predetermined by me and my partner.
    
    ------------Example Call-----------
    import zmq
    context = zmq.Context()
    print("Connecting to server...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:3000")

    print("Sending Request...")
    socket.send(b"Chest")
    message1 = socket.recv()
    socket.send(b"Beginner")
    
    
B) How to RECEIVE data from microservice:

    The microservices makes use of a Python library calls ZeroMQ. In order to RECEIVE data, a client and a server file is needed.
    The client file contains the code to REQUEST data from the server. Once the REQUEST is processed by the server, it will send back
    the matching data to the client 
    The client contains the code needed to RECEIVE data from the server.

C) UML DIAGRAM
![Capture](https://user-images.githubusercontent.com/76918818/218648641-a4ec9f73-6645-4eb5-bc7b-7a4477e972f8.PNG)


