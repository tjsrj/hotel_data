from RegistrationGUI import register_customer
from whatkit import send_message
from data_update import *
import pyautogui as pg
import webbrowser as wb
import time
import csv
from tkinter import *
from tkinter.messagebox import showinfo



root = Tk()
root.title("Welcome")

button_frame = Frame(root)
button_frame.pack()
registration_button = Button(button_frame, text="Register New Customer", padx = 10, pady = 20, command = register_customer)
registration_button.grid(row = 0, column = 0)
messaging = Button(button_frame, text= "Send new Message", padx = 20, pady = 20, command = send_message)
messaging.grid(row = 0, column = 2)
data_change = Button(button_frame, text = "Change data", padx = 45, pady = 20, command = run_treeview)
data_change.grid(row = 0, column = 3)
root.mainloop()


