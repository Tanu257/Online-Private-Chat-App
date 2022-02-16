import socket
from threading import Thread
from tkinter import *


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Port = []

# Functions

def Create_Lobby_Fnction():
    Port.append(int(Create_Lobby__port.get()))
    Port.append(socket.gethostbyname(socket.gethostname()))

    s.bind((Port[1],Port[0]))
    s.listen(2)

    Create_Join_Window.destroy()
    Port.append("Server")
    
def Join_Lobby_Function():

    Port.append(int(Join_Lobby_Port.get()))
    Port.append(Join_Lobby_Ip.get())

    s.connect((Port[1],Port[0]))

    Create_Join_Window.destroy()


Create_Join_Window = Tk()

Label(Create_Join_Window,text="Make A Lobby").grid(row=1,column=1)

Create_Lobby__port = Entry(Create_Join_Window)
Create_Lobby__port.grid(row=2,column=1)

Create_Lobby__Button = Button(Create_Join_Window,text="Create",command=Create_Lobby_Fnction,bg="#418ad9").grid(row=3,column=1)

# Join Lobby Part

Label(Create_Join_Window,text="-----------------------").grid(row=4,column=1)

Label(Create_Join_Window,text="Get A Lobby").grid(row=4,column=1)

Join_Lobby_Ip = Entry(Create_Join_Window)
Join_Lobby_Ip.grid(row=5,column=1)

Join_Lobby_Port = Entry(Create_Join_Window)
Join_Lobby_Port.grid(row=6,column=1)

Join_Lobby_Button = Button(Create_Join_Window,text="Join Lobby",command=Join_Lobby_Function,bg="#f06c6c").grid(row=7,column=1)


Create_Join_Window.mainloop()

# After That
clients_ed = []

def accepting():
    while True:
        got_pl,huh = s.accept()
        clients_ed.append(got_pl)


def listenning_on_0():
    while True:
        try:       
            got = clients_ed[0].recv(1024)

            clients_ed[1].send(got)
        except:
            None
def listenning_on_1():
    while True:
        try:       
            got = clients_ed[1].recv(1024)

            clients_ed[0].send(got)
        except:
            None
def listening_For_Client():
    while True:
        try:
            got_from_server = s.recv(1024).decode()
        except:
            continue
        Chat_Round.insert(END,("Other:-" + got_from_server))

def Send_it():
    mass = Send_span.get()
    s.send(mass.encode())
    Send_span.delete(0,END)
    Send_span.insert(0,"")
    Chat_Round.insert(END,( "You:-" + mass))

def Clear_ct():
    Chat_Round.delete(0,END)
        
if(len(Port) == 2):
    Thread(target=(listening_For_Client)).start()

if(len(Port) == 2):

    Main_Chat_Window = Tk()
    Label(Main_Chat_Window,text="----Chat----",bg="#ebc9a0").grid(row=0,column=2)
    Label(Main_Chat_Window,text=f"{Port[1]} -- {Port[0]}").grid(row=0,column=3)

    Chat_Round = Listbox(Main_Chat_Window)
    Chat_Round.grid(row=1,column=2)

    Clear_Button = Button(Main_Chat_Window,text="Clear Chat",command=Clear_ct,bg="#de5d0d").grid(row=1,column=3)

    Send_span = Entry(Main_Chat_Window,fg="#f25844")
    Send_span.grid(row=2,column=2)

    Send_Button = Button(Main_Chat_Window,text="Send",command=Send_it,bg="#2acafa").grid(row=2,column=3)

    Main_Chat_Window.mainloop()



if(len(Port) ==3):
    Thread(target=(listenning_on_0)).start()
    Thread(target=(listenning_on_1)).start()
    Thread(target=(accepting)).start()

if(len(Port) == 3):
    root = Tk()
    Label(root,text=f"{Port[1]} -- {Port[0]}").grid(row=0,column=0)
    root.mainloop()