from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox
import sqlite3


def exit1():
    exit()


def about():
    tkinter.messagebox.showinfo("Welcome to authors !", "This is a demo for menu")


def second_window():
    w2 = Tk()
    w2.geometry("500x600+450+100")
    w2.title("Second View")




w = Tk()
w.geometry("500x600+450+100")
w.title("Registration form")


img = Image.open("F:/Android/registration.jpg").resize((90, 90), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img)

fn = StringVar()
ln = StringVar()
db = StringVar()
cl = StringVar()
var_c1 = IntVar()
var_c2 = IntVar()
radio_var = StringVar()


menu = Menu(w)
w.config(menu=menu)


subm1 = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=subm1)
subm1.add_cascade(label="Exit", command=exit1)

subm2 = Menu(menu)
menu.add_cascade(label="Option", menu=subm2)
subm2.add_command(label="About", command=about)


def database():
    first = fn.get()
    last = ln.get()
    dob1 = db.get()
    cntry = cl.get()
    lang1 = var_c1
    lang2 = var_c2
    gen = radio_var.get()

    list2 = []

    if lang1.get() == 1:
        list2.append("Java")

    if lang2.get() == 1:
        list2.append("Python")

    lang = " , ".join(list2)
    conn = sqlite3.connect("Form.db")
    with conn:
        cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Student (Name TEXT, Last TEXT,DOB TEXT, country TEXT, Prog_lang TEXT, Gender TEXT)')
    cursor.execute('INSERT INTO Student (Name, Last, DOB, country, prog_lang, Gender) VALUES(?,?,?,?,?,?)', (first, last, dob1, cntry, lang, gen))
    conn.commit()


def printt():
    first = fn.get()
    last = ln.get()
    dob1 = db.get()
    cntry = cl.get()
    lang1 = var_c1
    lang2 = var_c2
    gen = radio_var.get()

    list2 = []
    print(f"Your fullname is : {first} {last}")
    print(f"Your Country is : {cntry}")
    print(f"Your Date of Birth is : {dob1}")
    print(f"Your Gender is : {gen}")
    print("Your chosen language is :", end="")
    if lang1.get()==1:
        list2.append("Java")

    if lang2.get()==1:
        list2.append("Python")

    addComma = " , ".join(list2)
    print(addComma)


formImage = Label(image=photo)
formImage.pack()

form = Label(w, text="Registration Form", relief="solid", width=20, font=("times", 19,"bold"))
form.place(x=90, y=90)

firstName = Label(w, text="First Name : ", width=20, font=("arial", 14))
firstName.place(x=80, y=130)

entry_1 = Entry(w, textvar=fn)
entry_1.place(x=250, y=135)

lastName = Label(w, text="Last Name : ", width=20, font=("arial", 14))
lastName.place(x=80, y=170)

entry_2 = Entry(w, textvar=ln)
entry_2.place(x=250, y=175)


dob = Label(w, text="DOB : ", width=20, font=("arial", 14))
dob.place(x=55, y=210)


entry_3 = Entry(w, textvar=db)
entry_3.place(x=250, y=215)


country = Label(w, text="Country : ", width=20, font=("arial", 14))
country.place(x=65, y=250)

list1 = ['America', 'Bangladesh', "Canada", "India"]
droplist = OptionMenu(w, cl, *list1)
cl.set("Select a country")
droplist.config(width=15)
droplist.place(x=250, y=250)


prog_lang = Label(w, text="Programming Language : ", width=20, font=("arial", 14))
prog_lang.place(x=135, y=290)

c1 = Checkbutton(w, text="Java", variable=var_c1, font=("arial", 12)).place(x=190, y=330)
c2 = Checkbutton(w, text="Python", variable=var_c2, font=("arial", 12)).place(x=290, y=330)


gender = Label(w, text="Gender : ", width=20, font=("arial", 14))
gender.place(x=65, y=370)

r1 = Radiobutton(w, text="Male", variable=radio_var, value="Male", font=("arial", 12)).place(x=230, y=370)
r2 = Radiobutton(w, text="Female", variable=radio_var, value="Female", font=("arial", 12)).place(x=300, y=370)


loginBtn = Button(w, text="Login", width=10, bg="yellow", relief="raised", font=("arial", 12),
                   command=second_window)
loginBtn.place(x=20, y=10)


signUpBtn = Button(w, text="Sign Up", width=20, bg="yellow", relief="raised", font=("arial", 14),
                   command=database)
signUpBtn.bind("<Return>", database)
signUpBtn.place(x=120, y=450)

exitBtn = Button(w, text="X",  bg="red", relief="raised", font=("arial", 14),
                   command=exit1)
exitBtn.place(x=400, y=5)




w.mainloop()