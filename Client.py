import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import ntpath #This is used to extract filename from path

from tkinter import filedialog
from pathlib import Path


from playsound import playsound
import pygame
from pygame import mixer

import ftplib
from ftplib import FTP
import os 
import time
import ntpath 
from pathlib import Path



ResumeButton=Button(window.text="Resume", width=10,bd=1,bg="SkyBlue".font = ("Calibri".10).command = resume)
ResumeButton.place(x=30,y=250)

PauseButton=Button(window.text="Pause", width=10,bd=1,bg="SkyBlue".font = ("Calibri".10).command = pause)
PauseButton.place(x=200,y=250)

def resume():
    global song_selected
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()

def pause():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()

def browseFiles():
    global listbox
    global song_counter
    global filePathLabel

    try:
        filename = fileddialog.askopenfilename()
        HOSTNAME = "127.0.0.1"
        USERNAME = "lftpd"
        PASSWORD = "lftpd"

        ftp_server = FTP(HOSTNAME, USERNAME, PASSWORD)
        ftp_server.encoding = "utf-8"
        ftp_server.cwd('shared_files')
        fname=ntpath.basename(filename)
        with open(filename, 'rb') as file:
            ftp_server.storbinary(f"STOR {fname}", file)
            
        ftp_server.dir()
        ftp_server.quit()

    except FileNotFoundError:
        print("Cancle Button Pressed")

