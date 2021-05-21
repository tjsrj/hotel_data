from tkinter import *
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
import csv


def register_customer():
    root1 = Tk()
    root1.title("Register Customer")

    def save():
        f_name = entry.get()
        l_name = entry1.get()
        ph = entry2.get()
        bulk_messaging = entry3.get()
        first_name = f_name
        last_name = l_name
        ph_no = ph
        message_services = bulk_messaging
        to_append = f'{first_name} {last_name} {ph_no} {message_services}'
        file = open('Registry.csv', 'a', newline='')
        with file:
            writer = csv.writer(file)
            writer.writerow(to_append.split())
            file.close
            showinfo("Saved", "Your Entry Has Been Saved")

    def clear():
        entry.delete(0, END)
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)

    label = Label(root1, text="First Name: ")
    label.grid(row=0, column=0, padx=8, pady=8)
    global entry
    entry = Entry(root1)
    entry.grid(row=0, column=1, padx=8, pady=8)

    label1 = Label(root1, text="Last Name: ")
    label1.grid(row=1, column=0, padx=8, pady=8)
    global entry1
    entry1 = Entry(root1)
    entry1.grid(row=1, column=1, padx=8, pady=8)

    label2 = Label(root1, text="Phone Number: ")
    label2.grid(row=2, column=0, padx=8, pady=8)
    global entry2
    entry2 = Entry(root1)
    entry2.grid(row=2, column=1, padx=8, pady=8)

    label3 = Label(root1, text="Messaging Services Activate: ")
    label3.grid(row=3, column=0, padx=8, pady=8)
    global entry3
    entry3 = Entry(root1)
    entry3.grid(row=3, column=1, padx=8, pady=8)

    button = Button(root1, text="Add", command=save)
    button.grid(row=4, column=0, padx=8, pady=8)

    button2 = Button(root1, text="Clear", command=clear)
    button2.grid(row=4, column=1, padx=8, pady=8)

    root1.mainloop()
    if __name__ == "__main__":
        register_customer()
