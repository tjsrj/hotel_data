import pyautogui as pg
import webbrowser as wb
import time
import pandas as pd
from tkinter import *

def send_message():
    root1 = Tk()
    root1.title("Sending fliers")

    def bulk_messenger():
        data = pd.read_csv(r'C:\Users\Admin\PyCharmProjects\hotel_data\Registry.csv')
        data_dict = data.to_dict('list')
        leads = data_dict['Phone Number']
        name = data_dict['First Name']
        activation = data_dict['Messaging Services']
        combo = zip(leads, name, activation)


        first = True
        for leads, name, activation in combo:

            time.sleep(2)
            message = entry.get()
            if activation == 1:
                print(f'Sending Message to: {name}')
                time.sleep(2)
                wb.open(f'https://web.whatsapp.com/send?phone=+91{leads}&text=Hello {name}, {message}')
                if first:
                    time.sleep(5)
                    first = False
                width, height = pg.size()
                pg.click(width / 2, height / 2)
                time.sleep(8)
                pg.press('enter')
                time.sleep(1)
                pg.hotkey('ctrl', 'w')
            else:
                print("Searching for next customer...")
                time.sleep(1)
        print("messages sent to everyone")
    def clear():
        entry.delete(0, END)


    label = Label(root1, text="Enter Message: ")
    label.grid(row=0, column=0, padx=8, pady=8)
    global entry
    entry = Entry(root1)
    entry.grid(row=0, column=1, padx=8, pady=8)

    button = Button(root1, text="Send", command = bulk_messenger)
    button.grid(row=1, column=0, padx=8, pady=8)

    button2 = Button(root1, text="Clear", command = clear)
    button2.grid(row=1, column=1, padx=8, pady=8)

    root1.mainloop()
    if __name__ == "__send_message__":
        send_message()

