#!/bin/python3
# Chat App Server Einrichtung
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

clients = {}
addresses = {}

HOST = '127.0.0.1'
PORT = 23847
BUFFERSIZE = 1024
ADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

def einkommende_verbindung():
    """Einrichtung der kommende Verbindungen"""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s hat sich verbunden." % client_address)
        client.send(bytes("Saizzou's Chat App! \n" +
                          "Bitte geben Sie in dem Nachricht bereich ihren name ein: ", "utf8"))
        addresses[client] = client_address
        Thread(target=client_verbindung, args=(client,)).start()

def client_verbindung(client):
    """Einzelne Client Verbindung funktion"""
    name = client.recv(BUFFERSIZE).decode("utf8")
    willkommen = 'Willkomen %s! Um sich auszuloggen schreiben Sie bitte {quit}!' %name
    client.send(bytes(willkommen, "utf8"))
    msg = "%s hat sich Verbunden!" %name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name
    while True:
        msg = client.recv(BUFFERSIZE)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s hat sich ausgeloggt." %name, "utf8"))
            break

def broadcast(msg, prefix=""):
    """Publikation von Nachrichten"""
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

if __name__ == "__main__":
    SERVER.listen(10) # Maximum 10 nutzer auf dem Server erlaubt
    print("Wartet auf Verbindungen...")
    ACCEPT_THREAD = Thread(target=einkommende_verbindung)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()