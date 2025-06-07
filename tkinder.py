from tkinter import *
def save_info():
    a=name_1.get()
    b=phone_1.get()
    with open("yuvi.txt", "w") as file:
        file.write("Name {}\n".format(a))
        file.write(f"Phone: {b}\n")

app=Tk()
app.geometry("500x300")

Label(app, text="Registration Form", font="ar 20 bold").grid(row=0, column=3)
name = Label(app, text="NAME")
phone = Label(app, text="PHONE")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
name_1 = StringVar()
phone_1 = StringVar()


name1entry = Entry(app, textvariable=name_1)
phoneentry = Entry(app, textvariable=phone_1)

name1entry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)

Button(app,text="submit",command=save_info).grid(row=7,column=3)

mainloop()