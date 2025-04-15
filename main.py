from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
win=Tk()
win.state('zoomed')
win.config(bg='black')
#===============================Button Function==================================================
def pd():
    if e1.get()==""or e2.get()=="":
        messagebox.showerror("Error","All field are required")
    else:
        conn = mysql.connector.connect(host="Localhost",username="root",password="Azm@1820#khi",database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            
           nameoftablets.get(),
           ref.get(),
           dose.get(),
           nooftablets.get(),
           issuedate.get(),
           expdate.get(),
           dailydose.get(),
           sideeffect.get(),
           nameofpatient.get(),
           dob.get(),
           patientaddress.get()
        ))
        conn.commit()
        fetch_data()
        conn.close()
        messagebox.showinfo("Success","Record has been inserted")
        
def fetch_data():
        conn = mysql.connector.connect(host="Localhost",username="root",password="Azm@1820#khi",database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute('select * from hospital')
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            table.delete(* table.get_children())
            for items in rows:
                table.insert('',END,values=items)
            conn.commit()
        conn.close()
def get_data(event=''):
    cursor_row=table.focus()
    data=table.item(cursor_row)
    row = data['values']
    nameoftablets.set(row[0]),
    ref.set(row[1]),
    dose.set(row[2]),
    nooftablets.set(row[3]),
    issuedate.set(row[4]),
    expdate.set(row[5]),
    dailydose.set(row[6]),
    sideeffect.set(row[7]),
    nameofpatient.set(row[8]),
    dob.set(row[9]),
    patientaddress.set(row[10])
#===============================Prescription Button Function==================================================
def pre():
    txt_frme.insert(END,'Name of Tablets:\t\t\t'+nameoftablets.get()+'\n')
    txt_frme.insert(END,'Reference No:\t\t\t'+ref.get()+'\n')
    txt_frme.insert(END,'Dose:\t\t\t'+dose.get()+'\n')
    txt_frme.insert(END,'No. of Tablets:\t\t\t'+nooftablets.get()+'\n')
    txt_frme.insert(END,'Issue Date:\t\t\t'+issuedate.get()+'\n')
    txt_frme.insert(END,'Expriy Date:\t\t\t'+expdate.get()+'\n')
    txt_frme.insert(END,'Daliy Dose:\t\t\t'+dailydose.get()+'\n')
    txt_frme.insert(END,'side Effect:\t\t\t'+sideeffect.get()+'\n')
    txt_frme.insert(END,'Blood Pressure:\t\t\t'+bloodpressure.get()+'\n')
    txt_frme.insert(END,'Storage Device:\t\t\t'+storage.get()+'\n')
    txt_frme.insert(END,'Medication:\t\t\t'+medication.get()+'\n')
    txt_frme.insert(END,'Patient Id:\t\t\t'+patientid.get()+'\n')
    txt_frme.insert(END,'Name of Patient:\t\t\t'+nameofpatient.get()+'\n')
    txt_frme.insert(END,'Date of Birth:\t\t\t'+dob.get()+'\n')
    txt_frme.insert(END,'Patient Address:\t\t\t'+patientaddress.get()+'\n')
#===============================Delete Button Function=========================================================
def delete():
    conn = mysql.connector.connect(host="Localhost",username="root",password="Azm@1820#khi",database="mydata")
    my_cursor = conn.cursor()
    querry=('delete from hospital where Reference=%s')
    value=(ref.get(),)
    my_cursor.execute(querry,value)
    conn.commit()
    conn.close()
    fetch_data()
    messagebox.showinfo('Deleted','Patient data has been deleted')
#===============================Clear Button Function==========================================================
def clear():
    nameoftablets.set('')
    ref.set('')
    dose.set('')
    nooftablets.set('')
    issuedate.set('')
    expdate.set('')
    dailydose.set('')
    sideeffect.set('')
    bloodpressure.set('')
    storage.set('')
    medication.set('')
    patientid.set('')
    nameofpatient.set('')
    dob.set('')
    patientaddress.set('')
    txt_frme.delete(1.0,END)
#===============================Exit Button Function==========================================================
def exit():
    confirm = messagebox.askyesno('confirmation','Are You Sure You Want To Exit')
    if confirm>0:
        win.destroy()
        return

Label(win,text='Hospital Management System',font='impack 31 bold',bg='blue',fg='white').pack(fill=X)
#Frame1
frame1=Frame(win,bd=15,relief=RIDGE)
frame1.place(x=0,y=54,width=1530,height=401)

lf1=LabelFrame(frame1,text='Patient Information',font='arial 10 bold',bd=10,bg='pink')
lf1.place(x=10,y=0,width=880,height=372)

Label(lf1,text='Name of Tablets', font='arial 12 bold',bg='pink').place(x=5,y=10)
Label(lf1,text='Reference N0', font='arial 12 bold',bg='pink').place(x=5,y=40)
Label(lf1,text='Dose', font='arial 12 bold',bg='pink').place(x=5,y=70)
Label(lf1,text='No of Tablets', font='arial 12 bold',bg='pink').place(x=5,y=100)
Label(lf1,text='Issue Date', font='arial 12 bold',bg='pink').place(x=5,y=130)
Label(lf1,text='Expriy Date', font='arial 12 bold',bg='pink').place(x=5,y=160)
Label(lf1,text='Daily Dose', font='arial 12 bold',bg='pink').place(x=5,y=190)
Label(lf1,text='Side Effect', font='arial 12 bold',bg='pink').place(x=5,y=220)
Label(lf1,text='Blood Pressure', font='arial 12 bold',bg='pink').place(x=370,y=10)
Label(lf1,text='Storage Device', font='arial 12 bold',bg='pink').place(x=370,y=40)
Label(lf1,text='Medication', font='arial 12 bold',bg='pink').place(x=370,y=70)
Label(lf1,text='Patient Id', font='arial 12 bold',bg='pink').place(x=370,y=100)
Label(lf1,text='Name of Patient', font='arial 12 bold',bg='pink').place(x=370,y=130)
Label(lf1,text='DOB', font='arial 12 bold',bg='pink').place(x=370,y=160)
Label(lf1,text='Patient Address', font='arial 12 bold',bg='pink').place(x=370,y=190)

nameoftablets=StringVar()
ref=StringVar()
dose=StringVar()
nooftablets=StringVar()
issuedate=StringVar()
expdate=StringVar()
dailydose=StringVar()
sideeffect=StringVar()
bloodpressure=StringVar()
storage=StringVar()
medication=StringVar()
patientid=StringVar()
nameofpatient=StringVar()
dob=StringVar()
patientaddress=StringVar()

e1=Entry(lf1,bd=4,textvariable=nameoftablets)
e1.place(x=130,y=10,width=200)
e2=Entry(lf1,bd=4,textvariable=ref)
e2.place(x=130,y=40,width=200)
e3=Entry(lf1,bd=4,textvariable=dose)
e3.place(x=130,y=70,width=200)
e4=Entry(lf1,bd=4,textvariable=nooftablets)
e4.place(x=130,y=100,width=200)
e5=Entry(lf1,bd=4,textvariable=issuedate)
e5.place(x=130,y=130,width=200)
e6=Entry(lf1,bd=4,textvariable=expdate)
e6.place(x=130,y=160,width=200)
e7=Entry(lf1,bd=4,textvariable=dailydose)
e7.place(x=130,y=190,width=200)
e8=Entry(lf1,bd=4,textvariable=sideeffect)
e8.place(x=130,y=220,width=200)
e9=Entry(lf1,bd=4,textvariable=bloodpressure)
e9.place(x=500,y=10,width=200)
e10=Entry(lf1,bd=4,textvariable=storage)
e10.place(x=500,y=40,width=200)
e11=Entry(lf1,bd=4,textvariable=medication)
e11.place(x=500,y=70,width=200)
e12=Entry(lf1,bd=4,textvariable=patientid)
e12.place(x=500,y=100,width=200)
e13=Entry(lf1,bd=4,textvariable=nameofpatient)
e13.place(x=500,y=130,width=200)
e14=Entry(lf1,bd=4,textvariable=dob)
e14.place(x=500,y=160,width=200)
e15=Entry(lf1,bd=4,textvariable=patientaddress)
e15.place(x=500,y=190,width=200)

lf2=LabelFrame(frame1,text='Prescription',font='arial 12 bold',bd=10)
lf2.place(x=890,y=0,width=610,height=372)
txt_frme=Text(lf2,font='impack 10 bold', width=40,height=30,bg='yellow')
txt_frme.pack(fill=BOTH)
#Frame2
frame2=Frame(win,bd=15,relief=RIDGE)
frame2.place(x=0,y=450,width=1530,height=290)
#Button
d_btn=Button(win,text='Delete',font='arial 15 bold',bg='brown',fg='white',bd=6,cursor='hand2',command=delete)
d_btn.place(x=0,y=740,width=268)

p_btn=Button(win,text='Prescription',font='arial 15 bold',bg='purple',fg='white',bd=6,cursor='hand2', command=pre)
p_btn.place(x=266,y=740,width=362)

pd_btn=Button(win,text='Save Prescription Data',font='arial 15 bold',bg='green',fg='white',bd=6,cursor='hand2', command=pd)
pd_btn.place(x=626,y=740,width=370)

c_btn=Button(win,text='Clear',font='arial 15 bold',bg='blue',fg='white',bd=6,cursor='hand2', command=clear)
c_btn.place(x=995,y=740,width=270)

e_btn=Button(win,text='Exit',font='arial 15 bold',bg='red',fg='white',bd=6,cursor='hand2', command=exit)
e_btn.place(x=1264,y=740,width=270)
#Scroll
scroll_X=ttk.Scrollbar(frame2, orient=HORIZONTAL)
scroll_X.pack(side='bottom',fill='x')
scroll_Y=ttk.Scrollbar(frame2, orient=VERTICAL)
scroll_Y.pack(side='right',fill='y')

table=ttk.Treeview(frame2,columns=('not','ref','dose','nots','issd','expd','dd','sd','pn','dob','pa'), xscrollcommand=scroll_Y.set,yscrollcommand=scroll_X.set)
scroll_X=ttk.Scrollbar(command=table.xview)
scroll_Y=ttk.Scrollbar(command=table.yview)

table.heading('not',text='Name of Tablets')
table.heading('ref',text='Reference')
table.heading('dose',text='Dose')
table.heading('nots',text='No of Tablets')
table.heading('issd',text='Issue Date')
table.heading('expd',text='Expriy Date')
table.heading('dd',text='Daily Dose')
table.heading('sd',text='Side Effect')
table.heading('pn',text='Patient Name')
table.heading('dob',text='Date of Birth')
table.heading('pa',text='Patient Address')

table['show']='headings'
table.pack(fill=BOTH,expand=1)

table.column('not',width=100)
table.column('ref',width=100)
table.column('dose',width=100)
table.column('nots',width=100)
table.column('issd',width=100)
table.column('expd',width=100)
table.column('dd',width=100)
table.column('sd',width=100)
table.column('pn',width=100)
table.column('dob',width=100)
table.column('pa',width=100)

table.bind('<ButtonRelease-1>',get_data)
fetch_data()
mainloop()
