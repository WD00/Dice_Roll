import random
import tkinter


screen = tkinter.Tk()
screen.geometry('650x450')
screen.title("Let's roll the dice!")

Text = tkinter.Label(screen, text = '', font = ('Helvetica', 260))

def roll_dice():
    MyDice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    Text.configure(text = f'{random.choice(MyDice)} {random.choice(MyDice)}')
    Text.pack()

roll_button = tkinter.Button(screen, text = 'dice roll', foreground = 'black', command = roll_dice)
roll_button.pack()
screen.mainloop()