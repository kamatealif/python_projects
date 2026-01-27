from tkinter import Tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import pygame


def root_window():
    pass


def pygame_init():
    pygame.init()


if __name__ == "__main__":
    root = Tk()
    pygame_init()
    root.title("Musializer")
    root.geometry("800x600")
    root.configure(bg="#1e1e1e")

    def on_q_press(event):
        root.destroy()

    root.bind("<q>", on_q_press)
    root.focus_set()

    root.mainloop()
