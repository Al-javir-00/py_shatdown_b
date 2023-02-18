

from tkinter import *
import time
import os

def r_p(re_pa):
    try:
        base_p = sys._MEIPASS
    except Exception:
        base_p = os.path.abspath(".")

    return os.path.join(base_p, re_pa)  


def Restart():
    os.system("shutdown /r /t 1")
def  Restar_time():
    os.system("shutdown /r /t 20")   
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")





t = Tk()
frameCnt = 9
frames = [PhotoImage(file=r_p('ig2.gif'),format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    t.after(100, update, ind)
label = Label(t)
label.pack()
t.after(0, update, 0)

l1 = Button(t,text="logout...",font=("Times New Roman",20),fg=("#39FF14"),bg="black",command=logout)
l1.place(x=200,y=35,height=45,width=170)

l1 = Button(t,text="Restar_time...",font=("Times New Roman",20),fg=("#39FF14"),bg="black",command=Restar_time)
l1.place(x=200,y=120,height=45,width=170)

l1 = Button(t,text="Restart...",font=("Times New Roman",20),fg=("#39FF14"),bg="black",command=Restart)
l1.place(x=200,y=220,height=45,width=170)

l1 = Button(t,text="Shut down...",font=("Times New Roman",20),fg=("#39FF14"),bg="black",command=shutdown)
l1.place(x=200,y=320,height=45,width=170)

t.mainloop()