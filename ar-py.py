import serial
from PIL import ImageTk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from playsound import playsound
import sys
import os
import random
import threading
import time
import sqlite3
import tkinter.messagebox


class Gui():
    def __init__(self):
        self.screen = Tk()
        self.screen.title("방문록 자동 입력 프로그램")
        self.screen.geometry("804x804")
        self.screen.resizable(width=False, height=False)
        arduino_thread = threading.Thread(target=self.arduino)
        arduino_thread.daemon = True
        arduino_thread.start()
        self.screen.mainloop()

    def arduino(self):
        ser = serial.Serial(
            port='COM7',
            baudrate=9600,
        )
        while True:
            if ser.readable():
                res = ser.readline()
                print(res.decode()[:len(res)-2])


a = Gui()
