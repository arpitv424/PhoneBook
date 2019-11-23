from Tkinter import *
#import splash
import sqlite3
import tkMessageBox
##import re
##regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

con=sqlite3.Connection('persondetails')
cur=con.cursor()
cur.execute('create table if not exists details(id INTEGER primary key AUTOINCREMENT,fname varchar(15), mname varchar(15), lname varchar(15), company varchar(30), address varchar(50), city varchar(20), pin number(7), website varchar(30), dob date, mob number(11), email varchar(50))')



root=Tk()
root.title('AV')
img=PhotoImage(file='l.gif')
Label(root,image=img).grid(row=0,column=5)
Label(root,text='PhoneBook', font='times 18').grid(row=1,column=5)
root.geometry("700x800")
Label(root,text='First Name',font='times 16').grid(row=5,column=4)
e1=Entry(root)
e1.grid(row=5,column=6)
Label(root,text='Middle Name',font='times 16').grid(row=6,column=4)
e2=Entry(root)
e2.grid(row=6,column=6)
Label(root,text='Last Name:',font='times 16').grid(row=7,column=4)
e3=Entry(root)
e3.grid(row=7,column=6)
Label(root,text='Company Name',font='times 16').grid(row=8,column=4)
e4=Entry(root)
e4.grid(row=8,column=6)
Label(root,text='Address',font='times 16').grid(row=9,column=4)
e5=Entry(root)
e5.grid(row=9,column=6)
Label(root,text='City',font='times 16').grid(row=10,column=4)
e6=Entry(root)
e6.grid(row=10,column=6)
Label(root,text='Pin Code',font='times 16').grid(row=11,column=4)
e7=Entry(root)
e7.grid(row=11,column=6)
Label(root,text='Website URL',font='times 16').grid(row=12,column=4)
e8=Entry(root)
e8.grid(row=12,column=6)
Label(root,text='Date of Birth',font='times 16').grid(row=13,column=4)
e9=Entry(root)
e9.grid(row=13,column=6)
Label(root,text='Select Phone Type',font='times 20', foreground="blue").grid(row=14,column=4)

v1=IntVar()
v2=IntVar()
x=Radiobutton(root,text='Home',variable=v1,value=1)
x.grid(row=14, column=5)
y=Radiobutton(root,text='Office',variable=v1,value=2)
y.grid(row=14, column=6)
z=Radiobutton(root,text='Personal',variable=v1,value=3)
z.grid(row=14, column=7)
Label(root,text='Phone', font='times 16').grid(row=15,column=4)
e10=Entry(root)
e10.grid(row=15,column=6)


Button(root,text='+').grid(row=15,column=7)

Label(root,text='Select E-mail Type',font='times 20', foreground="blue").grid(row=16,column=4)

a=Radiobutton(root,text='Home',variable=v2,value=1)
a.grid(row=16, column=5)
b=Radiobutton(root,text='Office',variable=v2,value=2)
b.grid(row=16, column=6)
Label(root,text='E-mail', font='times 16').grid(row=17,column=4)
e11=Entry(root)
e11.grid(row=17,column=6)
Button(root,text='+').grid(row=17,column=7)
##def checkm():
##            if not(re.search(regex,e11.get())):
##                tkMessageBox.showerror('Error','You have entered wrong Email')


def save():
    
    
    if e1.get()==e2.get()==e3.get():
        tkMessageBox.showerror('Error','You have entered wrong name')
    elif len(e7.get())>6:
        tkMessageBox.showerror('Error','You have entered wrong pincode')
    elif len(e10.get())>10:
        tkMessageBox.showerror('Error','You have entered wrong Phone')
    
##    elif len(e11.get())>0:
##        checkm()
        
    else:
        cur.execute("insert into details(fname,mname,lname,company,address,city,pin,website,dob,mob,email) values(?,?,?,?,?,?,?,?,?,?,?)",(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get()))
        con.commit()
        cur.execute('select * from details')
        tkMessageBox.showinfo('Success','Your contact is successfully saved!!')
        print cur.fetchall()
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
        e11.delete(0,END)


def search():
    root1=Tk()
    Label(root1,text='Search contacts',font='times 18', foreground="dark gray").grid(row=0,column=3)
    Label(root,text='').grid(row=1,column=0)
    d1=Entry(root1)
    d1.grid(row=2,column=3)
    lb=Listbox(root1,height='40', width='100')
    lb.grid(row=3,column=3)
    def val(e):
        lb.delete(0,END)
        bc=d1.get()+e.char
        cur.execute("select id,fname,mname,lname from details where fname like '%{0}%' or mname like '%{0}%' or lname like '%{0}%'".format(bc))
        t=cur.fetchall()
        for i in t:
            lb.insert(END,i[1]+' '+i[2]+' '+i[3])
        def show(event):
            widget=event.widget
            selection=widget.curselection()
            selection=selection[0]
            cur.execute("select * from details where id={0}".format(t[selection][0]))
            get=cur.fetchall()
            get=get[0]
            root1.destroy()
            root2=Tk()
            l=['First name','Middle Name','Last Name','Company','Address','City','Pin','Website','DOB','Phone','E-mail']
            Label(root2,text='Details', font='times 20',foreground="dark gray").grid(row=0,column=3)
            cou=1
            for i in range(1,12):
                Label(root2,text=l[i-1]).grid(row=cou,column=2)
                Label(root2,text=get[i]).grid(row=cou,column=4)
                cou+=1
            Label(root2,text=' ').grid(row=13,column=1)
            def delete():
                ask=tkMessageBox.askyesno('Delete','Are you sure you want to delete?')
                if ask==True:
                    cur.execute("delete from details where id={0}".format(t[selection][0]))
                    con.commit()
                    tkMessageBox.showinfo('Delete','Contact deleted')
                else:
                    tkMessageBox.showinfo('Delete','Contact not deleted')


            
            Button(root2,text='Delete',command=delete).grid(row=14,column=3)


            def showme():
                #root1.destroy()
                cur.execute("select * from details where id={0}".format(t[selection][0]))
                get=cur.fetchall()
                get=get[0]
                root2.destroy()
                root4=Tk()
                l=['First name','Middle Name','Last Name','Company','Address','City','Pin','Website','DOB','Phone','E-mail']
                Label(root4,text='Details', font='times 20',foreground="dark gray").grid(row=0,column=3)
                cou=1
                unique=[]
                for i in range(1,12):
                    Label(root4,text=l[i-1]).grid(row=cou,column=2)
                    f=Entry(root4)
                    f.grid(row=cou,column=4)
                    f.insert(0,get[i])
                    unique.append(f)
                    cou+=1
                
                Label(root4,text=' ').grid(row=13,column=1)
                def save1():
                    cur.execute("update details set fname='{0}',mname='{1}',lname='{2}',company='{3}',address='{4}',city='{5}',pin={6},website='{7}',dob='{8}',mob={9},email='{10}' where id={11}".format(unique[0].get(),unique[1].get(),unique[2].get(),unique[3].get(),unique[4].get(),unique[5].get(),unique[6].get(),unique[7].get(),unique[8].get(),unique[9].get(),unique[10].get(),get[0]))
                    con.commit()
                    tkMessageBox.showinfo('Success','Your contact is successfully changed!!')
                    print cur.fetchall()
                Button(root4,text='Save',command=save1).grid(row=14,column=3)
                

                
            Button(root2,text='Edit',command=showme).grid(row=15,column=3)
        lb.bind('<<ListboxSelect>>',show)

    d1.bind('<Key>',val)
        

    root1.mainloop()

def edit():
    root1=Tk()
    Label(root1,text='Search contacts',font='times 18', foreground="dark gray").grid(row=0,column=3)
    Label(root,text='').grid(row=1,column=0)
    d1=Entry(root1)
    d1.grid(row=2,column=3)
    lb=Listbox(root1,height='40', width='100')
    lb.grid(row=3,column=3)
    def val(e):
        lb.delete(0,END)
        bc=d1.get()+e.char
        cur.execute("select id,fname,mname,lname from details where fname like '%{0}%' or mname like '%{0}%' or lname like '%{0}%'".format(bc))
        t=cur.fetchall()
        for i in t:
            lb.insert(END,i[1]+' '+i[2]+' '+i[3])
        def show(event):
            #root1.destroy()
            widget=event.widget
            selection=widget.curselection()
            selection=selection[0]
            cur.execute("select * from details where id={0}".format(t[selection][0]))
            get=cur.fetchall()
            get=get[0]
            root1.destroy()
            root2=Tk()
            l=['First name','Middle Name','Last Name','Company','Address','City','Pin','Website','DOB','Phone','E-mail']
            Label(root2,text='Details', font='times 20',foreground="dark gray").grid(row=0,column=3)
            cou=1
            unique=[]
            for i in range(1,12):
                Label(root2,text=l[i-1]).grid(row=cou,column=2)
                f=Entry(root2)
                f.grid(row=cou,column=4)
                f.insert(0,get[i])
                unique.append(f)
                cou+=1
            
            Label(root2,text=' ').grid(row=13,column=1)
            def save1():
                cur.execute("update details set fname='{0}',mname='{1}',lname='{2}',company='{3}',address='{4}',city='{5}',pin={6},website='{7}',dob='{8}',mob={9},email='{10}'".format(unique[0].get(),unique[1].get(),unique[2].get(),unique[3].get(),unique[4].get(),unique[5].get(),unique[6].get(),unique[7].get(),unique[8].get(),unique[9].get(),unique[10].get(),get[0]))
                con.commit()
                tkMessageBox.showinfo('Success','Your contact is successfully changed!!')
                print cur.fetchall()
            Button(root2,text='Save',command=save1).grid(row=14,column=3)
            


                


            
        lb.bind('<<ListboxSelect>>',show)

    d1.bind('<Key>',val)
        

    root1.mainloop()


def close():
    root.destroy()


Label(root,text=' ').grid(row=19,column=0)
Button(root,text='Save',command=save).grid(row=20,column=4)
Button(root,text='Search',command=search).grid(row=20,column=5)
Button(root,text='Edit',command=edit).grid(row=20,column=6)
Button(root,text='Close',command=close).grid(row=20,column=7)

root.mainloop()
