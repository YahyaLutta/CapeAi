import customtkinter
import tkinter
import openai
import os
from dotenv import load_dotenv
import time

def configure():
    load_dotenv()

configure()

openai.api_key = os.getenv("api_key")
openai.Model.list()
import requests
import webbrowser
from flask import Flask, request
from CapeAi_Data import Messages
from PIL import Image, ImageTk
from customtkinter import* 
from tkinter import messagebox 
from tkinter import Message
import random
import paypalrestsdk
import logging
import mailbox
from io import BytesIO
import urllib.request

Pictures = []

Textbox = ""

LatestPicture = []

LatestUrlImage = "?"

URLS = []

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
x = (root.winfo_screenwidth()//2)-(1000//2)
y = (root.winfo_screenheight()//2)-(665//2)
root.geometry('{}x{}+{}+{}'.format(1000, 665, x, y))

root.title = "CapeAI"
root._fg_color = "#0a0a0a"
root.iconbitmap("Icon.ico")
root.wm_title("CapeAI")

root.resizable = False

File = open("User_Prompt.py", "w")

def Support_Email():
    mailbox.Mailbox("yahyalutta@gmail.com")

def Donate():
    webbrowser.open_new_tab("https://paypal.me/Accelerate4?country.x=SA&locale.x=en_US")

def Download():
    if LatestUrlImage == "?":
        messagebox.showerror(title="Error", message="You haven't generated an image")
    else:
        webbrowser.open_new_tab(LatestUrlImage)

def toggle_win():
    frame1 = customtkinter.CTkFrame(root, width= 300, height= 1000)
    frame1.place(relx=0,rely=0)

    def delete1():
        frame1.destroy()

    customtkinter.CTkButton(frame1, text="Close X", command=delete1, fg_color="#212121").place(relx=0.5, rely=0.05, anchor = "center")

    HomeIcon = ImageTk.PhotoImage(Image.open("Home.png").resize((20,20), Image.LANCZOS,reducing_gap=10))

    customtkinter.CTkButton(frame1, text="Home", image=HomeIcon, fg_color="#212121", bg_color="#212121" ,hover_color="#1c1c1c", width=380, height=50).place(relx = 0.5, rely = 0.1, anchor = "center")
    global ImageGenerationIcon
    ImageGenerationIcon = ImageTk.PhotoImage(Image.open("gen_image.png").resize((20,20), Image.LANCZOS,reducing_gap=10))

    customtkinter.CTkButton(frame1, text="Generate Images", image=ImageGenerationIcon, fg_color="#212121", bg_color="#212121", hover_color="#1c1c1c", width=380, height=50).place(relx = 0.5, rely = 0.15, anchor = "center")

    WebsiteIcon = ImageTk.PhotoImage(Image.open("link.png").resize((20,20), Image.LANCZOS,reducing_gap=10))

    customtkinter.CTkButton(frame1, text="Website", image=WebsiteIcon, fg_color="#212121", bg_color="#212121", hover_color="#1c1c1c", width=380, height=50).place(relx = 0.5, rely = 0.2, anchor = "center")

def Generate_Image():
    global Textbox
    Textbox = InputText.get()
    global response
    response = openai.Image.create(
    prompt=Textbox,
    n=1,
    size="1024x1024"
    )
    global image_url
    image_url = response['data'][0]['url']
    global LatestUrlImage
    LatestUrlImage = image_url

BackgroundImage = ImageTk.PhotoImage(Image.open("background.png").resize((1000,665)))
BackgroundFrame = customtkinter.CTkFrame(root, width=1000, height=665, fg_color="#0a0a0a")
BackgroundFrame.pack(fill = "both", expand = True)

HeaderIcon = ImageTk.PhotoImage(Image.open("Header.png").resize((250,150), Image.LANCZOS,reducing_gap=5))
HeaderText = customtkinter.CTkLabel(BackgroundFrame, fg_color="#0a0a0a", bg_color="#0a0a0a", width=250, height=150, image=HeaderIcon, text="", anchor=W)
HeaderText.place(relx = 0.5, rely = 0.075, anchor = "center")

MenuIcon = ImageTk.PhotoImage(Image.open("Menu.png").resize((35,35), Image.LANCZOS,reducing_gap=10))

Menu = customtkinter.CTkButton(master= root, image= MenuIcon, text="", fg_color="#0a0a0a", bg_color="#0a0a0a", height=70, width=70, anchor="w", hover_color="#0a0a0a", command=toggle_win)
Menu.place(relx = 0.06, rely = 0.075, anchor = "center")

FirstText = customtkinter.CTkLabel(BackgroundFrame, text="G E N E R A T E", anchor=W, font=CTkFont(family="Arial", size=40, weight="bold"))
FirstText.place(relx = 0.05, rely = 0.2, anchor = "w")

SecondText = customtkinter.CTkLabel(BackgroundFrame,justify = customtkinter.LEFT ,text="Describe the image you want to generate. Please be specific", anchor=customtkinter.W, font=CTkFont(family="Arial",size=20, weight="normal"), wraplength=400, width=50)
SecondText.place(relx = 0.05, rely = 0.3, anchor = "w")

InputText = customtkinter.CTkEntry(BackgroundFrame ,width= 400,border_width=0, placeholder_text="type here",border_color="#717171" ,height=250, corner_radius=15, bg_color="#0a0a0a", fg_color="#212121", text_color="#ffffff", font=customtkinter.CTkFont(family="Arial", size=15))
InputText.place(relx = 0.05, rely = 0.55, anchor = "w")

ImgeIconGeneration = ImageTk.PhotoImage(Image.open("gen_image.png").resize((30,30), Image.LANCZOS,reducing_gap=5))
EnterButton = customtkinter.CTkButton(BackgroundFrame, width=250,command=Generate_Image ,height=50, image=ImgeIconGeneration, text="G E N E R A T E", hover_color="#00d0ff", fg_color="#33a3ff", corner_radius=15, font=CTkFont(family="Arial", size=20, weight="bold"))
EnterButton.place(relx = 0.05, rely = 0.825, anchor = "w")

SupportText = customtkinter.CTkButton(BackgroundFrame, text="S U P P O R T", text_color="#ffffff", hover_color="#0a0a0a", fg_color="#0a0a0a", bg_color="#0a0a0a", font=customtkinter.CTkFont(family="Arial", weight="normal"))
SupportText.place(relx = 0.029, rely = 0.9, anchor = "w")

DonateText = customtkinter.CTkButton(BackgroundFrame, text="D O N A T E", text_color="#ffffff",command=Donate ,hover_color="#0a0a0a", fg_color="#0a0a0a", bg_color="#0a0a0a", font=customtkinter.CTkFont(family="Arial", weight="normal"))
DonateText.place(relx = 0.15, rely = 0.9, anchor = "w")

ImgeIconGenerationBIG = ImageTk.PhotoImage(Image.open("gen_image2.png").resize((250,250), Image.LANCZOS,reducing_gap=5))
ImageGenerationPlace = customtkinter.CTkButton(BackgroundFrame, image=ImgeIconGenerationBIG, width=400 ,height=400, corner_radius=15,text="" ,fg_color="#212121",border_width=0, border_color="#ffffff" ,bg_color="#0a0a0a", hover_color="#303030")
ImageGenerationPlace.place(relx = 0.72, rely = 0.53, anchor = "center")

DownloadIcon = ImageTk.PhotoImage(Image.open("download.png").resize((40,40), Image.LANCZOS,reducing_gap=5))
DownloadButton = customtkinter.CTkButton(ImageGenerationPlace, height=30, width=30, text="" ,bg_color="#212121" ,fg_color="#212121", image=DownloadIcon, command=Download )
DownloadButton.place(relx = 0.1, rely = 0.1, anchor = "center")

root.mainloop()