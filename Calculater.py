
from tkinter import *

root=Tk()

root.geometry('360x430')
root.title("Calculator")
root.maxsize(width=360,height=430)
root.minsize(width=360,height=430)
root.config(bg='#272533')

def enter(e):
    e.widget.config(bg='red')
def leave(l):
    l.widget.config(bg='yellow') 

def click(num):
    global help_tx
    help_tx+=str(num)
    tx.set(help_tx)
tx=StringVar()
help_tx=''

def math_error():
     global help_tx
     help_tx='Syntax_error'
     tx.set(help_tx)
    
def equal():
    try:
        global help_tx
        help_tx=str(int(eval(help_tx)))
        tx.set(help_tx)
    except:
        root.after(2000,clear)
        math_error()
        
def clear():
    global help_tx
    help_tx=''
    tx.set(help_tx)
    
def delete():
    global help_tx
    help_tx=''
    tx.set(help_tx)

tx=StringVar()
help_tx=''
                   
lcd=Entry(root,font=('aerial',20,'italic bold'),justify="center",bg='black',fg='red',bd=30,textvariable=tx)
lcd.grid(row=0,column=0,columnspan=4)

btn7=Button(root,text='7 ',font=('aerial',20,'italic bold'),bg='yellow',bd=8,padx=19,activebackground='green',command=lambda:click(7))
btn7.grid(row=1,column=0)
btn7.bind('<Enter>',enter),btn7.bind('<Leave>',leave)

btn8=Button(root,text='8 ',font=('aerial',20,'italic bold'),bg='yellow',bd=8,padx=19,activebackground='green',command=lambda:click(8))
btn8.grid(row=1,column=1)
btn8.bind('<Enter>',enter),btn8.bind('<Leave>',leave)

btn9=Button(root,text=9,font=('aerial',20,'italic bold'),bg='yellow',bd=8,padx=19,activebackground='green',command=lambda:click(9))
btn9.grid(row=1,column=2)
btn9.bind('<Enter>',enter),btn9.bind('<Leave>',leave)

btnplus=Button(root,text='+',fg='red',font=('aerial',20,'italic bold'),bg='yellow',bd=8,padx=18,activebackground='green',command=lambda:click('+'))
btnplus.grid(row=1,column=3)
btnplus.bind('<Enter>',enter),btnplus.bind('<Leave>',leave)

btn4=Button(root,text='4 ',font=('aerial',20,'italic bold'),bg='yellow',bd=8,padx=19,activebackground='green',command=lambda:click(4))
btn4.grid(row=2,column=0)
btn4.bind('<Enter>',enter),btn4.bind('<Leave>',leave)

btn5=Button(root,text='5 ',font=('aerial',20,'italic bold'),bg='yellow',bd=8,padx=19,activebackground='green',command=lambda:click(5))
btn5.grid(row=2,column=1)
btn5.bind('<Enter>',enter),btn5.bind('<Leave>',leave)

btn6=Button(root,text=6,font=('aerial',20,'italic bold'),bg='yellow',bd=8,padx=19,activebackground='green',command=lambda:click(6))
btn6.grid(row=2,column=2)
btn6.bind('<Enter>',enter),btn6.bind('<Leave>',leave)

btnsubtract=Button(root,text='-',fg='red',font=('aerial',20,'italic bold'),bg='yellow',bd=8,padx=21,activebackground='green',command=lambda:click('-'))
btnsubtract.grid(row=2,column=3)
btnsubtract.bind('<Enter>',enter),btnsubtract.bind('<Leave>',leave)

btn1=Button(root,text='1 ',font=('aerial',20,'italic bold'),bg='yellow',bd=8,padx=19,activebackground='green',command=lambda:click(1))
btn1.grid(row=3,column=0)
btn1.bind('<Enter>',enter),btn1.bind('<Leave>',leave)

btn2=Button(root,text='2 ',font=('aerial',20,'italic bold'),bg='yellow',bd=8,padx=19,activebackground='green',command=lambda:click(2))
btn2.grid(row=3,column=1)
btn2.bind('<Enter>',enter),btn2.bind('<Leave>',leave)

btn3=Button(root,text=3,font=('aerial',20,'italic bold'),bg='yellow',bd=8,padx=19,activebackground='green',command=lambda:click(3))
btn3.grid(row=3,column=2)
btn3.bind('<Enter>',enter),btn3.bind('<Leave>',leave)

btndivide=Button(root,text='/',fg='red',font=('aerial',20,'italic bold'),bg='yellow',bd=8,padx=22,activebackground='green',command=lambda:click('/'))
btndivide.grid(row=3,column=3)
btndivide.bind('<Enter>',enter),btndivide.bind('<Leave>',leave)

btn0=Button(root,text='0 ',font=('aerial',20,'italic bold'),bg='yellow',bd=8,padx=19,activebackground='green',command=lambda:click(0))
btn0.grid(row=4,column=0)
btn0.bind('<Enter>',enter),btn0.bind('<Leave>',leave)

btndot=Button(root,text='. ',fg='blue',font=('aerial',20,'italic bold'),bg='yellow',bd=8,padx=22,activebackground='green',command=lambda:click('.'))
btndot.grid(row=4,column=1)
btndot.bind('<Enter>',enter),btndot.bind('<Leave>',leave)

btndelete=Button(root,text='⇽',fg='blue',font=('aerial',20,'italic bold'),bg='yellow',bd=8,padx=15,activebackground='green',command=delete)
btndelete.grid(row=4,column=2)
btndelete.bind('<Enter>',enter),btndelete.bind('<Leave>',leave)

btnmultiple=Button(root,text='*',fg='red',font=('aerial',20,'italic bold'),bg='yellow',bd=8,padx=21,activebackground='green',command=lambda:click('*'))
btnmultiple.grid(row=4,column=3)
btnmultiple.bind('<Enter>',enter),btnmultiple.bind('<Leave>',leave)

btnequal=Button(root,text='=',fg='green',font=('aerial',20,'italic bold'),bg='yellow',bd=8,padx=62,activebackground='green',command=equal)
btnequal.grid(row=5,column=2,columnspan=2)
btnequal.bind('<Enter>',enter),btnequal.bind('<Leave>',leave)

btnclear=Button(root,text='Clear',fg='green',font=('aerial',20,'italic bold'),bg='yellow',bd=8,padx=43,activebackground='green',command=clear)
btnclear.grid(row=5,column=0,columnspan=2)
btnclear.bind('<Enter>',enter),btnclear.bind('<Leave>',leave)

root.mainloop()
