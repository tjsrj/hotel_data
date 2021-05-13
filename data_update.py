import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
import csv
import os
from csv import writer
import pandas as pd

def data_change():
    win = tk.Tk()
    win.title("Data Changer")

    def search():
        data = pd.read_csv(r'C:\Users\Admin\PyCharmProjects\hotel_data\Registry.csv')
        data['First Name'] = data['First Name'].str.lower()
        data['Last Name'] = data['Last Name'].str.lower()
        f_name = entry.get()
        f_name = f_name.str.lower()
        l_name = entry1.get()
        l_name = l_name.str.lower()
        ph = entry2.get()
        main = pd.DataFrame()

        if len(f_name) != 0:
            df = data[data['First Name']== f_name]
            main = main.append(df, ignore_index = True)
            main['First Name'] = main['First Name'].str.title()
            main['Last Name'] = main['Last Name'].str.title()
        else:
             messagebox.showinfo("System", "No First Name entered, trying other parameters")

        if len(l_name) != 0:
            df1 = data[data['Last Name'] == l_name]
            main = main.append(df1, ignore_index = True)
            main['First Name'] = main['First Name'].str.title()
            main['Last Name'] = main['Last Name'].str.title()
        else:
            messagebox.showinfo("System", "No Last Name entered, trying other Parameters")

        if len(str(ph)) != 0:
            ph = int(ph)
            df3 = data[data['Phone Number'] == ph]
            main = main.append(df3, ignore_index = True)
            main['First Name'] = main['First Name'].str.title()
            main['Last Name'] = main['Last Name'].str.title()
        else:
            messagebox.showinfo("System", "No Phone Number entered, trying other parameters")


        row_count = len(main.index)
        print(row_count)
        print(main)
        #win1 = tk.Tk()
        #win1.title("Select Data")

    def clear():
        entry.delete(0,tk.END)
        entry1.delete(0,tk.END)
        entry2.delete(0,tk.END)


    label = tk.Label(win,text = "First Name: ")
    label.grid(row=0,column=0, padx=8, pady=8)
    entry = tk.Entry(win)
    entry.grid(row=0,column=1, padx=8, pady=8)

    label1 = tk.Label(win,text="Last Name: ")
    label1.grid(row=1,column=0, padx=8, pady=8)
    entry1 = tk.Entry(win)
    entry1.grid(row=1,column=1, padx=8, pady=8)

    label2 = tk.Label(win,text="Phone Number: ")
    label2.grid(row=2, column=0, padx=8, pady=8)
    entry2 = tk.Entry(win)
    entry2.grid(row=2, column=1, padx=8, pady=8)

    button = ttk.Button(win, text="Search", command=search)
    button.grid(row=4, column=0, padx=8, pady=8)

    button2 = ttk.Button(win, text="Clear", command=clear)
    button2.grid(row=4, column=1, padx=8, pady=8)

    win.mainloop()

data_change()

