# impordi tk vidinad ja konstandid
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

###RAAM
# Funktsioonid Raami jaoks
def north():
    move = "go north"
    print(move)
    text.insert('1.0', move + '\n')

def south():
    move = "go south"
    print(move)
    text.insert('1.0', move + '\n')

def east():
    move = "go east"
    print(move)
    text.insert('1.0', move + '\n')
    
def west():
    move = "go west"
    print(move)
    text.insert('1.0', move + '\n')

# Aken
raam = Tk()
raam.title("Ultimaia")
raam.geometry("1280x720")
raam.configure(background="#ffa100")

# Tekstikast
text = ScrolledText(raam, width=150, height=15)
text.place(x=70, y=100, width=330)

#Nupud
nupp = ttk.Button(raam, text="East", command=east)
nupp.place(x=250, y=40, width=150)

nupp2 = ttk.Button(raam, text="West", command=west)
nupp2.place(x=70, y=40, width=150)

nupp3 = ttk.Button(raam, text="North", command=north)
nupp3.place(x=160, y=10, width=150)

nupp4 = ttk.Button(raam, text="South", command=south)
nupp4.place(x=160, y=70, width=150)

#LOOP
raam.mainloop()

###RAAM###