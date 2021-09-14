#!/usr/bin/env python

import socket
from socket import AF_INET, SOCK_DGRAM
from struct import pack, calcsize

# Send to the UDP protocol port
UDP_PORT = 21074

# Send the laser diodes current level datagrams to the address
dest = "127.0.0.1"

# Contants
MAGIC = 0xD10D
VERSION = 0x0100

# The UDP diagram payload has data fields described in struct format
payload_fmt = '>8H'
size = calcsize(payload_fmt)

# Payload data fields has constants and laser diode current level codes. 
angld1, angld2, linld1, linld2, focld1, focld2 = 1000, 0, 1000, 0, 1000, 0

# Returns a bytes object
packet = pack(payload_fmt, MAGIC, VERSION, angld1,
angld2, linld1, linld2, focld1, focld2)

# Create a socket object
s = socket.socket(family=AF_INET, type=SOCK_DGRAM, proto=0)

# Sends laser diodes current level broadcast protocol datagrams
s.sendto(packet,(dest, UDP_PORT))
