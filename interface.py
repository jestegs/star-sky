import star_sky as stars
from tkinter import *
from PIL import Image
import os

PROGRAM_PATH = os.getcwd()
SAVES_PATH = os.path.join(PROGRAM_PATH, "Saves")
if not os.path.exists(SAVES_PATH):
    os.mkdir(SAVES_PATH)


class MainWindow:
    def __init__(self):
        self.gen_im = Image

        root = Tk()
        root.title("Star Sky")
        root.geometry("300x200")

        button_frame = Frame(root, padx=10, pady=10)
        entry_frame = Frame(root, padx=10, pady=10)

        size_label = Label(entry_frame, text="Size:")
        size_entry = self.size_entry = Entry(entry_frame, width=15)
        freq_label = Label(entry_frame, text="Frequency:")
        freq_entry = self.freq_entry = Entry(entry_frame, width=15)

        size_entry.insert(0, "400x400")
        freq_entry.insert(0, "0.01")

        gen_button = Button(button_frame, text="Generate", width=20, command=self.generate_new)
        save_button = Button(button_frame, text="Save", width=20, command=self.save_image)

        entry_frame.pack()
        button_frame.pack()

        size_label.grid(row=0, column=0, padx=5)
        size_entry.grid(row=0, column=1, padx=5)
        freq_label.grid(row=1, column=0)
        freq_entry.grid(row=1, column=1)

        gen_button.pack(padx=5, pady=5)
        save_button.pack(padx=5, pady=5)

        root.mainloop()

    def save_image(self):
        self.gen_im.save(os.path.join(SAVES_PATH, "test.png"), "PNG")

    def generate_new(self):
        entry = self.size_entry.get().split("x")
        image_size = [0, 0]
        image_size[0] = int(entry[0])
        image_size[1] = int(entry[1])

        image_size = tuple(image_size)
        star_freq = float(self.freq_entry.get())

        self.gen_im = stars.generate_image(image_size, star_freq)


MainWindow()
