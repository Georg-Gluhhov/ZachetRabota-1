from tkinter import *
import time 
win=Tk()

fail=open("saves.txt","r",encoding="utf-8-sig")
mas=[] 
for rida in fail:
    mas.append(rida.strip())
fail.close
print(mas)
count=0
try:
    count=int(mas.pop(0))
    mult=int(mas.pop(0))
    autoclickers=int(mas.pop(0))
    pricemlt=int(mas.pop(0))
    autoprice=int(mas.pop(0))
except:
    pass
if count <=0:
    count = 0 #количество кликов
    mult = 1 #умножение кликов
    autoclickers = 0 #количество автокликов
    pricemlt = 1 #цена умножения
    autoprice = 1 #цена автокликов
else:
    pass




def exut(event):
    fail=open("saves.txt","w",encoding="utf-8-sig")
    fail.write(str(count)+"\n"+str(mult)+"\n"+str(autoclickers)+"\n"+str(pricemlt)+"\n"+str(autoprice))
    win.destroy()
    fail.close
    

def autoclickbuy(event):
    global count
    global autoprice
    global autoclickers #
    if count < 7*autoprice:
        nem()
    else:
        count -= 7*autoprice #
        autoclickers += 1+autoclickers #
        autoprice= autoprice*2
        albl.config(text="("+str(autoclickers)+")Купить авто клик: "+str(7*autoprice))
        btn['text']=str(count)
        sec()

def autoclick():
    global win
    global count
    global autoclickers
    count += autoclickers #
    win.after(1000, autoclick) #
    btn['text']=str(count)


def vajutame(event):
    global count
    global mult
    count = count+mult
    btn['text']=str(count)
def mltclickbuy(event):
    global count
    global pricemlt
    global mult
    if count < 5*pricemlt:
        nem()
    elif count >= 5*pricemlt:
        mult = mult*2
        count = count - 5*pricemlt
        pricemlt= pricemlt*3
        btn['text']=str(count)
        sec()
        lbl.config(text="(x"+str(mult)+") Купить двойной клик: "+str(5*pricemlt))
def nem():
    balbl.config(text="не хватает кридитов!",bg="red")
    win.after(3000, nol)
def sec():
    balbl.config(text="куплено!",bg="green")
    win.after(1800, nol)
def nol():
    balbl.config(text="...",bg="black")

def prpl():
    lbl.config(bg="purple",fg="white")
    win.config(bg="purple")
    albl.config(bg="purple",fg="white")
    btn.config(bg="purple",fg="white")
def wht():
    lbl.config(bg="white",fg="black")
    win.config(bg="white")
    albl.config(bg="white",fg="black")
    btn.config(bg="white",fg="black")
def gr():
    lbl.config(bg="black",fg="white")
    win.config(bg="black")
    albl.config(bg="black",fg="white")
    btn.config(bg="black",fg="white")
def blu():
    lbl.config(bg="blue",fg="black")
    win.config(bg="blue")
    albl.config(bg="blue",fg="black")
    btn.config(bg="blue",fg="black")

win.title("Akna nimetus")
win.geometry("1280x720")
win.config(bg="black")
btn=Button(win,text="Vajuta \nsiia",fg="white", bg="black", font="Arial 40",width=24,height=3)
lbl=Label(win,text="(x"+str(mult)+") Купить двойной клик: "+str(5*pricemlt),fg="white", bg="black", font="Arial 30", width=30,height=3)
albl=Label(win,text="("+str(autoclickers)+")Купить авто клик: "+str(7*autoprice),fg="white", bg="black", font="Arial 30", width=30,height=3)
balbl=Label(win,text="...",fg="white", bg="black", font="Arial 30", width=30,height=2)
ex=Label(win,text="Выход",fg="black", bg="gray", font="Arial 30", width=5,height=3)
var=IntVar()
var.set(3)
M=Menu(win)
win.config(menu=M)
m2=Menu(M,tearoff=0)
M.add_cascade(label="BGC",menu=m2)
m2.add_command(label="Black",command=gr)
m2.add_command(label="White",command=wht)
m2.add_command(label="Blue",command=blu)
m2.add_command(label="Purple",command=prpl)

btn.bind("<Button-1>",vajutame)
lbl.bind("<Button-1>",mltclickbuy)
albl.bind("<Button-1>",autoclickbuy)
ex.bind("<Button-1>",exut)
btn.pack()

lbl.pack()
btn.pack()
albl.pack()
balbl.pack()
ex.pack()
autoclick() 
win.mainloop()












