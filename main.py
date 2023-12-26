from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import qrcode
from resizeimage import resizeimage
from fpdf import FPDF
from tkinter import messagebox
import mysql.connector
from tkcalendar import DateEntry
import re


class Login:
    def __init__(self,master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("1530x850+0+0")
        self.master.configure(bg="lightblue")
        self.master.resizable(False, False)

        lblTitle=Label(self.master,text="Login",font=("times new roman",30,"bold"),fg="black",bg="white")
        lblTitle.place(x=700,y=100)

        mainframe=Frame(self.master,bg="white",width=1000,height=400)
        mainframe.place(x=280,y=150)

        self.logging = StringVar()
        self.passwording = StringVar()

        # Creating labels and entry widgets for username and password
        self.label_username = Label(mainframe, text="Username:",width=12,bd=2,font=("times new roman",20,"bold"),bg="white")
        self.label_username.place(x=250,y=45)
        
        self.entry_username = Entry(mainframe,textvariable=self.logging,width=12,bd=2,font=("times new roman",20,"bold"),relief=RIDGE)
        self.entry_username.place(x=420,y=50)

        self.label_password = Label(mainframe,text="Password:",width=12,bd=2,font=("times new roman",20,"bold"),bg="white")
        self.label_password.place(x=250,y=98)

        self.entry_password = Entry(mainframe,textvariable=self.passwording,width=12,bd=2,font=("times new roman",20,"bold"),relief=RIDGE,show="*")
        self.entry_password.place(x=420,y=100)

        # Creating login and reset buttons
        self.button_login = Button(mainframe, text="Login",font=("times new roman",18,"bold"),width="8",height="2",bg="black",fg="white",bd=0,command=self.login)
        self.button_login.place(x=280,y=250)

        self.button_reset = Button(mainframe, text="Reset",font=("times new roman",18,"bold"),width="8",height="2",bg="black",fg="white",bd=0,command=self.reset)
        self.button_reset.place(x=430,y=250)

        self.button_exit = Button(mainframe, text="Exit",font=("times new roman",18,"bold"),width="8",height="2",bg="black",fg="white",bd=0,command=self.exit)
        self.button_exit.place(x=590,y=250)

    def login(self):
        # checking the username and password entered by the user
        username = self.entry_username.get()
        password = self.entry_password.get()

# -----------------------------Login if-else condition------------------------------------------------------------
        
        # Checking if the username and password are correct
        
        if (username == "meet" and password == "1234"):
            messagebox.showinfo("Success", "Login successful!")

            conn = mysql.connector.connect(host="localhost",
                                           username="root",
                                           password="1234",
                                           database="mypharmacy",
                                           port="3307")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into mypharmacy.hello values(%s,%s)",(
                self.logging.get(),self.passwording.get()
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted.")

            self.open_firstpage_window()

        elif(username == "mitul" and password=="1033"):
            messagebox.showinfo("success","Login successfull")

            conn = mysql.connector.connect(host="localhost",
                                           username="root",
                                           password="1234",
                                           database="mypharmacy",
                                           port="3307")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into hello values(%s,%s)",(
                self.logging.get(),self.passwording.get()
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted.")

            self.open_firstpage_window()

        elif(username == "mohit" and password=="1036"):
            messagebox.showinfo("success","Login successfull")

            conn = mysql.connector.connect(host="localhost",
                                           username="root",
                                           password="1234",
                                           database="mypharmacy",
                                           port="3307")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into hello values(%s,%s)",(
                self.logging.get(),self.passwording.get()
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted.")

            self.open_firstpage_window()

        elif(username=="" and password==""):
            messagebox.showerror("Invalid","Please enter the username and password")
        elif(username==""):
            messagebox.showerror("Invalid","Please enter valid username")
        elif(password==""):
            messagebox.showerror("Invalid","Please enter valid password")
        elif(username!="meet" and password!="1234"):
            messagebox.showerror("Invalid","Invalid username and password")
        elif(username!="mitul" and password!="1033"):
            messagebox.showerror("Invalid","Invalid username and password")
        elif(username!="mohit" and password!="1036"):
            messagebox.showerror("Invalid","Invalid username and password")
        elif(password!="meet"):
            messagebox.showerror("Invalid","Please enter a valid username")
        elif(password!="1234"):
            messagebox.showerror("Invalid","Please enter a valid password")
        elif(password!="mitul"):
            messagebox.showerror("Invalid","Please enter a valid username")
        elif(password!="1033"):
            messagebox.showerror("Invalid","Please enter a valid password")
        elif(password!="mohit"):
            messagebox.showerror("Invalid","Please enter a valid username")
        elif(password!="1036"):
            messagebox.showerror("Invalid","Please enter a valid password")
            # If login is successful, then close the login window
            # self.master.destroy()
        else:
            messagebox.showerror("Error", "Invalid username or password.\nPlease try again.")

        self.master.mainloop()

    def reset(self):
        # Clearing the entered username and password
        self.entry_username.delete(0, END)
        self.entry_password.delete(0, END)

    def exit(self):
        if messagebox.askyesno("Exit","Do you really want to exit?"):
            self.master.destroy()

# class PharmacyManagementSystem:
    def open_firstpage_window(self):

        # def __init__(self,root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1530x850+0+0")

        lbltitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,bg="white",fg="darkgreen",
                    font=("times new roman",50,"bold"),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill=X)

        # self.var_ref_no=StringVar()
        # self.var_name=StringVar()
        # self.var_department=StringVar()
        # self.var_designation=StringVar()

        self.var_ref_no=StringVar()
        self.var_com_name=StringVar()
        self.var_type_of_med=StringVar()
        self.var_med_name=StringVar()
        self.var_batch_no=StringVar()
        self.var_manufactured_date=StringVar()
        self.var_expiry_date=StringVar()
        self.var_uses=StringVar()
        self.var_tablet_price=IntVar()
        self.var_product_qt=IntVar()

        # self.referencing = StringVar()
        self.companying = StringVar()
        self.typingofmedicing = StringVar()
        self.medicinenaming = StringVar()
        self.batching = StringVar()
        self.manufactureding = StringVar()
        self.expiring = IntVar()
        self.useing = IntVar()


        img1=Image.open("logo image file path")
        img1=img1.resize((70,70),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=80,y=18)

        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=18)
        DataFrame.place(x=0,y=114,width=1530,height=850)
        
        DataFrameLeft=LabelFrame(DataFrame,text="Medicine Information",bd=10,relief=RIDGE,bg="white",fg="darkgreen",
                     font=("times new roman",20,"bold"),padx=18)
        DataFrameLeft.place(x=0,y=5,width=900,height=400)

        self.lbl_ref_no=Label(DataFrameLeft,font=("times new roman",17,"bold"),text="Reference No :",padx=2,bg="white")
        self.lbl_ref_no.grid(row=0,column=0,sticky=W) 

        self.ref_combo=ttk.Combobox(DataFrameLeft,textvariable=self.var_ref_no,width=18,font=("times new roman",15,"bold"),state="readonly")
        self.ref_combo["values"]=[1,2,3,4,5,6,7,8,9,10]
        self.ref_combo.grid(row=0,column=1)

        self.lbl_comp=Label(DataFrameLeft,font=("times new roman",17,"bold"),text="Company Name:",padx=2,bg="white")
        self.lbl_comp.grid(row=1,column=0,sticky=W)

        self.comp_combo=ttk.Combobox(DataFrameLeft,textvariable=self.var_com_name,width=18,font=("times new roman",15,"bold"),state="readonly")
        self.comp_combo["values"]=["UNISON PHARMACEUTICAL","SUN PHARMACEUTICAL","CIPLA PHARMACEUTICAL","LUPIN PHARMACEUTICAL"]
        self.comp_combo.grid(row=1,column=1)
        
        self.lbl_type=Label(DataFrameLeft,font=("times new roman",17,"bold"),text="Type Of Medicine:",padx=2,bg="white")
        self.lbl_type.grid(row=2,column=0,sticky=W)

        self.type_medicine_combo=ttk.Combobox(DataFrameLeft,textvariable=self.var_type_of_med,width=18,font=("times new roman",15,"bold"),state="readonly")
        self.type_medicine_combo["values"]=("Tablet","Syrup","Injection","Ointment")
        self.type_medicine_combo.grid(row=2,column=1)
        
        self.lbl_med=Label(DataFrameLeft,font=("times new roman",17,"bold"),text="Medicine Name:",padx=2,bg="white")
        self.lbl_med.grid(row=3,column=0,sticky=W)

        self.med_combo=ttk.Combobox(DataFrameLeft,textvariable=self.var_med_name,width=18,font=("times new roman",15,"bold"),state="readonly")
        self.med_combo["values"]=["Azithromycin","Advil","Paraceutamol","Tynol","Moxitak"]
        self.med_combo.grid(row=3,column=1)
        
        self.lbl_lotno=Label(DataFrameLeft,font=("times new roman",17,"bold"),text="Batch No:",padx=2,pady=6,bg="white")
        self.lbl_lotno.grid(row=4,column=0,sticky=W)

        self.lotno_combo=ttk.Combobox(DataFrameLeft,textvariable=self.var_batch_no,width=18,font=("times new roman",15,"bold"),state="readonly")
        self.lotno_combo["values"]=[220610471,878454717,788452015,885453267,457820349]
        self.lotno_combo.grid(row=4,column=1)
        
        self.lbl_manu_issue=Label(DataFrameLeft,font=("times new roman",17,"bold"),text="Manufactured Date:",padx=2,bg="white")
        self.lbl_manu_issue.grid(row=0,column=7,sticky=W)

        self.entry_issue=DateEntry(DataFrameLeft,textvariable=self.var_manufactured_date,width=20,
                                   font=("times new roman",15,"bold"),bd=2,relief=RIDGE,state="readonly")
        self.entry_issue.grid(row=0,column=9)
        
        self.lbl_exp=Label(DataFrameLeft,font=("times new roman",17,"bold"),text="Expiry Date:",padx=2,pady=6,bg="white")
        self.lbl_exp.grid(row=1,column=7,sticky=W)

        self.entry_expiry=DateEntry(DataFrameLeft,textvariable=self.var_expiry_date,width=20,
                                    font=("times new roman",15,"bold"),bd=2,relief=RIDGE,state="readonly")
        self.entry_expiry.grid(row=1,column=9)
        
        self.lbl_use=Label(DataFrameLeft,font=("times new roman",17,"bold"),text="Uses:",padx=2,pady=6,bg="white")
        self.lbl_use.grid(row=2,column=7,sticky=W)

        self.use_combo=ttk.Combobox(DataFrameLeft,textvariable=self.var_uses,width=20,font=("times new roman",15,"bold"),state="readonly")
        self.use_combo["values"]=["cold","fever","skin"]
        self.use_combo.grid(row=2,column=9)
        
        self.lbl_Tablets_Price=Label(DataFrameLeft,font=("times new roman",17,"bold"),text="Tablet Price :",
                                     padx=2,pady=6,bg="white")
        self.lbl_Tablets_Price.grid(row=3,column=7,sticky=W)

        self.tablet_combo=ttk.Combobox(DataFrameLeft,textvariable=self.var_tablet_price,width=20,font=("times new roman",15,"bold"),state="readonly")
        self.tablet_combo["values"]=[10,20,50,100]
        self.tablet_combo.grid(row=3,column=9)
        
        self.lbl_Product_QT=Label(DataFrameLeft,font=("times new roman",17,"bold"),text="Product QT :",padx=2,pady=6,bg="white")
        self.lbl_Product_QT.grid(row=4,column=7,sticky=W)

        self.product_QT_combo=ttk.Combobox(DataFrameLeft,textvariable=self.var_product_qt,width=20,font=("times new roman",15,"bold"),state="readonly")
        self.product_QT_combo["values"]=[1,2,3,4,5]
        self.product_QT_combo.grid(row=4,column=9)

        self.button_generate=Button(DataFrameLeft,text="GENERATE QR",command=self.generate,
                                    font=("times new roman",21,"bold"),bg="lightblue",fg="darkred")
        self.button_generate.place(x=230,y=240,width=230,height=35)

        self.button_delete=Button(DataFrameLeft,text="CLEAR",command=self.clear,
                                  font=("times new roman",21,"bold"),bg="red",fg="white")
        self.button_delete.place(x=480,y=240,width=120,height=35)

        self.button_clear=Button(DataFrameLeft,text="NEXT",command=self.next,
                                 font=("times new roman",21,"bold"),bg="orange",fg="green")
        self.button_clear.place(x=620,y=240,width=120,height=35)

        self.msg="QR Code Successfully"
        self.lbl_msg=Label(DataFrameLeft,text=self.msg,font=("times new roman",20,"bold"),bg="white",fg="green")
        self.lbl_msg.place(x=0,y=310,relwidth=1)

#---------------here right side showing--------------------------------------------------------

        DataFrameRight=LabelFrame(DataFrame,text="QR Code Status",bd=10,relief=RIDGE,bg="white",fg="darkgreen",
                     font=("times new roman",20,"bold"),padx=10)
        DataFrameRight.place(x=920,y=5,width=550,height=400)

        self.qr_code=Label(DataFrameRight,text="No Qr\nAvailable",font=("times new roman",20,"bold"),bg="light green",fg="white",bd=1,relief=RIDGE)
        self.qr_code.place(x=170,y=90,width=180,height=180)


        
        img2=Image.open("medicine-tablets image file path")
        img2=img2.resize((314,213),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=40,y=580)


        img3=Image.open("medicine-syrup image file path")
        img3=img3.resize((330,213),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(self.root,image=self.photoimg3,borderwidth=0)
        b1.place(x=382,y=580)


        img4=Image.open("medicine-injection image file path")
        img4=img4.resize((340,213),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=742,y=580)


        img5=Image.open("medicine-ointment image file path")
        img5=img5.resize((350,213),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(self.root,image=self.photoimg5,borderwidth=0)
        b1.place(x=1115,y=580)
        

    def clear(self):
        self.var_ref_no.set('')
        self.var_com_name.set('')
        self.var_type_of_med.set('')
        self.var_med_name.set('')
        self.var_batch_no.set('')
        self.var_manufactured_date.set('')
        self.var_expiry_date.set('')
        self.var_uses.set('')
        # self.var_tablet_price.set('')
        # self.var_product_qt.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

    def generate(self):
        if(self.var_ref_no.get()=='' or self.var_com_name.get()=='' or self.var_type_of_med.get()=='' or 
           self.var_med_name.get()=='' or self.var_batch_no.get()=='' or self.var_manufactured_date.get()=='' or
           self.var_expiry_date.get()=='' or self.var_uses.get()=='' or self.var_tablet_price.get()=='' or self.var_product_qt.get()==''):
            
            self.msg='All fields are required!!!'
            self.lbl_msg.config(text=self.msg,fg='red')
        
        else:
            qr_data=(f"Reference No: {self.var_ref_no.get()}\nCompany Name: {self.var_com_name.get()}\nType Of Medicine: {self.var_type_of_med.get()}\nMedicine Name: {self.var_med_name.get()}\nBatch No: {self.var_batch_no.get()}\nManufactured Date: {self.var_manufactured_date.get()}\nExpiry Date: {self.var_expiry_date.get()}\nUses: {self.var_uses.get()}\nTablet Price: {self.var_tablet_price.get()}\nProduct QT: {self.var_product_qt.get()}\n")
            qr_code=qrcode.make(qr_data)
            print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("qr_code_generate/Med_"+str(self.var_ref_no.get())+'.png')

            self.im=ImageTk.PhotoImage(file="qr_code_generate/Med_"+str(self.var_ref_no.get())+'.png')
            self.qr_code.config(image=self.im)
# #-------------------------------------------------------------------------------------------------------------------------------------
            self.msg='Qr Code Generated successfully'
            self.lbl_msg.config(text=self.msg,fg='green')

            conn = mysql.connector.connect(host="localhost",
                                           username="root",
                                           password="1234",
                                           database="mypharmacy",
                                           port="3307")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into mypharmacy.swayam values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                # self.referencing.get(),self.companying.get(),
                # self.typingofmedicing.get(),self.medicinenaming.get(),
                # self.batching.get(),self.manufactureding.get(),
                # self.expiring.get(),self.useing.get(),
                # self.tableting.get(),self.producting.get()

                self.ref_combo.get(),self.comp_combo.get(),
                self.type_medicine_combo.get(),self.med_combo.get(),
                self.lotno_combo.get(),self.entry_issue.get(),
                self.entry_expiry.get(),self.use_combo.get(),
                self.var_tablet_price.get(),self.var_product_qt.get()
            ))

            conn.commit()

            self.fetch_data()

            conn.close()
            messagebox.showinfo("Success","Record has been inserting.")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",
                                           username="root",
                                           password="1234",
                                           database="mypharmacy",
                                           port="3307")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from mypharmacy.swayam")
        rows = my_cursor.fetchall()

        if len(rows)!=0:
            self.table.delete(* self.table.get_children())
            for items in rows:
                self.table.insert('',END,values=items)
            conn.commit()
        conn.close()

    def get_data(self,event=''):
        cursor_row = self.table.focus()
        data = self.table.item(cursor_row)
        row = data['values']

        self.ref_combo.set(row[0])
        self.comp_combo.set(row[1])
        self.type_medicine_combo.set(row[2])
        self.med_combo.set(row[3])
        self.lotno_combo.set(row[4])
        self.entry_issue.set_date(row[5])
        self.entry_expiry.set_date(row[6])
        self.use_combo.set(row[7])
        self.tablet_combo.set(row[8])
        self.product_QT_combo.set(row[9])


    def next(self):
        if(self.ref_combo.get()=='' or self.comp_combo.get()=='' or self.type_medicine_combo.get()=='' or 
           self.med_combo.get()=='' or self.lotno_combo.get()=='' or self.entry_issue.get()=='' or
           self.entry_expiry.get()=='' or self.use_combo.get()=='' or self.var_tablet_price.get()=='' or 
           self.var_product_qt.get()==''):
            
            self.msg='All fields are required!!!'
            self.lbl_msg.config(text=self.msg,fg='red')

        elif(self.open_thirdpage_window()):
            pass

    def open_thirdpage_window(self):
        self.next_window=Tk()
        self.next_window.title("Invoice")
        self.next_window.geometry("1530x850+0+0")
        # self.next_window.configure("lightblue")

        DataFrame=Frame(self.next_window,relief=RIDGE,bd=4)
        DataFrame.place(x=0,y=0,width=1527,height=780)

        DataFrameTop_up=Frame(DataFrame,relief=RIDGE,bd=3)
        DataFrameTop_up.place(x=2,y=2,width=395,height=130)

# --------------------------------for swami pharmacy box only--------------------------------------------------------------

        self.pharmacy_name=Label(DataFrameTop_up,text="Swami Pharmacy",font=("arial",18,"bold"),bg="lightgreen",fg="red")
        self.pharmacy_name.grid(row=0,column=0)

        self.road_name=Label(DataFrameTop_up,text="ABC Road,OPP.Hanuman Temple,Anand",font=("arial",15,))
        self.road_name.grid(row=1,column=0)

        self.phone_no=Label(DataFrameTop_up,text="Ph:1234567891 E-mail:abc123@gmail.com",font=("arial",15,))
        self.phone_no.grid(row=2,column=0)

        self.gst_no=Label(DataFrameTop_up,text="GSTIN:24AKPYY185223568974",font=("arial",15,))
        self.gst_no.grid(row=3,column=0)

# ------------------------------------for Customare Details box only-------------------------------------------------------

        DataFrameMiddle_up=Frame(DataFrame,relief=RIDGE,bd=3)
        DataFrameMiddle_up.place(x=398,y=2,width=690,height=130)

        self.firsting = StringVar()
        self.lasting = StringVar()
        self.mobile = StringVar()
        self.emailing = StringVar()

        self.custo_details=Label(DataFrameMiddle_up,text="Customare Details",font=("arial",18,"bold"),bg="lightgreen",fg="red")
        self.custo_details.grid(row=0,column=1)

        self.lbl_first_name=Label(DataFrameMiddle_up,font=("arial",15,),text="First Name:",padx=2,pady=6)
        self.lbl_first_name.grid(row=1,column=0)

        self.entry_first_name=Entry(DataFrameMiddle_up,textvariable=self.firsting,width=20,font=("arial",15,),bd=2,relief=RIDGE)
        self.entry_first_name.grid(row=1,column=1)

        self.lbl_last_name=Label(DataFrameMiddle_up,font=("arial",15,),text="Last Name:",padx=2,pady=6)
        self.lbl_last_name.grid(row=2,column=0,sticky=W)

        self.entry_last_name=Entry(DataFrameMiddle_up,textvariable=self.lasting,width=20,font=("arial",15,),bd=2,relief=RIDGE)
        self.entry_last_name.grid(row=2,column=1)

        self.lbl_mob_no=Label(DataFrameMiddle_up,font=("arial",15,),text="Mob No:",padx=2,pady=6)
        self.lbl_mob_no.grid(row=1,column=3,sticky=W)

        self.entry_mob_no=Entry(DataFrameMiddle_up,textvariable=self.mobile,width=20,font=("arial",15,),bd=2,relief=RIDGE)
        self.entry_mob_no.grid(row=1,column=4)

        self.lbl_email=Label(DataFrameMiddle_up,font=("arial",15,),text="E-mail:",padx=2,pady=6)
        self.lbl_email.grid(row=2,column=3,sticky=W)

        self.entry_email=Entry(DataFrameMiddle_up,textvariable=self.emailing,width=20,font=("arial",15,),bd=2,relief=RIDGE)
        self.entry_email.grid(row=2,column=4)

# ---------------------------------for invoice box only-----------------------------------------------------------------

        DataFrameLower_up=Frame(DataFrame,relief=RIDGE,bd=3)
        DataFrameLower_up.place(x=1090,y=2,width=430,height=130)

        self.invoice_title=Label(DataFrameLower_up,text="INVOICE",font=("arial",18,"bold"),bg="lightgreen",fg="red",bd=1,relief=RIDGE)
        self.invoice_title.place(x=180,y=2)

        self.invoicing = IntVar()
        self.referring = IntVar()
        self.dating = StringVar()

        self.lbl_date=Label(DataFrameLower_up,font=("arial",15,"bold"),text="Date:")
        self.lbl_date.place(x=4,y=40)

        self.entry_of_date=DateEntry(DataFrameLower_up,textvariable=self.dating,width=10,
                                  font=("arial",15,),bd=2,relief=RIDGE,state="readonly")
        self.entry_of_date.place(x=70,y=40)

        self.lbl_ref_no=Label(DataFrameLower_up,font=("arial",15,"bold"),text="Ref No:",padx=2,pady=6)
        self.lbl_ref_no.place(x=4,y=70)

        self.entry_ref_no=Entry(DataFrameLower_up,textvariable=self.referring,width=9,font=("arial",15,),bd=2,relief=RIDGE)
        self.entry_ref_no.place(x=104,y=75)

        self.lbl_ivoice_no=Label(DataFrameLower_up,font=("arial",15,"bold"),text="Invoice:",padx=2,pady=6)
        self.lbl_ivoice_no.place(x=225,y=35)

        # self.entry_ivoice_no=Entry(DataFrameLower_up,textvariable=self.invoicing,width=9,font=("arial",15,"bold"),bd=2,relief=RIDGE)
        # self.entry_ivoice_no.place(x=311,y=38)
        self.entry_ivoice_no=Entry(DataFrameLower_up,textvariable=self.invoicing,width=9,font=("arial",15,"bold"),bd=2,relief=RIDGE)
        self.entry_ivoice_no.place(x=311,y=38)


# ----------------------------------------for table frame centre only------------------------------------------------------

        Table_frame=Frame(self.next_window,bd=3,relief=RIDGE)
        Table_frame.place(x=0,y=142,width=1500,height=390)

        # # side_frame=Frame(Table_frame,bd=4,bg="white",relief=RIDGE) // always comment
        # # side_frame.place(x=0,y=185,width=290,height=125) // always comment

        # # sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL) // always comment
        # # sc_x.pack(side=BOTTOM,fill=X) // always comment
        # # sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL) // always comment
        # # sc_y.pack(side=RIGHT,fill=Y) // always comment
        
        sc_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        sc_x.pack(side="bottom",fill='x')
        
        sc_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        sc_y.pack(side='right',fill='y')
        
        self.table = ttk.Treeview(Table_frame,columns=('ref','com','type','medicine','batch','manufactured',
                                                             'expiry','uses','price','productqt'),
                                                              xscrollcommand=sc_y.set,yscrollcommand=sc_x.set)
        
        # # # # scroll_x.pack(side=BOTTOM,fill=X) // always comment
        # # # # scroll_y.pack(side=RIGHT,fill=Y) // always comment
        
        sc_x = ttk.Scrollbar(command=self.table.xview)
        sc_y = ttk.Scrollbar(command=self.table.yview)

        # # # sc_x = ttk.Scrollbar() // always comment
        # # # sc_y = ttk.Scrollbar() // always comment

        # # # sc_x.config(command=self.pharmacy_table.xview) // always comment
        # # # sc_y.config(command=self.pharmacy_table.yview) // always comment
        
        self.table.heading('ref',text='Reference No')
        self.table.heading('com',text='Company Name')
        self.table.heading('type',text='Type Of Medicine')
        self.table.heading('medicine',text='Medicine Name')
        self.table.heading('batch',text='Batch No')
        self.table.heading('manufactured',text='Manufactured Date')
        self.table.heading('expiry',text='Expiry Date')
        self.table.heading('uses',text='Uses')
        # # # # table.heading('side',text='Side Effects') // always comment
        # # # # table.heading('warn',text='Prec & Warning') // always comment
        # # # # table.heading('dos',text='Dosage') // always comment
        self.table.heading('price',text='Tablets Price')
        self.table.heading('productqt',text='Product QT')

        self.table['show']='headings'
        self.table.pack(fill=BOTH,expand=1)

        self.table.column('ref',width=100)
        self.table.column('com',width=100)
        self.table.column('type',width=105)
        self.table.column('medicine',width=100)
        self.table.column('batch',width=100)
        self.table.column('manufactured',width=100)
        self.table.column('expiry',width=100)
        self.table.column('uses',width=100)
        # # # # table.column('side',width=100) // always comment
        # # # # table.column('warn',width=100) // always comment
        # # # # table.column('dos',width=100) // always comment
        self.table.column('price',width=100)
        self.table.column('productqt',width=100)

        self.table.bind('<ButtonRelease-1>', self.get_data)

        self.fetch_data()

# ----------------------------for down box bank details only------------------------------------------------------------

        DataFrametable=Frame(DataFrame,relief=RIDGE,bd=3)
        DataFrametable.place(x=0,y=133,width=1520,height=400)

        DataFrameTop_down=Frame(DataFrame,relief=RIDGE,bd=3)
        DataFrameTop_down.place(x=0,y=534,width=450,height=180)

        self.bank_details=Label(DataFrameTop_down,text="Bank Details:",font=("arial",15,))
        self.bank_details.place(x=1,y=2)

        self.bank_name=Label(DataFrameTop_down,text="State Bank of India",font=("arial",15,))
        self.bank_name.place(x=1,y=28)

        self.account_no=Label(DataFrameTop_down,text="A/C No:22022248631255  IFSC Code:4127O457",font=("arial",15,))
        self.account_no.place(x=1,y=53)

        self.lbl_terms_conditions=Label(DataFrameTop_down,text="Terms & Conditions:",font=("arial",15,))
        self.lbl_terms_conditions.place(x=1,y=80)

        self.lbl_anand_jurisdication=Label(DataFrameTop_down,text="Subject to Anand Jurisdiction",font=("arial",15,))
        self.lbl_anand_jurisdication.place(x=1,y=110)

# -------------------------------for GST data box only-----------------------------------------------------------------

        DataFrameMiddle_down=Frame(DataFrame,relief=RIDGE,bd=3)
        DataFrameMiddle_down.place(x=450,y=534,width=540,height=170)

        self.medicine_tablet=DoubleVar()
        self.medicine_product=DoubleVar()
        self.taxing = DoubleVar()

        self.totalprice=DoubleVar()


        # self.lbl_Tablets_Price=Label(DataFrameMiddle_down,font=("times new roman",17,"bold"),text="Tablet Price:",
        #                              padx=2,pady=6)
        # # self.lbl_Tablets_Price.place(x=1,y=2)
        # self.lbl_Tablets_Price.grid(row=0,column=0,sticky=W)

        # self.tablet_combo=ttk.Combobox(DataFrameMiddle_down,textvariable=self.var_tablet_price,width=12,
        #                                font=("times new roman",15,"bold"),state="readonly")
        # self.tablet_combo["values"]=[10,20,50,100]
        # # self.tablet_combo.place(x=136,y=7)
        # self.tablet_combo.grid(row=0,column=1)

        self.lbl_tablets_price=Label(DataFrameMiddle_down,font=("times new roman",17,"bold"),text="Tablet Price:",
                                     padx=2,pady=6)
        self.lbl_tablets_price.grid(row=1,column=0,sticky=W)


        self.entry_tablet_combo=ttk.Combobox(DataFrameMiddle_down,textvariable=self.medicine_tablet,width=20,
                                       font=("times new roman",15,"bold"),state="readonly")
        self.entry_tablet_combo["values"]=[10,20,50,100]
        self.entry_tablet_combo.grid(row=1,column=1)


        self.lbl_Product_QT=Label(DataFrameMiddle_down,font=("times new roman",17,"bold"),text="Product QT:",
                                  padx=2,pady=6,)
        self.lbl_Product_QT.grid(row=2,column=0,sticky=W)


        self.entry_product_QT_tablet_combo=ttk.Combobox(DataFrameMiddle_down,textvariable=self.medicine_product,width=20,
                                     font=("times new roman",15,"bold"),state="readonly")
        self.entry_product_QT_tablet_combo["values"]=[1,2,3,4,5]
        self.entry_product_QT_tablet_combo.grid(row=2,column=1)

        # self.lbl_tax=Label(DataFrameMiddle_down,font=("times new roman",17,"bold"),text="Tax:",
        #                         padx=2,pady=6)
        # self.lbl_tax.grid(row=2,column=0,sticky=W)

        # self.entry_tax=Entry(DataFrameMiddle_down,textvariable=self.taxing,width=20,
        #                           font=("times new roman",15,"bold"))
        # self.entry_tax.grid(row=2,column=1)
        
        
        # self.lbl_Product_QT=Label(DataFrameMiddle_down,font=("times new roman",17,"bold"),text="Product QT:",padx=2,pady=6)
        # # self.lbl_Product_QT.place(x=1,y=37)
        # self.lbl_Product_QT.grid(row=1,column=0)

        # self.product_QT_combo=ttk.Combobox(DataFrameMiddle_down,textvariable=self.var_product_qt,width=12,
        #                                    font=("times new roman",15,"bold"),state="readonly")
        # self.product_QT_combo["values"]=[1,2,3,4,5]
        # # self.product_QT_combo.place(x=132,y=37)
        # self.product_QT_combo.grid(row=1,column=1)

        # self.lbl_net_amount=Label(DataFrameMiddle_down,text="Net Amount:",font=("arial",15,"bold"))
        # # self.lbl_net_amount.place(x=1,y=69)
        # self.lbl_net_amount.grid(row=2,column=0)



# ----------------------------------------for fourth frame---------------------------------------------------

        DataFrameLower_down=Frame(DataFrame,relief=RIDGE,bd=3)
        DataFrameLower_down.place(x=990,y=534,width=530,height=170)

        self.medicine_total = DoubleVar()



# ----------------------for calculation bill only---------------------------------------------------------------

        self.lbl_total_amount=Label(DataFrameLower_down,text="Total Amount:",font=("arial",15,))
        self.lbl_total_amount.place(x=1,y=2)
        self.entry_total_amount=Entry(DataFrameLower_down,textvariable=self.medicine_total,width=11,bd=2,font=("arial",15,),relief=RIDGE)
        self.entry_total_amount.place(x=132,y=3)

# ----------------------------------for invoice generate button only------------------------------------------------

        DataFramegenerate_invoice=Frame(DataFrame,relief=RIDGE,bd=3)
        DataFramegenerate_invoice.place(x=1,y=705,width=1519,height=70)

        self.button_back=Button(DataFramegenerate_invoice,text="Back",command=self.next_window.destroy,
                            font=("arial",18,"bold"),width=14,bd=2,relief=RIDGE,bg="lightblue",fg="red")
        self.button_back.place(x=40,y=5)

        self.button_generate_invoice=Button(DataFramegenerate_invoice,text="Next",command=self.biji_next_window,
                            font=("arial",18,"bold"),width=14,bd=2,relief=RIDGE,bg="lightblue",fg="red")
        self.button_generate_invoice.place(x=308,y=5)

        self.button_save_invoice=Button(DataFramegenerate_invoice,text="Generate Invoice",command=self.generate_print_invoice,
                            font=("arial",18,"bold"),width=14,bd=2,relief=RIDGE,bg="lightblue",fg="red")
        self.button_save_invoice.place(x=615,y=5)

        self.button_add_details=Button(DataFramegenerate_invoice,text="Add Details",command=self.add_details,
                            font=("arial",18,"bold"),width=14,bd=2,relief=RIDGE,bg="lightblue",fg="red")
        self.button_add_details.place(x=920,y=5)

        self.button_calculate=Button(DataFramegenerate_invoice,text="Calculate Invoice",command=self.multiply,
                                     font=("arial",18,"bold"),width=14,bd=2,relief=RIDGE,bg="lightblue",fg="red")
        self.button_calculate.place(x=1230,y=5)

        # self.button_calculate=Button(DataFrameLeft,text="Calculate Bill",command=self.bill,font=("times new roman",21,"bold")
                                    # ,bg="lightblue",fg="darkred",relief=RIDGE)
        # self.button_calculate.place(x=20,y=240,width=200,height=35)

    def multiply(self):
        self.medicine_tablet = float(self.entry_tablet_combo.get())
        self.medicine_product = float(self.entry_product_QT_tablet_combo.get())
        self.medicine_total.set(self.medicine_tablet * self.medicine_product)
        # self.totalprice.set(self.medicine_tablet * self.medicine_product)
        # self.medicine_total.set(self.totalprice)
        self.entry_total_amount.delete(0, END)
        self.entry_total_amount.insert(0, "Rs. "+str(self.medicine_total.get()))


    # def add_details(self):
    #     if(self.entry_ivoice_no.get()=='' 
    #        or self.entry_ref_no.get()=='' 
    #        or self.entry_of_date.get()=='' 
    #        or self.entry_first_name.get()=='' 
    #        or self.entry_last_name.get()=='' 
    #        or self.entry_mob_no.get()=='' 
    #        or self.entry_email.get()==''
    #     ):
    #        messagebox.showerror("Error","All information are required!!!")

    #     else:
    #         conn = mysql.connector.connect(host="localhost",
    #                                        username="root",
    #                                        password="1234",
    #                                        database="mypharmacy",
    #                                        port="3307")
    #         my_cursor = conn.cursor()
    #         my_cursor.execute(
    #             "insert into mypharmacy.medicine values(%s,%s,%s,%s,%s,%s,%s)",
    #             (

    #                 self.entry_ivoice_no.get(),
    #                 self.entry_ref_no.get(),
    #                 self.entry_of_date.get(),
    #                 self.entry_first_name.get(),
    #                 self.entry_last_name.get(),
    #                 self.entry_mob_no.get(),
    #                 self.entry_email.get()

    #             # self.entry_ivoice_no.get(),self.entry_ref_no.get(),
    #             # self.dating.get(),self.entry_first_name.get(),
    #             # self.entry_last_name.get(),self.entry_mob_no.get(),
    #             # self.entry_email.get()
                
    #             ),
    #         )
    #         conn.commit()
    #         conn.close()
    #         messagebox.showinfo("Successfull","Record has been added successfully!")
    
    def add_details(self):
        if self.entry_ivoice_no.get() == '':
                messagebox.showerror("Error", "Invoice number is required!")
        elif self.entry_ref_no.get() == '':
            messagebox.showerror("Error", "Reference number is required!")
        elif self.entry_of_date.get() == '':
            messagebox.showerror("Error", "Date is required!")
        elif self.entry_first_name.get() == '':
            messagebox.showerror("Error", "First name is required!")
        elif self.entry_last_name.get() == '':
            messagebox.showerror("Error", "Last name is required!")
        elif self.entry_mob_no.get() == '':
            messagebox.showerror("Error", "Mobile number is required!")
        elif not re.match(r'^\d{10}$', self.entry_mob_no.get()):
            messagebox.showerror("Error", "Invalid mobile number format. Please enter a 10-digit number.")
        elif self.entry_email.get() == '':
            messagebox.showerror("Error", "Email is required!")
        elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.entry_email.get()):
            messagebox.showerror("Error", "Invalid email address format.")
        else:
        # If all data is valid, proceed with the database insertion
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="mypharmacy",
                port="3307",
            )
            my_cursor = conn.cursor()
            my_cursor.execute(
                "INSERT INTO mypharmacy.medicine VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (
                    self.entry_ivoice_no.get(),
                    self.entry_ref_no.get(),
                    self.entry_of_date.get(),
                    self.entry_first_name.get(),
                    self.entry_last_name.get(),
                    self.entry_mob_no.get(),
                    self.entry_email.get(),
                ),
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("Successfull", "Record has been added successfully!")


    def biji_next_window(self):

        self.open_fourthpage_window()

    def open_fourthpage_window(self):
        self.last_window=Tk()
        self.last_window.title("Generate Invoice")
        self.last_window.geometry("1530x850+0+0")
        # self.textarea = Text(self.printingFrame)
        self.textarea = Text(self.last_window)
        self.textarea.pack()
        # self.last_window.configure("lightblue")

        # self.textarea = Text(self.root)
        # self.textarea.pack()

        self.DataFrame=Frame(self.last_window,relief=RIDGE,bd=4)
        self.DataFrame.place(x=0,y=0,width=1527,height=780)

        self.printingFrame=Frame(self.DataFrame,bd=4,relief=RIDGE)
        self.printingFrame.place(x=820,y=90,width=430,height=500)
        # self.print_Frame.pack(side='top',fill='x')

        
        # self.bill_title = Label(self.printingFrame,text="Receipt",font=("arial",15,"bold"),bd=7,relief=RIDGE)
        # # self.lbl_bill_invoice=Label(self.print_Frame,text="Swami Pharmacy",font=("arial",20,"bold"),)
        # self.bill_title.place(x=280,y=20)

        scrol_y = Scrollbar(self.printingFrame,orient=VERTICAL)
        scrol_y.pack(side=RIGHT,fill=Y,anchor="center")
        # # # scrol_x = Scrollbar(self.print_Frame,orient=HORIZONTAL)
        # # # scrol_x.pack(side=BOTTOM,fill=X)

        self.textarea=Text(self.printingFrame,font=("arial",15,"bold"),yscrollcommand=scrol_y.set)
        self.textarea.pack(fill=BOTH)
        # # # textarea = Text(self.print_Frame,font=("arial",15,"bold"),xscrollcommand=scrol_x.set)
        # # # textarea.pack(side=TOP)
        scrol_y.config(command=self.textarea.yview)
        # # scrol_x.config(command=textarea.xview)

        DataFramegenerate_last_page=Frame(self.DataFrame,relief=RIDGE,bd=3)
        DataFramegenerate_last_page.place(x=1,y=705,width=1519,height=70)

        self.button_back=Button(DataFramegenerate_last_page,text="Back",command=self.last_window.destroy,
                            font=("arial",18,"bold"),width=20,bd=2,relief=RIDGE,bg="lightblue",fg="red")
        self.button_back.place(x=30,y=5)

        # self.button_generate_invoice=Button(DataFramegenerate_last_page,text="Print Invoice",command=self.print_invoice,
        #                     font=("arial",18,"bold"),width=20,bd=2,relief=RIDGE,bg="lightblue",fg="red")
        # self.button_generate_invoice.place(x=450,y=5)

        # self.button_exit = Button(DataFramegenerate_last_page, text="Exit",command=self.master.destroy,
        #                           font=("times new roman",18,"bold"),width=20,bd=2,relief=RIDGE,bg="lightblue",fg="red")
        # # self.button_reset.pack()
        # self.button_exit.place(x=790,y=5)

    def generate_print_invoice(self):
        # self.pharmacy_name = self.pharmacy_name.get()
        # self.road_name = self.road_name.get()
        # self.phone_no = self.phone_no.get()
        self.invoice_no = self.entry_ivoice_no.get()
        self.ref_no = self.entry_ref_no.get()
        self.date = self.entry_of_date.get()
        self.first_name = self.entry_first_name.get()
        self.last_name = self.entry_last_name.get()
        self.mobile_no = self.entry_mob_no.get()
        self.email = self.entry_email.get()
        self.lbl_type = self.type_medicine_combo.get()
        self.lbl_med = self.med_combo.get()
        self.lbl_tablets_price = self.entry_tablet_combo.get()
        self.lbl_Product_QT = self.entry_product_QT_tablet_combo.get()
        self.lbl_total_amount = self.entry_total_amount.get()

        self.print_invoice()

    def print_invoice(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # pdf.cell(0, 10,f"Pharmacy Name: {self.pharmacy_name}", ln=True)
        # pdf.cell(0, 10,f"Address: {self.road_name}", ln=True)
        # pdf.cell(0, 10,f"Mobile No. Pharmacy: {self.phone_no}", ln=True)

        pdf.cell(0, 10, f"Invoice No: {self.invoice_no}", ln=True)
        pdf.cell(0, 10, f"Reference No: {self.ref_no}", ln=True)
        pdf.cell(0, 10, f"Date: {self.date}", ln=True)
        pdf.cell(0, 10, f"First Name: {self.first_name}", ln=True)
        pdf.cell(0, 10, f"Last Name: {self.last_name}", ln=True)
        pdf.cell(0, 10, f"Mobile No: {self.mobile_no}", ln=True)
        pdf.cell(0, 10, f"Email: {self.email}", ln=True)
        pdf.cell(0, 10, f"Medicine Type: {self.lbl_type}", ln=True)
        pdf.cell(0, 10, f"Medicine Name: {self.lbl_med}", ln=True)
        pdf.cell(0, 10, f"Tablet Price: {self.lbl_tablets_price}", ln=True)
        pdf.cell(0, 10, f"Product Qt: {self.lbl_Product_QT}", ln=True)
        pdf.cell(0, 10, f"Total Amount: {self.lbl_total_amount}", ln=True)

        # filename = f"Invoice_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.pdf"

        #/path/to/folder
        file_name = ("file_saved/First_"+str(self.entry_first_name.get())+'.pdf')
        pdf.output(file_name)

        messagebox.showinfo("Success", "Invoice generated and saved")

        

        # qr_code.save("qr_code_generate/Med_"+str(self.var_ref_no.get())+'.png')

        #     self.im=ImageTk.PhotoImage(file="qr_code_generate/Med_"+str(self.var_ref_no.get())+'.png')
        #     self.qr_code.config(image=self.im)


        self.next_window.mainloop()

if __name__ == "__main__":
    root = Tk()
    object = Login(root)
    root.mainloop()