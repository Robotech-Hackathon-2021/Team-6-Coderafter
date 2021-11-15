from tkinter import *
from PIL import Image, ImageTk
from room import RoomBooking
from student import Student


class HostelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hostel Management System")
        self.root.geometry("1520x800+0+0")

        #*************** TITLE IMAGE **********************
        img1 = Image.open(r"D:\Robotech - Hackathon\Hostel Management System\img\hostel2.jpg")
        img1 = img1.resize((1520,140), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root, image=self.photoimg1, bd=2, relief=RIDGE)
        lblimg1.place(x=0, y=0, width=1520, height=140)

        #*************** TITLE OF THE PAGE **********************
        lbl_title = Label(self.root, text="HOSTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black", fg="gold", relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1520, height=50) 
       
        #*************** MAIN FRAME **********************
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1520, height=610)

        #*************** MENU **********************
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230) 

        #*************** MENU BUTTON FRAME **********************
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        #*************** BUTTONS IN THE MENU **********************
        stu_btn = Button(btn_frame, text="ADD STUDENT", command=self.stu_details, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        stu_btn.grid(row=0, column=0, pady=1)
        
        room_btn = Button(btn_frame, text="ALLOT ROOM", command=self.room_booking_details, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS", width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="REPORT", width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0, pady=1)

        #*************** IMAGE IN RIGHT FRAME **********************
        img2 = Image.open(r"D:\Robotech - Hackathon\Hostel Management System\img\hostell.jpg")
        img2 = img2.resize((1220,510), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(main_frame, image=self.photoimg2, bd=2, relief=RIDGE)
        lblimg2.place(x=225, y=0, width=1220, height=510)

        #*************** IMAGE IN LOWER LEFT FRAME **********************
        img3 = Image.open(r"D:\Robotech - Hackathon\Hostel Management System\img\hostel5.jpg")
        img3 = img3.resize((225,140), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(main_frame, image=self.photoimg3, bd=2, relief=RIDGE)
        lblimg3.place(x=0, y=225, width=225, height=140)

        img4 = Image.open(r"D:\Robotech - Hackathon\Hostel Management System\img\hostel6.jpeg")
        img4 = img4.resize((225,140), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg4 = Label(main_frame, image=self.photoimg4, bd=2, relief=RIDGE)
        lblimg4.place(x=0, y=365, width=225, height=140)


    def stu_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def room_booking_details(self):
        self.new_window = Toplevel(self.root)
        self.app = RoomBooking(self.new_window)

if __name__== "__main__":
    root = Tk()
    obj = HostelManagementSystem(root)
    root.mainloop()