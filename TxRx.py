#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 14:29:28 2022

@author: Strontium

should be as a class, then instantiate and use methods
adapted from Sentdex 
https://pythonprogramming.net/server-chatroom-sockets-tutorial-python-3/
"""

import socket
import select
import errno
import sys

SECRET_KEY = b'pseudorandomly generated server secret key'
AUTH_SIZE = 16 

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

"""
"""
my_username = input("Username: ")

txsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
txsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind, so server informs operating system that it's going to use given IP and port
# For a server using 0.0.0.0 means to listen on all available interfaces, useful 
#to connect locally to 127.0.0.1 and remotely to LAN interface IP
txsock.bind((IP, PORT))
txsock.listen()
socksin = [txsock]
nodes = {}

rxsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rxsock.connect((IP, PORT))
# stop .recv() call from blocking
rxsock.setblocking(False)

uname = my_username.encode('utf-8')
uname_hdr = f"{len(uname):<{HEADER_LENGTH}}".encode('utf-8')
rxsock.send(uname_hdr + uname)

def rxmsg(insock):
    try:
        msghdr = insock.recv(HEADER_LENGTH)
        if not len(msghdr):
            return False
        msglen = int(msghdr.decode('utf-8').strip())
        return {'header': msghdr, 'data': insock.recv(msglen)}
    except:
        return False


def txmsg(modelinfo):
    if modelinfo:
        modelinfo = modelinfo.encode('utf-8')
        modelinfo_hdr = f"{len(modelinfo):<{HEADER_LENGTH}}".encode('utf-8')
        
        _, writes, excepts = select.select(socksin, [], socksin)
        for sock in writes:
            if sock == txsock:
                nodesock, nodeaddr = txsock.accept()
                user = rxmsg(nodesock)
                if user is False:
                    continue
                socksin.append(nodesock)
                nodes[nodesock] = user
                print('new conn from {}:{}, user: {}'.format(*nodeaddr, user['data'].decode('utf-8')))
            else:               
                user = nodes[sock]
                print(f'message from {user["data"].decode("utf-8")}: {msg["data"].decode("utf-8")}')
                for nodesock in nodes:
                    if nodesock != sock:
                        nodesock.send(modelinfo_hdr + modelinfo)
        for sock in excepts:
            socksin.remove(sock)
            del nodes[sock]
        #rxsock.send(modelinfo_hdr + modelinfo)
    

while True:
    reads, _, excepts = select.select(socksin, [], socksin)
    for sock in reads:
        if sock == txsock:
            nodesock, nodeaddr = txsock.accept()
            user = rxmsg(nodesock)
            if user is False:
                continue
            socksin.append(nodesock)
            nodes[nodesock] = user
            print('new conn from {}:{}, user: {}'.format(*nodeaddr, user['data'].decode('utf-8')))
        else:
            msg = rxmsg(sock)
            if msg is False:
                print('closed conn from: {}'.format(nodes[sock]['data'].decode('utf-8')))
                socksin.remove(sock)
                del nodes[sock]
                continue
            user = nodes[sock]
            print(f'message from {user["data"].decode("utf-8")}: {msg["data"].decode("utf-8")}')
            for nodesock in nodes:
                if nodesock != sock:
                    nodesock.send(user['header'] + user['data'] + msg['header'] + msg['data'])
    for sock in excepts:
        socksin.remove(sock)
        del nodes[sock]

