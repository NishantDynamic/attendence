from tkinter import *
# this is used to make  UI application
from tkinter import ttk 
# for stylish tools
from PIL import Image, ImageTk 
#  this is used for pil(for imort img)
import tkinter 
from student import Student
import os
from time import strftime
from datetime import datetime 
from train import Train
from face_recognize import Face_Recognition
from attendance import Attendance
from help import Help
#  class is a by default
class Face_Recognition_System:
    #  def for calling construction 
    #root is a window name and we have to write self,root 
    def __init__(self, root):

        self.root = root # we are initialing root using self.root
        self.root.geometry("1450x720+0+0") 
        self.root.title("Face Recognition System")
        

        # first image
        img1 = Image.open("shreesid.jpeg")
        # Image.open, this is used for open img path
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        # (500, 130) width or height ANTIALIAS , it will convert high level image to low level image
        self.photoimg1 = ImageTk.PhotoImage(img1)
        # we will store image in variable
        # photoimg1 , this is variable 

        f_lbl = Label(self.root, image=self.photoimg1) 
        f_lbl.place(x=0, y=0, width=500, height=130) # for saving image on window

        # second image
        img2 = Image.open("addwn.jpeg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # third image
        img3 = Image.open("siddang.png")
        img3 = img3.resize((500, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        #background image
        img4 = Image.open("siddang.png")
        
        # img4 = img4.resize((1350, 580), Image.ANTIALIAS)
        img4 = img4.resize((1550, 780), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        # bg_img.place(x=0, y=120, width=1350, height=580)
        bg_img.place(x=0, y=130, width=1550, height=780)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE ",
                          font=("Algerian", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1550, height=45)  # using .place u can place things at any part of the window

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        # different buttons with images
        # student button
        img5 = Image.open("sbutm.jpg")
        img5 = img5.resize((195, 195), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        btn1 = Button(bg_img, image=self.photoimg5, command=self.student_details, cursor="hand2") # this is for converting image to image button
        btn1.place(x=100, y=80, width=195, height=195)

        btn1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        btn1_1.place(x=100, y=245, width=195, height=40)


        # Face Detection button
        img6 = Image.open("facdecbut.jpg")
        img6 = img6.resize((195, 195), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        btn2 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.face_data)
        btn2.place(x=400, y=80, width=195, height=195)

        btn2_2 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data,font=("times new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        btn2_2.place(x=400, y=245, width=195, height=40)

        # attendance button
        img7 = Image.open("atenden.jpg")
        img7 = img7.resize((195, 195), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        btn3 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.attendance_data)
        btn3.place(x=700, y=80, width=195, height=195)

        btn3_3 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_data, font=("times new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        btn3_3.place(x=700, y=245, width=195, height=40)

        
        # train data button
        img9 = Image.open("trainbtn.jpg")
        img9 = img9.resize((195, 195), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        btn5 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.train_data)
        btn5.place(x=100, y=350, width=195, height=195)

        btn5_5 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        btn5_5.place(x=100, y=525, width=195, height=40)

        # Photos button
        img10 = Image.open("facdepho.jpg")
        img10 = img10.resize((195, 195), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        btn6 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.open_img)
        btn6.place(x=400, y=350, width=195, height=195)

        btn6_6 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img,font=("times new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        btn6_6.place(x=400, y=525, width=195, height=40)

         # Exit button
        img11 = Image.open("exitbtn.jpg")
        img11 = img11.resize((195, 195), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        btn7 = Button(bg_img, image=self.photoimg11, cursor="hand2",command=self.iExit)
        btn7.place(x=700, y=350, width=195, height=195)

        btn7_7 = Button(bg_img, text="Exit", cursor="hand2",command=self.iExit, font=("times new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        btn7_7.place(x=700, y=525, width=195, height=40)

        

    def open_img(self):
        os.startfile("datasample")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return




    # # # =================================== Functions buttons=========================================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)
    
    
    

        
        



# defining object
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()