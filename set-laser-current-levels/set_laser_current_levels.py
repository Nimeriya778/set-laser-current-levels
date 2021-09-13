#!/usr/bin/env python

import socket
from socket import AF_INET, SOCK_DGRAM

# Create a socket object
s = socket.socket(family=AF_INET, type=SOCK_DGRAM, proto=0)

# Send to this address
host = "127.0.0.1"

# Send to the UDP protocol port
UDP_PORT = 21074

s.sendto(bytes(16), (host, UDP_PORT))