import tkinter as tk
from tkinter import ttk 
import pyodbc 
class Student:
    def __init__(self,root):
        self.root = root
        self.root.title('Student Management System')
        self.root.geometry("1350x700+0+0")
        
        title = tk.Label(self.root, text = 'Student Management', font = ('times new roman', 40, 'bold'))
        title.pack(side=tk.TOP, fill=tk.X)
        
        self.id_No_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.contact_var = tk.StringVar()
        self.dob_var = tk.StringVar()
        
        manage_frm = tk.Frame(self.root, bd=4)
        manage_frm.place(x=20, y=100, width=450, height=560)
        title_lbl = tk.Label(manage_frm, text ='Manage Students', font = ('times new roman', 20, 'bold'))
        title_lbl.grid(row=0, columnspan=2, padx=20, pady=20, sticky='w')
        
        lbl_roll = tk.Label(manage_frm, text ='ID No.', font = ('times new roman', 15, 'bold'))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky='w')
        
        txt_Roll = tk.Entry(manage_frm, textvariable = self.id_No_var, font = ('times new roman', 15, 'bold') )
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky='w')
        
        lbl_name = tk.Label(manage_frm, text ='Name', font = ('times new roman', 15, 'bold'))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky='w')
        
        txt_name = tk.Entry(manage_frm,textvariable = self.name_var,font = ('times new roman', 15, 'bold') )
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky='w')
        
        lbl_gmail = tk.Label(manage_frm, text ='Gmail', font = ('times new roman', 15, 'bold'))
        lbl_gmail.grid(row=3, column=0, pady=10, padx=20, sticky='w')
        
        txt_gmail = tk.Entry(manage_frm,textvariable = self.email_var,font = ('times new roman', 15, 'bold') )
        txt_gmail.grid(row=3, column=1, pady=10, padx=20, sticky='w')
        
        lbl_gender = tk.Label(manage_frm, text ='Gender', font = ('times new roman', 15, 'bold'))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky='w')
        
        values = ['female', 'male','Other']
        combo_gender = ttk.Combobox(manage_frm, values = values, textvariable = self.gender_var,font = ('times new roman', 13,'bold'))
        combo_gender.grid(row=4, column=1, pady=10, padx=20, sticky='w')

        lbl_contact = tk.Label(manage_frm, text ='Contact', font = ('times new roman', 15, 'bold'))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky='w')
        
        txt_contact = tk.Entry(manage_frm,textvariable = self.contact_var,font = ('times new roman', 15, 'bold') )
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky='w')
        
        lbl_dob = tk.Label(manage_frm, text ='D.O.B', font = ('times new roman', 15, 'bold'))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky='w')
        
        txt_dob = tk.Entry(manage_frm,textvariable = self.dob_var,font = ('times new roman', 15, 'bold') )
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky='w')
        
        lbl_address = tk.Label(manage_frm, text ='Address', font = ('times new roman', 15, 'bold'))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky='w')
        
        self.txt_address = tk.Text(manage_frm,width =20, height =4, font = ('times new roman', 15, 'bold') )
        self.txt_address.grid(row=7, column=1, pady=10, padx=20, sticky='w')
        #######button frame
        btn_frm = tk.Frame(manage_frm, bd=4, relief='ridge')
        btn_frm.place(x=15, y=500, width=420)
        
        btn_add = tk.Button(btn_frm, text='Add',width=10, command = self.add_students).grid(row=0, column=0, padx=10, pady=10)
        btn_update = tk.Button(btn_frm, text='Update',width=10).grid(row=0, column=1, padx=10, pady=10)
        btn_delete = tk.Button(btn_frm, text='Delete',width=10).grid(row=0, column=2, padx=10, pady=10)
        btn_add = tk.Button(btn_frm, text='Clear',width=10).grid(row=0, column=3, padx=10, pady=10)

        #######
        detail_frm = tk.Frame(self.root, bd=4)
        detail_frm.place(x=500, y=100, width=750, height=560)
        
        lbl_search = tk.Label(detail_frm, text='Search by', font = ('times new roman', 13,'bold'))
        lbl_search.grid(row=0, column=0, padx=15, pady=10)

        values_search = ['Roll','Name','Contact']
        combo_search = ttk.Combobox(detail_frm, values = values_search,width =10, font = ('times new roman', 13,'bold'))
        combo_search.grid(row=0, column=1, padx=15, pady=10)
        
        txt_search = tk.Entry(detail_frm, text='Search by', font = ('times new roman', 13,'bold'))
        txt_search.grid(row=0, column=2, padx=15, pady=10)

        btn_search = tk.Button(detail_frm, text='Search',width=10).grid(row=0, column=3, padx=15, pady=10)
        btn_showall = tk.Button(detail_frm, text='Show all',width=10).grid(row=0, column=4, padx=15, pady=10)
        ## Table Frame
        table_frame = tk.Frame(detail_frm, bd=4, relief='ridge')
        table_frame.place(x=10, y=100, width =700, height=450)
        scroll_x = tk.Scrollbar(table_frame, orient='horizontal')
        scroll_y = tk.Scrollbar(table_frame, orient='vertical')

        self.student_table = ttk.Treeview(table_frame, columns=('id','name','email','gender','contact','DOB','address'), xscrollcommand =scroll_x.set, yscrollcommand =scroll_y.set)
        scroll_x.pack(side='bottom', fill='x')
        scroll_y.pack(side='right', fill='y')
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading('id', text='ID No')
        self.student_table.heading('name', text='Name')
        self.student_table.heading('email', text='Email')
        self.student_table.heading('gender', text='Gender')
        self.student_table.heading('contact', text='Contact')
        self.student_table.heading('DOB', text='DOB')
        self.student_table.heading('address', text='Address')
        self.student_table['show'] = 'headings'
        self.student_table.column('id', width=100)
        self.student_table.column('name', width=100)
        self.student_table.column('email', width=100)
        self.student_table.column('gender', width=100)
        self.student_table.column('contact', width=100)
        self.student_table.column('DOB', width=100)
        self.student_table.column('address', width=150)
        self.student_table.pack(fill='both', expand=1)
        self.fetch_data()
    def add_students(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                     'Server=LAPTOP-TOJSOVMJ\SQLEXPRESS;'
                     'Database=StudentManagement;' 
                     'Trusted_Connection=yes;')
        inser_sql = '''INSERT INTO student_info VALUES(?,?,?,?,?,?,?)'''
        cursor = conn.cursor()
        cursor.execute(inser_sql,self.id_No_var.get(), self.name_var.get(),
                       self.email_var.get(), self.gender_var.get(), self.contact_var.get(), 
                       self.dob_var.get(),self.txt_address.get('1.0', 'end'))
        
        conn.commit()
        self.fetch_data()
        conn.close()
        
    def fetch_data(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                     'Server=LAPTOP-TOJSOVMJ\SQLEXPRESS;'
                     'Database=StudentManagement;' 
                     'Trusted_Connection=yes;')
        select_sql = '''SELECT * FROM student_info'''
        cursor = conn.cursor()
        cursor.execute(select_sql)
        rows = cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', 'end', values=row)
                conn.commit()
        conn.close()
            
        
root = tk.Tk()
on = Student(root)
root.mainloop()