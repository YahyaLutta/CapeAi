import tkinter as tk
import os
import time


root = tk.Tk()
root.title = "CapeAI"
root.iconbitmap("Icon.ico")
root.wm_title("CapeAI")
root.geometry("1000x665")
root.config(bg = "#212121")

Picture = tk.PhotoImage(file="Logo.png")

root.overrideredirect(True)

root.resizable = False

x = (root.winfo_screenwidth()//2)-(1000//2)
y = (root.winfo_screenheight()//2)-(665//2)
root.geometry('{}x{}+{}+{}'.format(1000, 665, x, y))

Logo = tk.Button(master= root, image=Picture, width=1000, height=665, bg="#212121", highlightbackground="#212121", highlightcolor="#212121", state= "disabled")
Logo.place(rely=0.5,relx=0.5, anchor="center")

def Start():
    root.withdraw()
    os.system("home.py")
    root.destroy()

for i in range(0,10):
    Logo.after(1000, Start)


root.mainloop()
