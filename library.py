from tkinter import *
from tkinter import ttk
import mysql.connector


class LibraryMangementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Mangement System")
        self.root.geometry("1550x800+0+0")

        # =====================Variable=======================

        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.address1 = StringVar()
        self.address2 = StringVar()
        self.postcode = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.auther_var = StringVar()
        self.data_borrowed_var = StringVar()
        self.date_due_var = StringVar()
        self.days_on_book_var = StringVar()
        self.later_ate_fine_var = StringVar()
        self.dateoverdue = StringVar()
        self.finallprice = StringVar()

        lbltitle = Label(self.root, text="LIBRARY MANGEMENT SYSTEM", bg="powder blue", fg="green",
                         bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)

        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE,
                      padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1440, height=400)

        # ==========================DataFrameLeft=========================================

        DataFrameLeft = LabelFrame(frame, text="Library Membership Information",
                                   bg="powder blue", fg="Black", bd=20, relief=RIDGE, font=("times new roman", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        lblMembr = Label(DataFrameLeft, bg="powder blue", fg="Black", text="Member Type", font=(
            "times new roman", 15, "bold"), padx=2, pady=6)
        lblMembr.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, font=(
            "times new roman", 15, "bold"), width=27, state="readonly")
        comMember["value"] = ("Admin Staf", "Student", "Lecturer")
        comMember.grid(row=0, column=1)

        lblPRN_No = Label(DataFrameLeft, bg="powder blue", fg="Black", text="PRN No", font=(
            "times new roman", 15, "bold"), padx=2, pady=6)
        lblPRN_No.grid(row=1, column=0, sticky=W)

        txtPRN_No = Entry(DataFrameLeft, font=(
            "times new roman", 15, "bold"), width=29)
        txtPRN_No.grid(row=1, column=1)

        lblTitle = Label(DataFrameLeft, font=("arial", 13, "bold", ), fg="black",
                         text="ID No:", padx=2, pady=4, bg="powder blue")
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtTitle.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, font=(
            "arial", 13, "bold", ), text="FirstName", fg="Black", padx=2, pady=6, bg="powder blue")
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=29)
        txtFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, font=(
            "arial", 13, "bold"), text="Lastname", fg="Black", padx=2, pady=6, bg="powder blue")
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=29)
        txtLastName.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, font=(
            "arial", 13, "bold"), text="Address1", fg="Black", padx=2, pady=6, bg="powder blue")
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=29)
        txtAddress1.grid(row=5, column=1)

        lblAddress2 = Label(DataFrameLeft, font=(
            "arial", 13, "bold"), text="Address2", fg="Black", padx=2, pady=6, bg="powder blue")
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=29)
        txtAddress2.grid(row=6, column=1)

        lblPostCode = Label(DataFrameLeft, font=("arial", 12, "bold"),
                            text="Post Code", fg="Black", padx=2, pady=4, bg="powderblue")
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=29)
        txtPostCode.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, font=("arial", 12, "bold"),
                          text="Mobile No", fg="Black", padx=2, pady=6, bg="powderblue")
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=29)
        txtMobile.grid(row=8, column=1)

        lblBookId = Label(DataFrameLeft, font=("arial", 12, "bold"),
                          text="Mobile No", fg="Black", padx=2, pady=6, bg="powderblue")
        lblBookId.grid(row=1, column=2, sticky=W)
        txtBookId = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=29)
        txtBookId.grid(row=1, column=3)

        lblBookTitle = Label(DataFrameLeft, font=("arial", 12, "bold"),
                             text="Book Title", fg="Black", padx=2, pady=6, bg="powderblue")
        lblBookTitle.grid(row=0, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=29)
        txtBookTitle.grid(row=0, column=3)

        lblAuthor = Label(DataFrameLeft, font=("arial", 12, "bold"),
                          text="Book Title", fg="Black", padx=2, pady=6, bg="powderblue")
        lblAuthor.grid(row=2, column=2, sticky=W)
        txtAuthor = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=29)
        txtAuthor.grid(row=2, column=3)

        lblDateBorrow = Label(DataFrameLeft, font=("arial", 12, "bold"),
                              text="Date Borrowed", fg="Black", padx=2, pady=6, bg="powderblue")
        lblDateBorrow.grid(row=3, column=2, sticky=W)
        txtDateBorrow = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=29)
        txtDateBorrow.grid(row=3, column=3)

        lblDueDate = Label(DataFrameLeft, font=("arial", 12, "bold"),
                           text="Due Date", fg="Black", padx=2, pady=6, bg="powderblue")
        lblDueDate.grid(row=4, column=2, sticky=W)
        txtDueDate = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=29)
        txtDueDate.grid(row=4, column=3)

        lblDaysOnBook = Label(DataFrameLeft, font=("arial", 12, "bold"),
                              text="Days On Book", fg="Black", padx=2, pady=6, bg="powderblue")
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=29)
        txtDaysOnBook.grid(row=5, column=3)

        lblLateReturnFine = Label(DataFrameLeft, font=("arial", 12, "bold"),
                                  text="Late Return Fine", fg="Black", padx=2, pady=6, bg="powderblue")
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=29)
        txtLateReturnFine.grid(row=6, column=3)

        lblDateOverdate = Label(DataFrameLeft, font=("arial", 12, "bold"),
                                text="Date Over Due", fg="Black", padx=2, pady=6, bg="powderblue")
        lblDateOverdate.grid(row=7, column=2, sticky=W)
        txtDateOverdate = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=29)
        txtDateOverdate.grid(row=7, column=3)

        lblActualPrice = Label(DataFrameLeft, font=("arial", 12, "bold"),
                               text="Actual Price:", fg="Black", padx=2, pady=6, bg="powderblue")
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=29)
        txtActualPrice.grid(row=8, column=3)

        DataFrameRight = LabelFrame(frame, text="Book Details",
                                    bg="powder blue", fg="Black", bd=20, relief=RIDGE, font=("times new roman", 12, "bold"))
        DataFrameRight.place(x=910, y=5, width=480, height=350)

        self.txtBox = Text(DataFrameRight, font=(
            "arial", 12, "bold"), width=32, background="White",  height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrolbar = Scrollbar(DataFrameRight)
        listScrolbar.grid(row=0, column=1, sticky="ns")

        listBook = ['Chasing Tomorrow', 'Eye Of The Needle', 'The Buisness', 'Intro to Machine Learning',
                    'Linear Algebra', 'Basic Python', 'Differential Calculas', 'Introduction To Programming', 'Deep Learning', 'At The feet of master', 'Freedom from the known', 'The book of life', 'The first and the last freeddom', 'Hands on machine learning', 'Machine learning in python', 'Machine learning in Action', 'Mathematics for machine learning', 'Python for Data Analysis']

        listBox = Listbox(DataFrameRight, font=(
            "arial", 12, "bold"),  width=20, background="White", fg="Black", height=16)
        listBox.grid(row=0, column=0, padx=4)

        listScrolbar.config(command=listBox.yview)

        for item in listBook:
            listBox.insert(END, item)

        # ===========================Buttons Frame ============================
        Framebutton = Frame(self.root, bd=12, relief=RIDGE,
                            padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1530, height=60)

        btnAddData = Button(Framebutton, text="Add Data", font=(
            "arial", 12, "bold"), width=23, bg="blue", fg="Black")

        btnAddData.grid(row=0, column=0)

        btnAddData = Button(Framebutton, text="Show Data", font=(
            "arial", 12, "bold"), width=23, bg="blue", fg="Black")
        btnAddData.grid(row=0, column=1)

        btnAddData = Button(Framebutton, text="Update", font=(
            "arial", 12, "bold"), width=23, bg="blue", fg="Black")
        btnAddData.grid(row=0, column=2)

        btnAddData = Button(Framebutton, text="Delete", font=(
            "arial", 12, "bold"), width=23, bg="blue", fg="Black")
        btnAddData.grid(row=0, column=3)

        btnAddData = Button(Framebutton, text="Reset", font=(
            "arial", 12, "bold"), width=23, bg="blue", fg="Black")
        btnAddData.grid(row=0, column=4)

        btnAddData = Button(Framebutton, text="Exit", font=(
            "arial", 12, "bold"), width=23, bg="blue", fg="Black")
        btnAddData.grid(row=0, column=5)

        # ===========================Informations Frame ============================
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE,
                             padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=590, width=1530, height=210)

        Table_frame = Frame(FrameDetails, bd=6,
                            relief=RIDGE, bg="powder blue")
        Table_frame.place(x=0, y=2, width=1400, height=160)
        self.library_table = ttk.Treeview(Table_frame, column=("membertype", "prno", "title", "firstname", "lastname", "address1", "address2",
                                          "postid", "mobile", "bookid", "booktitle", "author", "dateborrowed", "datedue", "days", "laterreturnfine", "dateoverdue", "finalprice"))

        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("prno", text="Reference No.")
        self.library_table.heading("title", text="Title")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="LastName")
        self.library_table.heading("address1", text="Address1")
        self.library_table.heading("address2", text="Address2")
        self.library_table.heading("postid", text="Post ID")
        self.library_table.heading("mobile", text="Mobile No")
        self.library_table.heading("bookid", text="Book Id")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("dateborrowed", text="Date Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="Days On Book")
        self.library_table.heading("laterreturnfine", text="LateReturnFine")
        self.library_table.heading("dateoverdue", text="DataOverDue")
        self.library_table.heading("finalprice", text="Final Price")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("membertype", width=1000)


if __name__ == "__main__":
    root = Tk()
    obj = LibraryMangementSystem(root)
    root.mainloop()
