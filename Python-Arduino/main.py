
from tkinter import *
import threading
import socket

s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)#socket.AF_INET, socket.SOCK_DGRAM
host = '197.57.149.137'
port = 5000

address = ('197.57.149.137', 5000)




s.connect((host, port))



#s.sendto(str.encode('d'),address)


Metal_counter = 0
NonMetal_counter = 0

#no_error=True

def Socket_loop():
    while True:
        try:
            print("thread1")
            data = s.recv(1024)
            if len(data) > 0:
                if data.decode("utf-8") == 'M':
                    global Metal_counter
                    Metal_counter += 1
                    print(Metal_counter)


                elif data.decode("utf-8") == 'N':
                    global NonMetal_counter
                    NonMetal_counter += 1
                    print(NonMetal_counter)


        except socket.error:
            pass
            #global no_error
            #no_error = False
            #s.connect((host, port))




def GUI_loop():


    def BTN_command():
        while True:
            if Metal_counter == 1:
                print(Metal_counter)
                Metallbl1["bg"] = "Green"

            elif Metal_counter == 2:
                Metallbl2["bg"] = "Green"

            elif Metal_counter == 3:
                Metallbl3["bg"] = "Green"

            elif Metal_counter == 4:
                Metallbl4["bg"] = "Green"

            if NonMetal_counter == 1:
                NonMetallbl1["bg"] = "Green"

            elif NonMetal_counter == 2:
                NonMetallbl2["bg"] = "Green"

            elif NonMetal_counter == 3:
                NonMetallbl3["bg"] = "Green"

            elif NonMetal_counter == 4:
                NonMetallbl4["bg"] = "Green"
    root = Tk()
    root.geometry("2048x1024")
    root.configure(bg="#00a1a3")
    root.title("Production Line")

    bg = PhotoImage(file="20191226_181243-03.png")

    # Show image using label
    label1 = Label(root,width="1000", height="1000" ,image=bg)
    label1.place(x=0, y=0)



    print("thread2")
    print(Metal_counter)
    fr1 = Frame(root, bg="#00a1a3")
    #BTN=Button(root,command=BTN_command,text="update",bg="red",fg="blue")
    intr2 = Label(fr1, width="4", height="5", bg="#00a1a3")
    Metallbl1 = Label(fr1, width="10", height="5", bg="#003839")
    Metalintr1 = Label(fr1, width="10", height="2", bg="#00a1a3")
    Metallbl2 = Label(fr1, width="10", height="5", bg="#003839")
    Metalintr2 = Label(fr1, width="2", height="5", bg="#00a1a3")
    Metallbl3 = Label(fr1, width="10", height="5", bg="#003839")
    Metalintr3 = Label(fr1, width="10", height="2", bg="#00a1a3")
    Metallbl4 = Label(fr1, width="10", height="5", bg="#003839")
    intr = Label(fr1, width="10", height="5", bg="#00a1a3")
    NonMetallbl1 = Label(fr1, width="10", height="5", bg="#003839")
    NonMetalintr1 = Label(fr1, width="10", height="2", bg="#00a1a3")
    NonMetallbl2 = Label(fr1, width="10", height="5", bg="#003839")
    NonMetalintr2 = Label(fr1, width="2", height="5", bg="#00a1a3")
    NonMetallbl3 = Label(fr1, width="10", height="5", bg="#003839")
    NonMetalintr3 = Label(fr1, width="10", height="2", bg="#00a1a3")
    NonMetallbl4 = Label(fr1, width="10", height="5", bg="#003839")
    fr1.pack(side="right")
    #BTN.pack()
    intr2.grid(column=9, row=1)
    Metallbl1.grid(column=2, row=1)
    Metalintr1.grid(column=2, row=2)
    Metallbl2.grid(column=2, row=3)
    Metalintr2.grid(column=3, row=1)
    Metallbl3.grid(column=4, row=1)
    Metalintr3.grid(column=4, row=2)
    Metallbl4.grid(column=4, row=3)
    intr.grid(column=5, row=1)
    NonMetallbl1.grid(column=6, row=1)
    NonMetalintr1.grid(column=6, row=2)
    NonMetallbl2.grid(column=6, row=3)
    NonMetalintr2.grid(column=7, row=1)
    NonMetallbl3.grid(column=8, row=1)
    NonMetalintr3.grid(column=8, row=2)
    NonMetallbl4.grid(column=8, row=3)



    gui2_thread = threading.Thread(target=BTN_command,daemon=True)
    gui2_thread.start()


    root.mainloop()




gui_thread = threading.Thread(target=GUI_loop)
socket_thread = threading.Thread(target=Socket_loop,daemon=True)

gui_thread.start()
socket_thread.start()










