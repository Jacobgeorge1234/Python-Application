import tkinter as tk
import pyqrcode as qr
import png
from pyqrcode import QRCode

#Qstr = "https://www.instagram.com/technotitans360"
#url= qr.create(Qstr)
#url.png('myqr.png',scale = 100)
window = tk.Tk()
window.title("QR")
label = tk.Label(window,text="QR maker",font=("Helvetica",50))
label.grid(column=3,row=0)
label1 = tk.Label(window,text="Enter link",font=("Helvetica",10))
label1.grid(column=0,row=1)
txt = tk.Entry(window,width=50)
txt.grid(column=1,row=1)
label2 = tk.Label(window,text="Enter size",font=("Helvetica",10))
label2.grid(column=0,row=2)
txt2 = tk.Entry(window,width=10)
txt2.grid(column=1,row=2)
label3 = tk.Label(window,text="enter name",font=("Helvetica",10))
label3.grid(column=0,row=3)
txt3 = tk.Entry(window,width=50)
txt3.grid(column=1,row=3)
    

def clicked():
    Qstr = txt.get()
    a = int(txt2.get())
    b = txt3.get()
    url = qr.create(Qstr)
    url.png(b,scale=a)
   # res=  txt.get() + " is good"
   
but = tk.Button(window,text="press here",command=clicked)
but.grid(column=0,row=4)
window.geometry('1920x1080')
window.mainloop()
