from RegistrationGUI import register_customer
from whatkit import send_message
#import activation_change
import csv
from tkinter import *
from tkinter.messagebox import showinfo

root = Tk()
root.title("Welcome")



def change_data():
    return

registration_button = Button(root, text="Register New Customer", padx = 10, pady = 20, command = register_customer)
registration_button.grid(row = 0, column = 0)
messaging = Button(root, text= "Send new Message", padx = 20, pady = 20, command = send_message)
messaging.grid(row = 0, column = 2)
data_change = Button(root, text = "Change data", padx = 45, pady = 20, command = change_data)
data_change.grid(row = 0, column = 3)
root.mainloop()


