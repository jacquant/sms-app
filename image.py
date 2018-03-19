import tkinter as tk
import os
import shutil
import tkinter.messagebox
from PIL import Image, ImageTk

dirimage = "/home/jacquant/PycharmProjects/sms/images_a_valider"
dirimage_val = "/home/jacquant/PycharmProjects/sms/assets/images_valides"
dirimage_non_val = "/home/jacquant/PycharmProjects/sms/images_non_validees"


class MainWindow:
    def __init__(self, root):
        self.path_image = ""
        self.root = root
        self.root.title("Valider les Images")
        self.root.geometry("1024x768")
        self.root.configure(background='#000000')
        self.Frame_up = tk.Frame(self.root)
        self.Frame_down = tk.Frame(self.root)
        self.ButtonClear = tk.Button(self.Frame_up, text='Nettoyer', command=self.clear_image)
        self.ButtonClear.grid(column=0, row=0, sticky='NSEW')
        self.ButtonValidate = tk.Button(self.Frame_up, text='Valider', command=self.validate_image)
        self.ButtonValidate.grid(column=1, row=0, sticky='NSEW')
        self.ButtonMessageupdade = tk.Button(self.Frame_up, text='Mettre à jour', command=self.give_new_image)
        self.ButtonMessageupdade.grid(column=2, row=0, sticky='NSEW')
        self.Frame_up.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        self.label1 = tk.Label(self.Frame_down)
        self.label1.pack()
        self.Frame_down.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        self.give_new_image()
        self.path_image = ""
        self.updater()
        # self.update_new_message()

    def clear_image(self):
        if self.path_image != "":
            shutil.move(os.path.join(dirimage, self.path_image), os.path.join(dirimage_non_val, self.path_image))
            self.give_new_image()

    def validate_image(self):
        if self.path_image != "":
            shutil.move(os.path.join(dirimage, self.path_image), os.path.join(dirimage_val, self.path_image))
            self.give_new_image()

    def give_new_image(self):
        images = [f for f in os.listdir(dirimage) if os.path.isfile(os.path.join(dirimage, f))]
        images.sort()
        if len(images) > 0:
            self.path_image = images[0]
            image = Image.open(os.path.join(dirimage, images[0]))

        else:
            self.path_image = ""
            image = Image.open("no-img.png")

        gap = 100  # marge par rapport aux bords de l'écran
        screen_width = self.Frame_down.winfo_screenwidth() - gap
        screen_height = self.Frame_down.winfo_screenheight() - gap

        if image.width > screen_width:
            image = image.resize((screen_width, int(image.height * screen_width / image.width)), Image.ANTIALIAS)
        if image.height > screen_height:
            image = image.resize((int(image.width * screen_height / image.height), screen_height), Image.ANTIALIAS)

        photo = ImageTk.PhotoImage(image)
        self.label1.configure(image=photo)
        self.label1.image = photo
        self.Frame_down.update()
        self.root.update()

    def updater(self):
        self.give_new_image()
        self.root.after(10000, self.updater)


def on_closing():
    if tkinter.messagebox.askokcancel("Quitter l'application", "Voulez-vous vraiment fermer l'application?"):
        root.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    MainWindow(root)
    root.protocol('WM_DELETE_WINDOW', on_closing)
    root.mainloop()
