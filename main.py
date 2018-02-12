import tkinter as tk
# import datetime
import re
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
        # self.update_new_message()

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
        self.clear_message()
        self.give_new_message()

    def give_new_message(self):
        if self.label1.compare("end-1c", "==", "1.0"):
            with open('sms_reçu.txt', 'r') as file:
                line = file.readline()
                if line != '':
                    self.current_message = re.split(r"<br>", line)[1]
                    self.label1.insert(tk.INSERT, self.current_message)

    # def update_new_message(self):
    #     temps_debut = datetime.datetime.now()
    #     time = datetime.timedelta(seconds=30)
    #     temps_fin = temps_debut + time
    #     while datetime.datetime.now() < temps_fin:
    #         pass
    #     if self.label1.compare("end-1c", "==", "1.0"):
    #         print("the widget is empty")
    #         self.give_new_message()
    #     else:
    #         self.update_new_message()


if __name__ == '__main__':
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()
