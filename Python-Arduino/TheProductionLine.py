
from tkinter import *
import threading
import socket


host = '192.168.1.7'
port = 5000

#socket.AF_INET, socket.SOCK_DGRAM
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = (host, port)
try:
    s.connect((host, port))
except:
    pass

#s.sendto(str.encode('d'),address)

Metal_counter = 0
NonMetal_counter = 0

State = 0

def Socket_loop():
    while True:
        try:
            print("thread1")
            data = s.recv(1024)
            if len(data) > 0:
                global State
                if data.decode("utf-8") == 'M':
                    global Metal_counter
                    Metal_counter += 1
                    print(Metal_counter)


                elif data.decode("utf-8") == 'N':
                    global NonMetal_counter
                    NonMetal_counter += 1
                    print(NonMetal_counter)


                elif data.decode("utf-8") == 'F':
                    State =1
                elif data.decode("utf-8") == 'S':
                    State =2


        except socket.error:
            pass
            global no_error
            no_error = False
            s.connect((host, port))

def GUI_loop():
    root = Tk()
    root.geometry("1024x1024")
    root.configure(bg="#00a1a3")
    root.title("Production Line")

    # Show image using label
    #IMG_bg = PhotoImage(file="20191226_181243-03.png")
    #IMG_label = Label(root,width="1000", height="1000" ,image = IMG_bg)
    #IMG_label.place(x=0, y=0)

    StateLblHDR =Label(root, text="STATE:",font="arial",width="15", height="1",fg="black", bg="#00a1a3")
    StateLbl = Label(root, text="Unknown.", font="calibri", width="15", height="1", fg="white", bg="#00a1a3")

    MetalNameLbl = Label(root, text="METAL",font="arial",width="15", height="2",fg="white", bg="#00a1a3")
    Metallbl1    = Label(root, width="10", height="5", bg="#003839")
    Metallbl2    = Label(root, width="10", height="5", bg="#003839")
    Metallbl3    = Label(root, width="10", height="5", bg="#003839")
    Metallbl4    = Label(root, width="10", height="5", bg="#003839")

    NonMetalNameLbl = Label(root,text="NON-METAL",font="arial",width="15", height="2",fg="white", bg="#00a1a3")
    NonMetallbl1    = Label(root, width="10", height="5", bg="#003839")
    NonMetallbl2    = Label(root, width="10", height="5", bg="#003839")
    NonMetallbl3    = Label(root, width="10", height="5", bg="#003839")
    NonMetallbl4    = Label(root, width="10", height="5", bg="#003839")

    MetalNameLbl.place(x=1060, y=580)
    Metallbl1.place(x=1050, y=400)
    Metallbl2.place(x=1050, y=500)
    Metallbl3.place(x=1150, y=400)
    Metallbl4.place(x=1150, y=500)

    NonMetalNameLbl.place(x=1300, y=580)
    NonMetallbl1.place(x=1300, y=400)
    NonMetallbl2.place(x=1300, y=500)
    NonMetallbl3.place(x=1400, y=400)
    NonMetallbl4.place(x=1400, y=500)

    StateLblHDR.place(x=1060, y=200)
    StateLbl.place(x=1080, y=230)

    def BTN_command():
        while True:
            if Metal_counter == 1:
                if Metallbl1["bg"] == "#003839":
                    Metallbl1["bg"] = "Green"


            elif Metal_counter == 2:
                if Metallbl2["bg"] == "#003839":
                    Metallbl2["bg"] = "Green"


            elif Metal_counter == 3:
                if Metallbl3["bg"] == "#003839":
                    Metallbl3["bg"] = "Green"


            elif Metal_counter == 4:
                if Metallbl4["bg"] == "#003839":
                    Metallbl4["bg"] = "Green"


            if NonMetal_counter == 1:
                if NonMetallbl1["bg"] == "#003839":
                    NonMetallbl1["bg"] = "Green"


            elif NonMetal_counter == 2:
                if NonMetallbl2["bg"] == "#003839":
                    NonMetallbl2["bg"] = "Green"


            elif NonMetal_counter == 3:
                if NonMetallbl3["bg"] == "#003839":
                    NonMetallbl3["bg"] = "Green"


            elif NonMetal_counter == 4:
                if NonMetallbl4["bg"] == "#003839":
                    NonMetallbl4["bg"] = "Green"

            global State
            if State ==2:
                StateLbl["text"]="Storing"
            elif State ==1:
                StateLbl["text"] = "Feeding"



    gui2_thread = threading.Thread(target=BTN_command,daemon=True)
    gui2_thread.start()
    root.mainloop()


gui_thread = threading.Thread(target=GUI_loop)
socket_thread =threading.Thread(target=Socket_loop,daemon=True)
gui_thread.start()
socket_thread.start()
