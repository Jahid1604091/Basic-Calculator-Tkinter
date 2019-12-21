from tkinter import *


w = Tk()
w.geometry("500x300+500+100")
w.title("Demo")

label1 = Label(w, text="Welcome to Tkinter", fg='blue', bg='yellow', relief="solid", font=("arial", 20, "bold"))
label1.pack()

btn1 = Button(w, text="Click", fg='white', bg='blue', relief="ridge", font=("arial", 10, "bold"))
btn1.pack()

w.mainloop()