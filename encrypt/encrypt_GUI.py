import tkinter as tk
import encrypt as en
root = tk.Tk()
id="N"
var = ""
root.geometry('300x500')


def encoding():
    print(E1.get(),len(E1.get()))
    E.delete(0, 20)
    E.insert(0,en.encode(E1.get()))

    
def decoding():
    print(E.get(),len(E.get()))
    w['text']=en.decode(E.get())

    
E = tk.Entry(root, textvariable=var)
B = tk.Button(root, text ="加密", command = encoding)
z = tk.Label(root, text="")
E1 = tk.Entry(root)
B2 = tk.Button(root, text ="解密", command = decoding)
w = tk.Label(root, text="")


E1.pack()

B.pack()
E.pack()
B2.pack()
w.pack()
z.pack()
root.mainloop()
