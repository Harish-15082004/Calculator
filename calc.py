import tkinter
from tkinter import *
from tkinter import font
w=Tk()
w.geometry('245x310')
f1=font.Font(w,family='Calibri',size=14)
w.title('calculator')

def show(x):
    cur=e1.get()
    e1.delete(0,END)
    e1.insert(0,str(cur)+str(x))

def clear():
    e1.delete(0,END)

def add():
    global f_num
    f_num=str(e1.get())
    e1.delete(0,END)
    global val
    val="add"

def sub():
    global f_num
    f_num=str(e1.get())
    e1.delete(0,END)
    global val
    val="sub"

def mul():
    global f_num
    f_num=str(e1.get())
    e1.delete(0,END)
    global val
    val="mul"

def div():
    global f_num
    f_num=str(e1.get())
    e1.delete(0,END)
    global val
    val="div"


def calc():
    s_num=e1.get()
    e1.delete(0,END)
    if val=="add":
        e1.insert(0,int(f_num)+int(s_num))
    elif val=="sub":
        e1.insert(0,int(f_num)-int(s_num))
    elif val=="mul":
        e1.insert(0,int(f_num)*int(s_num))
    elif val=="div":
        e1.insert(0,int(f_num)/int(s_num))
fr=Frame(w,width=400,height=600,bg='black')
e1=Entry(fr,width=20,font=f1,bd=0)
e1.place(x=20,y=50)
b1=Button(fr,text='7',bg='grey',fg='white',width=5,height=2,bd=1,command=lambda:show(7))
b1.place(x=25,y=100)
b2=Button(fr,text='8',bg='grey',fg='white',width=5,height=2,bd=1,command=lambda:show(8))
b2.place(x=75,y=100)
b3=Button(fr,text='9',bg='grey',fg='white',width=5,height=2,bd=1,command=lambda:show(9))
b3.place(x=125,y=100)
b4=Button(fr,text='4',bg='grey',fg='white',width=5,height=2,bd=1,command=lambda:show(4))
b4.place(x=25,y=150)
b5=Button(fr,text='5',bg='grey',fg='white',width=5,height=2,bd=1,command=lambda:show(5))
b5.place(x=75,y=150)
b6=Button(fr,text='6',bg='grey',fg='white',width=5,height=2,bd=1,command=lambda:show(6))
b6.place(x=125,y=150)
b7=Button(fr,text='3',bg='grey',fg='white',width=5,height=2,bd=1,command=lambda:show(3))
b7.place(x=25,y=200)
b8=Button(fr,text='2',bg='grey',fg='white',width=5,height=2,bd=1,command=lambda:show(2))
b8.place(x=75,y=200)
b9=Button(fr,text='1',bg='grey',fg='white',width=5,height=2,bd=1,command=lambda:show(1))
b9.place(x=125,y=200)
b11=Button(fr,text='0',bg='grey',fg='white',width=5,height=2,bd=1,command=lambda:show(0))
b11.place(x=25,y=250)
b12=Button(fr,text='=',bg='grey',fg='white',width=5,height=2,bd=1,command=lambda:calc())
b12.place(x=75,y=250)
b13=Button(fr,text='C',bg='red',fg='white',width=5,height=2,bd=1,command=lambda:clear())
b13.place(x=175,y=100)

b15=Button(fr,text='+',bg='grey',fg='white',width=5,height=2,bd=1,command=add)
b15.place(x=175,y=150)
b16=Button(fr,text='-',bg='grey',fg='white',width=5,height=2,bd=1,command=sub)
b16.place(x=175,y=200)
b17=Button(fr,text='*',bg='grey',fg='white',width=5,height=2,bd=1,command=mul)
b17.place(x=125,y=250)
b18=Button(fr,text='/',bg='grey',fg='white',width=5,height=2,bd=1,command=div)
b18.place(x=175,y=250)

fr.grid()
w.mainloop()
