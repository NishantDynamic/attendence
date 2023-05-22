
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        

        ##### Variables  #####
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_searchtxt=StringVar()
        self.var_search=StringVar()

        # first image
        img1 = Image.open("shreesid.jpeg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=500, height=130)

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
        bg_img.place(x=0, y=120, width=1550, height=780)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT ",
                          font=("Algerian", 35, "bold"), bg="blue", fg="white")
        title_lbl.place(x=0, y=0, width=1550, height=45)  # using .place u can place things at any part of the window

        main_frame=Frame(bg_img,bd=2,bg="white",)
        main_frame.place(x=20,y=35,width=1480,height=600)

        # left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=5,y=5,width=740,height=600)

        img_left=Image.open("stufpic.png")
        #img_left = Image.open(r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\Images\re1.jpg")
        #img_left = Image.open("Images/NCIT.png")
        img_left = img_left.resize((660,100),Image.ANTIALIAS)  #Antialias lea high level image lai low level mah convert garxa
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5, y=0,width=660,height=100)

        #current course information
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=669,height=150)

        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)


        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly",width=18)
        dep_combo["values"]=("Select Department","Computer Science and Engineering","Information Science And Engnieering","Electronics and telecommunication engineering","Electronics and Communication")
        dep_combo.current(0)
        # current 0 is first section 
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        # grid used for row and column and padx for gapping
        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=18)
        course_combo["values"]=("Select Course","Machine learning","Artifical Intelligence","Data Communication & Coding Theory","Digital Electronics","Data Structure and Algorithm","Operating System","Computer Networks")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        #sticky w used for grid

        #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=18)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly",width=18)
        # semester_combo["values"]=("Select Semester","Semester-I","Semester-II","Semester-III","Semester-IV","Semester-V","Semester-VI","Semester-VII","Semester-VIII")
        semester_combo["values"]=("Select Semester","Semester-I","Semester-III","Semester-V","Semester-VII")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        #class student information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=260,width=669,height=500)

        #studen ID 
        studentId_label=Label(class_student_frame,text="StudentID:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=18,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,sticky=W)

        
        #student name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=18,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),state="readonly",width=16)
        div_combo["values"]=("Select Division","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        #roll_no
        roll_no_label=Label(class_student_frame,text="USN:",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=18,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        

        #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=16)
        gender_combo["values"]=("Select Gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)


        #DOB
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=18,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        
        #Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=18,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)



        email=Label(class_student_frame,text="*ex123@gmail.com",font=("times new roman",6,"bold"),fg="red",bg="white")
        # pswd.grid(row=8,column=1,padx=5,pady=5,sticky=W)
        email.place(x=150, y=149)


        




        #Phone no
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=18,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)



        
    
   

        #Address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=18,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        

        
         #Teacher Name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=18,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)



        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="NO")
        radiobtn2.grid(row=6,column=1)



        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=215,width=668,height=80)
        


        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=245,width=669,height=80)
        
        
        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)


        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)




      
    
    

        

 



        #Right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",17,"bold"))
        right_frame.place(x=750,y=5,width=700,height=580)

        # img_right=Image.open(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Images\NCIT.jpg")
        # img_right = Image.open(r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\Images\re1.jpg")
        img_right = Image.open("birla.jpg")
        img_right = img_right.resize((650,75),Image.ANTIALIAS)  #Antialias lea high level image lai low level mah convert garxa
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5, y=0,width=700,height=105)


        #Search System
       
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=669,height=349)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,textvariable=self.var_search,font=("times new roman",13,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll""Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=17,pady=10,sticky=W)



        search_btn=Button(search_frame,text="Search",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=17)

        showAll_btn=Button(search_frame,text="Show All",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=17)

        #Table frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=349)

        #scroll bar 
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="USN")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #==============function decleration ===========#
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="" or  self.var_course.get()=="Select Course" or self.var_semester.get()=="Select Semester" or self.var_gender.get()=="Select Gender":
            #speak_va("Alert!!! All Fields are Mandatory.")
            messagebox.showerror("Error", "All fields Are Required",parent=self.root)
        else:
            try:
                # conn=mysql.connector.connect(host="localhost",username="root",password="Keshav@123",database="mydata")
                conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                
                                                                                                                self.var_dep.get(),
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
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()


                                                                                                             ))
                conn.commit()
                self.fetch_data()
                conn.close()
                #commit for updating data and 
                messagebox.showinfo("Success","Student details has been added Sucessfully",parent=self.root)
            except Exception as es:
                #
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    ######======Fetch data ==============#####
    def fetch_data(self):
        
        conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close() 
        #  my_cursor.execute("select * from student") this execute for query


        #=================== get cursor ======================#
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])  

        #============= Update function =========================

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            #speak_va('Alert!!! All fields are required.')
            messagebox.showerror("Error", "All fields Are Required",parent=self.root)

        else:
            try:
                #speak_va("Do you want to Update this Student's Details?")
                Upadate = messagebox.askyesno("Upadate","Do You Want To Update This Student Details",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="face_recognizer")
                    # conn=mysql.connector.connect(host="localhost",username="root",password="Keshav@123",database="mydata")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Rool=%s,Gender=%s,Dob=%s,Email=%s,phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where student_ID=%s",(

                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        int(self.var_std_id.get())
                                                                                                                                                                                    ))   
                
                
                else:
                    if not Upadate:
                        return
                #speak_va('Student Details updated successfully.')
                messagebox.showinfo("Success","Student Details updated Successfully.",parent=self.root)                                                                                                                                              
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                #speak_va('An Exception Occurred!')
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

                # ===================Delete Function===================
    def delete_data(self):
        if self.var_std_id.get()=="":
            # speak_va('Student ID is mandatory')
            messagebox.showerror("Error","student_ID Must be Required",parent=self.root)
        else:
            try:
                #speak_va("Do you want to Delete this Student's Details?")
                delete=messagebox.askyesno("Student Delete Page","Do You Want To Delete This Student Details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="face_recognizer")
                    # conn=mysql.connector.connect(host="localhost",username="root",password="Keshav@123",database="mydata")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_ID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)

                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                #speak_va('Student Details deleted successfully.')
                messagebox.showinfo("Delete","Student Details Successfully deleted",parent=self.root)

            except Exception as es:
                #speak_va('An exception occurred!')
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

                #============Reset Function =============================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

        # ..............Generate data set or take photo sample

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            #speak_va('All Fields are mandatory.')
            messagebox.showerror("Error", "All fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="face_recognizer")
                # conn=mysql.connector.connect(host="localhost",username="root",password="Keshav@123",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set student_ID=%s ,Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Rool=%s,Gender=%s,Dob=%s,Email=%s,phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where student_ID=%s",(
                                                                                                                                                                                        id,
                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_std_id.get()
                                                                                                                                                                                    ))   
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                 # ..................load predefined data  face forntal from opencv.............
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)


                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)

                
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face =cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        # file_name_path="data/"+str(self.var_roll.get())+"."+str(id)+"."+str(img_id)+".jpg"
                        # file_name_path="data/"+str(Roll)+"."+str(id)+"."+str(img_id)+".jpg"
                        file_name_path="datasample/"+"user"+"."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==40:
                        break
                cap.release()
                cv2.destroyAllWindows()
                

                #speak_va("Generation of Data Set completed.")
                messagebox.showinfo("Result","Generation of datasample set completed!!!",parent=self.root)
            except Exception as es:
                #speak_va("An Exception occurred")
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



     
        
        
        



        
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()