import tkinter as tk
import time
import json
# import datetime
import re
import tkinter.messagebox
from tkinter.scrolledtext import ScrolledText

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Valider les Sms")
        self.label1 = ScrolledText(self.root)
        self.label1.grid(row=0, columnspan=3, sticky='NSEW')
        self.ButtonClear = tk.Button(self.root, text='Nettoyer', command=self.clear_message)
        self.ButtonClear.grid(column=0, row=1, sticky='NSEW')
        self.ButtonValidate = tk.Button(self.root, text='Valider', command=self.validate_message)
        self.ButtonValidate.grid(column=1, row=1, sticky='NSEW')
        self.ButtonMessageupdade = tk.Button(self.root, text='Mettre à jour', command=self.give_new_message)
        self.ButtonMessageupdade.grid(column=2, row=1, sticky='NSEW')
        self.current_message = ""
        self.give_new_message()
        self.updater()

    def clear_message(self):
        self.label1.delete(1.0, tk.END)
        file = open('sms_reçu.txt', "r+")
        lines = file.readlines()
        file.seek(0)
        for line in lines[1:]:
            file.write(line)
        file.truncate()
        file.close()
        self.give_new_message()

    def validate_message(self):
        path = 'sms_' + time.strftime("%Y-%m-%d_%I_%M_%S") + '.json'
        with open('sms_valides/' + path, 'w') as json_file:
            json.dump(self.label1.get(1.0, tk.END), json_file)
        self.clear_message()


    def give_new_message(self):
        if self.label1.compare("end-1c", "==", "1.0"):
            with open('sms_reçu.txt', 'r') as file:
                line = file.readline()
                if line != '':
                    self.current_message = re.split(r"<br>", line)[1]
                    self.label1.insert(tk.INSERT, self.current_message)

    def updater(self):
        self.give_new_message()
        self.root.after(5000, self.updater)


def on_closing():
    if tkinter.messagebox.askokcancel("Quitter l'application", "Voulez-vous vraiment fermer l'application?"):
        root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    MainWindow(root)
    root.protocol('WM_DELETE_WINDOW', on_closing)
    root.mainloop()
