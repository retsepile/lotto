from tkinter import *
from tkinter import ttk


window = Tk()
window.title("Banking Details")
window.geometry("900x900")

fill_in = Label(window, text="FILL IN YOUR BANKING DETAILS")
fill_in.place(x=150, y=10)
name = Label(window, text="Fill in your name:")
name.place(x=0, y=50)
name = Entry(window)
name.place(x=150, y=50)

surname = Label(window, text=" Fill in your surname:")
surname.place(x=0, y=100)

surname = Entry(window)
surname.place(x=150, y=100)

d_o_b = Label(window, text="Date of Birth:")
d_o_b.place(x=0, y=150)

d_o_b = Entry(window)
d_o_b.place(x=150, y=150)

i_d_num = Label(window, text="ID Number:")
i_d_num.place(x=0, y=200)

i_d_num = Entry(window)
i_d_num.place(x=150, y=200)

cell_no = Label(window, text="Cellphone number:")
cell_no.place(x=0, y=250)

cell_no = Entry(window)
cell_no.place(x=150, y=250)

city = Label(window, text="Citizen:")
city.place(x=0, y=300)

city = Entry(window)
city.place(x=150, y=300)

bank = Label(window, text="Choose Bank:")
bank.place(x=0, y=350)

#  combobox
var = StringVar()
category_list = ttk.Combobox(window, textvariable=var, width=18, value=["ABSA", "Ned Bank", "FNB", "Standard Bank"])
category_list.place(x=150, y=350)


account = Label(window, text="Enter your account number:")
account.place(x=0, y=400)

account_entry = Entry(window)
account_entry.place(x=200, y=400)

branch = Label(window, text="Branch Code:")
branch.place(x=0, y=450)

branch_entry = Entry(window)
branch_entry.place(x=150, y=450)

# clears the details


def clear():
    name.delete(0, END)
    surname.delete(0, END)
    i_d_num.delete(0, END)
    cell_no.delete(0, END)
    city.delete(0, END)
    d_o_b.delete(0, END)
    account_entry.delete(0, END)
    branch_entry.delete(0, END)


button = Button(window, text="Clear", borderwidth=10, command=clear)
button.place(x=300, y=550)

# sends the email after you filled in the details


def proceed():
    window.destroy()
    import mail


button = Button(window, text="Proceed", borderwidth=10, command=proceed)
button.place(x=150, y=550)

window.mainloop()
