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

#Icon
Image_icon=photoImage(file="Image/loop.png")
root.iconphoto(False,Image_icon)

root.mainloop()