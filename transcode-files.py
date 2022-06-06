from tkinter import filedialog
from tkinter import *
import os
from H265ToH264 import FFmpegH265ToH264
import logging

logging.basicConfig(filename='transcode-files.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

suported_files = ('mp4','mkv','avi','m4v')

tk = Tk()
folder =  filedialog.askdirectory(initialdir ="~",title = "Choose a path") 
tk.destroy()

logging.info(f'Starting transcode-files.py in {folder}')

for root, dirs, files in os.walk(folder, topdown=False):
   for name in files:
      if name.strip()[-3:] in suported_files:                      
         file = os.path.join(root, name)
         video = FFmpegH265ToH264(file)
         video.run()
         logging.info(f'{file} converted to {video.output_file}')