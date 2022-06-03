from tkinter import filedialog
from tkinter import *
import os

tk = Tk()
tk.folder =  filedialog.askdirectory(initialdir = "~",title = "Choose a path") 
folder = tk.folder

for root, dirs, files in os.walk("~", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))