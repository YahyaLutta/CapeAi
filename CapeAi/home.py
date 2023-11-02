import customtkinter
import tkinter
from PIL import Image, ImageTk
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1000x665")

root.title = "CapeAI"
root._fg_color = "#212121"
root.iconbitmap("Icon.ico")
root.wm_title("CapeAI")

root.wm_resizable = False

Headerframe = customtkinter.CTkFrame(master=root, height=200)
Headerframe.pack(pady=0, padx=0, fill = "both", expand = False)

frame = customtkinter.CTkFrame(master=root, height=465)
frame.pack(fill = "both", expand = False)

HeaderIcon = ImageTk.PhotoImage(Image.open("Header.png").resize((350,200), Image.LANCZOS,reducing_gap=10))

Header = customtkinter.CTkLabel(master=Headerframe, image=HeaderIcon, fg_color="#212121", text="", width= 350,height=250).place(relx = 0.5, rely = 0.5, anchor = "center")

def ChatGPT():
    root.withdraw()
    os.system("ChatGPT.py")

def ImageGenerate123():
    root.withdraw()
    os.system("ImageAI.py")

ChatGPTButton = customtkinter.CTkButton(master=frame, command=ChatGPT, text="ChatGPT", height= 100, width=300).grid(column = 1)
ImageGeneration = customtkinter.CTkButton(master=frame, command=ImageGenerate123, text="Ai Pictures", height=100, width=300).grid(column = 2)

root.mainloop()