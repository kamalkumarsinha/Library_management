from tkinter import *
from tkinter import ttk


class LibraryMangementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Mangement System")
        self.root.geometry("1550x800+0+0")

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

        lblPostCode = Label(DataFrameLeft, font=(
            "arial", 13, "bold"), text="Post Code", padx=2, pady=4, bg="powder blue")

        DataFrameRight = LabelFrame(frame, text="Book Details",
                                    bg="powder blue", fg="Black", bd=20, relief=RIDGE, font=("times new roman", 12, "bold"))
        DataFrameRight.place(x=910, y=5, width=480, height=350)

        # ===========================Buttons Frame ============================
        Framebutton = Frame(self.root, bd=12, relief=RIDGE,
                            padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1530, height=700)
        # ===========================Informations Frame ============================
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE,
                             padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=600, width=1530, height=195)

        # ===========================Buttons Frame ============================
        # Framebutton = Frame(self.root, bd=12, relief=RIDGE,
        #                     padx=20, bg="powder blue")
        # Framebutton.place(x=0, y=530, width=1530, height=195)


if __name__ == "__main__":
    root = Tk()
    obj = LibraryMangementSystem(root)
    root.mainloop()
