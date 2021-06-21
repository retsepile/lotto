# Retsepile Koloko class 2

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime
window = Tk()
window.geometry("500x500")
window.title("LOTTO")
window.geometry("1200x800")
loader = Image.open("balls.jpg")
render = ImageTk.PhotoImage(loader)
image = Label(window, image=render)
image.place(x=0, y=0)

# creating a class name for my functions


class InforMation:
    # constructing my widgets for the interface
    def __init__(self):
        self.window = window
        self.name_label = Label(window, text="Enter your name:", bg="yellow")
        self.name_label.place(x=5, y=10)
        self.user_entry = Entry(window)
        self.user_entry.place(x=150, y=10)
        self.address_lbl = Label(window, text="Enter address:", bg="yellow")
        self.address_lbl.place(x=5, y=50)
        self.address_entry = Entry(window)
        self.address_entry.place(x=150, y=50)
        self.id_no_label = Label(window, text="Enter ID No:", bg="yellow")
        self.id_no_label.place(x=5, y=100)
        self.identity_entry = Entry(window)
        self.identity_entry.place(x=150, y=100)
        self.email_label = Label(window, text="Email:", bg="yellow")
        self.email_label.place(x=10, y=150)
        self.mail_entry = Entry(window)
        self.mail_entry.place(x=150, y=150)
        self.btn_exit = Button(window, text="Exit", command=self.exit, borderwidth="10", bg="gold")
        self.btn_exit.place(x=150, y=200)
        self.btn_log = Button(window, text="Log in", command=self.login, borderwidth="10", bg="gold")
        self.btn_log.place(x=10, y=200)
        self.btn_clear = Button(window, text="Clear", command=self.clear, borderwidth="10", bg="gold")
        self.btn_clear.place(x=250, y=200)

# creating a login form so that users can enter they information

    def login(self):
        date = datetime.today()
        regular_express = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        try:
            for x in range(len(self.mail_entry.get())):
                if re.search(regular_express, self.mail_entry.get()):
                    with open("Text-File.txt", "w+") as f:
                        f.write(self.mail_entry.get())
                        f.write("\n")
                        f.write(self.user_entry.get())
                        f.write("\n")
                        f.write(self.identity_entry.get())
                        f.write("\n")
                        f.write(str(date))
                        f.write("\n")
                else:
                    messagebox.showerror("Error", "Invalid Email Address Provided.")
                    window.destroy()
            for x in range(int(self.identity_entry.get())):
                res = int(self.identity_entry.get()[0:2]) - int(date.strftime("%y"))
                if res >= 18:
                    messagebox.showinfo("Welcome", "Press OK To Start The Game.")
                    window.destroy()
                    import newpage
                elif len(self.identity_entry.get()) != 13:
                    messagebox.showerror("Error", "Invalid Identity Number Provided.")
                    break
                else:
                    messagebox.showerror("Error", "You Are Too Young To Proceed To The Game.")
                    break
        except ValueError:
            if self.identity_entry.get() != int:
                messagebox.showerror("Error", "Identity Number Must Only Be Provided Using Digits.")
            elif self.user_entry.get() != str:
                messagebox.showerror("Error", "Full Name Must Only Be Provided Using Alphabetical Letters.")
# creating a function for user to exit the application if they want too

    def exit(self):
        self.ask = messagebox.askquestion("Ithuba National Lottery", "Quit the app?")
        if self.ask == "yes":
            self.window.destroy()

# creating a function for user to clear any mistake
    def clear(self):
        self.user_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.mail_entry.delete(0, END)
        self.identity_entry.delete(0, END)


i = InforMation()
window.mainloop()
