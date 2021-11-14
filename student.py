from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1290x780+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")

        # 1st Image
        img_1 = Image.open(r"college_images\7th.jpg")
        img_1 = img_1.resize((430, 160), Image.ANTIALIAS)
        self.photoImg_1 = ImageTk.PhotoImage(img_1)

        self.btn_1 = Button(self.root, image=self.photoImg_1, cursor="hand2")
        self.btn_1.place(x=0, y=0, width=430, height=160)

        # 2nd Image
        img_2 = Image.open(r"college_images\7th.jpg")
        img_2 = img_2.resize((430, 160), Image.ANTIALIAS)
        self.photoImg_2 = ImageTk.PhotoImage(img_2)

        self.btn_2 = Button(self.root, image=self.photoImg_2, cursor="hand2")
        self.btn_2.place(x=430, y=0, width=430, height=160)

        # 3rd Image
        img_3 = Image.open(r"college_images\7th.jpg")
        img_3 = img_3.resize((430, 160), Image.ANTIALIAS)
        self.photoImg_3 = ImageTk.PhotoImage(img_3)

        self.btn_3 = Button(self.root, image=self.photoImg_3, cursor="hand2")
        self.btn_3.place(x=860, y=0, width=430, height=160)

        # bg image
        img_4 = Image.open(r"college_images\university.jpg")
        img_4 = img_4.resize((1290, 780), Image.ANTIALIAS)
        self.photoImg_4 = ImageTk.PhotoImage(img_4)

        bg_lbl = Label(self.root, image=self.photoImg_4, bd=2, relief=RIDGE)
        bg_lbl.place(x=0, y=160, width=1290, height=620)




if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
