
from tkinter import *
from PIL import Image, ImageTk
from random import sample
from tkinter import messagebox

window = Tk()
window.geometry("1200x630")
window.title("Let's play")
window.geometry("1200x630")
loader = Image.open("Daily-Lotto-Results-4-June-2021.webp")
render = ImageTk.PhotoImage(loader)
image = Label(window, image=render)
image.place(x=0, y=0)
my_list1 = []
my_list2 = []
my_list3 = []


class LottoButtons:
    # creating all the widgets and buttons
    def __init__(self):
        self.window = window
        self.button1 = Button(window, text="1", command=lambda: self.insert('1, '), bg="orange")
        self.button1.place(x=0, y=10)
        self.button2 = Button(window, text="2", command=lambda: self.insert('2, '), bg="orange")
        self.button2.place(x=50, y=10)
        self.button3 = Button(window, text="3", command=lambda: self.insert('3, '), bg="orange")
        self.button3.place(x=100, y=10)
        self.button4 = Button(window, text="4", command=lambda: self.insert('4, '), bg="orange")
        self.button4.place(x=150, y=10)
        self.button5 = Button(window, text="5", command=lambda: self.insert('5, '), bg="orange")
        self.button5.place(x=200, y=10)
        self.button6 = Button(window, text="6", command=lambda: self.insert('6, '), bg="orange")
        self.button6.place(x=250, y=10)
        self.button7 = Button(window, text="7", command=lambda: self.insert('7, '), bg="orange")
        self.button7.place(x=300, y=10)
        self.button8 = Button(window, text="8", command=lambda: self.insert('8, '), bg="orange")
        self.button8.place(x=350, y=10)
        self.button9 = Button(window, text="9", command=lambda: self.insert('9, '), bg="orange")
        self.button9.place(x=400, y=10)
        self.button10 = Button(window, text="10", command=lambda: self.insert('10, '), bg="orange")
        self.button10.place(x=450, y=10)
        self.button11 = Button(window, text="11", command=lambda: self.insert('11, '), bg="green")
        self.button11.place(x=0, y=50)
        self.button12 = Button(window, text="12", command=lambda: self.insert('12, '), bg="green")
        self.button12.place(x=50, y=50)
        self.button13 = Button(window, text="13", command=lambda: self.insert('13, '), bg="green")
        self.button13.place(x=100, y=50)
        self.button14 = Button(window, text="14", command=lambda: self.insert('14, '), bg="green")
        self.button14.place(x=150, y=50)
        self.button15 = Button(window, text="15", command=lambda: self.insert('15, '), bg="green")
        self.button15.place(x=200, y=50)
        self.button16 = Button(window, text="16", command=lambda: self.insert('16, '), bg="green")
        self.button16.place(x=250, y=50)
        self.button17 = Button(window, text="17", command=lambda: self.insert('17, '), bg="green")
        self.button17.place(x=300, y=50)
        self.button18 = Button(window, text="18", command=lambda: self.insert('18, '), bg="green")
        self.button18.place(x=350, y=50)
        self.button19 = Button(window, text="19", command=lambda: self.insert('19, '), bg="green")
        self.button19.place(x=400, y=50)
        self.button20 = Button(window, text="20", command=lambda: self.insert('20, '), bg="green")
        self.button20.place(x=450, y=50)
        self.button21 = Button(window, text="21", command=lambda: self.insert('21, '), bg="red")
        self.button21.place(x=0, y=100)
        self.button22 = Button(window, text="22", command=lambda: self.insert('22, '), bg="red")
        self.button22.place(x=50, y=100)
        self.button23 = Button(window, text="23", command=lambda: self.insert('23, '), bg="red")
        self.button23.place(x=100, y=100)
        self.button24 = Button(window, text="24", command=lambda: self.insert('24, '), bg="red")
        self.button24.place(x=150, y=100)
        self.button25 = Button(window, text="25", command=lambda: self.insert('25, '), bg="red")
        self.button25.place(x=200, y=100)
        self.button26 = Button(window, text="26", command=lambda: self.insert('26, '), bg="red")
        self.button26.place(x=250, y=100)
        self.button27 = Button(window, text="27", command=lambda: self.insert('27, '), bg="red")
        self.button27.place(x=300, y=100)
        self.button28 = Button(window, text="28", command=lambda: self.insert('28, '), bg="red")
        self.button28.place(x=350, y=100)
        self.button29 = Button(window, text="29", command=lambda: self.insert('29, '), bg="red")
        self.button29.place(x=400, y=100)
        self.button30 = Button(window, text="30", command=lambda: self.insert('30, '), bg="red")
        self.button30.place(x=450, y=100)
        self.button31 = Button(window, text="31", command=lambda: self.insert('31, '), bg="blue")
        self.button31.place(x=0, y=150)
        self.button32 = Button(window, text="32", command=lambda: self.insert('32, '), bg="blue")
        self.button32.place(x=50, y=150)
        self.button33 = Button(window, text="33", command=lambda: self.insert('33, '), bg="blue")
        self.button33.place(x=100, y=150)
        self.button34 = Button(window, text="34", command=lambda: self.insert('34, '), bg="blue")
        self.button34.place(x=150, y=150)
        self.button35 = Button(window, text="35", command=lambda: self.insert('35, '), bg="blue")
        self.button35.place(x=200, y=150)
        self.button36 = Button(window, text="36", command=lambda: self.insert('36, '), bg="blue")
        self.button36.place(x=250, y=150)
        self.button37 = Button(window, text="37", command=lambda: self.insert('37, '), bg="blue")
        self.button37.place(x=300, y=150)
        self.button38 = Button(window, text="38", command=lambda: self.insert('38, '), bg="blue")
        self.button38.place(x=350, y=150)
        self.button39 = Button(window, text="39", command=lambda: self.insert('39, '), bg="blue")
        self.button39.place(x=400, y=150)
        self.button40 = Button(window, text="40", command=lambda: self.insert('40, '), bg="blue")
        self.button40.place(x=450, y=150)
        self.button41 = Button(window, text="41",  command=lambda: self.insert('41, '), bg="hot pink")
        self.button41.place(x=0, y=200)
        self.button42 = Button(window, text="42", command=lambda: self.insert('42, '), bg="hot pink")
        self.button42.place(x=50, y=200)
        self.button43 = Button(window, text="43", command=lambda: self.insert('43, '), bg="hot pink")
        self.button43.place(x=100, y=200)
        self.button44 = Button(window, text="44", command=lambda: self.insert('44, '), bg="hot pink")
        self.button44.place(x=150, y=200)
        self.button45 = Button(window, text="45", command=lambda: self.insert('45, '), bg="hot pink")
        self.button45.place(x=200, y=200)
        self.button46 = Button(window, text="46", command=lambda: self.insert('46, '), bg="hot pink")
        self.button46.place(x=250, y=200)
        self.button47 = Button(window, text="47", command=lambda: self.insert('47, '), bg="hot pink")
        self.button47.place(x=300, y=200)
        self.button48 = Button(window, text="48", command=lambda: self.insert('48, '), bg="hot pink")
        self.button48.place(x=350, y=200)
        self.button49 = Button(window, text="49", command=lambda: self.insert('49, '), bg="hot pink")
        self.button49.place(x=400, y=200)
        self.play_btn = Button(window, text="Play", borderwidth=10, command=self.random, bg="hot pink")
        self.play_btn.place(x=0, y=450)
        self.redeem_btn = Button(window, text="Claim Prize", borderwidth=10, command=self.claim, bg="blue")
        self.redeem_btn.place(x=130, y=450)
        self.quit_btn = Button(window, text="Exit", borderwidth=10, command=self.close, bg="red")
        self.quit_btn.place(x=300, y=450)
        self.play_btn.config(command=self.random)
        self.label2 = Label(window, bg="green", text="Lotto Numbers!")
        self.label2.place(x=600, y=300)
        self.label3 = Label(window, bg="deep pink", fg="white", width=20, borderwidth=10)
        self.label3.place(x=600, y=350)
        self.entry1 = Entry(window, bg="hot pink", borderwidth=10, state='disabled')
        self.entry1.place(x=0, y=300)
        self.entry2 = Entry(window, bg="red", borderwidth=10, state='disabled')
        self.entry2.place(x=200, y=300)
        self.entry3 = Entry(window, bg="blue", borderwidth=10, state='disabled')
        self.entry3.place(x=400, y=300)
        self.active_btn1 = Button(window, text='ACTIVE', bg='green', fg='gold', font=('Georgia', 10, 'bold'),
                                  cursor='hand2', command=self.entry_widget1)
        self.active_btn1.place(x=0, y=350)

        self.active_btn2 = Button(window, text='ACTIVE', bg='green', fg='gold', font=('Georgia', 10, 'bold'),
                                  cursor='hand2', command=self.entry_widget2)
        self.active_btn2.place(x=200, y=350)

        self.active_btn3 = Button(window, text='ACTIVE', bg='green', fg='gold', font=('Georgia', 10, 'bold'),
                                  cursor='hand2', command=self.entry_widget3)
        self.active_btn3.place(x=400, y=350)
# making entries so that when user is entering his/her numbers that other 2 entries are disabled and active once
    # activated

    def entry_widget1(self):
        self.entry1.config(state='normal')
        self.entry2.config(state='disable')
        self.entry3.config(state='disable')

    def entry_widget2(self):
        self.entry1.config(state='disable')
        self.entry2.config(state='normal')
        self.entry3.config(state='disable')

    def entry_widget3(self):
        self.entry1.config(state='disable')
        self.entry2.config(state='disable')
        self.entry3.config(state='normal')
# inserting the value from the buttons to display in the entries

    def insert(self, val):
        self.entry1.insert(END, val)
        self.entry2.insert(END, val)
        self.entry3.insert(END, val)

    def numbers(self, number):
        if len(my_list1) <= 5 and number not in my_list1:
            my_list1.append(number)

            self.entry1.config(text=my_list1)

        elif len(my_list1) == 6 and len(my_list2) <= 5 and number not in my_list2:
            my_list2.append(number)
            self.entry2.config(text=my_list2)

        elif len(my_list2) == 6 and len(my_list3) <= 5 and number not in my_list3:
            my_list3.append(number)
            self.entry3.config(text=my_list3)

        else:
            messagebox.showinfo("ERROR", "NO repeating numbers")

# exiting of the current page function
    def close(self):
        self.query = messagebox.askquestion("Exiting Application", "Do you really want to exit the app?")
        if self.query == "yes":
            self.window.destroy()
# claiming of the prize function

    def claim(self):
        self.ask = messagebox.askquestion("ITHUBA National Lottery", "Would you like to convert to another currency?")
        if self.ask == "yes":
            self.window.destroy()
            import currency
        if self.ask == "no":
            self.window.destroy()
            import predictions

# generating of the numbers when the user wants to play
    def random(self):
        self.random_my_list1 = sample(range(1, 49), 6)
        self.random_my_list1.sort()
        self.label3.configure(text=self.random_my_list1)

        self.counter = 0
        for self.numbers in my_list1:
            if self.numbers in self.random_my_list1:
                self.counter += 1
            if self.counter <= 1:
                messagebox.showinfo("Sorry", "Better Luck Again Next Time.")
                break

            elif self.counter == 2:
                messagebox.showinfo("Congratulations", "You won R20.")
                break

            elif self.counter == 3:
                messagebox.showinfo("Congratulations", "You won R100.")
                break

            elif self.counter == 4:
                messagebox.showinfo("Congratulations", "You won R2,384.00.")
                break

            elif self.counter == 5:
                messagebox.showinfo("Congratulations", "You won R2,384.00.")
                break

            elif self.counter == 6:
                messagebox.showinfo("CONGRATULATIONS!", "You won R10,000 000.00")
                break


lotto_app = LottoButtons()
window.mainloop()
