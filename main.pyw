import winsound
import random
import tkinter as tk
import threading

sounds = ["SystemExclamation", "SystemHand"]


def create_window():
    global window
    window = tk.Tk()
    window.title("Your computer is under threat")
    window.geometry("800x500")
    window.configure(bg='red')
    window.attributes("-alpha", 0.7)
    window.attributes("-topmost", True)
    window.attributes("-toolwindow", 1)
    window.resizable(False, False)
    label = tk.Label(window, text="THERE IS NO ESCAPE", font=("Helvetica", 50), bg='red')
    label.pack()
    winsound.PlaySound(random.choice(sounds), winsound.SND_ALIAS)
    window.protocol("WM_DELETE_WINDOW", windows)
    window.mainloop()

def windows():
    create_window()

create_window()
