from  tkinter import *
from tkinter import ttk, filedialog
import csv

def run_treeview():
    root = Tk()

    tree = ttk.Treeview(root, height=25, selectmode='extended')
    tree.pack()

    def clear_tree():
        tree.delete(*tree.get_children())

    def load_csv():
        clear_tree()
        global filename
        filename = filedialog.askopenfilename(
            initialdir="C:",
            title="Open A File",
            filetype=(("csv files", "*.csv"), ("All File", "*.*"))
        )
        with open(filename) as myfile:
            csvread = csv.reader(myfile, delimiter=',')
            print(type(csvread))
            for row in csvread:
                tree.insert("", 'end', values=row)

    def search_record():
        query = str.lower(fn_box.get())
        query1 = str.lower(ln_box.get())
        query2 = str.lower(ph_box.get())
        query3 = str.lower(ms_box.get())
        selections = []
        for child in tree.get_children():
            search = str(tree.item(child)['values']).lower()
            if len(query) != 0:
                if query in search:
                    selections.append(child)
            else:
                pass
            if len(query1) != 0:
                if query1 in search:
                    selections.append(child)
            else:
                pass
            if len(query2) != 0:
                if query2 in search:
                    selections.append(child)
            else:
                pass
            if len(query3) != 0:
                if query3 in search:
                    selections.append(child)
            else:
                pass
        tree.selection_set(selections)

    def select_record():
        fn_box.delete(0, END)
        ln_box.delete(0, END)
        ph_box.delete(0, END)
        ms_box.delete(0, END)

        selected = tree.focus()
        values = tree.item(selected, 'values')
        fn_box.insert(0, values[0])
        ln_box.insert(0, values[1])
        ph_box.insert(0, values[2])
        ms_box.insert(0, values[3])

    def save_csv():
        selected = tree.focus()
        tree.item(selected, text="", values=(fn_box.get(), ln_box.get(), ph_box.get(), ms_box.get()))
        with open("Registry.csv", "w", newline='') as myfile:
            csvwriter = csv.writer(myfile, delimiter=',')

            for row_id in tree.get_children():
                row = tree.item(row_id)['values']
                csvwriter.writerow(row)
        fn_box.delete(0, END)
        ln_box.delete(0, END)
        ph_box.delete(0, END)
        ms_box.delete(0, END)

    def clear():
        fn_box.delete(0, END)
        ln_box.delete(0, END)
        ph_box.delete(0, END)
        ms_box.delete(0, END)

    tree["columns"] = ("one", "two", "three", "four")
    tree.column("one", width=120)
    tree.column("two", width=160)
    tree.column("three", width=130)
    tree.column("four", width=160)
    tree["show"] = "headings"

    # Menu options for selecting file
    my_menu = Menu(root)
    root.config(menu=my_menu)

    file_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Spreadsheets", menu=file_menu)
    file_menu.add_command(label="open", command=load_csv)

    # Create frame
    label_frame = Frame(root)
    label_frame.pack(pady=20)

    buttons_frame = Frame(root)
    buttons_frame.pack(pady=20)

    # Creating Buttons
    search_button = Button(buttons_frame, text="Search Record", command=search_record)
    search_button.grid(row=0, column=0)

    select_button = Button(buttons_frame, text="Select Record", command=select_record)
    select_button.grid(row=0, column=1)

    button_save = Button(buttons_frame, text='Save', command=save_csv)
    button_save.grid(row=0, column=2)

    clear = Button(buttons_frame, text='Clear', command=clear)
    clear.grid(row=0, column=3)

    # Add Labels
    fn_label = Label(label_frame, text="First Name")
    fn_label.grid(row=0, column=0)

    ln_label = Label(label_frame, text="Last Name")
    ln_label.grid(row=0, column=1)

    ph_label = Label(label_frame, text="Phone Number")
    ph_label.grid(row=0, column=2)

    ms_label = Label(label_frame, text="Messaging Services")
    ms_label.grid(row=0, column=3)

    # Entry Boxes
    fn_box = Entry(label_frame)
    fn_box.grid(row=1, column=0)

    ln_box = Entry(label_frame)
    ln_box.grid(row=1, column=1)

    ph_box = Entry(label_frame)
    ph_box.grid(row=1, column=2)

    ms_box = Entry(label_frame)
    ms_box.grid(row=1, column=3)

    root.mainloop()

if __name__ == "__main__":
    run_treeview()