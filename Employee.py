from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from matplotlib.pyplot import table
import mysql.connector
from tkinter import messagebox

#from mysqlx import Column
from requests import delete

class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0") # Specify according to your window.
        self.root.title("Employee Management System")
        
        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',
                        font=('times new roman', 37,'bold'),
                        foreground='midnightblue',
                        background='white')
        
        lbl_title.place(x=0,
                        y=0,
                        width=1920,
                        height=50)
        
        # logo
        img_logo = Image.open('logo.png')
        img_logo = img_logo.resize((50,50),Image.Resampling.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        
        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=340,y=0,width=50, height=50)
        
        # Frame for Image below title

        img_frame = Frame(self.root, bd=2, relief=RIDGE, background='white')
        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        img_frame.place(x=0, y=50, width=1920, height=200)

        title_image = Image.open('image_2.jpg')
        self.title_photo=ImageTk.PhotoImage(title_image)
        
        self.title_image=Label(img_frame,image=self.title_photo)
        self.title_image.place(x=0,y=0,width=1920, height=200)

        # Frames for employee information

        # Body frame

        body_frame = Frame(self.root, bd=2,relief=RIDGE, background='white')
        body_frame.place(x=10, y=260,width=1900,height=770)

        # Upper frame

        upper_frame = LabelFrame(body_frame, bd=2, relief=RIDGE, background='white',text='Employee Information', font=('times new roman', 14,'bold'),foreground='black')
        upper_frame.place(x=10, y=10,width=1880,height=330)

        # Variables

        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_designition = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_phone = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        # self.var_idproof = StringVar()
        self.var_empid = StringVar()

        self.var_gender = StringVar()
        self.var_marital_status = StringVar()
        self.var_country = StringVar()
        self.var_salary = StringVar()
        
        # Labels and Entry Field

        # Name

        lbl_name = Label(upper_frame, text='Name', font=('arial', 11,'bold'), background='white')
        lbl_name.grid(row=0, column=0, padx=4, sticky=W, pady=12)
        
        txt_name=ttk.Entry(upper_frame, textvariable=self.var_name, width=22, font=('arial', 11,'bold'))
        txt_name.grid(row=0, column=1, padx=4, pady=12)

        # Department

        lbl_department = Label(upper_frame, text='Department', font=('arial', 11,'bold'), background='white')
        lbl_department.grid(row=0, column=2, padx=4, sticky=W, pady=12)

        combo_department=ttk.Combobox(upper_frame, textvariable=self.var_department,font=('arial', 12,'bold'),width=18,state='readonly')
        combo_department['value']=('Select', 'Human Resource Deaprtment','Accounts and Finance', 'Sales and Marketing ', 'Infrastructures', 'Research and development', 'Learning and development' , 'IT services', 'Product development', 'Admin department' , 'Security and transport')
        combo_department.current(0)
        combo_department.grid(row=0, column=3, padx=4, pady=12, sticky=W)

        
        # Designition

        lbl_designition=Label(upper_frame, text='Designition', font=('arial', 11,'bold'), background='white')
        lbl_designition.grid(row=1, column=0, padx=4,pady=12, sticky=W)

        txt_designition=ttk.Entry(upper_frame, textvariable=self.var_designition, width=22, font=('arial', 11,'bold'))
        txt_designition.grid(row=1, column=1, padx=4, pady=12, sticky=W) 

        # Email

        lbl_email = Label(upper_frame, text='Email', font=('arial', 11,'bold'), background='white')
        lbl_email.grid(row=1, column=2, padx=4, sticky=W , pady=12)

        txt_email=ttk.Entry(upper_frame, textvariable=self.var_email, width=22, font=('arial', 11,'bold'))
        txt_email.grid(row=1, column=3, padx=4, pady=12)

        # Employee ID

        lbl_employee_id = Label(upper_frame, text='Employee_ID', font=('arial', 11,'bold'), background='white')
        lbl_employee_id.grid(row=2, column=0, padx=4, sticky=W, pady=12)

        lbl_employee_id=ttk.Entry(upper_frame, textvariable=self.var_empid, width=22, font=('arial', 11,'bold'))
        lbl_employee_id.grid(row=2, column=1, padx=4, pady=12)

        # Phone

        lbl_phone = Label(upper_frame, text='Phone_No', font=('arial', 11,'bold'), background='white')
        lbl_phone.grid(row=0, column=4, padx=4, sticky=W, pady=12)

        txt_phone=ttk.Entry(upper_frame, textvariable=self.var_phone, width=22, font=('arial', 11,'bold'))
        txt_phone.grid(row=0, column=5, padx=4, pady=12)

        # Date of birth

        lbl_dob = Label(upper_frame, text='DOB',font=('arial', 11,'bold'), background='white')
        lbl_dob.grid(row=3, column=0, padx=4, sticky=W, pady=12)

        txt_dob=ttk.Entry(upper_frame, textvariable=self.var_dob, width=22, font=('arial', 11,'bold'))
        txt_dob.grid(row=3, column=1, padx=4, pady=12)

        # Date of joining

        lbl_doj = Label(upper_frame, text='DOJ',font=('arial', 11,'bold'), background='white')
        lbl_doj.grid(row=3, column=2, padx=4, sticky=W, pady=12)

        txt_date_of_joining=ttk.Entry(upper_frame, textvariable=self.var_doj, width=22, font=('arial', 11,'bold'))
        txt_date_of_joining.grid(row=3, column=3, padx=4, pady=12)

        # Address 

        lbl_address = Label(upper_frame, text='Address', font=('arial', 11,'bold'), background='white')
        lbl_address.grid(row=4, column=0, padx=4, sticky=W, pady=12)

        txt_address=ttk.Entry(upper_frame, textvariable=self.var_address, width=22, font=('arial', 11,'bold'))
        txt_address.grid(row=4, column=1, padx=4, pady=12)


        # Gender

        lbl_gender = Label(upper_frame, text='Gender', font=('arial', 11,'bold'), background='white')
        lbl_gender.grid(row=4, column=2, padx=4, sticky=W, pady=12)

        combo_gender=ttk.Combobox(upper_frame, textvariable=self.var_gender,font=('arial', 12,'bold'),width=18,state='readonly')
        combo_gender['value']=('Select','Male', 'Female', 'Others')
        combo_gender.current(0)
        combo_gender.grid(row=4, column=3, padx=4, pady=12, sticky=W)

        # Married

        lbl_married = Label(upper_frame, text='Marital Status', font=('arial', 11,'bold'), background='white')
        lbl_married.grid(row=2, column=2, padx=4, sticky=W, pady=8)

        combo_married=ttk.Combobox(upper_frame, textvariable=self.var_marital_status,font=('arial', 12,'bold'),width=18,state='readonly')
        combo_married['value']=('Select','Married', 'Unmarried')
        combo_married.current(0)
        combo_married.grid(row=2, column=3, padx=4, pady=12, sticky=W)

        # Country

        lbl_country = Label(upper_frame, text='Country',font=('arial', 11,'bold'), background='white')
        lbl_country.grid(row=1, column=4, padx=4, sticky=W, pady=12)

        txt_country=ttk.Entry(upper_frame, textvariable=self.var_country, width=22, font=('arial', 11,'bold'))
        txt_country.grid(row=1, column=5, padx=4, pady=12)

        # Salary

        lbl_salary = Label(upper_frame, text='Salary(CTC) ',font=('arial', 11,'bold'), background='white')
        lbl_salary.grid(row=2, column=4, padx=4, sticky=W, pady=12)

        txt_salary=ttk.Entry(upper_frame, textvariable=self.var_salary,width=22, font=('arial', 11,'bold'))
        txt_salary.grid(row=2, column=5, padx=4, pady=12, sticky=W)    

        # buttons frame

        button_frame = Frame(upper_frame, bd=2,relief=RIDGE, background='white')
        button_frame.place(x=1250, y=15,width=500,height=260)

        # Save Button

        button_Save = Button(button_frame, text = 'Save',command=self.save_data , font=('arial', 15,'bold'),width=30,foreground='white',background='darkblue')
        button_Save.grid(row=0, column=0, padx=10,pady=5)

        # Update Button

        button_Update = Button(button_frame, text = 'Update',command=self.update_data, font=('arial', 15,'bold'),width=30,foreground='white',background='darkblue')
        button_Update.grid(row=1, column=0, padx=10,pady=5)

        # Delete Button

        button_Delete = Button(button_frame, text = 'Delete',command=self.delete_data, font=('arial', 15,'bold'),width=30,foreground='white',background='darkblue')
        button_Delete.grid(row=2, column=0, padx=10,pady=5)

        # Clear Button

        button_Clear = Button(button_frame, text = 'Clear', command=self.reset_data, font=('arial', 15,'bold'),width=30,foreground='white',background='darkblue')
        button_Clear.grid(row=3, column=0, padx=10,pady=5)
    

        # Bottom frame

        bottom_frame = LabelFrame(body_frame, bd=2, relief=RIDGE, background='white',text='Employee Information Table', font=('times new roman', 14,'bold'), foreground='black')
        bottom_frame.place(x=10, y=340,width=1880,height=410)

        # Search frame

        search_frame = LabelFrame(bottom_frame, bd=2, relief=RIDGE, background='white',text='Search Employee Information', font=('times new roman', 14,'bold'),foreground='black')
        search_frame.place(x=0, y=0,width=1875,height=90)

        # Search 

        self.var_search_by = StringVar()

        lbl_search_by=Label(search_frame, font=("arial", 12, "bold"), text="Search By", foreground="white", background="red")
        lbl_search_by.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        ## To give option to choose from for searching.
        combo_search_by=ttk.Combobox(search_frame, textvariable=self.var_search_by ,font=('arial', 12,'bold'),width=18,state='readonly')
        combo_search_by['value']=('Select','Employee_ID','Phone_No','Email')
        combo_search_by.current(0)
        combo_search_by.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        self.var_search = StringVar()

        txt_Search=ttk.Entry(search_frame, textvariable = self.var_search, width=22,font=('arial', 11,'bold'))
        txt_Search.grid(row=0, column=2, padx=10, pady=10)

        ## Button for searching a single row
        button_Search = Button(search_frame, text = 'Search', command=self.search_data, font=('arial', 11,'bold'),width=18,foreground='white',background='darkblue')
        button_Search.grid(row=0, column=3, padx=10,pady=10)

        ## Button for searching all rows.
        button_Search_all= Button(search_frame, text = 'Search All', command=self.call_data, font=('arial', 11,'bold'),width=18,foreground='white',background='darkblue')
        button_Search_all.grid(row=0, column=4, padx=10,pady=10)

        # Table frame

        table_frame = Frame(bottom_frame, bd=3, relief=RIDGE)
        table_frame.place(x=10, y=100,width=1860,height=270)


        # Scrool bar

        axis_x_scrollbar = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        axis_y_scrollbar = ttk.Scrollbar(table_frame, orient=VERTICAL)

        axis_x_scrollbar.pack(side=BOTTOM,fill=X)
        axis_y_scrollbar.pack(side=RIGHT,fill=Y)

        # Table Content

        ##  Heading to be represented in each column

        self.emp_info_table=ttk.Treeview(table_frame,columns=("empid", "name","designition", "department", "phone", "email", "gender", "dob", "doj","address", "salary", "country", "marital_status"), xscrollcommand=axis_x_scrollbar.set,yscrollcommand=axis_y_scrollbar.set)
        
        self.emp_info_table.heading("empid", text='Employee_ID')
        self.emp_info_table.heading("name", text='Name')
        self.emp_info_table.heading("designition", text='Designition')
        self.emp_info_table.heading("department", text='Department')
        self.emp_info_table.heading("phone", text='Phone_No')
        self.emp_info_table.heading("email", text='Email')
        self.emp_info_table.heading("gender", text='Gender')
        self.emp_info_table.heading("dob", text='DOB')
        self.emp_info_table.heading("doj", text='DOJ')
        self.emp_info_table.heading("address", text='Address')
        self.emp_info_table.heading("salary", text='Salary(CTC)')
        self.emp_info_table.heading("country", text='Country')
        self.emp_info_table.heading("marital_status", text='Marital_Status')
        
        ## To give proper spacing among columns in database area.
        self.emp_info_table['show']='headings'
        
        self.emp_info_table.column("empid",width=100)
        self.emp_info_table.column("name",width=100)
        self.emp_info_table.column("designition",width=100)
        self.emp_info_table.column("department",width=100)
        self.emp_info_table.column("phone",width=100)
        self.emp_info_table.column("email",width=100)
        self.emp_info_table.column("gender",width=100)
        self.emp_info_table.column("dob",width=100)
        self.emp_info_table.column("doj",width=100)
        self.emp_info_table.column("address",width=100)
        self.emp_info_table.column("salary",width=100)
        self.emp_info_table.column("country",width=100)
        self.emp_info_table.column("marital_status",width=100)
        
        self.emp_info_table.pack(fill=BOTH, expand=1)
        self.emp_info_table.bind("<ButtonRelease>",self.get_cursor)

        self.call_data()

        axis_x_scrollbar.config(command=self.emp_info_table.xview)
        axis_y_scrollbar.config(command=self.emp_info_table.yview)

    # Function Declaration

    ## Function to save data entered.
    def save_data(self):
        if self.var_name.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                # Setting connection with Mysql server to receive and send data.

                # Fill host, username, password, database according to your database.
                conn=mysql.connector.connect(host='', username='', password='', database='')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into employee_info values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(

                    self.var_empid.get(),
                    self.var_name.get(),
                    self.var_designition.get(),
                    self.var_department.get(),
                    self.var_phone.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_address.get(),
                    self.var_salary.get(),
                    self.var_country.get(),
                    self.var_marital_status.get()
                ))                
                
                conn.commit()
                self.call_data()
                conn.close()
                messagebox.showinfo('Success','Employee information has been saved', parent=self.root)
            except Exception as es:
                messagebox.showerror('Error', f'Due To:{str(es)}',parent=self.root)

    # Calling data from Database

    ## Function to call data from database.

    def call_data(self):
                                                                
        # Fill host, username, password, database according to your database
        conn=mysql.connector.connect(host='', username='', password='', database='')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from employee_info')
        data = my_cursor.fetchall()
        if len(data)!= 0:
            self.emp_info_table.delete(*self.emp_info_table.get_children())
            for i in data:
                self.emp_info_table.insert("", END,values=i)
            conn.commit()
        conn.close()

    #   Get Cursor

    def get_cursor(self,event=""):
        cursor_row= self.emp_info_table.focus()
        content=self.emp_info_table.item(cursor_row)
        data=content['values']

        self.var_empid.set(data[0]),
        self.var_name.set(data[1]),
        self.var_designition.set(data[2]),
        self.var_department.set(data[3]),
        self.var_phone.set(data[4]),
        self.var_email.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_dob.set(data[7]),
        self.var_doj.set(data[8]),
        self.var_address.set(data[9]),
        self.var_salary.set(data[10]),
        self.var_country.set(data[11]),
        self.var_marital_status.set(data[12])

    # Update

    ## Function to update data in database.

    def update_data(self):
        if self.var_name.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                update = messagebox.askyesno('Update','Are you sure to update this employee data ?')
                if update > 0:
                    # Fill host, username, password, database according to your database.
                    conn=mysql.connector.connect(host='', username='', password='', database='')
                    my_cursor=conn.cursor()
                    
                    my_cursor.execute ("UPDATE employee_info SET Name=%s,Designition=%s,Department=%s,Phone_No=%s,Email=%s,Gender=%s,DOB=%s,DOJ=%s,Address=%s,Salary(CTC)=%s,Country=%s,Marital_Status=%s where Employee_ID = %s"(

                                self.var_name.get(),
                                self.var_designition.get(),
                                self.var_department.get(),
                                self.var_phone.get(),
                                self.var_email.get(),
                                self.var_gender.get(),
                                self.var_dob.get(),
                                self.var_doj.get(),
                                self.var_address.get(),
                                self.var_salary.get(),
                                self.var_country.get(),
                                self.var_marital_status.get(),
                                self.var_empid.get()                       
                    ))
                   
                else:
                    if not update:
                           return
                conn.commit()
                self.call_data()
                conn.close()
                messagebox.showinfo('Success','Employee Information Successfully Updated')                                                                             
            except Exception as es:
                messagebox.showerror('Error', f'Due To:{str(es)}',parent=self.root)

    # Delete

    ## Function to delete data which is not needed anymore.

    def delete_data(self):
        if self.var_empid.get()=="":
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                Delete = messagebox.askyesno('Delete','Are you sure to delete this employee data ?', parent=self.root)
                if Delete > 0:
                    # Fill host, username, password, database according to your database
                    conn=mysql.connector.connect(host='', username='', password='', database='')
                    my_cursor=conn.cursor()
                    sql_delete = 'delete from employee_info where Employee_ID=%s'
                    value  = (self.var_empid.get(),)
                    my_cursor.execute(sql_delete,value)
                
                else:
                    if not Delete:
                        return
                conn.commit()
                self.call_data()
                conn.close()
                messagebox.showinfo('Delete','Employee Information Successfully Deleted', parent=self.root)                                                                             
            except Exception as es:
                messagebox.showerror('Error', f'Due To:{str(es)}',parent=self.root)

    # Reset/Clear

    ## To clear all inputs taken from The user into entry fields.

    def reset_data(self):
        self.var_empid.set(""),
        self.var_name.set(""),
        self.var_designition.set(""),
        self.var_department.set("Select Department"),
        self.var_phone.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_address.set(""),
        self.var_salary.set(""),
        self.var_country.set(""),
        self.var_marital_status.set("Select")

    # Search By option

    def search_data(self):
        if self.var_search_by.get() == '' or self.var_search.get() == '':
            messagebox.showerror('Error','Please select option')
        else:
            try:
                # Fill host, username, password, database according to your database
                conn=mysql.connector.connect(host='', username='', password='', database='')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from employee_info where ' +str(self.var_search_by.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.emp_info_table.delete(*self.emp_info_table.get_children())
                    for i in rows:
                        self.emp_info_table.insert("",END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error', f'Due To:{str(es)}',parent=self.root)





if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()