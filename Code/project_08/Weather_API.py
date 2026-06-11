from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root = Tk()
root.title("Weather API")
root.geometry("890x470+300+200")
root.configure(bg="#57adff")
root.resizable(False, False)

# Icon
Image_icon = PhotoImage(file="../../icon/loop.png")
root.iconphoto(False, Image_icon)

# Rounded Box Image
Round_box = PhotoImage(file="../../icon/Rounded_Rectangle_1.png")
Label(root, image=Round_box, bg="#57adff").place(x=30, y=110)

# Labels
label1 = Label(root, text="Temperature",
               font=('Helvetica',11),
               fg="white",
               bg="#203243")
label1.place(x=50, y=120)

label2 = Label(root, text="Humidity",
               font=('Helvetica',11),
               fg="white",
               bg="#203243")
label2.place(x=50, y=140)

label3 = Label(root, text="Pressure",
               font=('Helvetica',11),
               fg="white",
               bg="#203243")
label3.place(x=50, y=160)

label4 = Label(root, text="Wind Speed",
               font=('Helvetica',11),
               fg="white",
               bg="#203243")
label4.place(x=50, y=180)

label5 = Label(root, text="Description",
               font=('Helvetica',11),
               fg="white",
               bg="#203243")
label5.place(x=50, y=200)

root.mainloop()