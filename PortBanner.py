#!/usr/bin/python

import socket

def VulBan(ip,port):
    try:
        socket.setdefaulttimeout(1)
        s=socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return


def main():
    ip = input("[*] Type your Target IP Address")
    for port in range(1,100):
        banner=VulBan(ip,port)
        if banner:
            print("[*]" + ip + "/" + str(port) + ":" + banner.strip('/n'))

main()

