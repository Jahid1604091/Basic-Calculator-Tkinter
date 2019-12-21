from tkinter import *

w = Tk()
w.title("calculator")
w.config(bg='dark gray')
w.geometry('354x400+450+50')

scValue = StringVar()
scValue.set("")
metext=Entry(w,font=("Courier New",18,'bold'), textvar=scValue, width=28,bd=15,bg='powder blue')
metext.pack()


def clkbtn(event):
    global scValue
    text = event.widget.cget("text")
    if text == "=":
        if scValue.get().isdigit():
            value = int(scValue.get())
        else:
            try:
                value = eval(scValue.get())
            except Exception as e:
                scValue.set("Error")
                w.update()

            scValue.set(value)
            w.update()
    elif text == "CE":
        scValue.set("")
        w.update()
    else:
        scValue.set(scValue.get()+text)
        w.update()


but1 = Button(w, padx=14, pady=14, bd=4, bg='cyan', text="1", font=("Courier New", 16, 'bold'))
but1.place(x=10, y=100)
but1.bind("<Button-1>", clkbtn)

but2 = Button(w, padx=14, pady=14, bd=4, bg='cyan', text='2', font=("Courier New", 16, 'bold'))
but2.place(x=75, y=100)
but2.bind("<Button-1>", clkbtn)

but3 = Button(w, padx=14, pady=14, bd=4, bg='cyan', text='3', font=("Courier New", 16, 'bold'))
but3.place(x=140, y=100)
but3.bind("<Button-1>", clkbtn)

but4 = Button(w, padx=14, pady=14, bd=4, bg='cyan', text="4", font=("Courier New", 16, 'bold'))
but4.place(x=10, y=170)
but4.bind("<Button-1>", clkbtn)

but5 = Button(w, padx=14, pady=14, bd=4, bg='cyan', text='5', font=("Courier New", 16, 'bold'))
but5.place(x=75, y=170)
but5.bind("<Button-1>", clkbtn)

but6 = Button(w, padx=14, pady=14, bd=4, bg='cyan', text='6', font=("Courier New", 16, 'bold'))
but6.place(x=140, y=170)
but6.bind("<Button-1>", clkbtn)

but7 = Button(w, padx=14, pady=14, bd=4, bg='cyan', text="7", font=("Courier New", 16, 'bold'))
but7.place(x=10, y=240)
but7.bind("<Button-1>", clkbtn)


but8 = Button(w, padx=14, pady=14, bd=4, bg='cyan', text='8', font=("Courier New", 16, 'bold'))
but8.place(x=75, y=240)
but8.bind("<Button-1>", clkbtn)

but9 = Button(w, padx=14, pady=14, bd=4, bg='cyan', text='9', font=("Courier New", 16, 'bold'))
but9.place(x=140, y=240)
but9.bind("<Button-1>", clkbtn)

but0 = Button(w, padx=46, pady=14, bd=4, bg='cyan', text='0', font=("Courier New", 16, 'bold'))
but0.place(x=10, y=310)
but0.bind("<Button-1>", clkbtn)

butdot = Button(w, padx=14, pady=14, bd=4, bg='cyan', text='.', font=("Courier New", 16, 'bold'))
butdot.place(x=140, y=310)
butdot.bind("<Button-1>", clkbtn)

butplus = Button(w, padx=14, pady=14, bd=4, bg='cyan', text='+', font=("Courier New", 16, 'bold'))
butplus.place(x=205, y=100)
butplus.bind("<Button-1>", clkbtn)

butsub = Button(w, padx=14, pady=14, bd=4, bg='cyan', text='-', font=("Courier New", 16, 'bold'))
butsub.place(x=205, y=170)
butsub.bind("<Button-1>", clkbtn)

butmul = Button(w,padx=14, pady=14, bd=4, bg='cyan', text='*', font=("Courier New", 16, 'bold'))
butmul.place(x=205, y=240)
butmul.bind("<Button-1>", clkbtn)

butdiv = Button(w, padx=14, pady=14, bd=4, bg='cyan', text='/', font=("Courier New", 16, 'bold'))
butdiv.place(x=205, y=310)
butdiv.bind("<Button-1>", clkbtn)

butce = Button(w,padx=8, pady=49, bd=4, bg='cyan', text='CE', font=("Courier New", 16, 'bold'))
butce.place(x=270, y=100)
butce.bind("<Button-1>", clkbtn)

buteql = Button(w, padx=14, pady=48, bd=4, bg='cyan', text='=', font=("Courier New", 16, 'bold'))
buteql.place(x=270, y=241)
buteql.bind("<Button-1>", clkbtn)

w.mainloop()




#eval() evaluates the passed string as a Python expression and returns the result. For example, eval("1 + 1") interprets and executes the expression "1 + 1" and returns the result (2)