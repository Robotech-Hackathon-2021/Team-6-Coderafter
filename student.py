from os import lstat
from tkinter import *
from tkinter import ttk
from tkinter import font
import random
#import mysql.connector

class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Hostel Management System")
        self.root.geometry("1140x480+232+224")


        #*************** VARIABLES **********************
        self.var_ref = StringVar()
        x = random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_name = StringVar()
        self.var_father = StringVar()
        self.var_gender = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_state = StringVar()
        self.var_pincode = StringVar()
        self.var_idproof = StringVar()
        self.var_idnumber = StringVar()


        #*************** TITLE OF THE PAGE **********************
        lbl_title = Label(self.root, text="ADD STUDENT DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1140, height=50) 

        #*************** LABEL FRAME **********************
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="STUDENT DETAILS", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=420)

        #*************** ENTRIES IN THE LABEL **********************
            # stu_ref
        lbl_stu_ref = Label(labelframeleft, text="Reference No. :", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_stu_ref.grid(row=0, column=0, sticky=W)
        entry_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref, font=("arial", 13, "bold"), width=29, state="readonly")
        entry_ref.grid(row=0, column=1)

            # stu_name
        lbl_stu_name = Label(labelframeleft, text="Student Name :", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_stu_name.grid(row=1, column=0, sticky=W)
        entry_name = ttk.Entry(labelframeleft, textvariable=self.var_name, font=("arial", 13, "bold"), width=29)
        entry_name.grid(row=1, column=1)

            # father_name
        lbl_fath_name = Label(labelframeleft, text="Father's Name :", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_fath_name.grid(row=2, column=0, sticky=W)
        entry_fath = ttk.Entry(labelframeleft, textvariable=self.var_father, font=("arial", 13, "bold"), width=29)
        entry_fath.grid(row=2, column=1)

            # gender 
        lbl_gender = Label(labelframeleft, text="Gender :", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_gender.grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(labelframeleft, textvariable=self.var_gender, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_gender["value"] = ("Select One", "Male", "Female", "Others")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

            # mobile_number
        lbl_mobile = Label(labelframeleft, text="Mobile :", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_mobile.grid(row=4, column=0, sticky=W)
        entry_mobile = ttk.Entry(labelframeleft, textvariable=self.var_mobile, font=("arial", 13, "bold"), width=29)
        entry_mobile.grid(row=4, column=1)

            # email
        lbl_email = Label(labelframeleft, text="Email :", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_email.grid(row=5, column=0, sticky=W)
        entry_email = ttk.Entry(labelframeleft, textvariable=self.var_email, font=("arial", 13, "bold"), width=29)
        entry_email.grid(row=5, column=1)

            # address
        lbl_address = Label(labelframeleft, text="Address :", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_address.grid(row=6, column=0, sticky=W)
        entry_address = ttk.Entry(labelframeleft, textvariable=self.var_address, font=("arial", 13, "bold"), width=29)
        entry_address.grid(row=6, column=1)

            # state
        lbl_state = Label(labelframeleft, text="State :", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_state.grid(row=7, column=0, sticky=W)
        combo_state = ttk.Combobox(labelframeleft, textvariable=self.var_state, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_state["value"] = ("Select One", "Andaman and Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chandigarh", "Chhattisgarh", "Dadra and Nagar Haveli and Daman & Diu", "Delhi", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu & Kashmir", "Jharkhand", "Karnataka", "Kerala", "Ladakh", "Lakshadweep", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Puducherry", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttarakhand", "Uttar Pradesh", "West Bengal")
        combo_state.current(0)
        combo_state.grid(row=7, column=1)

            # pincode
        lbl_pincode = Label(labelframeleft, text="Pin Code :", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_pincode.grid(row=8, column=0, sticky=W)
        entry_pincode = ttk.Entry(labelframeleft, textvariable=self.var_pincode, font=("arial", 13, "bold"), width=29)
        entry_pincode.grid(row=8, column=1)

            # id_proof
        lbl_idproof = Label(labelframeleft, text="ID Proof Type :", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_idproof.grid(row=9, column=0, sticky=W)
        combo_idproof = ttk.Combobox(labelframeleft, textvariable=self.var_idproof, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_idproof["value"] = ("Aadhar Card", "Passport", "Voter ID Card", "PAN Card", "Driving License")
        combo_idproof.current(0)
        combo_idproof.grid(row=9, column=1)

            # id_number
        lbl_idnumber = Label(labelframeleft, text="ID Number :", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_idnumber.grid(row=10, column=0, sticky=W)
        entry_idnumber = ttk.Entry(labelframeleft, textvariable=self.var_idnumber, font=("arial", 13, "bold"), width=29)
        entry_idnumber.grid(row=10, column=1)

        #*************** BUTTONS **********************
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=350, width=410, height=37)

        btnAdd = Button(btn_frame, text="ADD", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="UPDATE", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="DELETE", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="RESET", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        #*************** TABLE FRAME **********************
        tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="VIEW DETAILS", font=("times new roman", 12, "bold"), padx=2)
        tableframe.place(x=435, y=50, width=700, height=420)

        lbl_search = Label(tableframe, text="Search By :", font=("arial", 11, "bold"), bg="red", fg="white")
        lbl_search.grid(row=0, column=0, sticky=W, padx=3)

        combo_search = ttk.Combobox(tableframe, font=("arial", 11, "bold"), width=16, state="readonly")
        combo_search["value"] = ("Reference No.", "Name", "Mobile")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=3)

        txt_search = ttk.Entry(tableframe, font=("arial", 11, "bold"), width=26)
        txt_search.grid(row=0, column=2, padx=3)

        btn_search = Button(tableframe, text="SEARCH", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btn_search.grid(row=0, column=3, padx=3)

        btn_showall = Button(tableframe, text="SHOW ALL", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btn_showall.grid(row=0, column=4, padx=3)

        #*************** DATA TABLE **********************
        data_table = Frame(tableframe, bd=2, relief=RIDGE)
        data_table.place(x=0, y=50, width=682, height=300)

        scroll_x = ttk.Scrollbar(data_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(data_table, orient=VERTICAL)

        self.Stud_Data_Table = ttk.Treeview(data_table, column=("ref", "name", "father", "gender", "mobile", "email", "address", "state", "pincode", "idproof", "idnumber"))

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Stud_Data_Table.xview)
        scroll_y.config(command=self.Stud_Data_Table.yview)

        self.Stud_Data_Table.heading("ref", text="Reference No.")
        self.Stud_Data_Table.heading("name", text="Name")
        self.Stud_Data_Table.heading("father", text="Father's Name")
        self.Stud_Data_Table.heading("gender", text="Gender")
        self.Stud_Data_Table.heading("mobile", text="Mobile")
        self.Stud_Data_Table.heading("email", text="Email")
        self.Stud_Data_Table.heading("address", text="Address")
        self.Stud_Data_Table.heading("state", text="State")
        self.Stud_Data_Table.heading("pincode", text="Pincode")
        self.Stud_Data_Table.heading("idproof", text="Id Proof")
        self.Stud_Data_Table.heading("idnumber", text="Id Number")

        self.Stud_Data_Table["show"] = "headings"

        self.Stud_Data_Table.column("ref", width=100) 
        self.Stud_Data_Table.column("name", width=100)
        self.Stud_Data_Table.column("father", width=100) 
        self.Stud_Data_Table.column("gender", width=100) 
        self.Stud_Data_Table.column("mobile", width=100) 
        self.Stud_Data_Table.column("email", width=100)
        self.Stud_Data_Table.column("address", width=100) 
        self.Stud_Data_Table.column("state", width=100) 
        self.Stud_Data_Table.column("pincode", width=100) 
        self.Stud_Data_Table.column("idproof", width=100) 
        self.Stud_Data_Table.column("idnumber", width=100) 

        self.Stud_Data_Table.pack(fill=BOTH, expand=1)




if __name__== "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()