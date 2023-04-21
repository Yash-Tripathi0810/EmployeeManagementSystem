import mysql.connector
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import string
from PIL import ImageTk, Image
import os

conn = mysql.connector.connect(
  host="localhost",
  user="user",
  password="Yash123",
  database="aissce_project"
)
cursor=conn.cursor()

root = Tk()
root.title('Employee Management System')
root.geometry('1024x768')
root.configure(bg='powder blue')

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def hide():
    for x in root.winfo_children():
        x.destroy()

def exits():
        exit=tkinter.messagebox.askyesno("Employee Management System","Do you want to exit the System ?")
        if exit>0:
            root.destroy()
            return

def mains():
    hide()
    Label(root,bg='sky blue',font=('Arial',30,'bold'),padx=10,pady=10,relief=RIDGE,text='Welcome to Employee Management System').place(relx=0.5,rely=0.05,anchor=CENTER)
    Button(root, text='Login', width=50,command=lambda: lg()).place(relx = 0.5, rely = 0.4,anchor=CENTER)
    Button(root, text='Help', width=50,command=lambda: helps(root)).place(relx = 0.5, rely = 0.45,anchor=CENTER)
    Button(root, text='Exit', width=50, command=lambda : exits()).place(relx = 0.5, rely = 0.5,anchor=CENTER)

def helps(root):
    hide()
    Label(root,bg='sky blue',font=('Standard',16,'bold','underline'),padx=10,pady=10,relief=RIDGE,text='Getting Started').pack(side=TOP)
    scrollbar = Scrollbar(root,orient=VERTICAL)
    scrollbar.pack(side=RIGHT, fill=Y)
    cvs=Canvas(root,bg='light blue',height=680,relief=RIDGE,width=1000,scrollregion=(0,0,0,2675))
    scrollbar.config(command=cvs.yview)
    cvs.config(yscrollcommand=scrollbar.set)
    cvs.pack(expand=YES,fill=BOTH)
    txtb1 = Text(cvs,bg='powder blue',font=('Standard',10),height=3,padx=5,pady=5,relief=SUNKEN,width=135,wrap=WORD)
    txtb1.insert(END, f"(1) Login - Press to login.\n")
    txtb1.insert(END, f"(2) Help - Press for help.\n")
    txtb1.insert(END, f"(3) Exit - Press to exit.\n")
    txtb1.config(state=DISABLED)
    txtb2 = Text(cvs,bg='powder blue',font=('Standard',10),height=5,padx=5,pady=5,relief=SUNKEN,width=135,wrap=WORD)
    txtb2.insert(END, f"(1) Credential Space #1 - Enter your username here.\n")
    txtb2.insert(END, f"(2) Credential Space #2 - Enter your password here.\n")
    txtb2.insert(END, f"(3) Login - Press to authenticate and login.\n")
    txtb2.insert(END, f"(4) Back - Press to return to Main Menu.\n")
    txtb2.insert(END, f"(5) Exit - Press to exit.\n")
    txtb2.config(state=DISABLED)
    txtb3 = Text(cvs,bg='powder blue',font=('Standard',10),height=11,padx=5,pady=5,relief=SUNKEN,width=135,wrap=WORD)
    txtb3.insert(END, f"(0) Manage Profile - Used to view own record and modify any error.\n")
    txtb3.insert(END, f"(1) Employee Management/Record - Used to view employee records.(For Administrators)- Create,Update and Delete records.\n")
    txtb3.insert(END, f"(2) Appraisal Management/Record - Used to view appraisal records.(For Administrators)- Create,Update and Delete records.\n")
    txtb3.insert(END, f"(3) Department Management/Record - Used to view department records.(For Administrators)- Create,Update and Delete records.\n")
    txtb3.insert(END, f"(4) Leave Management/Record - Used to view leave records.(For Administrators)- Create,Update and Delete records.\n")
    txtb3.insert(END, f"(5) Project Management/Record - Used to view project records.(For Administrators)- Create,Update and Delete records.\n")
    txtb3.insert(END, f"(6) Salary Management/Record - Used to view salary records.(For Administrators)- Create,Update and Delete records.\n")
    txtb3.insert(END, f"(7) Timesheet Management/Record - Used to view timesheet records.(For Administrators)- Create,Update and Delete records.\n")
    txtb3.insert(END, f"(8) Administrator Management (Only available in Administrator Console) - Used to Create,Read,Update and Delete administrator records.\n")
    txtb3.insert(END, f"(9) Log Out - Press to logout.\n")
    txtb3.insert(END, f"(10) Exit - Press to exit.\n")
    txtb3.config(state=DISABLED)
    txtb4 = Text(cvs,bg='powder blue',font=('Standard',10),height=4,padx=5,pady=5,relief=SUNKEN,width=135,wrap=WORD)
    txtb4.insert(END, f"(1) Update - Used for updating record.\n")
    txtb4.insert(END, f"(2) Main Menu - Press to return back to Home Screen.\n")
    txtb4.insert(END, f"(3) Log Out - Press to logout.\n")
    txtb4.insert(END, f"(4) Exit - Press to exit.\n")
    txtb4.config(state=DISABLED)
    txtb5 = Text(cvs,bg='powder blue',font=('Standard',10),height=7,padx=5,pady=5,relief=SUNKEN,width=135,wrap=WORD)
    txtb5.insert(END, f"(1) Insert Record (Only available in Administrator Console) - Used to create records.\n")
    txtb5.insert(END, f"(2) View Record - Used to view records.\n")
    txtb5.insert(END, f"(3) Update Record (Only available in Administrator Console) - Used to update records.\n")
    txtb5.insert(END, f"(4) Delete Record (Only available in Administrator Console) - Used to delete records.\n")
    txtb5.insert(END, f"(5) Main Menu - Press to return back to Home Screen.\n")
    txtb5.insert(END, f"(6) Log Out - Press to logout.\n")
    txtb5.insert(END, f"(7) Exit - Press to exit.\n")
    txtb5.config(state=DISABLED)
    png1=Image.open(resource_path('1.png'))
    png1=png1.resize((950,400), Image.ANTIALIAS)
    png1 = ImageTk.PhotoImage(png1)
    root.png1=png1
    png2=Image.open(resource_path('2.png'))
    png2=png2.resize((950,400), Image.ANTIALIAS)
    png2 = ImageTk.PhotoImage(png2)
    root.png2=png2
    png3=Image.open(resource_path('3.png'))
    png3=png3.resize((950,400), Image.ANTIALIAS)
    png3 = ImageTk.PhotoImage(png3)
    root.png3=png3
    png4=Image.open(resource_path('4.png'))
    png4=png4.resize((950,400), Image.ANTIALIAS)
    png4 = ImageTk.PhotoImage(png4)
    root.png4=png4
    png5=Image.open(resource_path('5.png'))
    png5=png5.resize((950,400), Image.ANTIALIAS)
    png5 = ImageTk.PhotoImage(png5)
    root.png5=png5
    cvs.create_text(2,10,anchor=NW,justify=LEFT,font=('Standard',13,'bold'),text='1.')
    cvs.create_window(500,215,anchor=CENTER,window=Label(cvs,bd=5,image=png1,relief=RIDGE))
    cvs.create_window(500,455,window=txtb1,anchor=CENTER)
    cvs.create_text(2,495,anchor=NW,justify=LEFT,font=('Standard',13,'bold'),text='2.')
    cvs.create_window(500,700,anchor=CENTER,window=Label(cvs,bd=5,image=png2,relief=RIDGE))
    cvs.create_window(500,956,window=txtb2,anchor=CENTER)
    cvs.create_text(2,1012,anchor=NW,justify=LEFT,font=('Standard',13,'bold'),text='3.')
    cvs.create_window(500,1217,anchor=CENTER,window=Label(cvs,bd=5,image=png3,relief=RIDGE))
    cvs.create_window(500,1521,window=txtb3,anchor=CENTER)
    cvs.create_text(2,1625,anchor=NW,justify=LEFT,font=('Standard',13,'bold'),text='4.')
    cvs.create_window(500,1830,anchor=CENTER,window=Label(cvs,bd=5,image=png4,relief=RIDGE))
    cvs.create_window(500,2078,window=txtb4,anchor=CENTER)
    cvs.create_text(2,2125,anchor=NW,justify=LEFT,font=('Standard',13,'bold'),text='5.')
    cvs.create_window(500,2330,anchor=CENTER,window=Label(cvs,bd=5,image=png5,relief=RIDGE))
    cvs.create_window(500,2602,window=txtb5,anchor=CENTER)
    Button(root, text='Back', width=5, command=lambda : mains()).pack(side=BOTTOM)

def lg():
    hide()
    Label(root,bg='sky blue',font=('Standard',30,'bold'),padx=10,pady=10,relief=RIDGE,text='Welcome to Employee Management System').place(relx=0.5,rely=0.05,anchor=CENTER)
    Label(root,bg='sky blue',font=('Standard',20,'bold'),padx=10,pady=10,relief=RIDGE,text='Log In to your account').place(relx=0.5,rely=0.20,anchor=CENTER)
    Label(root,bg='sky blue', text='Username',font=('Standard',13,'bold'),padx=4,pady=4,relief=RIDGE).place(relx = 0.27, rely = 0.30,anchor=CENTER) 
    Label(root,bg='sky blue', text='Password',font=('Standard',13,'bold'),padx=4,pady=4,relief=RIDGE).place(relx = 0.27, rely = 0.35,anchor=CENTER)
    global usne
    global pswd
    usne = StringVar()
    pswd = StringVar()
    global usne_entry
    global pswd_entry
    usne_entry=Entry(root,bd=4,font='Standard',textvariable=usne,width=30)
    usne_entry.place(relx = 0.5, rely = 0.30,anchor=CENTER)
    pswd_entry=Entry(root,bd=4,font='Standard',show='*',textvariable=pswd,width=30)
    pswd_entry.place(relx = 0.5, rely = 0.35,anchor=CENTER)
    Label(root,bg='sky blue',relief=RIDGE,padx=1,pady=1,text='Password is case sensitive',font=('Standard',10,'bold')).place(relx = 0.5, rely = 0.385,anchor=CENTER)
    Button(root, text='Login', width=40,command=lambda: login()).place(relx = 0.5, rely = 0.45,anchor=CENTER)
    Button(root, text='Back', width=40,command=lambda: mains()).place(relx = 0.5, rely = 0.5,anchor=CENTER)
    Button(root, text='Exit', width=40, command=lambda: exits()).place(relx = 0.5, rely = 0.55,anchor=CENTER)

def login():
    global user
    user=usne.get().lower().strip()
    global passw
    passw=pswd.get().strip()
    usne_entry.delete(0, END)
    pswd_entry.delete(0, END)
    cursor.execute('SELECT COUNT(*) FROM Users where `Login ID`="'+user+'" AND Password="'+passw+'"')
    alog=cursor.fetchall()
    cursor.execute('SELECT COUNT(*) FROM Users where `Login ID`="'+user+'" AND Password="'+passw+'"AND Role="Administrator"')
    admc=cursor.fetchall()
    if alog[0][0] == 1 and admc[0][0] == 1:
        tkinter.messagebox.showinfo('Success', "Logged In Successfully")
        adm_hs()
    elif alog[0][0] == 1 and admc[0][0] == 0:
        tkinter.messagebox.showinfo('Success', "Logged In Successfully")
        emp_hs()
    else :
        tkinter.messagebox.showerror('Failed.Please Retry or Exit', "Login failed\nInvalid Username or Password\nPlease Try Again!")

def adm_hs():
    hide()
    cursor.execute('SELECT Username from Users where `Login ID`="'+user+'" AND Password="'+passw+'"')
    userF=cursor.fetchone()
    Canvas(root,bg='sky blue',relief=RIDGE,height=75,width=600).place(anchor=CENTER,relx=0.5,rely=0.1)
    Label(root,bg='sky blue',font=('Standard',20,'bold'),padx=10,pady=10,text='Welcome back '+userF[0]+' !').place(anchor=CENTER,relx=0.41,rely=0.1)
    Button(root, text='Manage Profile', width=20,command=lambda: mp()).place(anchor=CENTER,relx=0.7,rely=0.1)
    Button(root, text='Employee Management', width=25,command=lambda: emp()).place(anchor=CENTER,relx=0.4,rely=0.2)
    Button(root, text='Appraisal Management', width=25, command=lambda : apr()).place(anchor=CENTER,relx=0.6,rely=0.2)
    Button(root, text='Department Management', width=25,command=lambda: dep()).place(anchor=CENTER,relx=0.4,rely=0.3)
    Button(root, text='Leave Management', width=25, command=lambda : lea()).place(anchor=CENTER,relx=0.6,rely=0.3)
    Button(root, text='Project Management', width=25,command=lambda: pro()).place(anchor=CENTER,relx=0.4,rely=0.4)
    Button(root, text='Salary Management', width=25, command=lambda : sal()).place(anchor=CENTER,relx=0.6,rely=0.4)
    Button(root, text='Timesheet Management', width=25,command=lambda: tim()).place(anchor=CENTER,relx=0.4,rely=0.5)
    Button(root, text='Administrator Management', width=25,command=lambda: adms()).place(anchor=CENTER,relx=0.6,rely=0.5)
    Button(root, text='Log Out', width=25,command=lambda: mains()).place(anchor=CENTER,relx=0.4,rely=0.6)
    Button(root, text='Exit', width=25, command=lambda : exits()).place(anchor=CENTER,relx=0.6,rely=0.6)

def emp_hs():
    hide()
    cursor.execute('SELECT Username from Users where `Login ID`="'+user+'" AND Password="'+passw+'"')
    userF=cursor.fetchone()
    Canvas(root,bg='sky blue',relief=RIDGE,height=75,width=600).place(anchor=CENTER,relx=0.5,rely=0.1)
    Label(root,bg='sky blue',font=('Standard',20,'bold'),padx=10,pady=10,text='Welcome back '+userF[0]+' !').place(anchor=CENTER,relx=0.41,rely=0.1)
    Button(root, text='Manage Profile', width=20,command=lambda: mpe()).place(anchor=CENTER,relx=0.7,rely=0.1)
    Button(root, text='Employee Record', width=25,command=lambda: empe()).place(anchor=CENTER,relx=0.4,rely=0.2)
    Button(root, text='Appraisal Record', width=25, command=lambda : apre()).place(anchor=CENTER,relx=0.6,rely=0.2)
    Button(root, text='Department Record', width=25,command=lambda: depe()).place(anchor=CENTER,relx=0.4,rely=0.3)
    Button(root, text='Leave Record', width=25, command=lambda : leae()).place(anchor=CENTER,relx=0.6,rely=0.3)
    Button(root, text='Project Record', width=25,command=lambda: proe()).place(anchor=CENTER,relx=0.4,rely=0.4)
    Button(root, text='Salary Record', width=25, command=lambda : sale()).place(anchor=CENTER,relx=0.6,rely=0.4)
    Button(root, text='Timesheet Record', width=25,command=lambda: time()).place(anchor=CENTER,relx=0.5,rely=0.5)
    Button(root, text='Log Out', width=25,command=lambda: mains()).place(anchor=CENTER,relx=0.4,rely=0.6)
    Button(root, text='Exit', width=25, command=lambda : exits()).place(anchor=CENTER,relx=0.6,rely=0.6)

def mp():
    hide()
    Canvas(root,bg='sky blue',relief=RIDGE,height=750,width=700).place(anchor=CENTER,relx=0.5,rely=0.5)
    Label(root,bg='sky blue',font=('Standard',20,'bold'),padx=10,pady=10,relief=RIDGE,text='HR Record Management').place(relx=0.5,rely=0.07,anchor=CENTER)
    Button(root, text='Update', width=25,command=lambda:update_mp()).place(anchor=CENTER,relx=0.6,rely=0.15)
    global u
    cursor.execute('Describe Users;')
    u=cursor.fetchall()
    n=0.2
    for x in range(0,len(u)):
        Label(root,bg='sky blue',relief=RIDGE,width=15,text=u[x][0],font=('Standard',13,'bold')).place(relx = 0.26, rely = n,anchor=CENTER)
        n+=0.05
    cursor.execute('select * from Users where `Login ID`="'+user+'" AND Password="'+passw+'"')
    i=cursor.fetchone()
    n=0.2
    for x in range(0,len(i)):
        Entry(root,textvariable=StringVar(value=i[x]),width=45,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',13)).place(relx = 0.6, rely = n,anchor=CENTER)
        n+=0.05
    Button(root, text='Main Menu', width=25,command=lambda: adm_hs()).place(anchor=CENTER,relx=0.3,rely=0.95)
    Button(root, text='Log Out', width=25,command=lambda: mains()).place(anchor=CENTER,relx=0.5,rely=0.95)
    Button(root, text='Exit', width=25, command=lambda : exits()).place(anchor=CENTER,relx=0.7,rely=0.95)
def update_mp():
    global u
    cursor.execute('Describe Users;')
    u=cursor.fetchall()
    global i
    cursor.execute('select * from Users where `'+u[3][0]+'`="'+user+'"')
    i=cursor.fetchone()
    global D
    D={}
    global up
    up=Toplevel(bg='powder blue',relief=RIDGE)
    up.maxsize(1024,768)
    up.title('Update Record')
    Label(up,bg='sky blue',relief=RIDGE,width=48,text = 'Current Data',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    Label(up,bg='sky blue',relief=RIDGE,width=48,text ='New Data',font=('Standard',10,'bold')).grid(row = 0, column = 3,columnspan=2)
    for x in range(0,len(i)):
        Label(up,bg='sky blue',relief=RIDGE,width=10,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(up, textvariable=StringVar(up, value = i[x]),width=42,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
        Label(up,bg='sky blue',relief=RIDGE,width=10,text =u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 3)
        m = Entry(up, textvariable=StringVar(up, value = i[x]),width=42,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
        m.grid(row = x+1, column = 4)
        D[string.ascii_lowercase[x]]=m
    Button(up, text = 'Save Changes', command = lambda:edit_records_mp()).grid(row = len(u)+1,column=1,columnspan = 4)
    up.mainloop()
def edit_records_mp(*args):
    try:
        query = 'UPDATE Users SET '+u[0][0]+'=%s,'+u[1][0]+'=%s,'+u[2][0]+'=%s,`'+u[3][0]+'`=%s,'+u[4][0]+'=%s,'+u[5][0]+'=%s,'+u[6][0]+'=%s,'+u[7][0]+'=%s,'+u[8][0]+'=%s,'+u[9][0]+'=%s,'+u[10][0]+'=%s,'+u[11][0]+'=%s,'+u[12][0]+'=%s,'+u[13][0]+'=%s,'+u[14][0]+'=%s where '+u[0][0]+' = "'+i[0]+'";'
        parameters = (tuple([D[x].get() for x in D.keys()]))
        cursor.execute(query, parameters)
        query_apr = 'UPDATE Appraisal SET '+u[0][0]+'=%s where '+u[0][0]+' = "'+i[0]+'";'
        parameters_apr = tuple([D['a'].get()])
        cursor.execute(query_apr, parameters_apr)
        query_lea = 'UPDATE `Leave` SET '+u[0][0]+'=%s where '+u[0][0]+' = "'+i[0]+'";'
        parameters_lea = tuple([D['a'].get()])
        cursor.execute(query_lea, parameters_lea)
        query_sal = 'UPDATE Salary SET '+u[0][0]+'=%s where '+u[0][0]+' = "'+i[0]+'";'
        parameters_sal = tuple([D['a'].get()])
        cursor.execute(query_sal, parameters_sal)
        query_tim = 'UPDATE timesheet SET '+u[0][0]+'=%s where '+u[0][0]+' = "'+i[0]+'";'
        parameters_tim = tuple([D['a'].get()])
        cursor.execute(query_tim, parameters_tim)
        conn.commit()
        up.destroy()
        tkinter.messagebox.showinfo('Success', 'Your Record is updated successfully !')
        newr_mp()
    except mysql.connector.IntegrityError:
        tkinter.messagebox.showerror('Failed.Please Retry or Exit', "Update failed\nUpdated Fields Not Unique\nPlease Try Again !")
def newr_mp():
    cursor.execute('select * from Users where  `Login ID`="'+user+'" AND Password="'+passw+'"')
    i=cursor.fetchone()
    n=0.2
    for x in range(0,len(i)):
        Entry(root,textvariable=StringVar(value=i[x]),width=45,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',13)).place(relx = 0.6, rely = n,anchor=CENTER)
        n+=0.05

def emp():
    hide()
    Button(root, text='Delete Record', width=25,command=lambda:delete_record_emp()).place(anchor=CENTER,relx=0.8,rely=0.90)
    Button(root, text='Insert Record', width=25,command=lambda:insert_emp()).place(anchor=CENTER,relx=0.2,rely=0.90)
    Button(root, text='View Record', width=25,command=lambda:viewr_emp()).place(anchor=CENTER,relx=0.4,rely=0.90)
    Button(root, text='Update Record', width=25,command=lambda:update_emp()).place(anchor=CENTER,relx=0.6,rely=0.90)
    Button(root, text='Main Menu', width=25,command=lambda: adm_hs()).place(anchor=CENTER,relx=0.3,rely=0.95)
    Button(root, text='Log Out', width=25,command=lambda: mains()).place(anchor=CENTER,relx=0.5,rely=0.95)
    Button(root, text='Exit', width=25, command=lambda : exits()).place(anchor=CENTER,relx=0.7,rely=0.95)
    Label(root,bg='sky blue',font=('Arial',20,'bold'),padx=10,pady=10,relief=RIDGE,text='Employee Management').place(relx=0.5,rely=0.04,anchor=CENTER)
    global tr_emp
    tr_emp = ttk.Treeview(root, selectmode ='browse',height='20')
    tr_emp.place(anchor=CENTER,height=600,width=990,relx=0.499,rely=0.47)
    vers = Scrollbar(root,orient =VERTICAL,command = tr_emp.yview)
    vers.place(anchor=CENTER,relx=0.99,rely=0.47,height=600)
    tr_emp.configure(yscrollcommand = vers.set)
    hrs = Scrollbar(root,orient =HORIZONTAL,command = tr_emp.xview)
    hrs.place(anchor=CENTER,relx=0.499,rely=0.871,width=990)
    tr_emp.configure(xscrollcommand = hrs.set)
    global u
    cursor.execute('Describe Users;')
    u=cursor.fetchall()
    l=[]
    for x in range(0,len(u)): l.append(u[x][0])
    tr_emp.column('#0', width=0, stretch=NO)
    tr_emp['columns'] = l
    for x in range(0,len(u)):
        tr_emp.column(u[x][0],width=10,anchor=CENTER)
        tr_emp.heading(u[x][0],text=u[x][0],anchor=CENTER)
    cursor.execute('select * from Users where Role!="Administrator";')
    i=cursor.fetchall()
    for x in range(0,len(i)):
        tr_emp.insert("", 'end',  values =(i[x]))
def update_emp():
    global ITF
    ITF=tr_emp.item(tr_emp.focus())
    global u
    cursor.execute('Describe Users;')
    u=cursor.fetchall()
    global i
    cursor.execute('select * from Users where '+u[0][0]+'="'+str(ITF['values'][0])+'"')
    i=cursor.fetchall()
    global D
    D={}
    global up
    up=Toplevel(bg='powder blue',relief=RIDGE)
    up.maxsize(1024,768)
    up.title('Update Record')
    Label(up,bg='sky blue',relief=RIDGE,width=48,text = 'Current Data',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    Label(up,bg='sky blue',relief=RIDGE,width=48,text ='New Data',font=('Standard',10,'bold')).grid(row = 0, column = 3,columnspan=2)
    for x in range(0,len(i[0])):
        Label(up,bg='sky blue',relief=RIDGE,width=10,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(up, textvariable=StringVar(up, value = i[0][x]),width=42,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
        Label(up,bg='sky blue',relief=RIDGE,width=10,text =u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 3)
        m = Entry(up, textvariable=StringVar(up, value = i[0][x]),width=42,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
        m.grid(row = x+1, column = 4)
        D[string.ascii_lowercase[x]]=m
    Button(up, text = 'Save Changes', command = lambda:edit_records_emp()).grid(row = len(u)+1,column=1,columnspan = 4)
    up.mainloop()
def edit_records_emp(*args):
    if D['b'].get()=='Administrator':
        tkinter.messagebox.showerror('Failed.Please Retry or Exit', "Update failed\nAdministrator Update Not Available\nPlease Try in Administrator Tab !")
    else:
        try:
            query = 'UPDATE Users SET '+u[0][0]+'=%s,'+u[1][0]+'=%s,'+u[2][0]+'=%s,`'+u[3][0]+'`=%s,'+u[4][0]+'=%s,'+u[5][0]+'=%s,'+u[6][0]+'=%s,'+u[7][0]+'=%s,'+u[8][0]+'=%s,'+u[9][0]+'=%s,'+u[10][0]+'=%s,'+u[11][0]+'=%s,'+u[12][0]+'=%s,'+u[13][0]+'=%s,'+u[14][0]+'=%s where '+u[0][0]+' = "'+str(ITF['values'][0])+'";'
            parameters = (tuple([D[x].get() for x in D.keys()]))
            cursor.execute(query, parameters)
            query_apr = 'UPDATE Appraisal SET '+u[0][0]+'=%s where '+u[0][0]+' = "'+i[0][0]+'";'
            parameters_apr = tuple([D['a'].get()])
            cursor.execute(query_apr, parameters_apr)
            query_lea = 'UPDATE `Leave` SET '+u[0][0]+'=%s where '+u[0][0]+' = "'+i[0][0]+'";'
            parameters_lea = tuple([D['a'].get()])
            cursor.execute(query_lea, parameters_lea)
            query_sal = 'UPDATE Salary SET '+u[0][0]+'=%s where '+u[0][0]+' = "'+i[0][0]+'";'
            parameters_sal = tuple([D['a'].get()])
            cursor.execute(query_sal, parameters_sal)
            query_tim = 'UPDATE timesheet SET '+u[0][0]+'=%s where '+u[0][0]+' = "'+i[0][0]+'";'
            parameters_tim = tuple([D['a'].get()])
            cursor.execute(query_tim, parameters_tim)
            conn.commit()
            up.destroy()
            tkinter.messagebox.showinfo('Success', 'UID: '+str(ITF['values'][0])+' updated successfully !')
            newr_emp()
        except mysql.connector.IntegrityError:
            tkinter.messagebox.showerror('Failed.Please Retry or Exit', "Update failed\nUpdated Fields Not Unique\nPlease Try Again !")
def newr_emp():
    cursor.execute('select * from Users where Role!="Administrator";')
    i=cursor.fetchall()
    tr_emp.delete(*tr_emp.get_children())
    for x in range(0,len(i)):
        tr_emp.insert("", 'end',  values =(i[x]))
def viewr_emp():
    ITF=tr_emp.item(tr_emp.focus())
    global u
    cursor.execute('Describe Users;')
    u=cursor.fetchall()
    cursor.execute('select * from Users where '+u[0][0]+'="'+str(ITF['values'][0])+'"')
    i=cursor.fetchall()
    v=Toplevel(bg='powder blue',relief=RIDGE)
    v.maxsize(1024,768)
    v.title('View Record')
    Label(v,bg='sky blue',relief=RIDGE,width=48,text = 'Record Details',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    for x in range(0,len(i[0])):
        Label(v,bg='sky blue',relief=RIDGE,width=10,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(v, textvariable=StringVar(v, value = i[0][x]),width=42,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
    Button(v, text = 'Back', command = lambda:v.destroy()).grid(row = len(u)+1,column=1,columnspan = 4)
    v.mainloop()
def insert_emp():
    global u
    cursor.execute('Describe Users;')
    u=cursor.fetchall()
    global D
    D={}
    global ins
    ins=Toplevel(bg='powder blue',relief=RIDGE)
    ins.maxsize(1024,768)
    ins.title('Insert Record')
    Label(ins,bg='sky blue',relief=RIDGE,width=48,text ='New Record',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    for x in range(0,len(u)):
        Label(ins,bg='sky blue',relief=RIDGE,width=10,text =u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        m = Entry(ins, textvariable=StringVar(ins),width=42,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
        m.grid(row = x+1, column = 2)
        D[string.ascii_lowercase[x]]=m
    Button(ins, text = 'Save Changes', command = lambda:insert_record_emp()).grid(row = len(u)+1,column=1,columnspan = 2)
    ins.mainloop()
def insert_record_emp(*args):
    if D['b'].get()=='Administrator':
        tkinter.messagebox.showerror('Failed.Please Retry or Exit', "Insert failed\nAdministrator Insert Not Available\nPlease Try in Administrator Tab !")
    else:
        try:
            query = 'insert into Users('+u[0][0]+','+u[1][0]+','+u[2][0]+',`'+u[3][0]+'`,'+u[4][0]+','+u[5][0]+','+u[6][0]+','+u[7][0]+','+u[8][0]+','+u[9][0]+','+u[10][0]+','+u[11][0]+','+u[12][0]+','+u[13][0]+','+u[14][0]+') values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            parameters = (tuple([D[x].get() for x in D.keys()]))
            cursor.execute(query, parameters)
            conn.commit()
            ins.destroy()
            tkinter.messagebox.showinfo('Success', 'UID: '+parameters[0]+' added successfully !')
            newr_emp()
        except mysql.connector.IntegrityError:
            tkinter.messagebox.showerror('Failed.Please Retry or Exit', "Insert failed\nInserted Fields Not Unique\nPlease Try Again !")
def delete_record_emp(*args):
    global ITF
    ITF=tr_emp.item(tr_emp.focus())
    try:
        i=tkinter.messagebox.askyesno("Delete Record","Do you want to delete the selected Record ?")
        if i>0:
            cursor.execute('DELETE FROM Users where UID="'+str(ITF['values'][0])+'";')
            conn.commit()
            tkinter.messagebox.showinfo('Success', 'UID: '+str(ITF['values'][0])+' deleted successfully !')
            newr_emp()
            return
    except IndexError:
        tkinter.messagebox.showerror('Failed !', "Deletion failed\nNo record Selected\nPlease Try Again !")

def apr():
    hide()
    Button(root, text='Delete Record', width=25,command=lambda:delete_record_apr()).place(anchor=CENTER,relx=0.8,rely=0.90)
    Button(root, text='Insert Record', width=25,command=lambda:insert_apr()).place(anchor=CENTER,relx=0.2,rely=0.90)
    Button(root, text='View Record', width=25,command=lambda:viewr_apr()).place(anchor=CENTER,relx=0.4,rely=0.90)
    Button(root, text='Update Record', width=25,command=lambda:update_apr()).place(anchor=CENTER,relx=0.6,rely=0.90)
    Button(root, text='Main Menu', width=25,command=lambda: adm_hs()).place(anchor=CENTER,relx=0.3,rely=0.95)
    Button(root, text='Log Out', width=25,command=lambda: mains()).place(anchor=CENTER,relx=0.5,rely=0.95)
    Button(root, text='Exit', width=25, command=lambda : exits()).place(anchor=CENTER,relx=0.7,rely=0.95)
    Label(root,bg='sky blue',font=('Arial',20,'bold'),padx=10,pady=10,relief=RIDGE,text='Appraisal Management').place(relx=0.5,rely=0.04,anchor=CENTER)
    global tr_apr
    tr_apr = ttk.Treeview(root, selectmode ='browse',height='20')
    tr_apr.place(anchor=CENTER,height=600,width=990,relx=0.499,rely=0.47)
    vers = Scrollbar(root,orient =VERTICAL,command = tr_apr.yview)
    vers.place(anchor=CENTER,relx=0.99,rely=0.47,height=600)
    tr_apr.configure(yscrollcommand = vers.set)
    hrs = Scrollbar(root,orient =HORIZONTAL,command = tr_apr.xview)
    hrs.place(anchor=CENTER,relx=0.499,rely=0.871,width=990)
    tr_apr.configure(xscrollcommand = hrs.set)
    global u
    cursor.execute('Describe Appraisal;')
    u=cursor.fetchall()
    l=[]
    for x in range(0,len(u)): l.append(u[x][0])
    tr_apr.column('#0', width=0, stretch=NO)
    tr_apr['columns'] = l
    for x in range(0,len(u)):
        tr_apr.column(u[x][0],width=10,anchor=CENTER)
        tr_apr.heading(u[x][0],text=u[x][0],anchor=CENTER)
    global i
    cursor.execute('select * from Appraisal;')
    i=cursor.fetchall()
    for x in range(0,len(i)):
        tr_apr.insert("", 'end',  values =(i[x]))
def update_apr():
    global ITF
    ITF=tr_apr.item(tr_apr.focus())
    global u
    cursor.execute('Describe Appraisal;')
    u=cursor.fetchall()
    global i
    cursor.execute('select * from Appraisal where '+u[0][0]+'="'+str(ITF['values'][0])+'"')
    i=cursor.fetchall()
    global D
    D={}
    global up
    up=Toplevel(bg='powder blue',relief=RIDGE)
    up.maxsize(1024,768)
    up.title('Update Record')
    Label(up,bg='sky blue',relief=RIDGE,width=35,text = 'Current Data',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    Label(up,bg='sky blue',relief=RIDGE,width=35,text ='New Data',font=('Standard',10,'bold')).grid(row = 0, column = 3,columnspan=2)
    for x in range(0,len(i[0])):
        Label(up,bg='sky blue',relief=RIDGE,width=18,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(up, textvariable=StringVar(up, value = i[0][x]),width=18,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
        Label(up,bg='sky blue',relief=RIDGE,width=18,text =u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 3)
        m = Entry(up, textvariable=StringVar(up, value = i[0][x]),width=18,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
        m.grid(row = x+1, column = 4)
        D[string.ascii_lowercase[x]]=m
    Button(up, text = 'Save Changes', command = lambda:edit_records_apr()).grid(row = len(u)+1,column=1,columnspan = 4)
    up.mainloop()
def edit_records_apr(*args):
    try:
        query = 'UPDATE Appraisal SET '+u[0][0]+'=%s,`'+u[1][0]+'`=%s,`'+u[2][0]+'`=%s,`'+u[3][0]+'`=%s,`'+u[4][0]+'`=%s,`'+u[5][0]+'`=%s,`'+u[6][0]+'`=%s where '+u[0][0]+' = "'+str(ITF['values'][0])+'";'
        parameters = (tuple([D[x].get() for x in D.keys()]))
        cursor.execute(query, parameters)
        conn.commit()
        up.destroy()
        tkinter.messagebox.showinfo('Success', 'UID: '+str(ITF['values'][0])+' updated successfully !')
        newr_apr()
    except mysql.connector.IntegrityError:
        tkinter.messagebox.showerror('Failed.Please Retry or Exit', "Update failed\nUpdated Fields Not Unique\nPlease Try Again !")
def newr_apr():
    cursor.execute('select * from Appraisal;')
    i=cursor.fetchall()
    tr_apr.delete(*tr_apr.get_children())
    for x in range(0,len(i)):
        tr_apr.insert("", 'end',  values =(i[x]))
def viewr_apr():
    ITF=tr_apr.item(tr_apr.focus())
    global u
    cursor.execute('Describe Appraisal;')
    u=cursor.fetchall()
    cursor.execute('select * from Appraisal where '+u[0][0]+'="'+str(ITF['values'][0])+'"')
    i=cursor.fetchall()
    v=Toplevel(bg='powder blue',relief=RIDGE)
    v.maxsize(1024,768)
    v.title('View Record')
    Label(v,bg='sky blue',relief=RIDGE,width=35,text = 'Record Details',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    for x in range(0,len(i[0])):
        Label(v,bg='sky blue',relief=RIDGE,width=18,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(v, textvariable=StringVar(v, value = i[0][x]),width=18,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
    Button(v, text = 'Back', command = lambda:v.destroy()).grid(row = len(u)+1,column=1,columnspan = 4)
    v.mainloop()
def insert_apr():
    global u
    cursor.execute('Describe Appraisal;')
    u=cursor.fetchall()
    global D
    D={}
    global ins
    ins=Toplevel(bg='powder blue',relief=RIDGE)
    ins.maxsize(1024,768)
    ins.title('Insert Record')
    Label(ins,bg='sky blue',relief=RIDGE,width=35,text ='New Record',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    for x in range(0,len(u)):
        Label(ins,bg='sky blue',relief=RIDGE,width=18,text =u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        m = Entry(ins, textvariable=StringVar(ins),width=18,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
        m.grid(row = x+1, column = 2)
        D[string.ascii_lowercase[x]]=m
    Button(ins, text = 'Save Changes', command = lambda:insert_record_apr()).grid(row = len(u)+1,column=1,columnspan = 2)
    ins.mainloop()
def insert_record_apr(*args):
    try:
        query = 'insert into Appraisal('+u[0][0]+',`'+u[1][0]+'`,`'+u[2][0]+'`,`'+u[3][0]+'`,`'+u[4][0]+'`,`'+u[5][0]+'`,`'+u[6][0]+'`) values(%s,%s,%s,%s,%s,%s,%s);'
        parameters = (tuple([D[x].get() for x in D.keys()]))
        cursor.execute(query, parameters)
        conn.commit()
        ins.destroy()
        tkinter.messagebox.showinfo('Success', 'UID: '+parameters[0]+' added successfully !')
        newr_apr()
    except mysql.connector.IntegrityError:
        tkinter.messagebox.showerror('Failed.Please Retry or Exit', "Insert failed\nInserted Fields Not Unique\nPlease Try Again !")
def delete_record_apr(*args):
    global ITF
    ITF=tr_apr.item(tr_apr.focus())
    try:
        i=tkinter.messagebox.askyesno("Delete Record","Do you want to delete the selected Record ?")
        if i>0:
            cursor.execute('DELETE FROM Appraisal where '+u[0][0]+'="'+str(ITF['values'][0])+'";')
            conn.commit()
            tkinter.messagebox.showinfo('Success', 'UID: '+str(ITF['values'][0])+' deleted successfully !')
            newr_apr()
            return
    except IndexError:
        tkinter.messagebox.showerror('Failed !', "Deletion failed\nNo record Selected\nPlease Try Again !")

def dep():
    hide()
    Button(root, text='Delete Record', width=25,command=lambda:delete_record_dep()).place(anchor=CENTER,relx=0.8,rely=0.90)
    Button(root, text='Insert Record', width=25,command=lambda:insert_dep()).place(anchor=CENTER,relx=0.2,rely=0.90)
    Button(root, text='View Record', width=25,command=lambda:viewr_dep()).place(anchor=CENTER,relx=0.4,rely=0.90)
    Button(root, text='Update Record', width=25,command=lambda:update_dep()).place(anchor=CENTER,relx=0.6,rely=0.90)
    Button(root, text='Main Menu', width=25,command=lambda: adm_hs()).place(anchor=CENTER,relx=0.3,rely=0.95)
    Button(root, text='Log Out', width=25,command=lambda: mains()).place(anchor=CENTER,relx=0.5,rely=0.95)
    Button(root, text='Exit', width=25, command=lambda : exits()).place(anchor=CENTER,relx=0.7,rely=0.95)
    Label(root,bg='sky blue',font=('Arial',20,'bold'),padx=10,pady=10,relief=RIDGE,text='Department Management').place(relx=0.5,rely=0.04,anchor=CENTER)
    global tr_dep
    tr_dep = ttk.Treeview(root, selectmode ='browse',height='20')
    tr_dep.place(anchor=CENTER,height=600,width=990,relx=0.499,rely=0.47)
    vers = Scrollbar(root,orient =VERTICAL,command = tr_dep.yview)
    vers.place(anchor=CENTER,relx=0.99,rely=0.47,height=600)
    tr_dep.configure(yscrollcommand = vers.set)
    hrs = Scrollbar(root,orient =HORIZONTAL,command = tr_dep.xview)
    hrs.place(anchor=CENTER,relx=0.499,rely=0.871,width=990)
    tr_dep.configure(xscrollcommand = hrs.set)
    global u
    cursor.execute('Describe Department;')
    u=cursor.fetchall()
    l=[]
    for x in range(0,len(u)): l.append(u[x][0])
    tr_dep.column('#0', width=0, stretch=NO)
    tr_dep['columns'] = l
    for x in range(0,len(u)):
        tr_dep.column(u[x][0],width=10,anchor=CENTER)
        tr_dep.heading(u[x][0],text=u[x][0],anchor=CENTER)
    cursor.execute('select * from Department;')
    i=cursor.fetchall()
    for x in range(0,len(i)):
        tr_dep.insert("", 'end',  values =(i[x]))
def update_dep():
    global ITF
    ITF=tr_dep.item(tr_dep.focus())
    global u
    cursor.execute('Describe Department;')
    u=cursor.fetchall()
    cursor.execute('select * from Department where '+u[0][0]+'="'+str(ITF['values'][0])+'"')
    i=cursor.fetchall()
    global D
    D={}
    global up
    up=Toplevel(bg='powder blue',relief=RIDGE)
    up.maxsize(1024,768)
    up.title('Update Record')
    Label(up,bg='sky blue',relief=RIDGE,width=46,text = 'Current Data',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    Label(up,bg='sky blue',relief=RIDGE,width=46,text ='New Data',font=('Standard',10,'bold')).grid(row = 0, column = 3,columnspan=2)
    for x in range(0,len(i[0])):
        Label(up,bg='sky blue',relief=RIDGE,width=10,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(up, textvariable=StringVar(up, value = i[0][x]),width=40,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
        Label(up,bg='sky blue',relief=RIDGE,width=10,text =u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 3)
        m = Entry(up, textvariable=StringVar(up, value = i[0][x]),width=40,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
        m.grid(row = x+1, column = 4)
        D[string.ascii_lowercase[x]]=m
    Button(up, text = 'Save Changes', command = lambda:edit_records_dep()).grid(row = len(u)+1,column=1,columnspan = 4)
    up.mainloop()
def edit_records_dep(*args):
    try:
        query = 'UPDATE Department SET '+u[0][0]+'=%s,'+u[1][0]+'=%s where '+u[0][0]+' = "'+str(ITF['values'][0])+'";'
        parameters = (tuple([D[x].get() for x in D.keys()]))
        cursor.execute(query, parameters)
        conn.commit()
        up.destroy()
        tkinter.messagebox.showinfo('Success', 'Name: "'+str(ITF['values'][0])+'" updated successfully !')
        newr_dep()
    except mysql.connector.IntegrityError:
        tkinter.messagebox.showerror('Failed.Please Retry or Exit', "Update failed\nUpdated Fields Not Unique\nPlease Try Again !")
def newr_dep():
    cursor.execute('select * from Department;')
    i=cursor.fetchall()
    tr_dep.delete(*tr_dep.get_children())
    for x in range(0,len(i)):
        tr_dep.insert("", 'end',  values =(i[x]))
def viewr_dep():
    ITF=tr_dep.item(tr_dep.focus())
    global u
    cursor.execute('Describe Department;')
    u=cursor.fetchall()
    cursor.execute('select * from Department where '+u[0][0]+'="'+str(ITF['values'][0])+'"')
    i=cursor.fetchall()
    v=Toplevel(bg='powder blue',relief=RIDGE)
    v.maxsize(1024,768)
    v.title('View Record')
    Label(v,bg='sky blue',relief=RIDGE,width=46,text = 'Record Details',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    for x in range(0,len(i[0])):
        Label(v,bg='sky blue',relief=RIDGE,width=10,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(v, textvariable=StringVar(v, value = i[0][x]),width=40,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
    Button(v, text = 'Back', command = lambda:v.destroy()).grid(row = len(u)+1,column=1,columnspan = 4)
    v.mainloop()
def insert_dep():
    global u
    cursor.execute('Describe Department;')
    u=cursor.fetchall()
    global D
    D={}
    global ins
    ins=Toplevel(bg='powder blue',relief=RIDGE)
    ins.maxsize(1024,768)
    ins.title('Insert Record')
    Label(ins,bg='sky blue',relief=RIDGE,width=46,text ='New Record',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    for x in range(0,len(u)):
        Label(ins,bg='sky blue',relief=RIDGE,width=10,text =u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        m = Entry(ins, textvariable=StringVar(ins),width=40,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
        m.grid(row = x+1, column = 2)
        D[string.ascii_lowercase[x]]=m
    Button(ins, text = 'Save Changes', command = lambda:insert_record_dep()).grid(row = len(u)+1,column=1,columnspan = 2)
    ins.mainloop()
def insert_record_dep(*args):
    try:
        query = 'insert into Department('+u[0][0]+','+u[1][0]+') values(%s,%s);'
        parameters = (tuple([D[x].get() for x in D.keys()]))
        cursor.execute(query, parameters)
        conn.commit()
        ins.destroy()
        tkinter.messagebox.showinfo('Success', 'Name: "'+parameters[0]+'" added successfully !')
        newr_dep()
    except mysql.connector.IntegrityError:
        tkinter.messagebox.showerror('Failed.Please Retry or Exit', "Insert failed\nInserted Fields Not Unique\nPlease Try Again !")
def delete_record_dep(*args):
    global ITF
    ITF=tr_dep.item(tr_dep.focus())
    try:
        i=tkinter.messagebox.askyesno("Delete Record","Do you want to delete the selected Record ?")
        if i>0:
            cursor.execute('DELETE FROM Department where Name="'+str(ITF['values'][0])+'";')
            conn.commit()
            tkinter.messagebox.showinfo('Success', 'Name: "'+str(ITF['values'][0])+'" deleted successfully !')
            newr_dep()
            return
    except IndexError:
        tkinter.messagebox.showerror('Failed !', "Deletion failed\nNo record Selected\nPlease Try Again !")

def lea():
    hide()
    Button(root, text='Delete Record', width=25,command=lambda:delete_record_lea()).place(anchor=CENTER,relx=0.8,rely=0.90)
    Button(root, text='Insert Record', width=25,command=lambda:insert_lea()).place(anchor=CENTER,relx=0.2,rely=0.90)
    Button(root, text='View Record', width=25,command=lambda:viewr_lea()).place(anchor=CENTER,relx=0.4,rely=0.90)
    Button(root, text='Update Record', width=25,command=lambda:update_lea()).place(anchor=CENTER,relx=0.6,rely=0.90)
    Button(root, text='Main Menu', width=25,command=lambda: adm_hs()).place(anchor=CENTER,relx=0.3,rely=0.95)
    Button(root, text='Log Out', width=25,command=lambda: mains()).place(anchor=CENTER,relx=0.5,rely=0.95)
    Button(root, text='Exit', width=25, command=lambda : exits()).place(anchor=CENTER,relx=0.7,rely=0.95)
    Label(root,bg='sky blue',font=('Arial',20,'bold'),padx=10,pady=10,relief=RIDGE,text='Leave Management').place(relx=0.5,rely=0.04,anchor=CENTER)
    global tr_lea
    tr_lea = ttk.Treeview(root, selectmode ='browse',height='20')
    tr_lea.place(anchor=CENTER,height=600,width=990,relx=0.499,rely=0.47)
    vers = Scrollbar(root,orient =VERTICAL,command = tr_lea.yview)
    vers.place(anchor=CENTER,relx=0.99,rely=0.47,height=600)
    tr_lea.configure(yscrollcommand = vers.set)
    hrs = Scrollbar(root,orient =HORIZONTAL,command = tr_lea.xview)
    hrs.place(anchor=CENTER,relx=0.499,rely=0.871,width=990)
    tr_lea.configure(xscrollcommand = hrs.set)
    global u
    cursor.execute('Describe `Leave`;')
    u=cursor.fetchall()
    l=[]
    for x in range(0,len(u)): l.append(u[x][0])
    tr_lea.column('#0', width=0, stretch=NO)
    tr_lea['columns'] = l
    for x in range(0,len(u)):
        tr_lea.column(u[x][0],width=10,anchor=CENTER)
        tr_lea.heading(u[x][0],text=u[x][0],anchor=CENTER)
    cursor.execute('select * from `Leave`;')
    i=cursor.fetchall()
    for x in range(0,len(i)):
        tr_lea.insert("", 'end',  values =(i[x]))
def update_lea():
    global ITF
    ITF=tr_lea.item(tr_lea.focus())
    global u
    cursor.execute('Describe `Leave`;')
    u=cursor.fetchall()
    cursor.execute('select * from `Leave` where '+u[0][0]+'="'+str(ITF['values'][0])+'"')
    i=cursor.fetchall()
    global D
    D={}
    global up
    up=Toplevel(bg='powder blue',relief=RIDGE)
    up.maxsize(1024,768)
    up.title('Update Record')
    Label(up,bg='sky blue',relief=RIDGE,width=27,text = 'Current Data',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    Label(up,bg='sky blue',relief=RIDGE,width=27,text ='New Data',font=('Standard',10,'bold')).grid(row = 0, column = 3,columnspan=2)
    for x in range(0,len(i[0])):
        Label(up,bg='sky blue',relief=RIDGE,width=14,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(up, textvariable=StringVar(up, value = i[0][x]),width=14,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
        Label(up,bg='sky blue',relief=RIDGE,width=14,text =u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 3)
        m = Entry(up, textvariable=StringVar(up, value = i[0][x]),width=14,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
        m.grid(row = x+1, column = 4)
        D[string.ascii_lowercase[x]]=m
    Button(up, text = 'Save Changes', command = lambda:edit_records_lea()).grid(row = len(u)+1,column=1,columnspan = 4)
    up.mainloop()
def edit_records_lea(*args):
    try:
        query = 'UPDATE `Leave` SET '+u[0][0]+'=%s,'+u[1][0]+'=%s,`'+u[2][0]+'`=%s,`'+u[3][0]+'`=%s,`'+u[4][0]+'`=%s,`'+u[5][0]+'`=%s,'+u[6][0]+'=%s where '+u[0][0]+' = "'+str(ITF['values'][0])+'";'
        parameters = (tuple([D[x].get() for x in D.keys()]))
        cursor.execute(query, parameters)
        conn.commit()
        up.destroy()
        tkinter.messagebox.showinfo('Success', 'LID: '+str(ITF['values'][0])+' updated successfully !')
        newr_lea()
    except mysql.connector.IntegrityError:
        tkinter.messagebox.showerror('Failed.Please Retry or Exit', "Update failed\nUpdated Fields Not Unique\nPlease Try Again !")
def newr_lea():
    cursor.execute('select * from `Leave`;')
    i=cursor.fetchall()
    tr_lea.delete(*tr_lea.get_children())
    for x in range(0,len(i)):
        tr_lea.insert("", 'end',  values =(i[x]))
def viewr_lea():
    ITF=tr_lea.item(tr_lea.focus())
    global u
    cursor.execute('Describe `Leave`;')
    u=cursor.fetchall()
    cursor.execute('select * from `Leave` where '+u[0][0]+'="'+str(ITF['values'][0])+'"')
    i=cursor.fetchall()
    v=Toplevel(bg='powder blue',relief=RIDGE)
    v.maxsize(1024,768)
    v.title('View Record')
    Label(v,bg='sky blue',relief=RIDGE,width=27,text = 'Record Details',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    for x in range(0,len(i[0])):
        Label(v,bg='sky blue',relief=RIDGE,width=14,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(v, textvariable=StringVar(v, value = i[0][x]),width=14,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
    Button(v, text = 'Back', command = lambda:v.destroy()).grid(row = len(u)+1,column=1,columnspan = 4)
    v.mainloop()
def insert_lea():
    global u
    cursor.execute('Describe `Leave`;')
    u=cursor.fetchall()
    global D
    D={}
    global ins
    ins=Toplevel(bg='powder blue',relief=RIDGE)
    ins.maxsize(1024,768)
    ins.title('Insert Record')
    Label(ins,bg='sky blue',relief=RIDGE,width=27,text ='New Record',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    for x in range(0,len(u)):
        Label(ins,bg='sky blue',relief=RIDGE,width=14,text =u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        m = Entry(ins, textvariable=StringVar(ins),width=14,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
        m.grid(row = x+1, column = 2)
        D[string.ascii_lowercase[x]]=m
    Button(ins, text = 'Save Changes', command = lambda:insert_record_lea()).grid(row = len(u)+1,column=1,columnspan = 2)
    ins.mainloop()
def insert_record_lea(*args):
    try:
        query = 'insert into `Leave`('+u[0][0]+','+u[1][0]+',`'+u[2][0]+'`,`'+u[3][0]+'`,`'+u[4][0]+'`,`'+u[5][0]+'`,'+u[6][0]+') values(%s,%s,%s,%s,%s,%s,%s);'
        parameters = (tuple([D[x].get() for x in D.keys()]))
        cursor.execute(query, parameters)
        conn.commit()
        ins.destroy()
        tkinter.messagebox.showinfo('Success', 'LID: '+parameters[0]+' added successfully !')
        newr_lea()
    except mysql.connector.IntegrityError:
        tkinter.messagebox.showerror('Failed.Please Retry or Exit', "Insert failed\nInserted Fields Not Unique\nPlease Try Again !")
def delete_record_lea(*args):
    global ITF
    ITF=tr_lea.item(tr_lea.focus())
    try:
        i=tkinter.messagebox.askyesno("Delete Record","Do you want to delete the selected Record ?")
        if i>0:
            cursor.execute('DELETE FROM `Leave` where LID="'+str(ITF['values'][0])+'";')
            conn.commit()
            tkinter.messagebox.showinfo('Success', 'LID: '+str(ITF['values'][0])+' deleted successfully !')
            newr_lea()
            return
    except IndexError:
        tkinter.messagebox.showerror('Failed !', "Deletion failed\nNo record Selected\nPlease Try Again !")

def pro():
    hide()
    Button(root, text='Delete Record', width=25,command=lambda:delete_record_pro()).place(anchor=CENTER,relx=0.8,rely=0.90)
    Button(root, text='Insert Record', width=25,command=lambda:insert_pro()).place(anchor=CENTER,relx=0.2,rely=0.90)
    Button(root, text='View Record', width=25,command=lambda:viewr_pro()).place(anchor=CENTER,relx=0.4,rely=0.90)
    Button(root, text='Update Record', width=25,command=lambda:update_pro()).place(anchor=CENTER,relx=0.6,rely=0.90)
    Button(root, text='Main Menu', width=25,command=lambda: adm_hs()).place(anchor=CENTER,relx=0.3,rely=0.95)
    Button(root, text='Log Out', width=25,command=lambda: mains()).place(anchor=CENTER,relx=0.5,rely=0.95)
    Button(root, text='Exit', width=25, command=lambda : exits()).place(anchor=CENTER,relx=0.7,rely=0.95)
    Label(root,bg='sky blue',font=('Arial',20,'bold'),padx=10,pady=10,relief=RIDGE,text='Project Management').place(relx=0.5,rely=0.04,anchor=CENTER)
    global tr_pro
    tr_pro = ttk.Treeview(root, selectmode ='browse',height='20')
    tr_pro.place(anchor=CENTER,height=600,width=990,relx=0.499,rely=0.47)
    vers = Scrollbar(root,orient =VERTICAL,command = tr_pro.yview)
    vers.place(anchor=CENTER,relx=0.99,rely=0.47,height=600)
    tr_pro.configure(yscrollcommand = vers.set)
    hrs = Scrollbar(root,orient =HORIZONTAL,command = tr_pro.xview)
    hrs.place(anchor=CENTER,relx=0.499,rely=0.871,width=990)
    tr_pro.configure(xscrollcommand = hrs.set)
    global u
    cursor.execute('Describe Project;')
    u=cursor.fetchall()
    l=[]
    for x in range(0,len(u)): l.append(u[x][0])
    tr_pro.column('#0', width=0, stretch=NO)
    tr_pro['columns'] = l
    for x in range(0,len(u)):
        tr_pro.column(u[x][0],width=10,anchor=CENTER)
        tr_pro.heading(u[x][0],text=u[x][0],anchor=CENTER)
    cursor.execute('select * from Project;')
    i=cursor.fetchall()
    for x in range(0,len(i)):
        tr_pro.insert("", 'end',  values =(i[x]))
def update_pro():
    global ITF
    ITF=tr_pro.item(tr_pro.focus())
    global u
    cursor.execute('Describe Project;')
    u=cursor.fetchall()
    cursor.execute('select * from Project where '+u[0][0]+'="'+str(ITF['values'][0])+'"')
    i=cursor.fetchall()
    global D
    D={}
    global up
    up=Toplevel(bg='powder blue',relief=RIDGE)
    up.maxsize(1024,768)
    up.title('Update Record')
    Label(up,bg='sky blue',relief=RIDGE,width=46,text = 'Current Data',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    Label(up,bg='sky blue',relief=RIDGE,width=46,text ='New Data',font=('Standard',10,'bold')).grid(row = 0, column = 3,columnspan=2)
    for x in range(0,len(i[0])):
        Label(up,bg='sky blue',relief=RIDGE,width=14,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(up, textvariable=StringVar(up, value = i[0][x]),width=35,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
        Label(up,bg='sky blue',relief=RIDGE,width=14,text =u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 3)
        m = Entry(up, textvariable=StringVar(up, value = i[0][x]),width=35,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
        m.grid(row = x+1, column = 4)
        D[string.ascii_lowercase[x]]=m
    Button(up, text = 'Save Changes', command = lambda:edit_records_pro()).grid(row = len(u)+1,column=1,columnspan = 4)
    up.mainloop()
def edit_records_pro(*args):
    try:
        query = 'UPDATE Project SET '+u[0][0]+'=%s,`'+u[1][0]+'`=%s,`'+u[2][0]+'`=%s,'+u[3][0]+'=%s where '+u[0][0]+' = "'+str(ITF['values'][0])+'";'
        parameters = (tuple([D[x].get() for x in D.keys()]))
        cursor.execute(query, parameters)
        conn.commit()
        up.destroy()
        tkinter.messagebox.showinfo('Success', 'Title: "'+str(ITF['values'][0])+'" updated successfully !')
        newr_pro()
    except mysql.connector.IntegrityError:
        tkinter.messagebox.showerror('Failed.Please Retry or Exit', "Update failed\nUpdated Fields Not Unique\nPlease Try Again !")
def newr_pro():
    cursor.execute('select * from Project;')
    i=cursor.fetchall()
    tr_pro.delete(*tr_pro.get_children())
    for x in range(0,len(i)):
        tr_pro.insert("", 'end',  values =(i[x]))
def viewr_pro():
    ITF=tr_pro.item(tr_pro.focus())
    global u
    cursor.execute('Describe Project;')
    u=cursor.fetchall()
    cursor.execute('select * from Project where '+u[0][0]+'="'+str(ITF['values'][0])+'"')
    i=cursor.fetchall()
    v=Toplevel(bg='powder blue',relief=RIDGE)
    v.maxsize(1024,768)
    v.title('View Record')
    Label(v,bg='sky blue',relief=RIDGE,width=46,text = 'Record Details',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    for x in range(0,len(i[0])):
        Label(v,bg='sky blue',relief=RIDGE,width=14,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(v, textvariable=StringVar(v, value = i[0][x]),width=35,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
    Button(v, text = 'Back', command = lambda:v.destroy()).grid(row = len(u)+1,column=1,columnspan = 4)
    v.mainloop()
def insert_pro():
    global u
    cursor.execute('Describe Project;')
    u=cursor.fetchall()
    global D
    D={}
    global ins
    ins=Toplevel(bg='powder blue',relief=RIDGE)
    ins.maxsize(1024,768)
    ins.title('Insert Record')
    Label(ins,bg='sky blue',relief=RIDGE,width=46,text ='New Record',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    for x in range(0,len(u)):
        Label(ins,bg='sky blue',relief=RIDGE,width=14,text =u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        m = Entry(ins, textvariable=StringVar(ins),width=35,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
        m.grid(row = x+1, column = 2)
        D[string.ascii_lowercase[x]]=m
    Button(ins, text = 'Save Changes', command = lambda:insert_record_pro()).grid(row = len(u)+1,column=1,columnspan = 2)
    ins.mainloop()
def insert_record_pro(*args):
    try:
        query = 'insert into Project('+u[0][0]+',`'+u[1][0]+'`,`'+u[2][0]+'`,'+u[3][0]+') values(%s,%s,%s,%s);'
        parameters = (tuple([D[x].get() for x in D.keys()]))
        cursor.execute(query, parameters)
        conn.commit()
        ins.destroy()
        tkinter.messagebox.showinfo('Success', 'Title: "'+parameters[0]+'" added successfully !')
        newr_pro()
    except mysql.connector.IntegrityError:
        tkinter.messagebox.showerror('Failed.Please Retry or Exit', "Insert failed\nInserted Fields Not Unique\nPlease Try Again !")
def delete_record_pro(*args):
    global ITF
    ITF=tr_pro.item(tr_pro.focus())
    try:
        i=tkinter.messagebox.askyesno("Delete Record","Do you want to delete the selected Record ?")
        if i>0:
            cursor.execute('DELETE FROM Project where Title="'+str(ITF['values'][0])+'";')
            conn.commit()
            tkinter.messagebox.showinfo('Success', 'Title: "'+str(ITF['values'][0])+'" deleted successfully !')
            newr_pro()
            return
    except IndexError:
        tkinter.messagebox.showerror('Failed !', "Deletion failed\nNo record Selected\nPlease Try Again !")

def sal():
    hide()
    Button(root, text='Delete Record', width=25,command=lambda:delete_record_sal()).place(anchor=CENTER,relx=0.8,rely=0.90)
    Button(root, text='Insert Record', width=25,command=lambda:insert_sal()).place(anchor=CENTER,relx=0.2,rely=0.90)
    Button(root, text='View Record', width=25,command=lambda:viewr_sal()).place(anchor=CENTER,relx=0.4,rely=0.90)
    Button(root, text='Update Record', width=25,command=lambda:update_sal()).place(anchor=CENTER,relx=0.6,rely=0.90)
    Button(root, text='Main Menu', width=25,command=lambda: adm_hs()).place(anchor=CENTER,relx=0.3,rely=0.95)
    Button(root, text='Log Out', width=25,command=lambda: mains()).place(anchor=CENTER,relx=0.5,rely=0.95)
    Button(root, text='Exit', width=25, command=lambda : exits()).place(anchor=CENTER,relx=0.7,rely=0.95)
    Label(root,bg='sky blue',font=('Arial',20,'bold'),padx=10,pady=10,relief=RIDGE,text='Salary Management').place(relx=0.5,rely=0.04,anchor=CENTER)
    global tr_sal
    tr_sal = ttk.Treeview(root, selectmode ='browse',height='20')
    tr_sal.place(anchor=CENTER,height=600,width=990,relx=0.499,rely=0.47)
    vers = Scrollbar(root,orient =VERTICAL,command = tr_sal.yview)
    vers.place(anchor=CENTER,relx=0.99,rely=0.47,height=600)
    tr_sal.configure(yscrollcommand = vers.set)
    hrs = Scrollbar(root,orient =HORIZONTAL,command = tr_sal.xview)
    hrs.place(anchor=CENTER,relx=0.499,rely=0.871,width=990)
    tr_sal.configure(xscrollcommand = hrs.set)
    global u
    cursor.execute('Describe Salary;')
    u=cursor.fetchall()
    l=[]
    for x in range(0,len(u)): l.append(u[x][0])
    tr_sal.column('#0', width=0, stretch=NO)
    tr_sal['columns'] = l
    for x in range(0,len(u)):
        tr_sal.column(u[x][0],width=10,anchor=CENTER)
        tr_sal.heading(u[x][0],text=u[x][0],anchor=CENTER)
    cursor.execute('select * from Salary;')
    i=cursor.fetchall()
    for x in range(0,len(i)):
        tr_sal.insert("", 'end',  values =(i[x]))
def update_sal():
    global ITF
    ITF=tr_sal.item(tr_sal.focus())
    global u
    cursor.execute('Describe Salary;')
    u=cursor.fetchall()
    cursor.execute('select * from Salary where '+u[0][0]+'="'+str(ITF['values'][0])+'"')
    i=cursor.fetchall()
    global D
    D={}
    global up
    up=Toplevel(bg='powder blue',relief=RIDGE)
    up.maxsize(1024,768)
    up.title('Update Record')
    Label(up,bg='sky blue',relief=RIDGE,width=27,text = 'Current Data',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    Label(up,bg='sky blue',relief=RIDGE,width=27,text ='New Data',font=('Standard',10,'bold')).grid(row = 0, column = 3,columnspan=2)
    for x in range(0,len(i[0])):
        Label(up,bg='sky blue',relief=RIDGE,width=13,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(up, textvariable=StringVar(up, value = i[0][x]),width=15,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
        Label(up,bg='sky blue',relief=RIDGE,width=13,text =u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 3)
        m = Entry(up, textvariable=StringVar(up, value = i[0][x]),width=15,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
        m.grid(row = x+1, column = 4)
        D[string.ascii_lowercase[x]]=m
    Button(up, text = 'Save Changes', command = lambda:edit_records_sal()).grid(row = len(u)+1,column=1,columnspan = 4)
    up.mainloop()
def edit_records_sal(*args):
    try:
        query = 'UPDATE Salary SET '+u[0][0]+'=%s,'+u[1][0]+'=%s,`'+u[2][0]+'`=%s,'+u[3][0]+'=%s,'+u[4][0]+'=%s,'+u[5][0]+'=%s,'+u[6][0]+'=%s,'+u[7][0]+'=%s,'+u[8][0]+'=%s,'+u[9][0]+'=%s,'+u[10][0]+'=%s,'+u[11][0]+'=%s,'+u[12][0]+'=%s,'+u[13][0]+'=%s,'+u[14][0]+'=%s,'+u[15][0]+'=%s where '+u[0][0]+' = "'+str(ITF['values'][0])+'";'
        parameters = (tuple([D[x].get() for x in D.keys()]))
        cursor.execute(query, parameters)
        conn.commit()
        up.destroy()
        tkinter.messagebox.showinfo('Success', 'UID: '+str(ITF['values'][0])+' updated successfully !')
        newr_sal()
    except mysql.connector.IntegrityError:
        tkinter.messagebox.showerror('Failed.Please Retry or Exit', "Update failed\nUpdated Fields Not Unique\nPlease Try Again !")
def newr_sal():
    cursor.execute('select * from Salary;')
    i=cursor.fetchall()
    tr_sal.delete(*tr_sal.get_children())
    for x in range(0,len(i)):
        tr_sal.insert("", 'end',  values =(i[x]))
def viewr_sal():
    ITF=tr_sal.item(tr_sal.focus())
    global u
    cursor.execute('Describe Salary;')
    u=cursor.fetchall()
    cursor.execute('select * from Salary where '+u[0][0]+'="'+str(ITF['values'][0])+'"')
    i=cursor.fetchall()
    v=Toplevel(bg='powder blue',relief=RIDGE)
    v.maxsize(1024,768)
    v.title('View Record')
    Label(v,bg='sky blue',relief=RIDGE,width=27,text = 'Record Details',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    for x in range(0,len(i[0])):
        Label(v,bg='sky blue',relief=RIDGE,width=13,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(v, textvariable=StringVar(v, value = i[0][x]),width=15,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
    Button(v, text = 'Back', command = lambda:v.destroy()).grid(row = len(u)+1,column=1,columnspan = 4)
    v.mainloop()
def insert_sal():
    global u
    cursor.execute('Describe Salary;')
    u=cursor.fetchall()
    global D
    D={}
    global ins
    ins=Toplevel(bg='powder blue',relief=RIDGE)
    ins.maxsize(1024,768)
    ins.title('Insert Record')
    Label(ins,bg='sky blue',relief=RIDGE,width=27,text ='New Record',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    for x in range(0,len(u)):
        Label(ins,bg='sky blue',relief=RIDGE,width=13,text =u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        m = Entry(ins, textvariable=StringVar(ins),width=15,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
        m.grid(row = x+1, column = 2)
        D[string.ascii_lowercase[x]]=m
    Button(ins, text = 'Save Changes', command = lambda:insert_record_sal()).grid(row = len(u)+1,column=1,columnspan = 2)
    ins.mainloop()
def insert_record_sal(*args):
    try:
        query = 'insert into Salary('+u[0][0]+','+u[1][0]+',`'+u[2][0]+'`,'+u[3][0]+','+u[4][0]+','+u[5][0]+','+u[6][0]+','+u[7][0]+','+u[8][0]+','+u[9][0]+','+u[10][0]+','+u[11][0]+','+u[12][0]+','+u[13][0]+','+u[14][0]+','+u[15][0]+') values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        parameters = (tuple([D[x].get() for x in D.keys()]))
        cursor.execute(query, parameters)
        conn.commit()
        ins.destroy()
        tkinter.messagebox.showinfo('Success', 'UID: '+parameters[0]+' added successfully !')
        newr_sal()
    except mysql.connector.IntegrityError:
        tkinter.messagebox.showerror('Failed.Please Retry or Exit', "Insert failed\nInserted Fields Not Unique\nPlease Try Again !")
def delete_record_sal(*args):
    global ITF
    ITF=tr_sal.item(tr_sal.focus())
    try:
        i=tkinter.messagebox.askyesno("Delete Record","Do you want to delete the selected Record ?")
        if i>0:
            cursor.execute('DELETE FROM Salary where UID="'+str(ITF['values'][0])+'";')
            conn.commit()
            tkinter.messagebox.showinfo('Success', 'UID: '+str(ITF['values'][0])+' deleted successfully !')
            newr_sal()
            return
    except IndexError:
        tkinter.messagebox.showerror('Failed !', "Deletion failed\nNo record Selected\nPlease Try Again !")

def tim():
    hide()
    Button(root, text='Delete Record', width=25,command=lambda:delete_record_tim()).place(anchor=CENTER,relx=0.8,rely=0.90)
    Button(root, text='Insert Record', width=25,command=lambda:insert_tim()).place(anchor=CENTER,relx=0.2,rely=0.90)
    Button(root, text='View Record', width=25,command=lambda:viewr_tim()).place(anchor=CENTER,relx=0.4,rely=0.90)
    Button(root, text='Update Record', width=25,command=lambda:update_tim()).place(anchor=CENTER,relx=0.6,rely=0.90)
    Button(root, text='Main Menu', width=25,command=lambda: adm_hs()).place(anchor=CENTER,relx=0.3,rely=0.95)
    Button(root, text='Log Out', width=25,command=lambda: mains()).place(anchor=CENTER,relx=0.5,rely=0.95)
    Button(root, text='Exit', width=25, command=lambda : exits()).place(anchor=CENTER,relx=0.7,rely=0.95)
    Label(root,bg='sky blue',font=('Arial',20,'bold'),padx=10,pady=10,relief=RIDGE,text='Timesheet Management').place(relx=0.5,rely=0.04,anchor=CENTER)
    global tr_tim
    tr_tim = ttk.Treeview(root, selectmode ='browse',height='20')
    tr_tim.place(anchor=CENTER,height=600,width=990,relx=0.499,rely=0.47)
    vers = Scrollbar(root,orient =VERTICAL,command = tr_tim.yview)
    vers.place(anchor=CENTER,relx=0.99,rely=0.47,height=600)
    tr_tim.configure(yscrollcommand = vers.set)
    hrs = Scrollbar(root,orient =HORIZONTAL,command = tr_tim.xview)
    hrs.place(anchor=CENTER,relx=0.499,rely=0.871,width=990)
    tr_tim.configure(xscrollcommand = hrs.set)
    global u
    cursor.execute('Describe Timesheet;')
    u=cursor.fetchall()
    l=[]
    for x in range(0,len(u)): l.append(u[x][0])
    tr_tim.column('#0', width=0, stretch=NO)
    tr_tim['columns'] = l
    for x in range(0,len(u)):
        tr_tim.column(u[x][0],width=10,anchor=CENTER)
        tr_tim.heading(u[x][0],text=u[x][0],anchor=CENTER)
    cursor.execute('select * from Timesheet;')
    i=cursor.fetchall()
    for x in range(0,len(i)):
        tr_tim.insert("", 'end',  values =(i[x]))
def update_tim():
    global ITF
    ITF=tr_tim.item(tr_tim.focus())
    global u
    cursor.execute('Describe Timesheet;')
    u=cursor.fetchall()
    cursor.execute('select * from Timesheet where '+u[0][0]+'="'+str(ITF['values'][0])+'"')
    i=cursor.fetchall()
    global D
    D={}
    global up
    up=Toplevel(bg='powder blue',relief=RIDGE)
    up.maxsize(1024,768)
    up.title('Update Record')
    Label(up,bg='sky blue',relief=RIDGE,width=48,text = 'Current Data',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    Label(up,bg='sky blue',relief=RIDGE,width=48,text ='New Data',font=('Standard',10,'bold')).grid(row = 0, column = 3,columnspan=2)
    for x in range(0,len(i[0])):
        Label(up,bg='sky blue',relief=RIDGE,width=10,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(up, textvariable=StringVar(up, value = i[0][x]),width=42,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
        Label(up,bg='sky blue',relief=RIDGE,width=10,text =u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 3)
        m = Entry(up, textvariable=StringVar(up, value = i[0][x]),width=42,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
        m.grid(row = x+1, column = 4)
        D[string.ascii_lowercase[x]]=m
    Button(up, text = 'Save Changes', command = lambda:edit_records_tim()).grid(row = len(u)+1,column=1,columnspan = 4)
    up.mainloop()
def edit_records_tim(*args):
    try:
        query = 'UPDATE Timesheet SET '+u[0][0]+'=%s,'+u[1][0]+'=%s,'+u[2][0]+'=%s,'+u[3][0]+'=%s,`'+u[4][0]+'`=%s,'+u[5][0]+'=%s,'+u[6][0]+'=%s,'+u[7][0]+'=%s where '+u[0][0]+' = "'+str(ITF['values'][0])+'";'
        parameters = (tuple([D[x].get() for x in D.keys()]))
        cursor.execute(query, parameters)
        conn.commit()
        up.destroy()
        tkinter.messagebox.showinfo('Success', 'TID: '+str(ITF['values'][0])+' updated successfully !')
        newr_tim()
    except mysql.connector.IntegrityError:
        tkinter.messagebox.showerror('Failed.Please Retry or Exit', "Update failed\nUpdated Fields Not Unique\nPlease Try Again !")
def newr_tim():
    cursor.execute('select * from Timesheet;')
    i=cursor.fetchall()
    tr_tim.delete(*tr_tim.get_children())
    for x in range(0,len(i)):
        tr_tim.insert("", 'end',  values =(i[x]))
def viewr_tim():
    ITF=tr_tim.item(tr_tim.focus())
    global u
    cursor.execute('Describe Timesheet;')
    u=cursor.fetchall()
    cursor.execute('select * from Timesheet where '+u[0][0]+'="'+str(ITF['values'][0])+'"')
    i=cursor.fetchall()
    v=Toplevel(bg='powder blue',relief=RIDGE)
    v.maxsize(1024,768)
    v.title('View Record')
    Label(v,bg='sky blue',relief=RIDGE,width=48,text = 'Record Details',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    for x in range(0,len(i[0])):
        Label(v,bg='sky blue',relief=RIDGE,width=10,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(v, textvariable=StringVar(v, value = i[0][x]),width=42,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
    Button(v, text = 'Back', command = lambda:v.destroy()).grid(row = len(u)+1,column=1,columnspan = 4)
    v.mainloop()
def insert_tim():
    global u
    cursor.execute('Describe Timesheet;')
    u=cursor.fetchall()
    global D
    D={}
    global ins
    ins=Toplevel(bg='powder blue',relief=RIDGE)
    ins.maxsize(1024,768)
    ins.title('Insert Record')
    Label(ins,bg='sky blue',relief=RIDGE,width=48,text ='New Record',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    for x in range(0,len(u)):
        Label(ins,bg='sky blue',relief=RIDGE,width=10,text =u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        m = Entry(ins, textvariable=StringVar(ins),width=42,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
        m.grid(row = x+1, column = 2)
        D[string.ascii_lowercase[x]]=m
    Button(ins, text = 'Save Changes', command = lambda:insert_record_tim()).grid(row = len(u)+1,column=1,columnspan = 2)
    ins.mainloop()
def insert_record_tim(*args):
    try:
        query = 'insert into Timesheet('+u[0][0]+','+u[1][0]+','+u[2][0]+','+u[3][0]+',`'+u[4][0]+'`,'+u[5][0]+','+u[6][0]+','+u[7][0]+') values(%s,%s,%s,%s,%s,%s,%s,%s);'
        parameters = (tuple([D[x].get() for x in D.keys()]))
        cursor.execute(query, parameters)
        conn.commit()
        ins.destroy()
        tkinter.messagebox.showinfo('Success', 'TID: '+parameters[0]+' added successfully !')
        newr_tim()
    except mysql.connector.IntegrityError:
        tkinter.messagebox.showerror('Failed.Please Retry or Exit', "Insert failed\nInserted Fields Not Unique\nPlease Try Again !")
def delete_record_tim(*args):
    global ITF
    ITF=tr_tim.item(tr_tim.focus())
    try:
        i=tkinter.messagebox.askyesno("Delete Record","Do you want to delete the selected Record ?")
        if i>0:
            cursor.execute('DELETE FROM Timesheet where TID="'+str(ITF['values'][0])+'";')
            conn.commit()
            tkinter.messagebox.showinfo('Success', 'TID: '+str(ITF['values'][0])+' deleted successfully !')
            newr_tim()
            return
    except IndexError:
        tkinter.messagebox.showerror('Failed !', "Deletion failed\nNo record Selected\nPlease Try Again !")

def adms():
    hide()
    Button(root, text='Delete Record', width=25,command=lambda:delete_record_adms()).place(anchor=CENTER,relx=0.8,rely=0.90)
    Button(root, text='Insert Record', width=25,command=lambda:insert_adms()).place(anchor=CENTER,relx=0.2,rely=0.90)
    Button(root, text='View Record', width=25,command=lambda:viewr_adms()).place(anchor=CENTER,relx=0.4,rely=0.90)
    Button(root, text='Update Record', width=25,command=lambda:update_adms()).place(anchor=CENTER,relx=0.6,rely=0.90)
    Button(root, text='Main Menu', width=25,command=lambda: adm_hs()).place(anchor=CENTER,relx=0.3,rely=0.95)
    Button(root, text='Log Out', width=25,command=lambda: mains()).place(anchor=CENTER,relx=0.5,rely=0.95)
    Button(root, text='Exit', width=25, command=lambda : exits()).place(anchor=CENTER,relx=0.7,rely=0.95)
    Label(root,bg='sky blue',font=('Arial',20,'bold'),padx=10,pady=10,relief=RIDGE,text='Administrator Management').place(relx=0.5,rely=0.04,anchor=CENTER)
    global tr_adms
    tr_adms = ttk.Treeview(root, selectmode ='browse',height='20')
    tr_adms.place(anchor=CENTER,height=600,width=990,relx=0.499,rely=0.47)
    vers = Scrollbar(root,orient =VERTICAL,command = tr_adms.yview)
    vers.place(anchor=CENTER,relx=0.99,rely=0.47,height=600)
    tr_adms.configure(yscrollcommand = vers.set)
    hrs = Scrollbar(root,orient =HORIZONTAL,command = tr_adms.xview)
    hrs.place(anchor=CENTER,relx=0.499,rely=0.871,width=990)
    tr_adms.configure(xscrollcommand = hrs.set)
    global u
    cursor.execute('Describe Users;')
    u=cursor.fetchall()
    l=[]
    for x in range(0,len(u)): l.append(u[x][0])
    tr_adms.column('#0', width=0, stretch=NO)
    tr_adms['columns'] = l
    for x in range(0,len(u)):
        tr_adms.column(u[x][0],width=10,anchor=CENTER)
        tr_adms.heading(u[x][0],text=u[x][0],anchor=CENTER)
    cursor.execute('select * from Users where Role="Administrator";')
    i=cursor.fetchall()
    for x in range(0,len(i)):
        tr_adms.insert("", 'end',  values =(i[x]))
def update_adms():
    global ITF
    ITF=tr_adms.item(tr_adms.focus())
    global u
    cursor.execute('Describe Users;')
    u=cursor.fetchall()
    cursor.execute('select * from Users where '+u[0][0]+'="'+str(ITF['values'][0])+'"')
    i=cursor.fetchall()
    global D
    D={}
    global up
    up=Toplevel(bg='powder blue',relief=RIDGE)
    up.maxsize(1024,768)
    up.title('Update Record')
    Label(up,bg='sky blue',relief=RIDGE,width=48,text = 'Current Data',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    Label(up,bg='sky blue',relief=RIDGE,width=48,text ='New Data',font=('Standard',10,'bold')).grid(row = 0, column = 3,columnspan=2)
    for x in range(0,len(i[0])):
        Label(up,bg='sky blue',relief=RIDGE,width=10,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(up, textvariable=StringVar(up, value = i[0][x]),width=42,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
        Label(up,bg='sky blue',relief=RIDGE,width=10,text =u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 3)
        m = Entry(up, textvariable=StringVar(up, value = i[0][x]),width=42,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
        m.grid(row = x+1, column = 4)
        D[string.ascii_lowercase[x]]=m
    Button(up, text = 'Save Changes', command = lambda:edit_records_adms()).grid(row = len(u)+1,column=1,columnspan = 4)
    up.mainloop()
def edit_records_adms(*args):
    try:
        query = 'UPDATE Users SET '+u[0][0]+'=%s,'+u[1][0]+'=%s,'+u[2][0]+'=%s,`'+u[3][0]+'`=%s,'+u[4][0]+'=%s,'+u[5][0]+'=%s,'+u[6][0]+'=%s,'+u[7][0]+'=%s,'+u[8][0]+'=%s,'+u[9][0]+'=%s,'+u[10][0]+'=%s,'+u[11][0]+'=%s,'+u[12][0]+'=%s,'+u[13][0]+'=%s,'+u[14][0]+'=%s where '+u[0][0]+' = "'+str(ITF['values'][0])+'";'
        parameters = (tuple([D[x].get() for x in D.keys()]))
        cursor.execute(query, parameters)
        conn.commit()
        up.destroy()
        tkinter.messagebox.showinfo('Success', 'UID: '+str(ITF['values'][0])+' updated successfully !')
        newr_adms()
    except mysql.connector.IntegrityError:
        tkinter.messagebox.showerror('Failed.Please Retry or Exit', "Update failed\nUpdated Fields Not Unique\nPlease Try Again !")
def newr_adms():
    cursor.execute('select * from Users where Role="Administrator";')
    i=cursor.fetchall()
    tr_adms.delete(*tr_adms.get_children())
    for x in range(0,len(i)):
        tr_adms.insert("", 'end',  values =(i[x]))
def viewr_adms():
    ITF=tr_adms.item(tr_adms.focus())
    global u
    cursor.execute('Describe Users;')
    u=cursor.fetchall()
    cursor.execute('select * from Users where '+u[0][0]+'="'+str(ITF['values'][0])+'"')
    i=cursor.fetchall()
    v=Toplevel(bg='powder blue',relief=RIDGE)
    v.maxsize(1024,768)
    v.title('View Record')
    Label(v,bg='sky blue',relief=RIDGE,width=48,text = 'Record Details',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    for x in range(0,len(i[0])):
        Label(v,bg='sky blue',relief=RIDGE,width=10,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(v, textvariable=StringVar(v, value = i[0][x]),width=42,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
    Button(v, text = 'Back', command = lambda:v.destroy()).grid(row = len(u)+1,column=1,columnspan = 4)
    v.mainloop()
def insert_adms():
    global u
    cursor.execute('Describe Users;')
    u=cursor.fetchall()
    global D
    D={}
    global ins
    ins=Toplevel(bg='powder blue',relief=RIDGE)
    ins.maxsize(1024,768)
    ins.title('Insert Record')
    Label(ins,bg='sky blue',relief=RIDGE,width=48,text ='New Record',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    for x in range(0,len(u)):
        Label(ins,bg='sky blue',relief=RIDGE,width=10,text =u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        m = Entry(ins, textvariable=StringVar(ins),width=42,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
        m.grid(row = x+1, column = 2)
        D[string.ascii_lowercase[x]]=m
    Button(ins, text = 'Save Changes', command = lambda:insert_record_adms()).grid(row = len(u)+1,column=1,columnspan = 2)
    ins.mainloop()
def insert_record_adms(*args):
    try:
        query = 'insert into Users('+u[0][0]+','+u[1][0]+','+u[2][0]+',`'+u[3][0]+'`,'+u[4][0]+','+u[5][0]+','+u[6][0]+','+u[7][0]+','+u[8][0]+','+u[9][0]+','+u[10][0]+','+u[11][0]+','+u[12][0]+','+u[13][0]+','+u[14][0]+') values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        parameters = (tuple([D[x].get() for x in D.keys()]))
        cursor.execute(query, parameters)
        conn.commit()
        ins.destroy()
        tkinter.messagebox.showinfo('Success', 'UID: '+parameters[0]+' added successfully !')
        newr_adms()
    except mysql.connector.IntegrityError:
        tkinter.messagebox.showerror('Failed.Please Retry or Exit', "Insert failed\nInserted Fields Not Unique\nPlease Try Again !")
def delete_record_adms(*args):
    global ITF
    ITF=tr_adms.item(tr_adms.focus())
    try:
        i=tkinter.messagebox.askyesno("Delete Record","Do you want to delete the selected Record ?")
        if i>0:
            cursor.execute('DELETE FROM Users where UID="'+str(ITF['values'][0])+'";')
            conn.commit()
            tkinter.messagebox.showinfo('Success', 'UID: '+str(ITF['values'][0])+' deleted successfully !')
            newr_adms()
            return
    except IndexError:
        tkinter.messagebox.showerror('Failed !', "Deletion failed\nNo record Selected\nPlease Try Again !")

def mpe():
    hide()
    Canvas(root,bg='sky blue',relief=RIDGE,height=750,width=700).place(anchor=CENTER,relx=0.5,rely=0.5)
    Label(root,bg='sky blue',font=('Standard',20,'bold'),padx=10,pady=10,relief=RIDGE,text='My Record').place(relx=0.5,rely=0.07,anchor=CENTER)
    Button(root, text='Update', width=25,command=lambda:update_mpe()).place(anchor=CENTER,relx=0.6,rely=0.15)
    global u
    cursor.execute('Describe Users;')
    u=cursor.fetchall()
    n=0.2
    for x in range(0,len(u)):
        Label(root,bg='sky blue',relief=RIDGE,width=15,text=u[x][0],font=('Standard',13,'bold')).place(relx = 0.26, rely = n,anchor=CENTER)
        n+=0.05
    global i
    cursor.execute('select * from Users where `Login ID`="'+user+'" AND Password="'+passw+'"')
    i=cursor.fetchone()
    n=0.2
    for x in range(0,len(i)):
        Entry(root,textvariable=StringVar(value=i[x]),width=45,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',13)).place(relx = 0.6, rely = n,anchor=CENTER)
        n+=0.05
    Button(root, text='Main Menu', width=25,command=lambda: emp_hs()).place(anchor=CENTER,relx=0.3,rely=0.95)
    Button(root, text='Log Out', width=25,command=lambda: mains()).place(anchor=CENTER,relx=0.5,rely=0.95)
    Button(root, text='Exit', width=25, command=lambda : exits()).place(anchor=CENTER,relx=0.7,rely=0.95)
def update_mpe():
    global u
    cursor.execute('Describe Users;')
    u=cursor.fetchall()
    global i
    cursor.execute('select * from Users where `'+u[3][0]+'`="'+user+'"')
    i=cursor.fetchone()
    global D
    D={}
    global up
    up=Toplevel(bg='powder blue',relief=RIDGE)
    up.maxsize(1024,768)
    up.title('Update Record')
    Label(up,bg='sky blue',relief=RIDGE,width=48,text = 'Current Data',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    Label(up,bg='sky blue',relief=RIDGE,width=48,text ='New Data',font=('Standard',10,'bold')).grid(row = 0, column = 3,columnspan=2)
    for x in range(0,len(i)):
        Label(up,bg='sky blue',relief=RIDGE,width=10,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(up, textvariable=StringVar(up, value = i[x]),width=42,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
        Label(up,bg='sky blue',relief=RIDGE,width=10,text =u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 3)
    a = Entry(up, textvariable=StringVar(up, value = i[0]),width=42,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10))
    b = Entry(up, textvariable=StringVar(up, value = i[1]),width=42,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10))
    c = Entry(up, textvariable=StringVar(up, value = i[2]),width=42,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
    d = Entry(up, textvariable=StringVar(up, value = i[3]),width=42,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
    e = Entry(up, textvariable=StringVar(up, value = i[4]),width=42,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
    f = Entry(up, textvariable=StringVar(up, value = i[5]),width=42,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
    g = Entry(up, textvariable=StringVar(up, value = i[6]),width=42,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
    h = Entry(up, textvariable=StringVar(up, value = i[7]),width=42,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
    j = Entry(up, textvariable=StringVar(up, value = i[8]),width=42,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
    k = Entry(up, textvariable=StringVar(up, value = i[9]),width=42,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
    l = Entry(up, textvariable=StringVar(up, value = i[10]),width=42,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
    m = Entry(up, textvariable=StringVar(up, value = i[11]),width=42,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
    n = Entry(up, textvariable=StringVar(up, value = i[12]),width=42,relief=RIDGE,bd=2,justify=CENTER,state=NORMAL,font=('Standard',10))
    o = Entry(up, textvariable=StringVar(up, value = i[13]),width=42,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10))
    p = Entry(up, textvariable=StringVar(up, value = i[14]),width=42,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10))
    a.grid(row = 1, column = 4)
    b.grid(row = 2, column = 4)
    c.grid(row = 3, column = 4)
    d.grid(row = 4, column = 4)
    e.grid(row = 5, column = 4)
    f.grid(row = 6, column = 4)
    g.grid(row = 7, column = 4)
    h.grid(row = 8, column = 4)
    j.grid(row = 9, column = 4)
    k.grid(row = 10, column = 4)
    l.grid(row = 11, column = 4)
    m.grid(row = 12, column = 4)
    n.grid(row = 13, column = 4)
    o.grid(row = 14, column = 4)
    p.grid(row = 15, column = 4)
    D[string.ascii_lowercase[0]]=a
    D[string.ascii_lowercase[1]]=b
    D[string.ascii_lowercase[2]]=c
    D[string.ascii_lowercase[3]]=d
    D[string.ascii_lowercase[4]]=e
    D[string.ascii_lowercase[5]]=f
    D[string.ascii_lowercase[6]]=g
    D[string.ascii_lowercase[7]]=h
    D[string.ascii_lowercase[8]]=j
    D[string.ascii_lowercase[9]]=k
    D[string.ascii_lowercase[10]]=l
    D[string.ascii_lowercase[11]]=m
    D[string.ascii_lowercase[12]]=n
    D[string.ascii_lowercase[13]]=o
    D[string.ascii_lowercase[14]]=p
    Button(up, text = 'Save Changes', command = lambda:edit_records_mpe()).grid(row = len(u)+1,column=1,columnspan = 4)
    up.mainloop()
def edit_records_mpe(*args):
    try:
        query = 'UPDATE Users SET '+u[0][0]+'=%s,'+u[1][0]+'=%s,'+u[2][0]+'=%s,`'+u[3][0]+'`=%s,'+u[4][0]+'=%s,'+u[5][0]+'=%s,'+u[6][0]+'=%s,'+u[7][0]+'=%s,'+u[8][0]+'=%s,'+u[9][0]+'=%s,'+u[10][0]+'=%s,'+u[11][0]+'=%s,'+u[12][0]+'=%s,'+u[13][0]+'=%s,'+u[14][0]+'=%s where '+u[0][0]+' = "'+i[0]+'";'
        parameters = (tuple([D[x].get() for x in D.keys()]))
        cursor.execute(query, parameters)
        query_apre = 'UPDATE Appraisal SET '+u[0][0]+'=%s where '+u[0][0]+' = "'+i[0]+'";'
        parameters_apre = tuple([D['a'].get()])
        cursor.execute(query_apre, parameters_apre)
        query_leae = 'UPDATE `Leave` SET '+u[0][0]+'=%s where '+u[0][0]+' = "'+i[0]+'";'
        parameters_leae = tuple([D['a'].get()])
        cursor.execute(query_leae, parameters_leae)
        query_sale = 'UPDATE Salary SET '+u[0][0]+'=%s where '+u[0][0]+' = "'+i[0]+'";'
        parameters_sale = tuple([D['a'].get()])
        cursor.execute(query_sale, parameters_sale)
        query_time = 'UPDATE timesheet SET '+u[0][0]+'=%s where '+u[0][0]+' = "'+i[0]+'";'
        parameters_time = tuple([D['a'].get()])
        cursor.execute(query_time, parameters_time)
        conn.commit()
        up.destroy()
        tkinter.messagebox.showinfo('Success', 'Your Record is updated successfully !')
        newr_mpe()
    except mysql.connector.IntegrityError:
        tkinter.messagebox.showerror('Failed.Please Retry or Exit', "Update failed\nUpdated Fields Not Unique\nPlease Try Again !")
def newr_mpe():
    cursor.execute('select * from Users where  `Login ID`="'+user+'" AND Password="'+passw+'"')
    i=cursor.fetchone()
    n=0.2
    for x in range(0,len(i)):
        Entry(root,textvariable=StringVar(value=i[x]),width=45,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',13)).place(relx = 0.6, rely = n,anchor=CENTER)
        n+=0.05

def empe():
    hide()
    Button(root, text='View Record', width=25,command=lambda:viewr_empe()).place(anchor=CENTER,relx=0.5,rely=0.90)
    Button(root, text='Main Menu', width=25,command=lambda: emp_hs()).place(anchor=CENTER,relx=0.3,rely=0.95)
    Button(root, text='Log Out', width=25,command=lambda: mains()).place(anchor=CENTER,relx=0.5,rely=0.95)
    Button(root, text='Exit', width=25, command=lambda : exits()).place(anchor=CENTER,relx=0.7,rely=0.95)
    Label(root,bg='sky blue',font=('Arial',20,'bold'),padx=10,pady=10,relief=RIDGE,text='My Employee Record').place(relx=0.5,rely=0.04,anchor=CENTER)
    global tr_empe
    tr_empe = ttk.Treeview(root, selectmode ='browse',height='20')
    tr_empe.place(anchor=CENTER,height=600,width=990,relx=0.499,rely=0.47)
    vers = Scrollbar(root,orient =VERTICAL,command = tr_empe.yview)
    vers.place(anchor=CENTER,relx=0.99,rely=0.47,height=600)
    tr_empe.configure(yscrollcommand = vers.set)
    hrs = Scrollbar(root,orient =HORIZONTAL,command = tr_empe.xview)
    hrs.place(anchor=CENTER,relx=0.499,rely=0.871,width=990)
    tr_empe.configure(xscrollcommand = hrs.set)
    global u
    cursor.execute('Describe Users;')
    u=cursor.fetchall()
    l=[]
    for x in range(0,len(u)): l.append(u[x][0])
    tr_empe.column('#0', width=0, stretch=NO)
    tr_empe['columns'] = l
    for x in range(0,len(u)):
        tr_empe.column(u[x][0],width=10,anchor=CENTER)
        tr_empe.heading(u[x][0],text=u[x][0],anchor=CENTER)
    cursor.execute('select * from Users where `Login ID`="'+user+'" AND Password="'+passw+'";')
    i=cursor.fetchall()
    for x in range(0,len(i)):
        tr_empe.insert("", 'end',  values =(i[x]))
def viewr_empe():
    ITF=tr_empe.item(tr_empe.focus())
    global u
    cursor.execute('Describe Users;')
    u=cursor.fetchall()
    cursor.execute('select * from Users where '+u[0][0]+'="'+str(ITF['values'][0])+'"')
    i=cursor.fetchall()
    v=Toplevel(bg='powder blue',relief=RIDGE)
    v.maxsize(1024,768)
    v.title('View Record')
    Label(v,bg='sky blue',relief=RIDGE,width=48,text = 'Record Details',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    for x in range(0,len(i[0])):
        Label(v,bg='sky blue',relief=RIDGE,width=10,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(v, textvariable=StringVar(v, value = i[0][x]),width=42,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
    Button(v, text = 'Back', command = lambda:v.destroy()).grid(row = len(u)+1,column=1,columnspan = 4)
    v.mainloop()

def apre():
    hide()
    Button(root, text='View Record', width=25,command=lambda:viewr_apre()).place(anchor=CENTER,relx=0.5,rely=0.90)
    Button(root, text='Main Menu', width=25,command=lambda: emp_hs()).place(anchor=CENTER,relx=0.3,rely=0.95)
    Button(root, text='Log Out', width=25,command=lambda: mains()).place(anchor=CENTER,relx=0.5,rely=0.95)
    Button(root, text='Exit', width=25, command=lambda : exits()).place(anchor=CENTER,relx=0.7,rely=0.95)
    Label(root,bg='sky blue',font=('Arial',20,'bold'),padx=10,pady=10,relief=RIDGE,text='Appraisal Record').place(relx=0.5,rely=0.04,anchor=CENTER)
    global tr_apre
    tr_apre = ttk.Treeview(root, selectmode ='browse',height='20')
    tr_apre.place(anchor=CENTER,height=600,width=990,relx=0.499,rely=0.47)
    vers = Scrollbar(root,orient =VERTICAL,command = tr_apre.yview)
    vers.place(anchor=CENTER,relx=0.99,rely=0.47,height=600)
    tr_apre.configure(yscrollcommand = vers.set)
    hrs = Scrollbar(root,orient =HORIZONTAL,command = tr_apre.xview)
    hrs.place(anchor=CENTER,relx=0.499,rely=0.871,width=990)
    tr_apre.configure(xscrollcommand = hrs.set)
    global u
    cursor.execute('Describe Appraisal;')
    u=cursor.fetchall()
    l=[]
    for x in range(0,len(u)): l.append(u[x][0])
    tr_apre.column('#0', width=0, stretch=NO)
    tr_apre['columns'] = l
    for x in range(0,len(u)):
        tr_apre.column(u[x][0],width=10,anchor=CENTER)
        tr_apre.heading(u[x][0],text=u[x][0],anchor=CENTER)
    cursor.execute('select * from Users where `Login ID`="'+user+'"and Password="'+passw+'"')
    x=cursor.fetchone()
    cursor.execute('select * from Appraisal where UID="'+x[0]+'";')
    i=cursor.fetchall()
    for x in range(0,len(i)):
        tr_apre.insert("", 'end',  values =(i[x]))
def viewr_apre():
    ITF=tr_apre.item(tr_apre.focus())
    global u
    cursor.execute('Describe Appraisal;')
    u=cursor.fetchall()
    cursor.execute('select * from Appraisal where '+u[0][0]+'="'+str(ITF['values'][0])+'"')
    i=cursor.fetchall()
    v=Toplevel(bg='powder blue',relief=RIDGE)
    v.maxsize(1024,768)
    v.title('View Record')
    Label(v,bg='sky blue',relief=RIDGE,width=35,text = 'Record Details',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    for x in range(0,len(i[0])):
        Label(v,bg='sky blue',relief=RIDGE,width=18,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(v, textvariable=StringVar(v, value = i[0][x]),width=18,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
    Button(v, text = 'Back', command = lambda:v.destroy()).grid(row = len(u)+1,column=1,columnspan = 4)
    v.mainloop()

def depe():
    hide()
    Button(root, text='View Record', width=25,command=lambda:viewr_depe()).place(anchor=CENTER,relx=0.5,rely=0.90)
    Button(root, text='Main Menu', width=25,command=lambda: emp_hs()).place(anchor=CENTER,relx=0.3,rely=0.95)
    Button(root, text='Log Out', width=25,command=lambda: mains()).place(anchor=CENTER,relx=0.5,rely=0.95)
    Button(root, text='Exit', width=25, command=lambda : exits()).place(anchor=CENTER,relx=0.7,rely=0.95)
    Label(root,bg='sky blue',font=('Arial',20,'bold'),padx=10,pady=10,relief=RIDGE,text='Department Record').place(relx=0.5,rely=0.04,anchor=CENTER)
    global tr_depe
    tr_depe = ttk.Treeview(root, selectmode ='browse',height='20')
    tr_depe.place(anchor=CENTER,height=600,width=990,relx=0.499,rely=0.47)
    vers = Scrollbar(root,orient =VERTICAL,command = tr_depe.yview)
    vers.place(anchor=CENTER,relx=0.99,rely=0.47,height=600)
    tr_depe.configure(yscrollcommand = vers.set)
    hrs = Scrollbar(root,orient =HORIZONTAL,command = tr_depe.xview)
    hrs.place(anchor=CENTER,relx=0.499,rely=0.871,width=990)
    tr_depe.configure(xscrollcommand = hrs.set)
    global u
    cursor.execute('Describe Department;')
    u=cursor.fetchall()
    l=[]
    for x in range(0,len(u)): l.append(u[x][0])
    tr_depe.column('#0', width=0, stretch=NO)
    tr_depe['columns'] = l
    for x in range(0,len(u)):
        tr_depe.column(u[x][0],width=10,anchor=CENTER)
        tr_depe.heading(u[x][0],text=u[x][0],anchor=CENTER)
    cursor.execute('select * from Users where `Login ID`="'+user+'" AND Password="'+passw+'";')
    x=cursor.fetchone()
    cursor.execute('select * from Department where Name="'+x[13]+'";')
    i=cursor.fetchall()
    for x in range(0,len(i)):
        tr_depe.insert("", 'end',  values =(i[x]))
def viewr_depe():
    ITF=tr_depe.item(tr_depe.focus())
    global u
    cursor.execute('Describe Department;')
    u=cursor.fetchall()
    cursor.execute('select * from Department where '+u[0][0]+'="'+str(ITF['values'][0])+'"')
    i=cursor.fetchall()
    v=Toplevel(bg='powder blue',relief=RIDGE)
    v.maxsize(1024,768)
    v.title('View Record')
    Label(v,bg='sky blue',relief=RIDGE,width=46,text = 'Record Details',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    for x in range(0,len(i[0])):
        Label(v,bg='sky blue',relief=RIDGE,width=10,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(v, textvariable=StringVar(v, value = i[0][x]),width=40,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
    Button(v, text = 'Back', command = lambda:v.destroy()).grid(row = len(u)+1,column=1,columnspan = 4)
    v.mainloop()

def leae():
    hide()
    Button(root, text='View Record', width=25,command=lambda:viewr_leae()).place(anchor=CENTER,relx=0.5,rely=0.90)
    Button(root, text='Main Menu', width=25,command=lambda: emp_hs()).place(anchor=CENTER,relx=0.3,rely=0.95)
    Button(root, text='Log Out', width=25,command=lambda: mains()).place(anchor=CENTER,relx=0.5,rely=0.95)
    Button(root, text='Exit', width=25, command=lambda : exits()).place(anchor=CENTER,relx=0.7,rely=0.95)
    Label(root,bg='sky blue',font=('Arial',20,'bold'),padx=10,pady=10,relief=RIDGE,text='Leave Record').place(relx=0.5,rely=0.04,anchor=CENTER)
    global tr_leae
    tr_leae = ttk.Treeview(root, selectmode ='browse',height='20')
    tr_leae.place(anchor=CENTER,height=600,width=990,relx=0.499,rely=0.47)
    vers = Scrollbar(root,orient =VERTICAL,command = tr_leae.yview)
    vers.place(anchor=CENTER,relx=0.99,rely=0.47,height=600)
    tr_leae.configure(yscrollcommand = vers.set)
    hrs = Scrollbar(root,orient =HORIZONTAL,command = tr_leae.xview)
    hrs.place(anchor=CENTER,relx=0.499,rely=0.871,width=990)
    tr_leae.configure(xscrollcommand = hrs.set)
    global u
    cursor.execute('Describe `Leave`;')
    u=cursor.fetchall()
    l=[]
    for x in range(0,len(u)): l.append(u[x][0])
    tr_leae.column('#0', width=0, stretch=NO)
    tr_leae['columns'] = l
    for x in range(0,len(u)):
        tr_leae.column(u[x][0],width=10,anchor=CENTER)
        tr_leae.heading(u[x][0],text=u[x][0],anchor=CENTER)
    cursor.execute('select * from Users where `Login ID`="'+user+'" AND Password="'+passw+'";')
    x=cursor.fetchone()
    cursor.execute('select * from `Leave` where UID="'+x[0]+'";')
    i=cursor.fetchall()
    for x in range(0,len(i)):
        tr_leae.insert("", 'end',  values =(i[x]))
def viewr_leae():
    ITF=tr_leae.item(tr_leae.focus())
    global u
    cursor.execute('Describe `Leave`;')
    u=cursor.fetchall()
    cursor.execute('select * from `Leave` where '+u[0][0]+'="'+str(ITF['values'][0])+'"')
    i=cursor.fetchall()
    v=Toplevel(bg='powder blue',relief=RIDGE)
    v.maxsize(1024,768)
    v.title('View Record')
    Label(v,bg='sky blue',relief=RIDGE,width=27,text = 'Record Details',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    for x in range(0,len(i[0])):
        Label(v,bg='sky blue',relief=RIDGE,width=14,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(v, textvariable=StringVar(v, value = i[0][x]),width=14,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
    Button(v, text = 'Back', command = lambda:v.destroy()).grid(row = len(u)+1,column=1,columnspan = 4)
    v.mainloop()

def proe():
    hide()
    Button(root, text='View Record', width=25,command=lambda:viewr_proe()).place(anchor=CENTER,relx=0.5,rely=0.90)
    Button(root, text='Main Menu', width=25,command=lambda: emp_hs()).place(anchor=CENTER,relx=0.3,rely=0.95)
    Button(root, text='Log Out', width=25,command=lambda: mains()).place(anchor=CENTER,relx=0.5,rely=0.95)
    Button(root, text='Exit', width=25, command=lambda : exits()).place(anchor=CENTER,relx=0.7,rely=0.95)
    Label(root,bg='sky blue',font=('Arial',20,'bold'),padx=10,pady=10,relief=RIDGE,text='Project Record').place(relx=0.5,rely=0.04,anchor=CENTER)
    global tr_proe
    tr_proe = ttk.Treeview(root, selectmode ='browse',height='20')
    tr_proe.place(anchor=CENTER,height=600,width=990,relx=0.499,rely=0.47)
    vers = Scrollbar(root,orient =VERTICAL,command = tr_proe.yview)
    vers.place(anchor=CENTER,relx=0.99,rely=0.47,height=600)
    tr_proe.configure(yscrollcommand = vers.set)
    hrs = Scrollbar(root,orient =HORIZONTAL,command = tr_proe.xview)
    hrs.place(anchor=CENTER,relx=0.499,rely=0.871,width=990)
    tr_proe.configure(xscrollcommand = hrs.set)
    global u
    cursor.execute('Describe Project;')
    u=cursor.fetchall()
    l=[]
    for x in range(0,len(u)): l.append(u[x][0])
    tr_proe.column('#0', width=0, stretch=NO)
    tr_proe['columns'] = l
    for x in range(0,len(u)):
        tr_proe.column(u[x][0],width=10,anchor=CENTER)
        tr_proe.heading(u[x][0],text=u[x][0],anchor=CENTER)
    cursor.execute('select * from Users where `Login ID`="'+user+'" AND Password="'+passw+'";')
    x=cursor.fetchone()
    cursor.execute('select * from Project where Title="'+x[14]+'";')
    i=cursor.fetchall()
    for x in range(0,len(i)):
        tr_proe.insert("", 'end',  values =(i[x]))
def viewr_proe():
    ITF=tr_proe.item(tr_proe.focus())
    global u
    cursor.execute('Describe Project;')
    u=cursor.fetchall()
    cursor.execute('select * from Project where '+u[0][0]+'="'+str(ITF['values'][0])+'"')
    i=cursor.fetchall()
    v=Toplevel(bg='powder blue',relief=RIDGE)
    v.maxsize(1024,768)
    v.title('View Record')
    Label(v,bg='sky blue',relief=RIDGE,width=46,text = 'Record Details',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    for x in range(0,len(i[0])):
        Label(v,bg='sky blue',relief=RIDGE,width=14,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(v, textvariable=StringVar(v, value = i[0][x]),width=35,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
    Button(v, text = 'Back', command = lambda:v.destroy()).grid(row = len(u)+1,column=1,columnspan = 4)
    v.mainloop()

def sale():
    hide()
    Button(root, text='View Record', width=25,command=lambda:viewr_sale()).place(anchor=CENTER,relx=0.5,rely=0.90)
    Button(root, text='Main Menu', width=25,command=lambda: emp_hs()).place(anchor=CENTER,relx=0.3,rely=0.95)
    Button(root, text='Log Out', width=25,command=lambda: mains()).place(anchor=CENTER,relx=0.5,rely=0.95)
    Button(root, text='Exit', width=25, command=lambda : exits()).place(anchor=CENTER,relx=0.7,rely=0.95)
    Label(root,bg='sky blue',font=('Arial',20,'bold'),padx=10,pady=10,relief=RIDGE,text='Salary Record').place(relx=0.5,rely=0.04,anchor=CENTER)
    global tr_sale
    tr_sale = ttk.Treeview(root, selectmode ='browse',height='20')
    tr_sale.place(anchor=CENTER,height=600,width=990,relx=0.499,rely=0.47)
    vers = Scrollbar(root,orient =VERTICAL,command = tr_sale.yview)
    vers.place(anchor=CENTER,relx=0.99,rely=0.47,height=600)
    tr_sale.configure(yscrollcommand = vers.set)
    hrs = Scrollbar(root,orient =HORIZONTAL,command = tr_sale.xview)
    hrs.place(anchor=CENTER,relx=0.499,rely=0.871,width=990)
    tr_sale.configure(xscrollcommand = hrs.set)
    global u
    cursor.execute('Describe Salary;')
    u=cursor.fetchall()
    l=[]
    for x in range(0,len(u)): l.append(u[x][0])
    tr_sale.column('#0', width=0, stretch=NO)
    tr_sale['columns'] = l
    for x in range(0,len(u)):
        tr_sale.column(u[x][0],width=10,anchor=CENTER)
        tr_sale.heading(u[x][0],text=u[x][0],anchor=CENTER)
    cursor.execute('select * from Users where `Login ID`="'+user+'" AND Password="'+passw+'";')
    x=cursor.fetchone()
    cursor.execute('select * from Salary where UID="'+x[0]+'";')
    i=cursor.fetchall()
    for x in range(0,len(i)):
        tr_sale.insert("", 'end',  values =(i[x]))
def viewr_sale():
    ITF=tr_sale.item(tr_sale.focus())
    global u
    cursor.execute('Describe Salary;')
    u=cursor.fetchall()
    cursor.execute('select * from Salary where '+u[0][0]+'="'+str(ITF['values'][0])+'"')
    i=cursor.fetchall()
    v=Toplevel(bg='powder blue',relief=RIDGE)
    v.maxsize(1024,768)
    v.title('View Record')
    Label(v,bg='sky blue',relief=RIDGE,width=27,text = 'Record Details',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    for x in range(0,len(i[0])):
        Label(v,bg='sky blue',relief=RIDGE,width=13,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(v, textvariable=StringVar(v, value = i[0][x]),width=15,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
    Button(v, text = 'Back', command = lambda:v.destroy()).grid(row = len(u)+1,column=1,columnspan = 4)
    v.mainloop()

def time():
    hide()
    Button(root, text='View Record', width=25,command=lambda:viewr_time()).place(anchor=CENTER,relx=0.5,rely=0.90)
    Button(root, text='Main Menu', width=25,command=lambda: emp_hs()).place(anchor=CENTER,relx=0.3,rely=0.95)
    Button(root, text='Log Out', width=25,command=lambda: mains()).place(anchor=CENTER,relx=0.5,rely=0.95)
    Button(root, text='Exit', width=25, command=lambda : exits()).place(anchor=CENTER,relx=0.7,rely=0.95)
    global tr_time
    Label(root,bg='sky blue',font=('Arial',20,'bold'),padx=10,pady=10,relief=RIDGE,text='Timesheet Record').place(relx=0.5,rely=0.04,anchor=CENTER)
    tr_time = ttk.Treeview(root, selectmode ='browse',height='20')
    tr_time.place(anchor=CENTER,height=600,width=990,relx=0.499,rely=0.47)
    vers = Scrollbar(root,orient =VERTICAL,command = tr_time.yview)
    vers.place(anchor=CENTER,relx=0.99,rely=0.47,height=600)
    tr_time.configure(yscrollcommand = vers.set)
    hrs = Scrollbar(root,orient =HORIZONTAL,command = tr_time.xview)
    hrs.place(anchor=CENTER,relx=0.499,rely=0.871,width=990)
    tr_time.configure(xscrollcommand = hrs.set)
    global u
    cursor.execute('Describe Timesheet;')
    u=cursor.fetchall()
    l=[]
    for x in range(0,len(u)): l.append(u[x][0])
    tr_time.column('#0', width=0, stretch=NO)
    tr_time['columns'] = l
    for x in range(0,len(u)):
        tr_time.column(u[x][0],width=10,anchor=CENTER)
        tr_time.heading(u[x][0],text=u[x][0],anchor=CENTER)
    cursor.execute('select * from Users where `Login ID`="'+user+'" AND Password="'+passw+'";')
    x=cursor.fetchone()
    cursor.execute('select * from Timesheet where UID="'+x[0]+'";')
    i=cursor.fetchall()
    for x in range(0,len(i)):
        tr_time.insert("", 'end',  values =(i[x]))
def viewr_time():
    ITF=tr_time.item(tr_time.focus())
    global u
    cursor.execute('Describe Timesheet;')
    u=cursor.fetchall()
    cursor.execute('select * from Timesheet where '+u[0][0]+'="'+str(ITF['values'][0])+'"')
    i=cursor.fetchall()
    v=Toplevel(bg='powder blue',relief=RIDGE)
    v.maxsize(1024,768)
    v.title('View Record')
    Label(v,bg='sky blue',relief=RIDGE,width=48,text = 'Record Details',font=('Standard',10,'bold')).grid(row = 0, column = 1,columnspan=2)
    for x in range(0,len(i[0])):
        Label(v,bg='sky blue',relief=RIDGE,width=10,text = u[x][0],font=('Standard',10,'bold')).grid(row = x+1, column = 1)
        Entry(v, textvariable=StringVar(v, value = i[0][x]),width=42,relief=RIDGE,bd=2,justify=CENTER,state='readonly',font=('Standard',10)).grid(row = x+1, column = 2)
    Button(v, text = 'Back', command = lambda:v.destroy()).grid(row = len(u)+1,column=1,columnspan = 4)
    v.mainloop()

mains()
root.mainloop()
