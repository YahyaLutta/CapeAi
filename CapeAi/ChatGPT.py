import customtkinter
import tkinter
import openai
import os
from dotenv import load_dotenv
import time

def configure():
    load_dotenv()

configure()

time.sleep(0.1)

openai.api_key = os.getenv("api_key")
openai.Model.list()
import requests
import webbrowser
from flask import Flask, request
from CapeAi_Data import Messages
from PIL import Image, ImageTk
from customtkinter import* 
import pygame
from tkinter import messagebox 
from tkinter import Message
import random
import paypalrestsdk
import logging
import mailbox

app = Flask(__name__)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1000x665")

root.title = "CapeAI"
root._fg_color = "#212121"
root.iconbitmap("Icon.ico")
root.wm_title("CapeAI")

root.wm_resizable = False

MessageHistory = []

MessagesText = " Messages"

print(Messages)

LatestReplyFromAi = " "

CanCopy = False

var = customtkinter.StringVar()

Question = ""

#root.wm_attributes('-transparentcolor', '#d04cdc')

def login():
    print("Test")

   

def Enter():

 f = open("CapeAi_Data.py", "w")


 if Messages >0:

    Question = TextBox.get()
    HumanMessage = customtkinter.CTkLabel(master=frame, text=Question, height=50, width=25, corner_radius=5,  anchor="w", wraplength=600)
    HumanMessage.grid(padx = 5, sticky = "w")
    print(Messages)
    Thing = Messages -1 
    TokensText.configure(text = str(Messages))
    f.writelines("Messages = "+str(Thing))
    print(Messages)
    var.set(Messages)
    var.set(Messages)
    TokensText.update()
    f.close()

    time.sleep(0.1)

    MessageHistory.append({"role": "user", "content": Question})
 
    completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=MessageHistory
  
    )

    Response = completion.choices[0].message.content
     
    MessageHistory.append({"role": "assistant", "content": Response})
    Colors = ["#543f3f", "#3f663d", "#533f54", "#41543f"]
    RandomColor = random.choice(Colors)
    AiReply = customtkinter.CTkLabel(master=frame, fg_color=RandomColor, text=Response, height=50, width=100, justify = "left", corner_radius=5, font=customtkinter.CTkFont(family="Italic"), anchor="w", wraplength=800)
    AiReply.grid(padx = 5, sticky = "w")
    global LatestReplyFromAi
    LatestReplyFromAi = Response
    print(LatestReplyFromAi)
    global CanCopy
    CanCopy = True
    print(completion.choices[0].message.content)
 else:
     
     print("Not enough messages")
     popup = messagebox.showerror("ERROR", message="You ran out of enough prompts")
     print("qadafa")
     TokensText.configure(text = "0")
     f.close()

def LaunchWebsite():
    webbrowser.open_new_tab("www.CapeAi.net")

Height1 = 35
width1 = 35

def ButtonAnimation():
    global Height1, width1
    SendPicture.height = 10
    SendPicture.width = 10
    root.after(1000, GoBack)

def GoBack():
    global Height1, width1
    SendPicture.height = 35
    SendPicture.width = 35
    Enter()

def GoToTwitter():
    webbrowser.open_new_tab("https://twitter.com/Accelerate2_")

def Gen_iMAGE():
    root.withdraw()
    os.system("ImageAI.py")

def message():
    root.withdraw()
    os.system("home.py")

def toggle_win():
    frame1 = customtkinter.CTkFrame(root, width= 300, height= 1000)
    frame1.place(relx=0,rely=0)

    def delete1():
        frame1.destroy()

    customtkinter.CTkButton(frame1, text="Close X", command=delete1, fg_color="#212121").place(relx=0.5, rely=0.05, anchor = "center")

    HomeIcon = ImageTk.PhotoImage(Image.open("Home.png").resize((20,20), Image.LANCZOS,reducing_gap=10))

    customtkinter.CTkButton(frame1, text="Home", image=HomeIcon, fg_color="#212121", bg_color="#212121",command=message() ,hover_color="#1c1c1c", width=380, height=50).place(relx = 0.5, rely = 0.1, anchor = "center")
    global ImageGenerationIcon
    ImageGenerationIcon = ImageTk.PhotoImage(Image.open("gen_image.png").resize((20,20), Image.LANCZOS,reducing_gap=10))

    customtkinter.CTkButton(frame1, text="Generate Images", image=ImageGenerationIcon, fg_color="#212121", bg_color="#212121", hover_color="#1c1c1c", command=Gen_iMAGE, width=380, height=50).place(relx = 0.5, rely = 0.15, anchor = "center")

    WebsiteIcon = ImageTk.PhotoImage(Image.open("link.png").resize((20,20), Image.LANCZOS,reducing_gap=10))

    customtkinter.CTkButton(frame1, text="Website", image=WebsiteIcon, fg_color="#212121", bg_color="#212121", hover_color="#1c1c1c", command=LaunchWebsite, width=380, height=50).place(relx = 0.5, rely = 0.2, anchor = "center")

def Support():
    pygame.mixer.init()
    pygame.mixer.music.load("Click.mp3")
    pygame.mixer.music.play()
    
    webbrowser.open("https://paypal.me/Accelerate4?country.x=SA&locale.x=en_US")

Headerframe = customtkinter.CTkFrame(master=root, height=5)
Headerframe.pack(pady=5, padx=0, fill = "both", expand = False)

frame = customtkinter.CTkScrollableFrame(master=root, bg_color="#212121", fg_color="#212121", scrollbar_button_color="#575757", orientation=VERTICAL)
frame.pack(pady=0,padx= 0, fill = BOTH, expand = True)

#bottom = customtkinter.CTkFrame(master=root)
#bottom.pack(pady=20,padx=60, anchor = "w", fill ="both", expand = False)

AppName = customtkinter.CTkLabel(master=Headerframe, text="CapeAI", font = customtkinter.CTkFont(family="Andante", weight="normal", size=10), anchor="e")
AppName.pack(pady=0,padx=0, side = "top")

#DropDown = customtkinter.CTkOptionMenu(master=Headerframe, corner_radius=15)
#DropDown.pack(pady =0, padx=0, side = "left")

#DropDown.configure(values= ["Credits", "Developer"])

def clearMessages():
    Delete = messagebox.askyesno("Clear data", message="Are you sure you want to delete all previous messages?")
    if Delete:
        MessageHistory.clear()
        for widgets in frame.winfo_children():
            root.after(100)
            widgets.destroy()   

def CopyText():
    if CanCopy == True:
        CTk.clipboard_append(self=root, string=LatestReplyFromAi)

MessagesIcon = ImageTk.PhotoImage(Image.open("chaticon.png").resize((17,17)))

TokensText = customtkinter.CTkButton(master=Headerframe, image=MessagesIcon,text=var.get(), font=customtkinter.CTkFont(family="Andante", weight="normal", size=17),bg_color="#212121", fg_color="#212121", hover_color="#212121")
TokensText.pack(pady=1,padx=1)

Header123 = ImageTk.PhotoImage(Image.open("Header.png").resize((150,85), Image.LANCZOS,reducing_gap=5))

TextBox = customtkinter.CTkEntry(master=root,bg_color="#212121", border_color="white" ,border_width=0, corner_radius= 10 ,placeholder_text=  "Type here",height=35, width=35, font=customtkinter.CTkFont(family=("Helvetica")))
TextBox.pack(pady=15,padx=5, side = "left", expand = True, fill = "both")

SendPicture = ImageTk.PhotoImage(Image.open("Send_Icon.png").resize((35,35), Image.LANCZOS,reducing_gap=10))

MenuIcon = ImageTk.PhotoImage(Image.open("Menu.png").resize((35,35), Image.LANCZOS,reducing_gap=10))

Menu = customtkinter.CTkButton(master= Headerframe, image= MenuIcon, text="", fg_color="#212121", bg_color="#212121", height=70, width=70, anchor="w", hover_color="#373737", command=toggle_win)
Menu.place(relx = 0.04, rely = 0.5, anchor = "center")

PictyureHeader = customtkinter.CTkButton(master= Headerframe, image= Header123, text="", fg_color="#212121", bg_color="#212121", height=70, width=145, anchor="w", hover_color="#373737", command=LaunchWebsite)
PictyureHeader.place(relx = 0.14, rely = 0.5, anchor = "center")

TwitterIcon = ImageTk.PhotoImage(Image.open("twitter.png").resize((25,25)))

Twitter = customtkinter.CTkButton(master=Headerframe,bg_color="#212121" ,image=TwitterIcon, text="Developer", compound=LEFT, command=GoToTwitter, width=100, height=25, corner_radius=25, font=CTkFont(weight="bold"), fg_color="#212121")
Twitter.place(relx = 0.925, rely = 0.5, anchor = "center")

paypalImage = ImageTk.PhotoImage(Image.open("paypal.png").resize((25,25)))

Donate = customtkinter.CTkButton(master=Headerframe,bg_color="#212121" ,image=paypalImage, text="SUPPORT", compound=LEFT, command=Support, width=100, height=25, corner_radius=25, fg_color="#212121", hover_color="#453f1d",font=CTkFont(family="Andante" ,weight="bold"))
Donate.place(relx = 0.78, rely = 0.5, anchor = "center")

PlusPicture = ImageTk.PhotoImage(Image.open("Plus.png").resize((17,17), Image.LANCZOS,reducing_gap=5))

SendPicture = ImageTk.PhotoImage(Image.open("Send_Icon.png").resize((30,30), Image.LANCZOS,reducing_gap=10))

TrashIcon = ImageTk.PhotoImage(Image.open("trash.png").resize((30,30), Image.LANCZOS,reducing_gap=10))

CopyIcon = ImageTk.PhotoImage(Image.open("Copy.png").resize((30,30), Image.LANCZOS,reducing_gap=10))

DATA = customtkinter.CTkButton(master=root, bg_color="#1c1c1c",fg_color="#212121",corner_radius=10 ,hover_color="#1c1c1c", border_color="White", width=35, height=35, command= clearMessages, text="", border_spacing=0 ,image=TrashIcon)
DATA.pack(pady=15, padx= 5, side= "right", fill = "both", expand = False)

Copy = customtkinter.CTkButton(master=root, bg_color="#1c1c1c",fg_color="#212121",corner_radius=10 ,hover_color="#1c1c1c", border_color="White", width=35, height=35, command= CopyText, text="", border_spacing=0 ,image=CopyIcon)
Copy.pack(pady=15, padx= 5, side= "right", fill = "both", expand = False)

EnterButton = customtkinter.CTkButton(master=root, bg_color="#1c1c1c",fg_color="#212121",corner_radius=10 ,hover_color="#1c1c1c", border_color="White", width=35, height=35, command= ButtonAnimation, text="", border_spacing=0 ,image=SendPicture)
EnterButton.pack(pady=15, padx= 5, side= "right", fill = "both", expand = False)

root.mainloop()


