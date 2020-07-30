#!/usr/bin/env python
#Python server
#The program is optimized and may run on any
#other python version with/without modifications
import socket;
import sys;
import argparse;
host = 'localhost'
data_payload = 2048
backlog = 5
def echo_server(port):
    "A simple echo server"
    #Create a TCP socket
    sock = socket.setsockopt(socket.AF_INET, socket.SOCK_STREAM)
    #Enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    #Bind the socket to the port
    server_address = (host, port)
    print ( "starting up echo server on %s port %s" % server_address)
    sock.bind(server_address)
    #Listen to clients, backlog argument specifies the max no. of queued connections
    sock.listen(backlog)
    while True:
        print("Waiting to receive message from client" )
        client, address = sock.accept();
        data = client.recv(data_payload)
        if data:
            print("Data: %s" %data)
            client.send(data)
            print("sent %s bytes back to %s" %(data,address))
            #end connection
            client.close()
            if _name_ == '_main_':
                parser = argparse.ArgumentParser(description= 'Socket Server Example')
                parser.add_argument('--port', action= "store", dest = "port", type = int,
                                    required= True)
                given_args = parser.parse_args()
                port = given_args.port
                echo_server(port)

