#!/bin/python3
"""Chat Applikation mit einem GUI - Client Seite"""

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter

def eingehende_nachricht():
    """Die funktion zur erhaltung von Nachrichten"""
    while True:
        try:
            msg = client_socket.recv(BUFFERSIZE).decode("utf8")
            nachricht_liste.insert(tkinter.END, msg)
        except OSError:
            break # Falls der nutzer sich ausloggt

def versenden(event=None):
    """Nachrichten sendung funktion"""
    msg = nachricht.get()
    nachricht.set("") # Girdi kismini bosaltacak
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        app.quit()

def ausloggen(event=None):
    """Falls der Nutzer die kreuz taste drückt sendet es die {quit} funktion damit
    es nicht zur dupplikationen kommt."""
    nachricht.set("{quit}")
    versenden()



app = tkinter.Tk()
app.title("Saizzou's Chat")

nachricht_bereich = tkinter.Frame(app)
nachricht = tkinter.StringVar()
nachricht.set("Name Eingeben...")
scrollbar = tkinter.Scrollbar(nachricht_bereich)
nachricht_liste = tkinter.Listbox(nachricht_bereich, height=20, width=70,
                                yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
nachricht_liste.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
nachricht_liste.see("end")
nachricht_liste.pack()
nachricht_bereich.pack()

eingabe_feld = tkinter.Entry(app, textvariable=nachricht)
eingabe_feld.bind("<Return>", versenden)
eingabe_feld.pack()
sende_button = tkinter.Button(app, text="Senden", command=versenden)
sende_button.pack()

app.protocol("WM_DELETE_WINDOW", ausloggen)

HOST = '127.0.0.1'
PORT = 23847 #input("Server Port (OTO:23847): ")


if not PORT:
    PORT = 23847
else:
    PORT = int(PORT)

BUFFERSIZE = 1024
ADDR = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=eingehende_nachricht)
receive_thread.start()
tkinter.mainloop()