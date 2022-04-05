# IS496: Computer Networks (Spring 2022)
# Programming Assignment 3 - Starter Code
# Name and Netid of each member:
# Member 1: 
# Member 2: 
# Member 3: 



# Note: 
# This starter code is optional. Feel free to develop your own solution. 


# Import any necessary libraries below
import socket
import threading
import sys, os, struct

# Any global variables
BUFFER =  2048



# Convert from int to byte
def sendint(data):
    return int(data).to_bytes(4, byteorder='big', signed=True)

# Convert from byte to int
def receiveint(data):
    return int.from_bytes(data, byteorder='big', signed=True)



"""
The thread target fuction to handle any incoming message from the server.
Args:
    None
Returns:
    None
Hint: you can use the first character of the message to distinguish different types of message
"""
def accept_messages():
    print()





if __name__ == '__main__': 
    # TODO: Validate input arguments
    
    hostname = sys.argv[1]
    PORT = sys.argv[2]

    # Find the host by its name and create host's address
    try:
        HOST = socket.gethostbyname(hostname)
    except socket.error as e:
        print(f"Unknown host {hostname}")
    sin = (HOST, int(PORT))

    # TODO: create a socket with UDP or TCP, and connect to the server
    # Create a socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print('Failed to create socket.')
        sys.exit()


    # Connect to the host from Command-line input
    try:
        sock.connect(sin)
    except socket.error as msg:
        print("Connection failed!")
        sys.exit()

    print("Connection to server established")
    
    
    # Using while loop to make sure that we can go back to "prompt user for operation" state as we want
    while True:
        # TODO: Send username to the server and login/register the user
        username = input("Please enter your operation: ")
        sock.send(sendint(len(username)))
        sock.send(username.encode())


        # TODO: initiate a thread for receiving message
        


        # TODO: use a loop to handle the operations (i.e., BM, PM, EX)
    
