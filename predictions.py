from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
window = Tk()
window.title("LOTTO PRIZES")
window.geometry("500x500")

window.geometry("1536x945")
loader = Image.open("Daily-Lotto-Results-5-June-2021-1536x945.jpg")
render = ImageTk.PhotoImage(loader)
image = Label(window, image=render)
image.place(x=0, y=0)

# class name


class PredicTion:
    # widgets and buttons
    def __init__(self):
        self.window = window
        self.prediction = Label(window, text="Prediction",)
        self.prediction.place(x=0, y=10)
        self.prize = Label(window, text="Prizes(R)")
        self.prize.place(x=150, y=10)
        self.number1 = Label(window, text="6 correct numbers")
        self.number1.place(x=0, y=50)
        self.money1 = Label(window, text='10,000 000.00')
        self.money1.place(x=150, y=50)
        self.number2 = Label(window, text="5 correct numbers")
        self.number2.place(x=0, y=100)
        self.money2 = Label(window, text="8,584.00")
        self.money2.place(x=150, y=100)
        self.number3 = Label(window, text="4 correct numbers")
        self.number3.place(x=0, y=150)
        self.money3 = Label(window, text="2,384.00")
        self.money3.place(x=150, y=150)
        self.number4 = Label(window, text="3 correct numbers")
        self.number4.place(x=0, y=200)
        self.money4 = Label(window, text="100.50")
        self.money4.place(x=150, y=200)
        self.number5 = Label(window, text="2 correct numbers")
        self.number5.place(x=0, y=250)
        self.money5 = Label(window, text="20.00")
        self.money5.place(x=150, y=250)
        self.number6 = Label(window, text="1 correct number")
        self.number6.place(x=0, y=300)
        self.money6 = Label(window, text="0")
        self.money6.place(x=150, y=300)
        self.number7 = Label(window, text="0 correct number")
        self.number7.place(x=0, y=350)
        self.money7 = Label(window, text="0")
        self.money7.place(x=150, y=350)
        self.btn1 = Button(window, text="Play Again", borderwidth=10, bg="red", command=self.play_again)
        self.btn1.place(x=0, y=400)
        self.btn2 = Button(window, text="Proceed", borderwidth=10, bg="red", command=self.proceed)
        self.btn2.place(x=150, y=400)
        self.btn3 = Button(window, text="Exit", borderwidth=10, bg="red", command=self.exit)
        self.btn3.place(x=300, y=400)
# function for players to play again when they not satisfied
    def play_again(self):
        self.window.destroy()
        import newpage

# function for when user wants to claim they prize

    def proceed(self):
        self.window.destroy()
        import form

# exit function

    def exit(self):
        self.query = messagebox.askquestion("Exiting Application", "Do you really want to exit the app?")
        if self.query == "yes":
            self.window.destroy()


prediction = PredicTion()
window.mainloop()
