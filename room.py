from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk

class RoomBooking:
    def __init__(self , root):
        self.root=root
        self.root.title("Hostel Management System")
        self.root.geometry("1140x480+232+224")

        #============title=========
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("Times new roman",18,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1140,height=50)


        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking  Details",font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=420)

        #=======================labels and Entry=============
        #stu_contact
        label_stu_contact=Label(labelframeleft,text="Student Contact",font=("arial",12,"bold"),padx=2,pady=6)
        label_stu_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
        entry_contact.grid(row=0,column=1)

        #checkin date
        label_CheckInDate=Label(labelframeleft,text="Check In Date",font=("arial",12,"bold"),padx=2,pady=6)
        label_CheckInDate.grid(row=1,column=0,sticky=W)

        txtcheckindate=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtcheckindate.grid(row=1,column=1)

        #CheckOutDate
        label_CheckOutDate=Label(labelframeleft,text="Check Out Date",font=("arial",12,"bold"),padx=2,pady=6)
        label_CheckOutDate.grid(row=2,column=0,sticky=W)

        txtCheckOutDate=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtCheckOutDate.grid(row=2,column=1)

        #Room Type
        label_room_type=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        label_room_type.grid(row=3,column=0,sticky=W)
        combo_room_type=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_room_type["value"]=("Single","Double","Triple")
        combo_room_type.current(0)
        combo_room_type.grid(row=3,column=1)

        #Available Room
        label_Available_room=Label(labelframeleft,text="Available Room :",font=("arial",12,"bold"),padx=2,pady=6)
        label_Available_room.grid(row=4,column=0,sticky=W)

        txt_Available_room=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txt_Available_room.grid(row=4,column=1)

        #meal
        label_meal=Label(labelframeleft,text="Meal",font=("arial",12,"bold"),padx=2,pady=6)
        label_meal.grid(row=5,column=0,sticky=W)

        txtmeal=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtmeal.grid(row=5,column=1)

        #No of Days : 
        label_no_of_days=Label(labelframeleft,text="No of Days : ",font=("arial",12,"bold"),padx=2,pady=6)
        label_no_of_days.grid(row=6,column=0,sticky=W)

        txt_no_of_days=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txt_no_of_days.grid(row=6,column=1)

        #Paid Tax :
        label_nationality=Label(labelframeleft,text="Paid Tax :",font=("arial",12,"bold"),padx=2,pady=6)
        label_nationality.grid(row=7,column=0,sticky=W)

        txt_paid_tax=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txt_paid_tax.grid(row=7,column=1)


        #Sub Total
        label_sub_total=Label(labelframeleft,text="Sub Total",font=("arial",12,"bold"),padx=2,pady=6)
        label_sub_total.grid(row=9,column=0,sticky=W)

        txt_sub_total=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txt_sub_total.grid(row=9,column=1)

        #TotalCost
        labelTotalCost=Label(labelframeleft,text="Total Cost",font=("arial",12,"bold"),padx=2,pady=6)
        labelTotalCost.grid(row=10,column=0,sticky=W)

        txtTotalCost=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtTotalCost.grid(row=10,column=1)

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


if __name__ =="__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop()