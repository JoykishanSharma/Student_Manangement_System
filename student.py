from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
import mysql.connector  # pip install mysql-connector-python


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1290x780+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")

        # Variables
        self.var_dept = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

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

        # title label
        lbl_title = Label(bg_lbl, text="STUDENT MANAGEMENT SYSTEM",
                          font=("times new roman", 37, "bold"),
                          fg="blue", bg="white")
        lbl_title.place(x=0, y=0, width=1290, height=50)

        # manage frame
        manage_frame = Frame(bg_lbl, bd=2, relief=RIDGE, bg="white")
        manage_frame.place(x=15, y=60, width=1260, height=550)

        # left frame
        data_left_frame = LabelFrame(manage_frame, bd=4, relief=RIDGE,
                                     padx=2, text="Student Information",
                                     font=("times new roman", 12, "bold"),
                                     fg="red", bg="white")
        data_left_frame.place(x=10, y=5, width=560, height=535)

        # image - inside left frame
        img_5 = Image.open(r"college_images\3rd.jpg")
        img_5 = img_5.resize((560, 120), Image.ANTIALIAS)
        self.photoImg_5 = ImageTk.PhotoImage(img_5)

        left_top_img = Label(data_left_frame, image=self.photoImg_5, bd=2, relief=RIDGE)
        left_top_img.place(x=0, y=0, width=550, height=120)

        # current course label frame Information
        std_lbl_info_frame = LabelFrame(data_left_frame, bd=4, relief=RIDGE,
                                        padx=2, text="Current Course Information",
                                        font=("times new roman", 12, "bold"),
                                        fg="red", bg="white")
        std_lbl_info_frame.place(x=0, y=120, width=550, height=115)

        # Label and Combobox
        # department
        lbl_dept = Label(std_lbl_info_frame, text="Department",
                         font=("arial", 11, "bold"), bg="white")
        lbl_dept.grid(row=0, column=0, padx=2, sticky=W)

        combo_dept = ttk.Combobox(std_lbl_info_frame,
                                  textvariable=self.var_dept,
                                  font=("arial", 10, "bold"),
                                  width=17, state="readonly")
        combo_dept["value"] = ("Select Department",
                               "Computer Science",
                               "Computer Application",
                               "Civil Engineering",
                               "Mechanical Engineering")
        combo_dept.current(0)
        combo_dept.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # course
        course_std = Label(std_lbl_info_frame, text="Courses:",
                           font=("arial", 11, "bold"), bg="white")
        course_std.grid(row=0, column=2, padx=2, pady=10, sticky=W)

        combo_course = ttk.Combobox(std_lbl_info_frame,
                                    textvariable=self.var_course,
                                    font=("arial", 10, "bold"),
                                    width=17, state="readonly")
        combo_course["value"] = ("Select Course",
                                 "FE",
                                 "SE",
                                 "TE",
                                 "BE")
        combo_course.current(0)
        combo_course.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # year
        current_year = Label(std_lbl_info_frame, text="Year:",
                             font=("arial", 11, "bold"), bg="white")
        current_year.grid(row=1, column=0, padx=2, pady=10, sticky=W)

        combo_current_year = ttk.Combobox(std_lbl_info_frame,
                                          textvariable=self.var_year,
                                          font=("arial", 10, "bold"),
                                          width=17, state="readonly")
        combo_current_year["value"] = ("Select Year",
                                       "2020-2021",
                                       "2021-2022",
                                       "2022-2023",
                                       "2023-2024")
        combo_current_year.current(0)
        combo_current_year.grid(row=1, column=1, padx=2, sticky=W)

        # semester
        semester_label = Label(std_lbl_info_frame, text="Semester:",
                               font=("arial", 11, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=2, pady=10, sticky=W)

        combo_semester_label = ttk.Combobox(std_lbl_info_frame,
                                            textvariable=self.var_semester,
                                            font=("arial", 10, "bold"),
                                            width=17, state="readonly")
        combo_semester_label["value"] = ("Select Semester",
                                         "Semester-1",
                                         "Semester-2")
        combo_semester_label.current(0)
        combo_semester_label.grid(row=1, column=3, padx=2, pady=0, sticky=W)

        # student class label frame Information
        std_lbl_class_frame = LabelFrame(data_left_frame, bd=4, relief=RIDGE,
                                         padx=2, text="Student Class Information",
                                         font=("times new roman", 12, "bold"),
                                         fg="red", bg="white")
        std_lbl_class_frame.place(x=0, y=235, width=550, height=220)

        # Label and Combobox
        # ID
        lbl_id = Label(std_lbl_class_frame, text="StudentID:",
                       font=("arial", 11, "bold"), bg="white")
        lbl_id.grid(row=0, column=0, padx=2, pady=7, sticky=W)

        id_entry = ttk.Entry(std_lbl_class_frame,
                             textvariable=self.var_std_id,
                             font=("arial", 10, "bold"),
                             width=15)
        id_entry.grid(row=0, column=1, padx=2, pady=7, sticky=W)

        # Name
        lbl_name = Label(std_lbl_class_frame, text="Student Name:",
                         font=("arial", 11, "bold"), bg="white")
        lbl_name.grid(row=0, column=2, padx=2, pady=7, sticky=W)

        name_entry = ttk.Entry(std_lbl_class_frame,
                               textvariable=self.var_std_name,
                               font=("arial", 10, "bold"),
                               width=15)
        name_entry.grid(row=0, column=3, padx=2, pady=7, sticky=W)

        # Division
        lbl_div = Label(std_lbl_class_frame, text="Class Div:",
                        font=("arial", 11, "bold"), bg="white")
        lbl_div.grid(row=1, column=0, padx=2, pady=7, sticky=W)

        div_combo = ttk.Combobox(std_lbl_class_frame,
                                 textvariable=self.var_div,
                                 font=("arial", 10, "bold"),
                                 width=15, state="readonly")
        div_combo["value"] = ("Select Division",
                              "A",
                              "B",
                              "C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=2, pady=7, sticky=W)

        # Roll
        lbl_roll = Label(std_lbl_class_frame, text="Roll No.:",
                         font=("arial", 11, "bold"), bg="white")
        lbl_roll.grid(row=1, column=2, padx=2, pady=7, sticky=W)

        roll_entry = ttk.Entry(std_lbl_class_frame,
                               textvariable=self.var_roll,
                               font=("arial", 10, "bold"),
                               width=15)
        roll_entry.grid(row=1, column=3, padx=2, pady=7, sticky=W)

        # Gender
        lbl_gender = Label(std_lbl_class_frame, text="Gender:",
                           font=("arial", 11, "bold"), bg="white")
        lbl_gender.grid(row=2, column=0, padx=2, pady=7, sticky=W)

        gender_combo = ttk.Combobox(std_lbl_class_frame,
                                    textvariable=self.var_gender,
                                    font=("arial", 10, "bold"),
                                    width=15, state="readonly")
        gender_combo["value"] = ("Male",
                                 "Female",
                                 "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=2, pady=7, sticky=W)

        # Date Of Birth
        lbl_dob = Label(std_lbl_class_frame, text="DOB:",
                        font=("arial", 11, "bold"), bg="white")
        lbl_dob.grid(row=2, column=2, padx=2, pady=7, sticky=W)

        dob_entry = ttk.Entry(std_lbl_class_frame,
                              textvariable=self.var_dob,
                              font=("arial", 10, "bold"),
                              width=15)
        dob_entry.grid(row=2, column=3, padx=2, pady=7, sticky=W)

        # Email
        lbl_email = Label(std_lbl_class_frame, text="Email:",
                          font=("arial", 11, "bold"), bg="white")
        lbl_email.grid(row=3, column=0, padx=2, pady=7, sticky=W)

        email_entry = ttk.Entry(std_lbl_class_frame,
                                textvariable=self.var_email,
                                font=("arial", 10, "bold"),
                                width=15)
        email_entry.grid(row=3, column=1, padx=2, pady=7, sticky=W)

        # phone
        lbl_phone = Label(std_lbl_class_frame, text="Phone:",
                          font=("arial", 11, "bold"), bg="white")
        lbl_phone.grid(row=3, column=2, padx=2, pady=7, sticky=W)

        phone_entry = ttk.Entry(std_lbl_class_frame,
                                textvariable=self.var_phone,
                                font=("arial", 10, "bold"),
                                width=15)
        phone_entry.grid(row=3, column=3, padx=2, pady=7, sticky=W)

        # Address
        lbl_address = Label(std_lbl_class_frame, text="Address:",
                            font=("arial", 11, "bold"), bg="white")
        lbl_address.grid(row=4, column=0, padx=2, pady=7, sticky=W)

        address_entry = ttk.Entry(std_lbl_class_frame,
                                  textvariable=self.var_address,
                                  font=("arial", 10, "bold"),
                                  width=15)
        address_entry.grid(row=4, column=1, padx=2, pady=7, sticky=W)

        # Teacher
        lbl_teacher = Label(std_lbl_class_frame, text="Teacher:",
                            font=("arial", 11, "bold"), bg="white")
        lbl_teacher.grid(row=4, column=2, padx=2, pady=7, sticky=W)

        teacher_entry = ttk.Entry(std_lbl_class_frame,
                                  textvariable=self.var_teacher,
                                  font=("arial", 10, "bold"),
                                  width=15)
        teacher_entry.grid(row=4, column=3, padx=2, pady=7, sticky=W)

        # button frame
        button_frame = Frame(data_left_frame, bd=2, relief=RIDGE, bg="white")
        button_frame.place(x=0, y=460, width=550, height=50)

        # save button
        btn_add = Button(button_frame, text="Save",
                         font=("arial", 11, "bold"),
                         command=self.add_data,
                         width=13, bg="blue", fg="white")
        btn_add.grid(row=0, column=0, padx=6, pady=6, sticky=W)

        # update button
        btn_update = Button(button_frame, text="Update",
                            font=("arial", 11, "bold"),
                            width=13, bg="blue", fg="white")
        btn_update.grid(row=0, column=1, padx=4, pady=6, sticky=W)

        # delete button
        btn_delete = Button(button_frame, text="Delete",
                            font=("arial", 11, "bold"),
                            width=13, bg="blue", fg="white")
        btn_delete.grid(row=0, column=2, padx=4, pady=6, sticky=W)

        # reset button
        btn_reset = Button(button_frame, text="Reset",
                           font=("arial", 11, "bold"),
                           width=13, bg="blue", fg="white")
        btn_reset.grid(row=0, column=3, padx=4, pady=6, sticky=W)

        # right frame
        data_right_frame = LabelFrame(manage_frame, bd=4, relief=RIDGE,
                                      padx=2, text="Student Information",
                                      font=("times new roman", 11, "bold"),
                                      fg="red", bg="white")
        data_right_frame.place(x=585, y=10, width=660, height=530)

        # image - inside right frame
        img_6 = Image.open(r"college_images\6th.jpg")
        img_6 = img_6.resize((650, 120), Image.ANTIALIAS)
        self.photoImg_6 = ImageTk.PhotoImage(img_6)

        right_top_img = Label(data_right_frame, image=self.photoImg_6, bd=2, relief=RIDGE)
        right_top_img.place(x=0, y=0, width=650, height=120)

        # search frame
        search_frame = LabelFrame(data_right_frame, bd=4, relief=RIDGE,
                                  padx=2, text="Search Student Information",
                                  font=("times new roman", 11, "bold"),
                                  fg="red", bg="white")
        search_frame.place(x=0, y=120, width=650, height=60)

        # search by label
        search_by = Label(search_frame, text="Search By:",
                          font=("arial", 11, "bold"), fg="red", bg="black")
        search_by.grid(row=0, column=0, padx=5, sticky=W)

        search_combo = ttk.Combobox(search_frame,
                                    font=("arial", 10, "bold"),
                                    width=15, state="readonly")
        search_combo["value"] = ("Select Option",
                                 "Roll No",
                                 "Phone",
                                 "Student_id")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, sticky=W)

        id_entry = ttk.Entry(search_frame,
                             font=("arial", 10, "bold"),
                             width=20)
        id_entry.grid(row=0, column=2, padx=2, sticky=W)

        # search button
        btn_search = Button(search_frame, text="Search",
                            font=("arial", 11, "bold"),
                            width=12, bg="blue", fg="white")
        btn_search.grid(row=0, column=3, padx=5, sticky=W)

        # show all button
        btn_show_all = Button(search_frame, text="Show All",
                              font=("arial", 11, "bold"),
                              width=12, bg="blue", fg="white")
        btn_show_all.grid(row=0, column=4, padx=5, sticky=W)

        # Student Table & scroll bar
        table_frame = Frame(data_right_frame, bd=4, relief=RIDGE)
        table_frame.place(x=0, y=180, width=650, height=325)

        scroll_bar_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_bar_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, column=("dept",
                                                               "course",
                                                               "year",
                                                               "sem",
                                                               "id",
                                                               "name",
                                                               "div",
                                                               "roll",
                                                               "gender",
                                                               "dob",
                                                               "email",
                                                               "phone",
                                                               "address",
                                                               "teacher"),
                                          xscrollcommand=scroll_bar_x.set,
                                          yscrollcommand=scroll_bar_y.set)
        scroll_bar_x.pack(side=BOTTOM, fill=X)
        scroll_bar_y.pack(side=RIGHT, fill=Y)

        scroll_bar_x.config(command=self.student_table.xview)
        scroll_bar_y.config(command=self.student_table.yview)

        self.student_table.heading("dept", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("div", text="Class Div")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher Name")

        self.student_table["show"] = "headings"

        self.student_table.column("dept", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if (self.var_dept.get() == "" or
                self.var_email.get() == "" or
                self.var_std_id.get() == ""):
            messagebox.showerror("Error", "All Field are required!")
        else:
            try:
                connection = mysql.connector.connect(host="localhost",
                                                     username="root",
                                                     password="devServerSQL@123",
                                                     database="student_management_system")
                cursor = connection.cursor()
                cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s)",
                               (self.var_dept.get(),
                                self.var_course.get(),
                                self.var_year.get(),
                                self.var_semester.get(),
                                self.var_std_id.get(),
                                self.var_std_name.get(),
                                self.var_div.get(),
                                self.var_roll.get(),
                                self.var_gender.get(),
                                self.var_dob.get(),
                                self.var_email.get(),
                                self.var_phone.get(),
                                self.var_address.get(),
                                self.var_teacher.get()
                                ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("Success", "Student has been Added!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # fetch function
    def fetch_data(self):
        connection = mysql.connector.connect(host="localhost",
                                             username="root",
                                             password="devServerSQL@123",
                                             database="student_management_system")
        cursor = connection.cursor()
        cursor.execute("select * from student")
        data = cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            connection.commit()
        connection.close()

    # Get Cursor
    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content["values"]

        self.var_dept.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])

    # update data
    # def update_data(self):



if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
