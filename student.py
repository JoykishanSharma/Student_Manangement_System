from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1290x780+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")




if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
