# Kira Intenet Cafe program
import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import time
import array
from datetime import date
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from subprocess import Popen
pdfmetrics.registerFont(TTFont('angsana', 'angsana.ttc'))

def mainWindow():
    root = Tk()
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#F6F6F6')
    icon = PhotoImage(file="img/icon.png")  
    root.iconphoto(FALSE,icon)                 
    root.title("Kira Internet Cafe")
    root.option_add('*font',"Times 20")
    root.rowconfigure((0,1,2,3),weight=1)
    root.columnconfigure((0,1,2,3),weight=1)
    return root

def createconnection():
    global conn,cursor
    conn = sqlite3.connect('kirainternet.db')
    cursor = conn.cursor()

# Login Page
def loginlayout() :
    global loginframe
    bgframe = Frame(root,bg='#F6F6F6')
    bgframe.place(x=0,y=0,width=w,height=h)
    loginframe = Frame(root,bg='#F6F6F6')
    loginframe.rowconfigure((0,1,2,3),weight=1)
    loginframe.columnconfigure((0,1),weight=1)
    root.config(bg='#F6F6F6')
    root.title("Kira Internet Cafe")

    Label(loginframe,bg='#F6F6F6',text="Kira Intenet Cafe",font="Times 40 bold").grid(row=0,column=0,columnspan=2)
    Label(loginframe,bg='#F6F6F6',text="ใครเป็นผู้ใช้งาน",font="Times 30 bold",fg="#292929").grid(row=1,column=0,columnspan=2)
    Button(loginframe,image=userpic,bg='#F6F6F6',command=employee).grid(row=2,column=0)
    Button(loginframe,image=userpic,bg='#F6F6F6',command=manager).grid(row=2,column=1)
    Label(loginframe,bg='#F6F6F6',text="พนักงาน",font="Times 20 bold").grid(row=3,column=0)
    Label(loginframe,bg='#F6F6F6',text="ผู้จัดการ",font="Times 20 bold").grid(row=3,column=1)
    loginframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')

def manager():
    global userentry,pwdentry,mlframe
    bgframe = Frame(root,bg='#F6F6F6')
    bgframe.place(x=0,y=0,width=w,height=h)
    mlframe = Frame(root,bg='#F6F6F6')
    mlframe.rowconfigure((0,1,2,3),weight=1)
    mlframe.columnconfigure((0,1),weight=1)
    root.config(bg='#F6F6F6')

    Label(mlframe,image=userpic,bg='#F6F6F6').grid(row=0,column=0,columnspan=2)
    Label(mlframe,text="ชื่อผู้ใช้งาน: ",bg='#F6F6F6').grid(row=1,column=0,sticky='e',padx=10)
    userentry = Entry(mlframe,bg='lightgrey',width=20,textvariable=muserinfo)
    userentry.insert(0,"ชื่อผู้ใช้งาน")
    userentry.config(state=DISABLED)
    userentry.bind("<Button-1>",click_u)
    userentry.grid(row=1,column=1,sticky='w',padx=(0,10))

    pwdentry = Entry(mlframe,bg='lightgrey',width=20,textvariable=mpwdinfo)
    Label(mlframe,text="รหัสผ่าน: ",bg='#F6F6F6').grid(row=2,column=0,sticky='e',padx=10)
    pwdentry.insert(0,"รหัสผ่าน")
    pwdentry.config(state=DISABLED)
    pwdentry.bind("<Button-1>",click_p)
    pwdentry.grid(row=2,column=1,sticky='w',padx=(0,10))

    Button(mlframe,text="ยกเลิก",font="Calibri 18 bold",bg="grey",width=10,command=cancelm).grid(row=3,column=1,pady=(0,20),sticky='w')
    Button(mlframe,text="ยืนยัน",font="Calibri 18 bold",bg="grey",width=10,command=mnlogin).grid(row=3,column=1,pady=(0,20),sticky='w',padx=(150,0))
    mlframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')

def employee():
    global userentry,pwdentry,elframe
    bgframe = Frame(root,bg='#F6F6F6')
    bgframe.place(x=0,y=0,width=w,height=h)
    elframe = Frame(root,bg='#F6F6F6')
    elframe.rowconfigure((0,1,2,3),weight=1)
    elframe.columnconfigure((0,1),weight=1)
    root.config(bg='#F6F6F6')

    Label(elframe,image=userpic,bg='#F6F6F6').grid(row=0,column=0,columnspan=2)
    Label(elframe,text="ชื่อผู้ใช้งาน: ",bg='#F6F6F6').grid(row=1,column=0,sticky='e',padx=10)
    userentry = Entry(elframe,bg='lightgrey',width=20,textvariable=userinfo)
    userentry.insert(0,"ชื่อผู้ใช้งาน")
    userentry.config(state=DISABLED)
    userentry.bind("<Button-1>",click_u)
    userentry.grid(row=1,column=1,sticky='w',padx=(0,10))

    pwdentry = Entry(elframe,bg='lightgrey',width=20,textvariable=epwdinfo)
    Label(elframe,text="รหัสผ่าน: ",bg='#F6F6F6').grid(row=2,column=0,sticky='e',padx=10)
    pwdentry.insert(0,"รหัสผ่าน")
    pwdentry.config(state=DISABLED)
    pwdentry.bind("<Button-1>",click_p)
    pwdentry.grid(row=2,column=1,sticky='w',padx=(0,10))

    Button(elframe,text="ยกเลิก",font="Calibri 18 bold",bg="grey",width=10,command=cancele).grid(row=3,column=1,pady=(0,20),sticky='w')
    Button(elframe,text="ยืนยัน",font="Calibri 18 bold",bg="grey",width=10,command=emlogin).grid(row=3,column=1,pady=(0,20),sticky='w',padx=(150,0))
    elframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')

def click_u(event):
    userentry.config(state=NORMAL)
    userentry.delete(0,END)
def click_p(event):
    pwdentry.config(state=NORMAL)
    pwdentry.delete(0,END)
    pwdentry.config(show='*')

def cancelm():
    userentry.config(state=NORMAL)
    userentry.delete(0,END)
    pwdentry.config(state=NORMAL)
    pwdentry.delete(0,END)
    mlframe.destroy()
    loginframe.destroy()
    loginlayout()

def cancele():
    userentry.config(state=NORMAL)
    userentry.delete(0,END)
    pwdentry.config(state=NORMAL)
    pwdentry.delete(0,END)
    elframe.destroy()
    loginframe.destroy()
    loginlayout()

def mnlogin():
    if muserinfo.get() == "" or muserinfo.get() == "ชื่อผู้ใช้งาน":
        messagebox.showwarning("Admin","กรุณากรอกชื่อผู้ใช้งาน")
        userentry.focus_force() 
    else:  
        if mpwdinfo.get() == "" or mpwdinfo.get() == "รหัสผ่าน":
            messagebox.showwarning("Admin","กรุณากรอกรหัสผ่าน")
            pwdentry.focus_force()
        else:
            sql = "select * from manager where username=? and pwd=?"
            cursor.execute(sql,[muserinfo.get(),mpwdinfo.get()])
            result_m = cursor.fetchall()
            if result_m: 
                loginframe.destroy()
                mlframe.destroy()
                homepage()
            else:
                messagebox.showwarning("Admin : ","ชื่อผู้ใช้งานหรือรหัสผ่านไม่ถูกต้อง")
                pwdentry.select_range(0,END)
                pwdentry.focus_force()
    
def emlogin():
    if userinfo.get() == "" or userinfo.get() == "ชื่อผู้ใช้งาน":
        messagebox.showwarning("Admin","กรุณากรอกชื่อผู้ใช้งาน")
        userentry.focus_force() 
    else: 
        sql  = "select * from employee where username=?"
        cursor.execute(sql,[userinfo.get()])
        result = cursor.fetchall()  
        if epwdinfo.get() == "" or epwdinfo.get() == "รหัสผ่าน":
            messagebox.showwarning("Admin","กรุณากรอกรหัสผ่าน")
            pwdentry.focus_force()
        else:
            sql = "select * from employee where username=? and pwd=?"
            cursor.execute(sql,[userinfo.get(),epwdinfo.get()])
            result = cursor.fetchall()
            if result: 
                loginframe.destroy()
                elframe.destroy()
                homepage()
            else:
                messagebox.showwarning("Admin : ","ชื่อผู้ใช้งานหรือรหัสผ่านไม่ถูกต้อง")
                pwdentry.select_range(0,END)
                pwdentry.focus_force()

def homepage():
    global unlock1,unlock2,unlock3,unlock4,unlock5,unlock6,unlock7,unlock8,unlock9,unlock10
    global homeframe
    loginframe.destroy()
    bgframe = Frame(root,bg='#F6F6F6')
    bgframe.place(x=0,y=0,width=w,height=h)
    homeframe = Frame(root,bg='#F6F6F6')
    homeframe.rowconfigure((0,1,2,3,4,5,6),weight=1)
    homeframe.columnconfigure((0,1,2,3,4,5),weight=1)
    root.config(bg='#F6F6F6')
    
    Button(homeframe,image=logout,bg='#F6F6F6',border=0,command=logouthome).grid(row=1,column=5,sticky='ne',padx=10,pady=10)
    Button(homeframe,text="สมัครพนักงาน",bg="grey",command=emplo).grid(row=0,column=0,sticky='news')
    Button(homeframe,text="สมัครสมาชิก",bg="grey",command=user).grid(row=0,column=1,sticky='news')
    Button(homeframe,text="ข้อมูลพนักงาน",bg="grey",command=emploedit).grid(row=0,column=2,sticky='news')
    Button(homeframe,text="ข้อมูลสมาชิก",bg="grey",command=useredit).grid(row=0,column=3,sticky='news')
    Button(homeframe,text="ร้านค้า",bg="grey",command=shop).grid(row=0,column=4,sticky='news')
    Button(homeframe,text="รายงาน",bg="grey",command=report).grid(row=0,column=5,sticky='news')
    for i in range(0,5):
        com = "Computer",i+1
        com2 = "Computer",i+6
        Label(homeframe,text=com,bg='#F6F6F6').grid(row=i+1,column=0,columnspan=2,sticky='wn',padx=60,pady=(10,0))
        Label(homeframe,text=com2,bg='#F6F6F6').grid(row=i+1,column=3,columnspan=2,sticky='wn',padx=60,pady=(10,0))
    for i in range(5):
        Label(homeframe,image=computer,bg='#F6F6F6').grid(row=i+1,column=0,columnspan=2,sticky="wn",padx=60,pady=(50,0))
        Label(homeframe,image=computer,bg='#F6F6F6').grid(row=i+1,column=3,columnspan=2,sticky="wn",padx=60,pady=(50,0))
        Label(homeframe,text=":",bg="#F6F6F6").grid(row=i+1,column=2,padx=(0,100),pady=(48,0))
        Label(homeframe,text=":",bg="#F6F6F6").grid(row=i+1,column=2,pady=(48,0))
        Label(homeframe,text=":",bg="#F6F6F6").grid(row=i+1,column=5,padx=(0,100),pady=(48,0))
        Label(homeframe,text=":",bg="#F6F6F6").grid(row=i+1,column=5,pady=(48,0))
    unlock1 = Button(homeframe,image=lock,bg='#F6F6F6',command=unlockc1,border=0,textvariable=ulk)
    unlock1.grid(row=1,column=1,columnspan=2,sticky="w",padx=50,pady=(50,0))
    unlock2 = Button(homeframe,image=lock,bg='#F6F6F6',command=unlockc2,border=0,textvariable=ulk)
    unlock2.grid(row=2,column=1,columnspan=2,sticky="w",padx=50,pady=(50,0))
    unlock3 = Button(homeframe,image=lock,bg='#F6F6F6',command=unlockc3,border=0,textvariable=ulk)
    unlock3.grid(row=3,column=1,columnspan=2,sticky="w",padx=50,pady=(50,0))
    unlock4 = Button(homeframe,image=lock,bg='#F6F6F6',command=unlockc4,border=0,textvariable=ulk)
    unlock4.grid(row=4,column=1,columnspan=2,sticky="w",padx=50,pady=(50,0))
    unlock5 = Button(homeframe,image=lock,bg='#F6F6F6',command=unlockc5,border=0,textvariable=ulk)
    unlock5.grid(row=5,column=1,columnspan=2,sticky="w",padx=50,pady=(50,0))
    unlock6 = Button(homeframe,image=lock,bg='#F6F6F6',command=unlockc6,border=0,textvariable=ulk)
    unlock6.grid(row=1,column=4,columnspan=2,sticky="w",padx=50,pady=(50,0))
    unlock7 = Button(homeframe,image=lock,bg='#F6F6F6',command=unlockc7,border=0,textvariable=ulk)
    unlock7.grid(row=2,column=4,columnspan=2,sticky="w",padx=50,pady=(50,0))
    unlock8 = Button(homeframe,image=lock,bg='#F6F6F6',command=unlockc8,border=0,textvariable=ulk)
    unlock8.grid(row=3,column=4,columnspan=2,sticky="w",padx=50,pady=(50,0))
    unlock9 = Button(homeframe,image=lock,bg='#F6F6F6',command=unlockc9,border=0,textvariable=ulk)
    unlock9.grid(row=4,column=4,columnspan=2,sticky="w",padx=50,pady=(50,0))
    unlock10 = Button(homeframe,image=lock,bg='#F6F6F6',command=unlockc10,border=0,textvariable=ulk)
    unlock10.grid(row=5,column=4,columnspan=2,sticky="w",padx=50,pady=(50,0))
    # hour
    Label(homeframe,bg='#F6F6F6',textvariable=hrspy1).grid(row=1,column=2,padx=(0,150),pady=(50,0))
    Label(homeframe,bg='#F6F6F6',textvariable=hrspy2).grid(row=2,column=2,padx=(0,150),pady=(50,0))
    Label(homeframe,bg='#F6F6F6',textvariable=hrspy3).grid(row=3,column=2,padx=(0,150),pady=(50,0))
    Label(homeframe,bg='#F6F6F6',textvariable=hrspy4).grid(row=4,column=2,padx=(0,150),pady=(50,0))
    Label(homeframe,bg='#F6F6F6',textvariable=hrspy5).grid(row=5,column=2,padx=(0,150),pady=(50,0))
    Label(homeframe,bg='#F6F6F6',textvariable=hrspy6).grid(row=1,column=5,padx=(0,150),pady=(50,0))
    Label(homeframe,bg='#F6F6F6',textvariable=hrspy7).grid(row=2,column=5,padx=(0,150),pady=(50,0))
    Label(homeframe,bg='#F6F6F6',textvariable=hrspy8).grid(row=3,column=5,padx=(0,150),pady=(50,0))
    Label(homeframe,bg='#F6F6F6',textvariable=hrspy9).grid(row=4,column=5,padx=(0,150),pady=(50,0))
    Label(homeframe,bg='#F6F6F6',textvariable=hrspy10).grid(row=5,column=5,padx=(0,150),pady=(50,0))
    # minutes
    Label(homeframe,bg='#F6F6F6',textvariable=mnspy1).grid(row=1,column=2,padx=(0,50),pady=(50,0))
    Label(homeframe,bg='#F6F6F6',textvariable=mnspy2).grid(row=2,column=2,padx=(0,50),pady=(50,0))
    Label(homeframe,bg='#F6F6F6',textvariable=mnspy3).grid(row=3,column=2,padx=(0,50),pady=(50,0))
    Label(homeframe,bg='#F6F6F6',textvariable=mnspy4).grid(row=4,column=2,padx=(0,50),pady=(50,0))
    Label(homeframe,bg='#F6F6F6',textvariable=mnspy5).grid(row=5,column=2,padx=(0,50),pady=(50,0))
    Label(homeframe,bg='#F6F6F6',textvariable=mnspy6).grid(row=1,column=5,padx=(0,50),pady=(50,0))
    Label(homeframe,bg='#F6F6F6',textvariable=mnspy7).grid(row=2,column=5,padx=(0,50),pady=(50,0))
    Label(homeframe,bg='#F6F6F6',textvariable=mnspy8).grid(row=3,column=5,padx=(0,50),pady=(50,0))
    Label(homeframe,bg='#F6F6F6',textvariable=mnspy9).grid(row=4,column=5,padx=(0,50),pady=(50,0))
    Label(homeframe,bg='#F6F6F6',textvariable=mnspy10).grid(row=5,column=5,padx=(0,50),pady=(50,0))
    # seconds
    Label(homeframe,text="00",bg='#F6F6F6',textvariable=scspy1).grid(row=1,column=2,padx=(40,0),pady=(50,0))
    Label(homeframe,text="00",bg='#F6F6F6',textvariable=scspy2).grid(row=2,column=2,padx=(40,0),pady=(50,0))
    Label(homeframe,text="00",bg='#F6F6F6',textvariable=scspy3).grid(row=3,column=2,padx=(40,0),pady=(50,0))
    Label(homeframe,text="00",bg='#F6F6F6',textvariable=scspy4).grid(row=4,column=2,padx=(40,0),pady=(50,0))
    Label(homeframe,text="00",bg='#F6F6F6',textvariable=scspy5).grid(row=5,column=2,padx=(40,0),pady=(50,0))
    Label(homeframe,text="00",bg='#F6F6F6',textvariable=scspy6).grid(row=1,column=5,padx=(40,0),pady=(50,0))
    Label(homeframe,text="00",bg='#F6F6F6',textvariable=scspy7).grid(row=2,column=5,padx=(40,0),pady=(50,0))
    Label(homeframe,text="00",bg='#F6F6F6',textvariable=scspy8).grid(row=3,column=5,padx=(40,0),pady=(50,0))
    Label(homeframe,text="00",bg='#F6F6F6',textvariable=scspy9).grid(row=4,column=5,padx=(40,0),pady=(50,0))
    Label(homeframe,text="00",bg='#F6F6F6',textvariable=scspy10).grid(row=5,column=5,padx=(40,0),pady=(50,0))
    homeframe.grid(row=0,column=0,columnspan=6,sticky='news')

def popcount():
    global top
    top = Toplevel(homeframe)
    top.geometry('470x150')
    Label(top,text="    กรุณาเลือกใช้บริการรายชั่วโมงหรือรายวัน").grid(row=0,column=0,columnspan=2,sticky='news',pady=10)
    Button(top,text="รายชั่วโมง",command=pophourpay,width=8).grid(row=1,column=0)
    Button(top,text="รายวัน",command=popdaypay,width=8).grid(row=1,column=1)

def pophourpay():
    global askhour,chhr
    askhour = Toplevel(top)
    askhour.geometry('330x180')
    Label(askhour,text="    เลือกจำนวนชั่วโมงที่ต้องการ").grid(row=0,column=0,columnspan=2,pady=10)
    chhr = Combobox(askhour,values=list(range(1,24)),width=10,textvariable=chhrspy)
    chhr.grid(row=1,column=0,columnspan=2)
    Button(askhour,text="ยืนยัน",command=choosehour).grid(row=2,column=0,pady=10)
    def canhr():
        askhour.destroy()
    Button(askhour,text="ยกเลิก",command=canhr).grid(row=2,column=1,pady=10)

def choosehour():
    global top2,usep,total_mem
    if chhrspy.get() == "" or chhrspy.get() == "0":
        messagebox.showwarning("Admin","กรุณาเลือกจำนวนชั่วโมง")
    else:
        member = messagebox.askquestion("Admin","คุณเป็นสมาชิกหรือไม่")
        if member == "yes":
            total_mem = int(chhrspy.get()) * 10
            ask = messagebox.askokcancel("Admin","ราคาทั้งหมด: %s บาท"%total_mem)
            if ask == True:
                top2 = Toplevel(top)
                top2.geometry('290x180')
                Label(top2,text="    กรุณากรอกชื่อผู้ใช้งาน").grid(row=0,column=0,columnspan=2,pady=10)
                usep = Entry(top2,textvariable=usepspy,width=15)
                usep.grid(row=1,column=0,columnspan=2)
                Button(top2,text="ยืนยัน",command=confirmpayhour).grid(row=2,column=0,pady=10)
                Button(top2,text="ยกเลิก",command=top2.destroy).grid(row=2,column=1,pady=10)
            else:
                chhrspy.set(1)
        else:
            total_nomem = (int(chhrspy.get()) * 10) + 5
            ask = messagebox.askokcancel("Admin","ราคาทั้งหมด: %s บาท"%total_nomem)
            if ask == True:
                if chhrspy.get() != "0":
                    sql_r1 = "insert into report1 values(?,?,?,?,?,?)"
                    cursor.execute(sql_r1,[retimed,retimem,retimey,"รายรับ","จำนวนชั่วโมงเข้าใช้งาน",total_nomem])
                    conn.commit()
                    sql_r2 = "insert into report2 values(?,?,?,?,?,?)"
                    cursor.execute(sql_r2,[retimed,retimem,retimey,"no",chhrspy.get(),0])
                    conn.commit()
                top.destroy()
                if ulk.get() == 1:
                    hrspy1.set(chhrspy.get())
                    unlock1['image'] = unlock
                    cntdownhourtime()
                elif ulk.get() == 2:
                    hrspy2.set(chhrspy.get())
                    unlock2['image'] = unlock
                    cntdownhourtime()
                elif ulk.get() == 3:
                    hrspy3.set(chhrspy.get())
                    unlock3['image'] = unlock
                    cntdownhourtime()
                elif ulk.get() == 4:
                    hrspy4.set(chhrspy.get())
                    unlock4['image'] = unlock
                    cntdownhourtime()
                elif ulk.get() == 5:
                    hrspy5.set(chhrspy.get())
                    unlock5['image'] = unlock
                    cntdownhourtime()
                elif ulk.get() == 6:
                    hrspy6.set(chhrspy.get())
                    unlock6['image'] = unlock
                    cntdownhourtime()
                elif ulk.get() == 7:
                    hrspy7.set(chhrspy.get())
                    unlock7['image'] = unlock
                    cntdownhourtime()
                elif ulk.get() == 8:
                    hrspy8.set(chhrspy.get())
                    unlock8['image'] = unlock
                    cntdownhourtime()
                elif ulk.get() == 9:
                    hrspy9.set(chhrspy.get())
                    unlock9['image'] = unlock
                    cntdownhourtime()
                else:
                    hrspy10.set(chhrspy.get())
                    unlock10['image'] = unlock
                    cntdownhourtime()
            else:
                chhrspy.set(1)
           
def confirmpayhour():
    sql = "select * from user where username=?"
    cursor.execute(sql,[usepspy.get()])
    result = cursor.fetchone()
    if result:
        pluspoint = int(result[7]) + (50 * int(chhrspy.get()))
        if chhrspy.get() != "0":
            sql_r1 = "insert into report1 values(?,?,?,?,?,?)"
            cursor.execute(sql_r1,[retimed,retimem,retimey,"รายรับ","จำนวนชั่วโมงเข้าใช้งาน",total_mem])
            conn.commit()
            sql_r2 = "insert into report2 values(?,?,?,?,?,?)"    
            cursor.execute(sql_r2,[retimed,retimem,retimey,"yes",chhrspy.get(),pluspoint])
            conn.commit()
        sql = "update user set point=? where username=?"
        cursor.execute(sql,[pluspoint,usepspy.get()])
        conn.commit()
        messagebox.showinfo("Admin","สะสมคะแนนสำเร็จ")
        usep.delete(0,END)
        top.destroy()
        top2.destroy()
        if ulk.get() == 1:
            hrspy1.set(chhrspy.get())
            unlock1['image'] = unlock
            cntdownhourtime()
        elif ulk.get() == 2:
            hrspy2.set(chhrspy.get())
            unlock2['image'] = unlock
            cntdownhourtime()
        elif ulk.get() == 3:
            hrspy3.set(chhrspy.get())
            unlock3['image'] = unlock
            cntdownhourtime()
        elif ulk.get() == 4:
            hrspy4.set(chhrspy.get())
            unlock4['image'] = unlock
            cntdownhourtime()
        elif ulk.get() == 5:
            hrspy5.set(chhrspy.get())
            unlock5['image'] = unlock
            cntdownhourtime()
        elif ulk.get() == 6:
            hrspy6.set(chhrspy.get())
            unlock6['image'] = unlock
            cntdownhourtime()
        elif ulk.get() == 7:
            hrspy7.set(chhrspy.get())
            unlock7['image'] = unlock
            cntdownhourtime()
        elif ulk.get() == 8:
            hrspy8.set(chhrspy.get())
            unlock8['image'] = unlock
            cntdownhourtime()
        elif ulk.get() == 9:
            hrspy9.set(chhrspy.get())
            unlock9['image'] = unlock
            cntdownhourtime()
        else:
            hrspy10.set(chhrspy.get())
            unlock10['image'] = unlock
            cntdownhourtime()
    else:
        usep.delete(0,END)
        messagebox.showwarning("Admin","ไม่พบชื่อผู้ใช้นี้ กรุณาลองใหม่อีกครั้ง")

def popdaypay():
    global top2,usep
    member = messagebox.askquestion("Admin","คุณเป็นสมาชิกหรือไม่")
    if member == "yes":
        ask = messagebox.askokcancel("Admin","ราคาทั้งหมด: 200 บาท")
        if ask == True:
            top2 = Toplevel(top)
            top2.geometry('290x180')
            Label(top2,text="    กรุณากรอกชื่อผู้ใช้งาน").grid(row=0,column=0,columnspan=2,pady=10)
            usep = Entry(top2,textvariable=usepspy,width=15)
            usep.grid(row=1,column=0,columnspan=2)
            Button(top2,text="ยืนยัน",command=confirmpayday).grid(row=2,column=0,pady=10)
            Button(top2,text="ยกเลิก",command=top2.destroy).grid(row=2,column=1,pady=10)
    else:
        ask = messagebox.askokcancel("Admin","ราคาทั้งหมด: 200 บาท")
        if ask == True:
            sql_r1 = "insert into report1 values(?,?,?,?,?,?)"
            cursor.execute(sql_r1,[retimed,retimem,retimey,"รายรับ","จำนวนชั่วโมงเข้าใช้งาน",200])
            conn.commit()
            sql_r2 = "insert into report2 values(?,?,?,?,?,?)"
            cursor.execute(sql_r2,[retimed,retimem,retimey,"no",24,0])
            conn.commit()
            top.destroy()
            if ulk.get() == 1:
                unlock1['image'] = unlock
                cntdowndaytime()
            elif ulk.get() == 2:
                unlock2['image'] = unlock
                cntdowndaytime()
            elif ulk.get() == 3:
                unlock3['image'] = unlock
                cntdowndaytime()
            elif ulk.get() == 4:
                unlock4['image'] = unlock
                cntdowndaytime()
            elif ulk.get() == 5:
                unlock5['image'] = unlock
                cntdowndaytime()
            elif ulk.get() == 6:
                unlock6['image'] = unlock
                cntdowndaytime()
            elif ulk.get() == 7:
                unlock7['image'] = unlock
                cntdowndaytime()
            elif ulk.get() == 8:
                unlock8['image'] = unlock
                cntdowndaytime()
            elif ulk.get() == 9:
                unlock9['image'] = unlock
                cntdowndaytime()
            else:
                unlock10['image'] = unlock
                cntdowndaytime()
 
def confirmpayday():
    sql = "select * from user where username=?"
    cursor.execute(sql,[usepspy.get()])
    result = cursor.fetchone()
    if result:
        pluspoint = int(result[7]) + (50 * 24)
        sql_r1 = "insert into report1 values(?,?,?,?,?,?)"
        cursor.execute(sql_r1,[retimed,retimem,retimey,"รายรับ","จำนวนชั่วโมงเข้าใช้งาน",200])
        conn.commit()
        sql_r2 = "insert into report2 values(?,?,?,?,?,?)"
        cursor.execute(sql_r2,[retimed,retimem,retimey,"yes",24,pluspoint])
        conn.commit()
        sql = "update user set point=? where username=?"
        cursor.execute(sql,[pluspoint,usepspy.get()])
        conn.commit()
        messagebox.showinfo("Admin","สะสมคะแนนสำเร็จ")
        usep.delete(0,END)
        top.destroy()
        top2.destroy()
        if ulk.get() == 1:
            unlock1['image'] = unlock
            cntdowndaytime()
        elif ulk.get() == 2:
            unlock2['image'] = unlock
            cntdowndaytime()
        elif ulk.get() == 3:
            unlock3['image'] = unlock
            cntdowndaytime()
        elif ulk.get() == 4:
            unlock4['image'] = unlock
            cntdowndaytime()
        elif ulk.get() == 5:
            unlock5['image'] = unlock
            cntdowndaytime()
        elif ulk.get() == 6:
            unlock6['image'] = unlock
            cntdowndaytime()
        elif ulk.get() == 7:
            unlock7['image'] = unlock
            cntdowndaytime()
        elif ulk.get() == 8:
            unlock8['image'] = unlock
            cntdowndaytime()
        elif ulk.get() == 9:
            unlock9['image'] = unlock
            cntdowndaytime()
        else:
            unlock10['image'] = unlock
            cntdowndaytime()
    else:
        usep.delete(0,END)
        messagebox.showwarning("Admin","ไม่พบชื่อผู้ใช้นี้ กรุณาลองใหม่อีกครั้ง")

def cntdownhourtime(): #อธิบายว่าจะแจ้งที่เครื่องลูกค้า
    pc_times = int(chhrspy.get())* 3600 + 0 * 60 + 0 
    chhrspy.set(0)
    idxPc = ulk.get() - 1
    arrPc[idxPc] = pc_times
    maxLoop = 0
    for index, item in enumerate(arrPc):
        if item > maxLoop:
            maxLoop = item
    while maxLoop > -1:
        for index, item in enumerate(arrPc):
            if item != -1:
                minute,second=(item//60, item %60)
                hour=0
                if minute>60:
                    hour,minute=(minute//60,minute%60)
                pcIdx = index + 1
                eval("scspy%d.set(second)" % (pcIdx))
                eval("mnspy%d.set(minute)" % (pcIdx))
                eval("hrspy%d.set(hour)" % (pcIdx))
                if index == 0:
                    scspy1.set(second)
                    mnspy1.set(minute)
                    hrspy1.set(hour)
                    if hrspy1.get() == "0" and mnspy1.get() == "0" and scspy1.get() == "1":
                        unlock1['image'] = lock
                        messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer1")
                if index == 1:
                    scspy2.set(second)
                    mnspy2.set(minute)
                    hrspy2.set(hour)
                    if hrspy2.get() == "0" and mnspy2.get() == "0" and scspy2.get() == "1":
                        unlock2['image'] = lock
                        print(unlock2['image'])
                        messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer2")
                if index == 2:
                    scspy3.set(second)
                    mnspy3.set(minute)
                    hrspy3.set(hour)
                    if hrspy3.get() == "0" and mnspy3.get() == "0" and scspy3.get() == "1":
                        unlock3['image'] = lock
                        messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer3")
                if index == 3:
                    scspy4.set(second)
                    mnspy4.set(minute)
                    hrspy4.set(hour)
                    if hrspy4.get() == "0" and mnspy4.get() == "0" and scspy4.get() == "1":
                        unlock2['image'] = lock
                        messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer4")
                if index == 4:
                    scspy5.set(second)
                    mnspy5.set(minute)
                    hrspy5.set(hour)
                    if hrspy5.get() == "0" and mnspy5.get() == "0" and scspy5.get() == "1":
                        unlock5['image'] = lock
                        messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer5")
                if index == 5:
                    scspy6.set(second)
                    mnspy6.set(minute)
                    hrspy6.set(hour)
                    if hrspy6.get() == "0" and mnspy6.get() == "0" and scspy6.get() == "1":
                        unlock6['image'] = lock
                        messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer6")
                if index == 6:
                    scspy7.set(second)
                    mnspy7.set(minute)
                    hrspy7.set(hour)
                    if hrspy7.get() == "0" and mnspy7.get() == "0" and scspy7.get() == "1":
                        unlock7['image'] = lock
                        messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer7")
                if index == 7:
                    scspy8.set(second)
                    mnspy8.set(minute)
                    hrspy8.set(hour)
                    if hrspy8.get() == "0" and mnspy8.get() == "0" and scspy8.get() == "1":
                        unlock8['image'] = lock
                        messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer8")
                if index == 8:
                    scspy9.set(second)
                    mnspy9.set(minute)
                    hrspy9.set(hour)
                    if hrspy9.get() == "0" and mnspy9.get() == "0" and scspy9.get() == "1":
                        unlock9['image'] = lock
                        messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer9")
                if index == 9:
                    scspy10.set(second)
                    mnspy10.set(minute)
                    hrspy10.set(hour)
                    if hrspy10.get() == "0" and mnspy10.get() == "0" and scspy10.get() == "1":
                        unlock10['image'] = lock
                        messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer10")
                arrPc[index] = arrPc[index] - 1
        root.update()
        time.sleep(1)
        maxLoop -= 1

def cntdowndaytime(): #อธิบายว่าจะแจ้งที่เครื่องลูกค้า
    pc_times = int(daytime.get()) * 3600 + 0 * 60 + 0 
    idxPc = ulk.get() - 1
    arrPc[idxPc] = pc_times
    maxLoop = 0
    for index, item in enumerate(arrPc):
        if item > maxLoop:
            maxLoop = item
    while maxLoop > -1:
        for index, item in enumerate(arrPc):
            if item != -1:
                minute,second=(item//60, item %60)
                hour=0
                if minute>60:
                    hour,minute=(minute//60,minute%60)
                pcIdx = index + 1
                eval("scspy%d.set(second)" % (pcIdx))
                eval("mnspy%d.set(minute)" % (pcIdx))
                eval("hrspy%d.set(hour)" % (pcIdx))
                if index == 0:
                    scspy1.set(second)
                    mnspy1.set(minute)
                    hrspy1.set(hour)
                    if hrspy1.get() == "0" and mnspy1.get() == "10" and scspy1.get() == "0":
                        messagebox.showinfo("Admin","เหลือเวลาอีก 10 นาทีในการใช้บริการ Computer1")
                    if hrspy1.get() == "0" and mnspy1.get() == "0" and scspy1.get() == "1":
                        unlock1['image'] = lock
                        messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer1")
                if index == 1:
                    scspy2.set(second)
                    mnspy2.set(minute)
                    hrspy2.set(hour)
                    if hrspy2.get() == "0" and mnspy2.get() == "10" and scspy2.get() == "0":
                        messagebox.showinfo("Admin","เหลือเวลาอีก 10 นาทีในการใช้บริการ Computer2")
                    if hrspy2.get() == "0" and mnspy2.get() == "0" and scspy2.get() == "1":
                        unlock2['image'] = lock
                        print(unlock2['image'])
                        messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer2")
                if index == 2:
                    scspy3.set(second)
                    mnspy3.set(minute)
                    hrspy3.set(hour)
                    if hrspy3.get() == "0" and mnspy3.get() == "10" and scspy3.get() == "0":
                        messagebox.showinfo("Admin","เหลือเวลาอีก 10 นาทีในการใช้บริการ Computer3")
                    if hrspy3.get() == "0" and mnspy3.get() == "0" and scspy3.get() == "1":
                        unlock3['image'] = lock
                        messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer3")
                if index == 3:
                    scspy4.set(second)
                    mnspy4.set(minute)
                    hrspy4.set(hour)
                    if hrspy4.get() == "0" and mnspy4.get() == "10" and scspy4.get() == "0":
                        messagebox.showinfo("Admin","เหลือเวลาอีก 10 นาทีในการใช้บริการ Computer4")
                    if hrspy4.get() == "0" and mnspy4.get() == "0" and scspy4.get() == "1":
                        unlock2['image'] = lock
                        messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer4")
                if index == 4:
                    scspy5.set(second)
                    mnspy5.set(minute)
                    hrspy5.set(hour)
                    if hrspy5.get() == "0" and mnspy5.get() == "10" and scspy5.get() == "0":
                        messagebox.showinfo("Admin","เหลือเวลาอีก 10 นาทีในการใช้บริการ Computer5")
                    if hrspy5.get() == "0" and mnspy5.get() == "0" and scspy5.get() == "1":
                        unlock5['image'] = lock
                        messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer5")
                if index == 5:
                    scspy6.set(second)
                    mnspy6.set(minute)
                    hrspy6.set(hour)
                    if hrspy6.get() == "0" and mnspy6.get() == "10" and scspy6.get() == "0":
                        messagebox.showinfo("Admin","เหลือเวลาอีก 10 นาทีในการใช้บริการ Computer6")
                    if hrspy6.get() == "0" and mnspy6.get() == "0" and scspy6.get() == "1":
                        unlock6['image'] = lock
                        messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer6")
                if index == 6:
                    scspy7.set(second)
                    mnspy7.set(minute)
                    hrspy7.set(hour)
                    if hrspy7.get() == "0" and mnspy7.get() == "10" and scspy7.get() == "0":
                        messagebox.showinfo("Admin","เหลือเวลาอีก 10 นาทีในการใช้บริการ Computer7")
                    if hrspy7.get() == "0" and mnspy7.get() == "0" and scspy7.get() == "1":
                        unlock7['image'] = lock
                        messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer7")
                if index == 7:
                    scspy8.set(second)
                    mnspy8.set(minute)
                    hrspy8.set(hour)
                    if hrspy8.get() == "0" and mnspy8.get() == "10" and scspy8.get() == "0":
                        messagebox.showinfo("Admin","เหลือเวลาอีก 10 นาทีในการใช้บริการ Computer8")
                    if hrspy8.get() == "0" and mnspy8.get() == "0" and scspy8.get() == "1":
                        unlock8['image'] = lock
                        messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer8")
                if index == 8:
                    scspy9.set(second)
                    mnspy9.set(minute)
                    hrspy9.set(hour)
                    if hrspy9.get() == "0" and mnspy9.get() == "10" and scspy9.get() == "0":
                        messagebox.showinfo("Admin","เหลือเวลาอีก 10 นาทีในการใช้บริการ Computer9")
                    if hrspy9.get() == "0" and mnspy9.get() == "0" and scspy9.get() == "1":
                        unlock9['image'] = lock
                        messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer9")
                if index == 9:
                    scspy10.set(second)
                    mnspy10.set(minute)
                    hrspy10.set(hour)
                    if hrspy10.get() == "0" and mnspy10.get() == "10" and scspy10.get() == "0":
                        messagebox.showinfo("Admin","เหลือเวลาอีก 10 นาทีในการใช้บริการ Computer10")
                    if hrspy10.get() == "0" and mnspy10.get() == "0" and scspy10.get() == "1":
                        unlock10['image'] = lock
                        messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer10")
                arrPc[index] = arrPc[index] - 1
        root.update()
        time.sleep(1)
        maxLoop -= 1
    
def unlockc1():
    ulk.set(1)
    if unlock1['image'] == 'pyimage11':
        daytime.set(24)
        popcount()       
    else:
        can = messagebox.askquestion("Admin","ต้องการเลิกใช้งานหรือไม่")
        if can == "yes":
            chhrspy.set(0)
            daytime.set(0)
            unlock1['image'] = lock
            messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer1")
            cntdownhourtime()
def unlockc2():
    ulk.set(2)
    if unlock2['image'] == 'pyimage11':
        daytime.set(24)
        popcount()
    else:
        can = messagebox.askquestion("Admin","ต้องการเลิกใช้งานหรือไม่")
        if can == "yes":
            chhrspy.set(0)
            daytime.set(0)
            unlock2['image'] = lock
            messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer2")
            cntdownhourtime()
def unlockc3():
    ulk.set(3)
    if unlock3['image'] == 'pyimage11':
        daytime.set(24)
        popcount()
    else:
        can = messagebox.askquestion("Admin","ต้องการเลิกใช้งานหรือไม่")
        if can == "yes":
            chhrspy.set(0)
            daytime.set(0)
            unlock3['image'] = lock
            messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer3")
            cntdownhourtime()
def unlockc4():
    ulk.set(4)
    if unlock4['image'] == 'pyimage11':
        daytime.set(24)
        popcount()
    else:
        can = messagebox.askquestion("Admin","ต้องการเลิกใช้งานหรือไม่")
        if can == "yes":
            chhrspy.set(0)
            daytime.set(0)
            unlock4['image'] = lock
            messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer4")
            cntdownhourtime()
def unlockc5():
    ulk.set(5)
    if unlock5['image'] == 'pyimage11':
        daytime.set(24)
        popcount()
    else:
        can = messagebox.askquestion("Admin","ต้องการเลิกใช้งานหรือไม่")
        if can == "yes":
            chhrspy.set(0)
            daytime.set(0)
            unlock5['image'] = lock
            messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer5")
            cntdownhourtime()
def unlockc6():
    ulk.set(6)
    if unlock6['image'] == 'pyimage11':
        daytime.set(24)
        popcount()
    else:
        can = messagebox.askquestion("Admin","ต้องการเลิกใช้งานหรือไม่")
        if can == "yes":
            chhrspy.set(0)
            daytime.set(0)
            unlock6['image'] = lock
            messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer6")
            cntdownhourtime()
def unlockc7():
    ulk.set(7)
    if unlock7['image'] == 'pyimage11':
        daytime.set(24)
        popcount()
    else:
        can = messagebox.askquestion("Admin","ต้องการเลิกใช้งานหรือไม่")
        if can == "yes":
            chhrspy.set(0)
            daytime.set(0)
            unlock7['image'] = lock
            messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer7")
            cntdownhourtime()
def unlockc8():
    ulk.set(8)
    if unlock8['image'] == 'pyimage11':
        daytime.set(24)
        popcount()
    else:
        can = messagebox.askquestion("Admin","ต้องการเลิกใช้งานหรือไม่")
        if can == "yes":
            chhrspy.set(0)
            daytime.set(0)
            unlock8['image'] = lock
            messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer8")
            cntdownhourtime()
def unlockc9():
    ulk.set(9)
    if unlock9['image'] == 'pyimage11':
        daytime.set(24)
        popcount()
    else:
        can = messagebox.askquestion("Admin","ต้องการเลิกใช้งานหรือไม่")
        if can == "yes":
            chhrspy.set(0)
            daytime.set(0)
            unlock9['image'] = lock
            messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer9")
            cntdownhourtime()
def unlockc10():
    ulk.set(10)
    if unlock10['image'] == 'pyimage11':
        daytime.set(24)
        popcount()
    else:
        can = messagebox.askquestion("Admin","ต้องการเลิกใช้งานหรือไม่")
        if can == "yes":
            chhrspy.set(0)
            daytime.set(0)
            unlock10['image'] = lock
            messagebox.showinfo("Admin","หมดเวลาการใช้บริการ Computer10")
            cntdownhourtime()

################################################################### สมัคร สมาชิก & พนักงาน ###################################################################

def emplo():
    global firstname,lastname,birthday,address,phonenum,email,newuser,newpwd,cfpwd
    global emploframe
    bgframe = Frame(root,bg='#F6F6F6')
    bgframe.place(x=0,y=0,width=w,height=h)
    homeframe.destroy()
    emploframe = Frame(root,bg='#F6F6F6')
    emploframe.rowconfigure((0,1,2,3,4,5,6,7,8,9,10),weight=2)
    emploframe.columnconfigure((0,1),weight=2)

    Label(emploframe,text="สมัครพนักงาน",font="Times 24 bold",bg='grey').grid(row=0,column=0,rowspan=4,columnspan=4,sticky='news',pady=(0,10))
    Button(emploframe,image=home,bg='grey',border=0,command=ebackhome).grid(row=3,column=3,sticky='e',padx=30,pady=10)
    Label(emploframe,text="ชื่อ: ",font="Times 18",bg='#F6F6F6').grid(row=4,column=0,sticky='e',padx=20,pady=10)
    Label(emploframe,text="นามสกุล: ",font="Times 18",bg='#F6F6F6').grid(row=4,column=2,sticky='e',padx=20,pady=10)
    Label(emploframe,text="วัน/เดือน/ปีเกิด: ",font="Times 18",bg='#F6F6F6').grid(row=5,column=0,sticky='e',padx=20,pady=10)
    Label(emploframe,text="ที่อยู่: ",font="Times 18",bg='#F6F6F6').grid(row=6,column=0,sticky='e',padx=20,pady=10)
    Label(emploframe,text="เบอร์โทร: ",font="Times 18",bg='#F6F6F6').grid(row=7,column=0,sticky='e',padx=20,pady=10)
    Label(emploframe,text="อีเมล: ",font="Times 18",bg='#F6F6F6').grid(row=7,column=2,sticky='e',padx=20,pady=10)
    Label(emploframe,text="ชื่อผู้ใช้งาน: ",font="Times 18",bg='#F6F6F6').grid(row=8,column=0,sticky='e',padx=20,pady=10)
    Label(emploframe,text="รหัสผ่าน: ",font="Times 18",bg='#F6F6F6').grid(row=9,column=0,sticky='e',padx=20,pady=10)
    Label(emploframe,text="ยืนยันรหัสผ่าน: ",font="Times 18",bg='#F6F6F6').grid(row=10,column=0,sticky='e',padx=20,pady=10)

    firstname = Entry(emploframe,bg='lightgrey',textvariable=fname)
    firstname.grid(row=4,column=1,sticky='w',padx=10,pady=10)
    firstname.insert(0,"xxxxxx")
    firstname.config(state=DISABLED)
    firstname.bind("<Button-1>",fn)
    lastname = Entry(emploframe,bg='lightgrey',textvariable=lname)
    lastname.grid(row=4,column=3,sticky='w',padx=(0,100),pady=10)
    lastname.insert(0,"xxxxxx")
    lastname.config(state=DISABLED)
    lastname.bind("<Button-1>",ln)
    birthday = Entry(emploframe,bg='lightgrey',textvariable=bday)
    birthday.grid(row=5,column=1,sticky='w',padx=10,pady=10)
    birthday.insert(0,"ddmmyyyy")
    birthday.config(state=DISABLED)
    birthday.bind("<Button-1>",bd) 
    address = Entry(emploframe,bg='lightgrey',textvariable=ads,width=55)
    address.grid(row=6,column=1,columnspan=4,sticky='w',padx=10,pady=10)
    address.insert(0,"xxxxxx bkk")
    address.config(state=DISABLED)
    address.bind("<Button-1>",ad)
    phonenum = Entry(emploframe,bg='lightgrey',textvariable=phnum)
    phonenum.grid(row=7,column=1,sticky='w',padx=10,pady=10)
    phonenum.insert(0,"0000000000")
    phonenum.config(state=DISABLED)
    phonenum.bind("<Button-1>",phn)
    email = Entry(emploframe,bg='lightgrey',textvariable=em)
    email.grid(row=7,column=3,sticky='w',padx=(0,100),pady=10)
    email.insert(0,"xxxxxx@gmail.com")
    email.config(state=DISABLED)
    email.bind("<Button-1>",ema)
    newuser = Entry(emploframe,bg='lightgrey',textvariable=newuserinfo)
    newuser.grid(row=8,column=1,sticky='w',padx=10,pady=10)
    newuser.insert(0,"xxxxxx.x")
    newuser.config(state=DISABLED)
    newuser.bind("<Button-1>",nu)
    newpwd = Entry(emploframe,bg='lightgrey',show='*',textvariable=newpwdinfo)
    newpwd.grid(row=9,column=1,sticky='w',padx=10,pady=10)
    newpwd.insert(0,"########") 
    newpwd.config(state=DISABLED)
    newpwd.bind("<Button-1>",np)
    cfpwd = Entry(emploframe,bg='lightgrey',show='*',textvariable=cfpwdinfo)
    cfpwd.grid(row=10,column=1,sticky='w',padx=10,pady=10)
    cfpwd.insert(0,"########")
    cfpwd.config(state=DISABLED)
    cfpwd.bind("<Button-1>",cfp)

    Button(emploframe,text="ยกเลิก",bg="grey",width=10,command=cancel_emplo).grid(row=11,column=2)
    Button(emploframe,text="ยืนยัน",bg="grey",width=10,command=confirm_emplo).grid(row=11,column=3)
    emploframe.grid(row=0,column=0,columnspan=4,sticky='news')

def fn(event):
    firstname.config(state=NORMAL)
    firstname.delete(0,END)
def ln(event):
    lastname.config(state=NORMAL)
    lastname.delete(0,END)
def bd(event):
    birthday.config(state=NORMAL)
    birthday.delete(0,END)
def ad(event):
    address.config(state=NORMAL)
    address.delete(0,END)
def phn(event):
    phonenum.config(state=NORMAL)
    phonenum.delete(0,END)
def ema(event):
    email.config(state=NORMAL)
    email.delete(0,END)
def nu(event):
    newuser.config(state=NORMAL)
    newuser.delete(0,END)
def np(event):
    newpwd.config(state=NORMAL)
    newpwd.delete(0,END)
def cfp(event):
    cfpwd.config(state=NORMAL)
    cfpwd.delete(0,END)

def cancel_emplo():
    cancelem = messagebox.askquestion("Cancel Register","คุณแน่ใจหรือว่าต้องการยกเลิกการสมัครพนักงาน")
    if cancelem == "yes" :
        ebackhome()

def confirm_emplo():
    bday_t = bday.get()
    phnum_t = phnum.get()
    em_t = em.get()
    newpwdinfo_t = newpwdinfo.get()
    if fname.get() == "" or fname.get() == "xxxxxx":
        messagebox.showwarning("Admin","กรุณากรอกชื่อ")
        firstname.focus_force()
    elif lname.get() == "" or lname.get() == "xxxxxx" :
        messagebox.showwarning("Admin","กรุณากรอกนามสกุล")
        lastname.focus_force()
    elif bday.get() == "" or bday.get() == "ddmmyyyy":
        messagebox.showwarning("Admin","กรุณากรอก วัน/เดือน/ปีเกิด")
        birthday.focus_force()
    elif bday_t.isdigit() != True :
        messagebox.showwarning("Admin","กรุณากรอก วัน/เดือน/ปีเกิดเป็นตัวเลขเท่านั้น")
        birthday.focus_force()
    elif len(bday_t) != 8 :
        messagebox.showwarning("Admin","กรุณากรอก วัน/เดือน/ปีเกิด ในรูปแบบ ddmmyyyy เท่านั้น \nexample(01012000) ")
        birthday.focus_force()
    elif ads.get() == "" or ads.get() == "xxxxxx bkk" :
        messagebox.showwarning("Admin","กรุณากรอกที่อยู่")
        address.focus_force()
    elif phnum.get() == "" or phnum.get() == "0000000000" : 
        messagebox.showwarning("Admin","กรุณากรอกเบอร์โทร")
        phonenum.focus_force()
    elif phnum_t.isdigit() != True:
        messagebox.showwarning("Admin","กรุณากรอกเบอร์โทรเป็นตัวเลขเท่านั้น")
        phonenum.focus_force()
    elif len(phnum_t) != 10:
        messagebox.showwarning("Admin","กรุณากรอกเบอร์โทรให้ครบ 10 หลัก")
        phonenum.focus_force()
    elif em.get() == "" or em.get() == "xxxxxx@gmail.com" : 
        messagebox.showwarning("Admin","กรุณากรอกอีเมล")
        email.focus_force()
    elif em_t[-10:] != "@gmail.com" :      
        messagebox.showwarning("Admin","กรุณากรอกข้อมูลในรูปแบบ example@gmail.com")
        email.focus_force()
    elif newuserinfo.get() == "" or newuserinfo.get() == "xxxxxx.x" : 
        messagebox.showwarning("Admin","กรุณากรอกชื่อผู้ใช้งาน")
        newuser.focus_force()
    elif newpwdinfo.get()== "" or newpwdinfo.get()== "########" : 
        messagebox.showwarning("Admin","กรุณากรอกรหัสผ่าน")
        newpwd.focus_force()
    elif len(newpwdinfo_t) < 8 or len(newpwdinfo_t) > 16 : 
        messagebox.showwarning("Admin","กรุณากรอกรหัสผ่านระหว่าง 8-16 ตัว")
        newpwd.focus_force()
    elif newpwdinfo_t.isalnum() != True: 
        messagebox.showwarning("Admin","กรุณากรอกรหัสผ่านเป็นตัวอักษรหรือตัวเลขเท่านั้น")
        newpwd.focus_force()
    elif cfpwdinfo.get() == "" or cfpwdinfo.get() == "########" : 
        messagebox.showwarning("Admin","กรุณากรอกยืนยันรหัสผ่าน")
        cfpwd.focus_force()
    else:
        sql = "select * from employee where username=?"
        cursor.execute(sql,[newuserinfo.get()])
        result  = cursor.fetchall()
        if result :
            if result : 
                messagebox.showwarning("Admin","มีชื่อผู้ใช้งานนี้แล้ว กรุณากรอกชื่อผู้ใช้งานใหม่")
                newuser.select_range(0,END)
                newuser.focus_force()
        else:
            if newpwdinfo.get() == cfpwdinfo.get():
                confirmms = messagebox.askquestion("Confirm Register","คุณแน่ใจหรือว่าต้องการยืนยันการสมัครพนักงาน")
                if confirmms == "yes" :
                    sql="insert into employee values(?,?,?,?,?,?,?,?)"
                    cursor.execute(sql,[fname.get(),lname.get(),bday.get(),ads.get(),phnum.get(),em.get(),newuserinfo.get(),newpwdinfo.get()])
                    conn.commit()
                    messagebox.showinfo("Admin","บันทึกข้อมูลเรียบร้อย")
                    ebackhome()
            else:
                messagebox.showwarning("Admin","รหัสผ่านไม่ตรงกัน")
                cfpwd.select_range(0,END)
                cfpwd.focus_force()

def ebackhome():
    firstname.config(state=NORMAL)
    firstname.delete(0,END)
    lastname.config(state=NORMAL)
    lastname.delete(0,END)
    birthday.config(state=NORMAL)
    birthday.delete(0,END)
    address.config(state=NORMAL)
    address.delete(0,END)
    phonenum.config(state=NORMAL)
    phonenum.delete(0,END)
    email.config(state=NORMAL)
    email.delete(0,END)
    newuser.config(state=NORMAL)
    newuser.delete(0,END)
    newpwd.config(state=NORMAL)
    newpwd.delete(0,END)
    cfpwd.config(state=NORMAL)
    cfpwd.delete(0,END)
    emploframe.destroy()
    homepage()

def user():
    global firstname2,lastname2,birthday2,address2,phonenum2,email2,newuser2
    global userframe
    bgframe = Frame(root,bg='#F6F6F6')
    bgframe.place(x=0,y=0,width=w,height=h)
    homeframe.destroy()
    userframe = Frame(root,bg='#F6F6F6')
    userframe.rowconfigure((0,1,2,3,4,5,6,7,8,9,10),weight=2)
    userframe.columnconfigure((0,1),weight=2)

    Label(userframe,text="สมัครสมาชิก",font="Times 24 bold",bg='grey').grid(row=0,column=0,rowspan=4,columnspan=4,sticky='news',pady=(0,10))
    Button(userframe,image=home,bg='grey',border=0,command=ubackhome).grid(row=3,column=3,sticky='e',padx=30,pady=10)
    Label(userframe,text="ชื่อ: ",font="Times 18",bg='#F6F6F6').grid(row=4,column=0,sticky='e',padx=20,pady=10)
    Label(userframe,text="นามสกุล: ",font="Times 18",bg='#F6F6F6').grid(row=4,column=2,sticky='e',padx=20,pady=10)
    Label(userframe,text="วัน/เดือน/ปีเกิด: ",font="Times 18",bg='#F6F6F6').grid(row=5,column=0,sticky='e',padx=20,pady=10)
    Label(userframe,text="ที่อยู่: ",font="Times 18",bg='#F6F6F6').grid(row=6,column=0,sticky='e',padx=20,pady=10)
    Label(userframe,text="เบอร์โทร: ",font="Times 18",bg='#F6F6F6').grid(row=7,column=0,sticky='e',padx=20,pady=10)
    Label(userframe,text="อีเมล: ",font="Times 18",bg='#F6F6F6').grid(row=7,column=2,sticky='e',padx=20,pady=10)
    Label(userframe,text="ชื่อผู้ใช้งาน: ",font="Times 18",bg='#F6F6F6').grid(row=8,column=0,sticky='e',padx=20,pady=10)

    firstname2 = Entry(userframe,bg='lightgrey',textvariable=fname2)
    firstname2.grid(row=4,column=1,sticky='w',padx=10,pady=10)
    firstname2.insert(0,"xxxxxx")
    firstname2.config(state=DISABLED)
    firstname2.bind("<Button-1>",fn2)
    lastname2 = Entry(userframe,bg='lightgrey',textvariable=lname2)
    lastname2.grid(row=4,column=3,sticky='w',padx=(0,100),pady=10)
    lastname2.insert(0,"xxxxxx")
    lastname2.config(state=DISABLED)
    lastname2.bind("<Button-1>",ln2)
    birthday2 = Entry(userframe,bg='lightgrey',textvariable=bday2)
    birthday2.grid(row=5,column=1,sticky='w',padx=10,pady=10)
    birthday2.insert(0,"ddmmyyyy")
    birthday2.config(state=DISABLED)
    birthday2.bind("<Button-1>",bd2) 
    address2 = Entry(userframe,bg='lightgrey',textvariable=ads2,width=55)
    address2.grid(row=6,column=1,columnspan=4,sticky='w',padx=10,pady=10)
    address2.insert(0,"xxxxxx bkk")
    address2.config(state=DISABLED)
    address2.bind("<Button-1>",ad2)
    phonenum2 = Entry(userframe,bg='lightgrey',textvariable=phnum2)
    phonenum2.grid(row=7,column=1,sticky='w',padx=10,pady=10)
    phonenum2.insert(0,"0000000000")
    phonenum2.config(state=DISABLED)
    phonenum2.bind("<Button-1>",phn2)
    email2 = Entry(userframe,bg='lightgrey',textvariable=em2)
    email2.grid(row=7,column=3,sticky='w',padx=(0,100),pady=10)
    email2.insert(0,"xxxxxx@gmail.com")
    email2.config(state=DISABLED)
    email2.bind("<Button-1>",ema2)
    newuser2 = Entry(userframe,bg='lightgrey',textvariable=newuserinfo2)
    newuser2.grid(row=8,column=1,sticky='w',padx=10,pady=10)
    newuser2.insert(0,"xxxxxx.x")
    newuser2.config(state=DISABLED)
    newuser2.bind("<Button-1>",nu2)

    Button(userframe,text="ยกเลิก",bg="grey",width=10,command=cancel_user).grid(row=11,column=2)
    Button(userframe,text="ยืนยัน",bg="grey",width=10,command=confirm_user).grid(row=11,column=3)
    userframe.grid(row=0,column=0,columnspan=4,sticky='news')

def fn2(event):
    firstname2.config(state=NORMAL)
    firstname2.delete(0,END)
def ln2(event):
    lastname2.config(state=NORMAL)
    lastname2.delete(0,END)
def bd2(event):
    birthday2.config(state=NORMAL)
    birthday2.delete(0,END)
def ad2(event):
    address2.config(state=NORMAL)
    address2.delete(0,END)
def phn2(event):
    phonenum2.config(state=NORMAL)
    phonenum2.delete(0,END)
def ema2(event):
    email2.config(state=NORMAL)
    email2.delete(0,END)
def nu2(event):
    newuser2.config(state=NORMAL)
    newuser2.delete(0,END)

def cancel_user():
    cancelus = messagebox.askquestion("Cancel Register","คุณแน่ใจหรือว่าต้องการยกเลิกการสมัครสมาชิก")
    if cancelus == "yes" :
        ubackhome()

def confirm_user():
    bday_t = bday2.get()
    phnum_t = phnum2.get()
    em_t = em2.get()
    if fname2.get() == "" or fname2.get() == "xxxxxx":
        messagebox.showwarning("Admin","กรุณากรอกชื่อ")
        firstname2.focus_force()
    elif lname2.get() == "" or lname2.get() == "xxxxxx" :
        messagebox.showwarning("Admin","กรุณากรอกนามสกุล")
        lastname2.focus_force()
    elif bday2.get() == "" or bday2.get() == "ddmmyyyy":
        messagebox.showwarning("Admin","กรุณากรอก วัน/เดือน/ปีเกิด")
        birthday2.focus_force()
    elif bday_t.isdigit() != True :
        messagebox.showwarning("Admin","กรุณากรอก วัน/เดือน/ปีเกิดเป็นตัวเลขเท่านั้น")
        birthday2.focus_force()
    elif len(bday_t) != 8 :
        messagebox.showwarning("Admin","กรุณากรอก วัน/เดือน/ปีเกิด ในรูปแบบ ddmmyyyy เท่านั้น \nexample(01012000) ")
        birthday2.focus_force()
    elif ads2.get() == "" or ads2.get() == "xxxxxx bkk" :
        messagebox.showwarning("Admin","กรุณากรอกที่อยู่")
        address2.focus_force()
    elif phnum2.get() == "" or phnum2.get() == "0000000000" : 
        messagebox.showwarning("Admin","กรุณากรอกเบอร์โทร")
        phonenum2.focus_force()
    elif phnum_t.isdigit() != True:
        messagebox.showwarning("Admin","กรุณากรอกเบอร์โทรเป็นตัวเลขเท่านั้น")
        phonenum2.focus_force()
    elif len(phnum_t) != 10:
        messagebox.showwarning("Admin","กรุณากรอกเบอร์โทรให้ครบ 10 หลัก")
        phonenum2.focus_force()
    elif em2.get() == "" or em2.get() == "xxxxxx@gmail.com" : 
        messagebox.showwarning("Admin","กรุณากรอกอีเมล")
        email2.focus_force()
    elif em_t[-10:] != "@gmail.com" :      
        messagebox.showwarning("Admin","กรุณากรอกข้อมูลในรูปแบบ example@gmail.com")
        email2.focus_force()
    elif newuserinfo2.get() == "" or newuserinfo2.get() == "xxxxxx.x" : 
        messagebox.showwarning("Admin","กรุณากรอกชื่อผู้ใช้งาน")
        newuser2.focus_force()
    else:
        sql = "select * from user where username=?" #Check username is already exists ?
        cursor.execute(sql,[newuserinfo2.get()])
        result  = cursor.fetchall()
        if result :
            if result : 
                messagebox.showwarning("Admin","มีชื่อผู้ใช้งานนี้แล้ว กรุณากรอกชื่อผู้ใช้งานใหม่")
                newuser2.select_range(0,END)
                newuser2.focus_force()
        else:
            confirmms = messagebox.askquestion("Confirm Register","คุณแน่ใจหรือว่าต้องการยืนยันการสมัครสมาชิก")
            if confirmms == "yes" :
                sql="insert into user values(?,?,?,?,?,?,?,?)"
                cursor.execute(sql,[fname2.get(),lname2.get(),bday2.get(),ads2.get(),phnum2.get(),em2.get(),newuserinfo2.get(),0])
                conn.commit()
                messagebox.showinfo("Admin","บันทึกข้อมูลเรียบร้อย")
                ubackhome()

def ubackhome():
    firstname2.config(state=NORMAL)
    firstname2.delete(0,END)
    lastname2.config(state=NORMAL)
    lastname2.delete(0,END)
    birthday2.config(state=NORMAL)
    birthday2.delete(0,END)
    address2.config(state=NORMAL)
    address2.delete(0,END)
    phonenum2.config(state=NORMAL)
    phonenum2.delete(0,END)
    email2.config(state=NORMAL)
    email2.delete(0,END)
    newuser2.config(state=NORMAL)
    newuser2.delete(0,END)
    userframe.destroy()
    homepage()

################################################################### ข้อมูล สมาชิก & พนักงาน ###################################################################

def emplosearch():
    global fname_e,lname_e,bd_e,ads_e,phone_e,email_e,user_e,result_s,sql_s,emeditframe
    sql_s = "select * from employee where username=?"
    cursor.execute(sql_s,[searchspy.get()])
    result_s = cursor.fetchone()
    if searchspy.get() == "":
        messagebox.showwarning("Admin","กรุณากรอกชื่อผู้ใช้งาน")
    elif result_s:
        searchemen.delete(0,END)
        Label(emeditframe,bg="#F6F6F6").grid(row=1,column=0,rowspan=7,columnspan=4,sticky="news")
        Label(emeditframe,text="ชื่อ: ",bg="#F6F6F6").grid(row=1,column=0,sticky="e",padx=20)
        Label(emeditframe,text="นามสกุล: ",bg="#F6F6F6").grid(row=1,column=2,sticky="e",padx=20)
        Label(emeditframe,text="วัน/เดือน/ปีเกิด: ",bg="#F6F6F6").grid(row=2,column=0,sticky="e",padx=20)
        Label(emeditframe,text="ที่อยู่: ",bg="#F6F6F6").grid(row=3,column=0,sticky="e",padx=20)
        Label(emeditframe,text="เบอร์โทร: ",bg="#F6F6F6").grid(row=4,column=0,sticky="e",padx=20)
        Label(emeditframe,text="อีเมล: ",bg="#F6F6F6").grid(row=4,column=2,sticky="e",padx=20)
        Label(emeditframe,text="ชื่อผู้ใช้งาน: ",bg="#F6F6F6").grid(row=5,column=0,sticky="e",padx=20)

        Button(emeditframe,text="เปลี่ยนรหัสผ่าน",bg="lightgrey",command=changepwd,width=20).grid(row=6,column=0,columnspan=4,pady=20,sticky='ns')
        Button(emeditframe,text="ออก",bg="grey",command=searchemback,width=10).grid(row=7,column=3,sticky="e",padx=(0,230))
        Button(emeditframe,text="แก้ไขข้อมูล",bg="grey",command=editem,width=10).grid(row=7,column=3,sticky="e",padx=(0,50))
    
        fname_e = Entry(emeditframe,textvariable=fname_espy,state=DISABLED,width=20)
        fname_e.grid(row=1,column=1,sticky="w")
        lname_e = Entry(emeditframe,textvariable=lname_espy,state=DISABLED,width=20)
        lname_e.grid(row=1,column=3,sticky="w",padx=(0,20))
        bd_e = Entry(emeditframe,textvariable=bd_espy,state=DISABLED,width=20)
        bd_e.grid(row=2,column=1,sticky="w")
        ads_e = Entry(emeditframe,textvariable=ads_espy,state=DISABLED,width=50)
        ads_e.grid(row=3,column=1,columnspan=3,sticky="w")
        phone_e = Entry(emeditframe,textvariable=phone_espy,state=DISABLED)
        phone_e.grid(row=4,column=1,sticky="w")
        email_e = Entry(emeditframe,textvariable=email_espy,state=DISABLED)
        email_e.grid(row=4,column=3,sticky="w",padx=(0,20))
        user_e = Entry(emeditframe,width=20,textvariable=user_espy,state=DISABLED)
        user_e.grid(row=5,column=1,sticky="w")

        phone = 0,result_s[4]
        fname_espy.set(result_s[0])
        lname_espy.set(result_s[1])
        bd_espy.set(result_s[2])
        ads_espy.set(result_s[3])
        phone_espy.set(phone)
        email_espy.set(result_s[5])
        user_espy.set(result_s[6])
    else:
        messagebox.showwarning("Admin","ไม่พบชื่อผู้ใช้งานนี้ในระบบ กรุณาลองอีกครั้ง")

def emploedit():
    global emeditframe,searchemen
    sql = "select * from manager where username=?"
    cursor.execute(sql,[muserinfo.get()])
    result = cursor.fetchall()
    if result: 
        bgframe = Frame(root,bg='#F6F6F6')
        bgframe.place(x=0,y=0,width=w,height=h)
        homeframe.destroy()
        emeditframe = Frame(root,bg='#F6F6F6')
        emeditframe.rowconfigure((0,1,2,3,4,5,6),weight=2)
        emeditframe.columnconfigure((0,1,2,3),weight=1)

        Label(emeditframe,text="ข้อมูลพนักงาน",font="Times 24 bold",bg="#F6F6F6").grid(row=0,column=0,columnspan=4,padx=20,pady=40)
        Button(emeditframe,image=home,bg="#F6F6F6",command=searchemclear,border=0).grid(row=0,column=0,columnspan=4,sticky='e',padx=20,pady=40)
        searchemen = Entry(emeditframe,bg="lightgrey",textvariable=searchspy)
        searchemen.grid(row=1,column=0,columnspan=4,sticky="e",padx=60)
        Button(emeditframe,image=search,bg="#F6F6F6",border=0,command=emplosearch).grid(row=1,column=0,columnspan=4,sticky="e",padx=20)
        Label(emeditframe,text="กรุณากรอกชื่อผู้ใช้งานของพนักงาน",bg="#F6F6F6").grid(row=1,column=0,rowspan=8,columnspan=4,sticky="news",pady=(300,0))
        emeditframe.grid(row=0,column=0,columnspan=4,sticky='news')
    else:
        messagebox.showwarning("Admin","หน้านี้สามารถเข้าได้เฉพาะผู้จัดการเท่านั้น")

def searchemback():
    emeditframe.destroy()
    emploedit()

def editem():
    fname_e.config(state=NORMAL)
    lname_e.config(state=NORMAL)
    ads_e.config(state=NORMAL)
    phone_e.config(state=NORMAL)
    email_e.config(state=NORMAL)
    fname_e.delete(0,END)
    lname_e.delete(0,END)
    ads_e.delete(0,END)
    phone_e.delete(0,END)
    email_e.delete(0,END)
    Button(emeditframe,text="ออก",bg="grey",command=editemback,width=10).grid(row=7,column=2,sticky="e",padx=10)
    Button(emeditframe,text="ลบบัญชี",bg="grey",command=deleteeminfo,width=10).grid(row=7,column=3,sticky="e",padx=(0,230))
    Button(emeditframe,text="บันทึกข้อมูล",bg="grey",command=saveeminfo,width=10).grid(row=7,column=3,sticky="e",padx=(0,50))

def editemback():
    emeditframe.destroy()
    emploedit()

def changepwd():
    global password,newpassword,confirm,changeframe
    bgframe = Frame(root,bg='#F6F6F6')
    bgframe.place(x=0,y=0,width=w,height=h)
    changeframe = Frame(root,bg='#F6F6F6')
    changeframe.rowconfigure((0,1,2,3),weight=1)
    changeframe.columnconfigure((0,1,2,3),weight=1)
    root.config(bg='#F6F6F6')

    Label(changeframe,text="เปลี่ยนรหัสผ่าน",font='Times 24 bold',bg='#F6F6F6').grid(row=0,column=0,columnspan=4)
    Button(changeframe,image=back,border=0,bg='#F6F6F6',command=cancelpwd).grid(row=0,column=0,columnspan=4,sticky='e',padx=30)
    Label(changeframe,text="รหัสผ่านปัจจุบัน: ",bg='#F6F6F6').grid(row=1,column=0,sticky='e',columnspan=2)
    Label(changeframe,text="รหัสผ่านใหม่: ",bg='#F6F6F6').grid(row=2,column=0,sticky='e',columnspan=2)
    Label(changeframe,text="ยืนยันรหัสผ่านใหม่: ",bg='#F6F6F6').grid(row=3,column=0,sticky='e',columnspan=2)
    password = Entry(changeframe,bg='lightgrey',width=20,textvariable=pwd,show='*')
    password.grid(row=1,column=2,sticky='w',columnspan=2,padx=10)
    newpassword = Entry(changeframe,bg='lightgrey',width=20,textvariable=newpwd,show='*')
    newpassword.grid(row=2,column=2,sticky='w',columnspan=2,padx=10)
    confirm = Entry(changeframe,bg='lightgrey',width=20,textvariable=cfpwd,show='*')
    confirm.grid(row=3,column=2,sticky='w',columnspan=2,padx=10)
    Button(changeframe,text="ยืนยัน",bg='grey',width=10,command=updatepwd).grid(row=4,column=0,columnspan=4)
    changeframe.grid(row=0,column=0,columnspan=4,sticky='news')

def updatepwd():
    sql = "select * from employee where pwd=?"
    cursor.execute(sql,[pwd.get()])
    result = cursor.fetchall()
    newpd_t = newpwd.get()
    if pwd.get() == "" :
        messagebox.showwarning("Admin","กรุณากรอกรหัสผ่านปัจจุบัน")
        password.focus_force()
    elif not result:
        messagebox.showwarning("Admin","รหัสผ่านปัจจุบันไม่ถูกต้อง กรุณาลองอีกครั้ง")
        password.focus_force()
    elif newpwd.get() == "" :
        messagebox.showwarning("Admin","กรุณากรอกรหัสผ่านใหม่")
        newpassword.focus_force()
    elif len(newpd_t) < 8 or len(newpd_t) > 16: 
        messagebox.showwarning("Admin","กรุณากรอกรหัสผ่านระหว่าง 8-16 ตัว")
        newpassword.delete(0,END)
        newpassword.focus_force()
    elif newpd_t.isalnum() != True:
        messagebox.showwarning("Admin","กรุณากรอกรหัสผ่านเป็นตัวอักษรหรือตัวเลขเท่านั้น")
        newpassword.delete(0,END)
        newpassword.focus_force()
    elif cfpwd.get() == "":
        messagebox.showwarning("Admin","กรุณากรอกยืนยันรหัสผ่านใหม่")
        confirm.focus_force()
    elif newpwd.get() != cfpwd.get():
        messagebox.showwarning("Admin","รหัสผ่านไม่ตรงกัน")
        confirm.delete(0,END)
        confirm.focus_force()
    else:
        confirmms = messagebox.askquestion("Confirm Register","คุณแน่ใจหรือว่าต้องการเปลี่ยนแปลงรหัสผ่าน")
        if confirmms == "yes":
            sql = "update employee set pwd=? where username=?"
            cursor.execute(sql,[newpwd.get(),searchspy.get()])
            conn.commit()
            messagebox.showinfo("Admin","บันทึกข้อมูลเรียบร้อย")
            cancelpwd()  

def cancelpwd():
    password.delete(0,END)
    newpassword.delete(0,END)
    confirm.delete(0,END)
    changeframe.destroy()
    emeditframe.destroy()
    emploedit()

def deleteeminfo():
    delemplo = messagebox.askquestion("Admin","ต้องการลบบัญชีหรือไม่")
    if delemplo == "yes":
        sql = "delete from employee where username=?"
        cursor.execute(sql,[result_s[6]])
        conn.commit()
        messagebox.showinfo("Admin","ลบบัญชีพนักงานเรียบร้อย")
        emeditframe.destroy()
        emploedit()

def saveeminfo():
    phone_t = phone_espy.get()
    email_t = email_espy.get()
    if fname_espy.get() == "" :
        messagebox.showwarning("Admin","กรุณากรอกชื่อ")
    elif lname_espy.get() == "" :
        messagebox.showwarning("Admin","กรุณากรอกนามสกุล")
    elif ads_espy.get() == "" :
        messagebox.showwarning("Admin","กรุณากรอกที่อยู่")
    elif phone_espy.get() == "" :
        messagebox.showwarning("Admin","กรุณากรอกเบอร์โทร")
    elif phone_t.isdigit() != True:
        messagebox.showwarning("Admin","กรุณากรอกตัวเลขเท่านั้น")
    elif len(phone_t) != 10 :
        messagebox.showwarning("Admin","กรุณากรอกให้ครบ 10 หลัก")
    elif email_espy.get() == "" :
        messagebox.showwarning("Admin","กรุณากรอกอีเมล")
    elif email_t[-10:] != "@gmail.com" :
        messagebox.showwarning("Admin","กรุณากรอกข้อมูลในรูปแบบ example@gmail.com")
    else :
        saveemplo = messagebox.askquestion("Admin","คุณแน่ใจหรือว่าต้องการบันทึกข้อมูล")
        if saveemplo == "yes":
            sql = "update employee set fname=?,lname=?,address=?,phone=?,email=? where username=?"
            cursor.execute(sql,[fname_espy.get(),lname_espy.get(),ads_espy.get(),phone_espy.get(),email_espy.get(),result_s[6]])
            conn.commit()
            messagebox.showinfo("Admin","บันทึกข้อมูลเรียบร้อย")
            emeditframe.destroy()
            emploedit()

def searchemclear():
    searchemen.delete(0,END)
    emeditframe.destroy()
    homepage()

def usersearch():
    global result_us
    global fname_u,lname_u,bd_u,ads_u,phone_u,email_u,user_u
    sql_us = "select * from user where username=?"
    cursor.execute(sql_us,[searchuspy.get()])
    result_us = cursor.fetchone()
    if searchuspy.get() == "":
        messagebox.showwarning("Admin","กรุณากรอกชื่อผู้ใช้งาน")
    elif result_us:
        searchuseen.delete(0,END)
        Label(useditframe,bg="#F6F6F6").grid(row=1,column=0,rowspan=9,columnspan=4,sticky="news")
        Label(useditframe,text="ชื่อ: ",bg="#F6F6F6").grid(row=1,column=0,sticky="e",padx=20)
        Label(useditframe,text="นามสกุล: ",bg="#F6F6F6").grid(row=1,column=2,sticky="e",padx=20)
        Label(useditframe,text="วัน/เดือน/ปีเกิด: ",bg="#F6F6F6").grid(row=2,column=0,sticky="e",padx=20)
        Label(useditframe,text="ที่อยู่: ",bg="#F6F6F6").grid(row=3,column=0,sticky="e",padx=20)
        Label(useditframe,text="เบอร์โทร: ",bg="#F6F6F6").grid(row=4,column=0,sticky="e",padx=20)
        Label(useditframe,text="อีเมล: ",bg="#F6F6F6").grid(row=4,column=2,sticky="e",padx=20)
        Label(useditframe,text="ชื่อผู้ใช้งาน: ",bg="#F6F6F6").grid(row=5,column=0,sticky="e",padx=20)

        Button(useditframe,text="คะแนนสะสม",bg="lightgrey",command=point,width=20).grid(row=7,column=0,columnspan=4,pady=20,sticky='ns')
        Button(useditframe,text="ออก",bg="grey",command=searchuseback,width=10).grid(row=8,column=3,sticky="e",padx=(0,230))
        Button(useditframe,text="แก้ไขข้อมูล",bg="grey",command=edituse,width=10).grid(row=8,column=3,sticky="e",padx=(0,50))

        fname_u = Entry(useditframe,textvariable=fname_uspy,state=DISABLED,width=20)
        fname_u.grid(row=1,column=1,sticky="w")
        lname_u = Entry(useditframe,textvariable=lname_uspy,state=DISABLED,width=20)
        lname_u.grid(row=1,column=3,sticky="w",padx=(0,20))
        bd_u = Entry(useditframe,textvariable=bd_uspy,state=DISABLED,width=20)
        bd_u.grid(row=2,column=1,sticky="w")
        ads_u = Entry(useditframe,textvariable=ads_uspy,state=DISABLED,width=50)
        ads_u.grid(row=3,column=1,columnspan=3,sticky="w")
        phone_u = Entry(useditframe,textvariable=phone_uspy,state=DISABLED)
        phone_u.grid(row=4,column=1,sticky="w")
        email_u = Entry(useditframe,textvariable=email_uspy,state=DISABLED)
        email_u.grid(row=4,column=3,sticky="w",padx=(0,20))
        user_u = Entry(useditframe,width=20,textvariable=user_uspy,state=DISABLED)
        user_u.grid(row=5,column=1,sticky="w")

        phone = 0,result_us[4]
        fname_uspy.set(result_us[0])
        lname_uspy.set(result_us[1])
        bd_uspy.set(result_us[2])
        ads_uspy.set(result_us[3])
        phone_uspy.set(phone)
        email_uspy.set(result_us[5])
        user_uspy.set(result_us[6])
    else:
        messagebox.showwarning("Admin","ไม่พบชื่อผู้ใช้งานนี้ในระบบ กรุณาลองอีกครั้ง")

def useredit():
    global useditframe,searchuseen
    bgframe = Frame(root,bg='#F6F6F6')
    bgframe.place(x=0,y=0,width=w,height=h)
    homeframe.destroy()
    useditframe = Frame(root,bg='#F6F6F6')
    useditframe.rowconfigure((0,1,2,3,4,5,6,7,8),weight=2)
    useditframe.columnconfigure((0,1,2,3),weight=1)

    Label(useditframe,text="ข้อมูลสมาชิก",font="Times 24 bold",bg="#F6F6F6").grid(row=0,column=0,columnspan=4,padx=20,pady=40)
    Button(useditframe,image=home,bg="#F6F6F6",command=searchclear,border=0).grid(row=0,column=0,columnspan=4,sticky='e',padx=20,pady=40)
    searchuseen = Entry(useditframe,bg="lightgrey",textvariable=searchuspy)
    searchuseen.grid(row=1,column=0,columnspan=4,sticky="e",padx=60)
    Button(useditframe,image=search,bg="#F6F6F6",border=0,command=usersearch).grid(row=1,column=0,columnspan=4,sticky="e",padx=20)
    Label(useditframe,text="กรุณากรอกชื่อผู้ใช้งานของสมาชิก",bg="#F6F6F6").grid(row=1,column=0,rowspan=9,columnspan=4,sticky="news",pady=(300,0))
    useditframe.grid(row=0,column=0,columnspan=4,sticky='news')

def searchuseback():
    useditframe.destroy()
    useredit()

def edituse():
    fname_u.config(state=NORMAL)
    lname_u.config(state=NORMAL)
    ads_u.config(state=NORMAL)
    phone_u.config(state=NORMAL)
    email_u.config(state=NORMAL)
    fname_u.delete(0,END)
    lname_u.delete(0,END)
    ads_u.delete(0,END)
    phone_u.delete(0,END)
    email_u.delete(0,END)
    Button(useditframe,text="ออก",bg="grey",command=edituseback,width=10).grid(row=8,column=2,sticky="e",padx=10)
    Button(useditframe,text="ลบบัญชี",bg="grey",command=deleteuseinfo,width=10).grid(row=8,column=3,sticky="e",padx=(0,230))
    Button(useditframe,text="บันทึกข้อมูล",bg="grey",command=saveuseinfo,width=10).grid(row=8,column=3,sticky="e",padx=(0,50))

def edituseback():
    useditframe.destroy()
    useredit()

def point():
    global pointframe
    bgframe = Frame(root,bg='#F6F6F6')
    bgframe.place(x=0,y=0,width=w,height=h)
    pointframe = Frame(root,bg='#F6F6F6')
    pointframe.rowconfigure((0,1,2,4),weight=1)
    pointframe.rowconfigure((5),weight=3)
    pointframe.columnconfigure((0,1),weight=1)

    Label(pointframe,text="คะแนนสะสม",bg="#F6F6F6",font="Times 24 bold").grid(row=0,column=0,columnspan=4)
    Button(pointframe,image=back,bg="#F6F6F6",command=canpoint,border=0).grid(row=0,column=3,sticky='e',padx=60)
    Label(pointframe,text="ชื่อ-นามสกุล: ",bg="#F6F6F6").grid(row=1,column=1,sticky='w')
    Entry(pointframe,state=DISABLED,textvariable=unamespy).grid(row=1,column=1,columnspan=2)
    Label(pointframe,text="คะแนนสะสม: ",bg="#F6F6F6").grid(row=2,column=1,sticky='w')
    Entry(pointframe,state=DISABLED,textvariable=upointspy).grid(row=2,column=1,columnspan=2)
    Label(pointframe,text="คะแนน",bg="#F6F6F6").grid(row=2,column=2,sticky='e',padx=10)
    Label(pointframe,text=("_"*50),bg="#F6F6F6").grid(row=3,column=0,columnspan=4)
    Label(pointframe,text="แลกคะแนน",bg="#F6F6F6").grid(row=4,column=0,padx=60)
    Button(pointframe,text="ดูทั้งหมด",bg="#F6F6F6",border=0,command=allpoint).grid(row=4,column=3,padx=60)
    
    Button(pointframe,image=voucher1,bg="#F6F6F6",border=0,command=v1).grid(row=5,column=1,sticky='nw')
    Button(pointframe,image=voucher2,bg="#F6F6F6",border=0,command=v2).grid(row=5,column=2,sticky='ne')

    uname = result_us[0] , result_us[1]
    unamespy.set(uname)
    upointspy.set(result_us[-1])
    pointframe.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='news')

def allpoint():
    global allpointframe
    bgframe = Frame(root,bg='#F6F6F6')
    bgframe.place(x=0,y=0,width=w,height=h)
    allpointframe = Frame(root,bg='#F6F6F6')
    allpointframe.rowconfigure((0,1,2),weight=1)
    allpointframe.columnconfigure((0,1,2,3),weight=1)

    Label(allpointframe,text="แลกคะแนน",bg="#F6F6F6",font="Times 24 bold").grid(row=0,column=0,columnspan=4)
    Button(allpointframe,image=back,bg="#F6F6F6",command=canpoint2,border=0).grid(row=0,column=3,padx=30)
    Label(allpointframe).grid(row=1,column=0,padx=50)
    Button(allpointframe,image=voucher1,bg="#F6F6F6",border=0,command=v1).grid(row=1,column=1,pady=20)
    Button(allpointframe,image=voucher2,bg="#F6F6F6",border=0,command=v2).grid(row=1,column=2,pady=20)
    Button(allpointframe,image=voucher3,bg="#F6F6F6",border=0,command=v3).grid(row=2,column=1,pady=20)
    Button(allpointframe,image=voucher4,bg="#F6F6F6",border=0,command=v4).grid(row=2,column=2,pady=20)
    Button(allpointframe,image=voucher5,bg="#F6F6F6",border=0,command=v5).grid(row=3,column=1,pady=20)
    allpointframe.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='news')

#################################################### ชั่วโมงตอนแลกคะแนน (จะใส่เป็นไม่มีสมาชิก) ##################################

def v1(): 
    global userpoint
    userpoint = upointspy.get()
    p = messagebox.askquestion("Admin","ต้องการแลกคะแนนใช่หรือไม่")
    if p == "yes" :
        if int(userpoint) < 1000 :
            messagebox.showwarning("Admin","ไม่สามารถแลกเปลี่ยนคะแนนได้ เนื่องจากคะแนนไม่ถึงที่กำหนด")
        else:
            total = int(userpoint)-1000
            sql = "update user set point=? where username=?"
            cursor.execute(sql,[total,result_us[6]])
            conn.commit()
            upointspy.set(total)
            messagebox.showinfo("Admin","แลกเปลี่ยนคะแนนสำเร็จ")
def v2():
    p = messagebox.askquestion("Admin","ต้องการแลกคะแนนใช่หรือไม่")
    if p == "yes" :
        if int(userpoint) < 3000 :
            messagebox.showwarning("Admin","ไม่สามารถแลกเปลี่ยนคะแนนได้ เนื่องจากคะแนนไม่ถึงที่กำหนด")
        else:
            total = int(userpoint)-3000
            sql = "update user set point=? where username=?"
            cursor.execute(sql,[total,result_us[6]])
            conn.commit()
            upointspy.set(total)
            messagebox.showinfo("Admin","แลกเปลี่ยนคะแนนสำเร็จ")
def v3():
    p = messagebox.askquestion("Admin","ต้องการแลกคะแนนใช่หรือไม่")
    if p == "yes" :
        if int(userpoint) < 5000 :
            messagebox.showwarning("Admin","ไม่สามารถแลกเปลี่ยนคะแนนได้ เนื่องจากคะแนนไม่ถึงที่กำหนด")
        else:
            total = int(userpoint)-5000
            sql = "update user set point=? where username=?"
            cursor.execute(sql,[total,result_us[6]])
            conn.commit()
            upointspy.set(total)
            messagebox.showinfo("Admin","แลกเปลี่ยนคะแนนสำเร็จ")
def v4():
    p = messagebox.askquestion("Admin","ต้องการแลกคะแนนใช่หรือไม่")
    if p == "yes" :
        if int(userpoint) < 7000 :
            messagebox.showwarning("Admin","ไม่สามารถแลกเปลี่ยนคะแนนได้ เนื่องจากคะแนนไม่ถึงที่กำหนด")
        else:
            total = int(userpoint)-7000
            sql = "update user set point=? where username=?"
            cursor.execute(sql,[total,result_us[6]])
            conn.commit()
            upointspy.set(total)
            messagebox.showinfo("Admin","แลกเปลี่ยนคะแนนสำเร็จ")
def v5():
    p = messagebox.askquestion("Admin","ต้องการแลกคะแนนใช่หรือไม่")
    if p == "yes" :
        if int(userpoint) < 9000 :
            messagebox.showwarning("Admin","ไม่สามารถแลกเปลี่ยนคะแนนได้ เนื่องจากคะแนนไม่ถึงที่กำหนด")
        else:
            total = int(userpoint)-9000
            sql = "update user set point=? where username=?"
            cursor.execute(sql,[total,result_us[6]])
            conn.commit()
            upointspy.set(total)
            messagebox.showinfo("Admin","แลกเปลี่ยนคะแนนสำเร็จ")

def canpoint():
    useditframe.destroy()
    pointframe.destroy()
    unamespy.set("")
    upointspy.set(0)
    useredit()

def canpoint2():
    pointframe.destroy()
    allpointframe.destroy()
    point()

def deleteuseinfo():
    deluser = messagebox.askquestion("Admin","ต้องการลบบัญชีหรือไม่")
    if deluser == "yes":
        sql = "delete from user where username=?"
        cursor.execute(sql,[result_us[6]])
        conn.commit()
        messagebox.showinfo("Admin","ลบบัญชีผู้ใช้งานเรียบร้อย")
        useditframe.destroy()
        useredit()

def saveuseinfo():
    phone_t = phone_uspy.get()
    email_t = email_uspy.get()
    if fname_uspy.get() == "" :
        messagebox.showwarning("Admin","กรุณากรอกชื่อ")
    elif lname_uspy.get() == "" :
        messagebox.showwarning("Admin","กรุณากรอกนามสกุล")
    elif ads_uspy.get() == "" :
        messagebox.showwarning("Admin","กรุณากรอกที่อยู่")
    elif phone_uspy.get() == "" :
        messagebox.showwarning("Admin","กรุณากรอกเบอร์โทร")
    elif phone_t.isdigit() != True:
        messagebox.showwarning("Admin","กรุณากรอกตัวเลขเท่านั้น")
    elif len(phone_t) != 10 :
        messagebox.showwarning("Admin","กรุณากรอกให้ครบ 10 หลัก")
    elif email_uspy.get() == "" :
        messagebox.showwarning("Admin","กรุณากรอกอีเมล")
    elif email_t[-10:] != "@gmail.com" :
        messagebox.showwarning("Admin","กรุณากรอกข้อมูลในรูปแบบ example@gmail.com")
    else :
        saveuser = messagebox.askquestion("Admin","คุณแน่ใจหรือว่าต้องการบันทึกข้อมูล")
        if saveuser == "yes":
            sql = "update user set fname=?,lname=?,address=?,phone=?,email=? where username=?"
            cursor.execute(sql,[fname_uspy.get(),lname_uspy.get(),ads_uspy.get(),phone_uspy.get(),email_uspy.get(),result_us[6]])
            conn.commit()
            messagebox.showinfo("Admin","บันทึกข้อมูลเรียบร้อย")
            useditframe.destroy()
            useredit()

def searchclear():
    searchuseen.delete(0,END)
    useditframe.destroy()
    homepage()

######################################################## ร้านค้า ########################################################

def shop():
    global spinpd1,spinpd2,spinpd3,spinpd4,spinpd5,spinpd6,result_s,shopframe
    bgframe = Frame(root,bg='#F6F6F6')
    bgframe.place(x=0,y=0,width=w,height=h)
    homeframe.destroy()
    shopframe = Frame(root,bg='#F6F6F6')
    shopframe.rowconfigure((0,1,2,3,4,5,6),weight=2)
    shopframe.columnconfigure((0,1,2),weight=1)

    sql = "select stock from product"
    cursor.execute(sql)
    result_s = cursor.fetchall()

    Label(shopframe,bg="#F6F6F6",text="Kira Internet Cafe Shop",font="Times 24 bold").grid(row=0,column=0,columnspan=3,pady=20)
    Label(shopframe,bg="#F6F6F6",image=pd1).grid(row=1,column=0)
    Label(shopframe,bg="#F6F6F6",text="ชื่อสินค้า: ตะวัน\nราคา 7 บาท").grid(row=2,column=0)
    spinpd1 = Spinbox(shopframe,from_=0,to=result_s[0],justify=CENTER,width=10,textvariable=sp1)
    spinpd1.grid(row=3,column=0)

    Label(shopframe,bg="#F6F6F6",image=pd2).grid(row=1,column=1)
    Label(shopframe,bg="#F6F6F6",text="ชื่อสินค้า: เลย์\nราคา 20 บาท").grid(row=2,column=1)
    spinpd2 = Spinbox(shopframe,from_=0,to=result_s[1],justify=CENTER,width=10,textvariable=sp2)
    spinpd2.grid(row=3,column=1)

    Label(shopframe,bg="#F6F6F6",image=pd3).grid(row=1,column=2)
    Label(shopframe,bg="#F6F6F6",text="ชื่อสินค้า: โค้กกระป๋อง\nราคา 10 บาท").grid(row=2,column=2)
    spinpd3 = Spinbox(shopframe,from_=0,to=result_s[2],justify=CENTER,width=10,textvariable=sp3)
    spinpd3.grid(row=3,column=2)

    Label(shopframe,bg="#F6F6F6",image=pd4).grid(row=4,column=0)
    Label(shopframe,bg="#F6F6F6",text="ชื่อสินค้า: โค้กขวดเล็ก\nราคา 12 บาท").grid(row=5,column=0)
    spinpd4 = Spinbox(shopframe,from_=0,to=result_s[3],justify=CENTER,width=10,textvariable=sp4)
    spinpd4.grid(row=6,column=0)

    Label(shopframe,bg="#F6F6F6",image=pd5).grid(row=4,column=1)
    Label(shopframe,bg="#F6F6F6",text="ชื่อสินค้า: โค้ดขวดใหญ่\nราคา 24 บาท").grid(row=5,column=1)
    spinpd5 = Spinbox(shopframe,from_=0,to=result_s[4],justify=CENTER,width=10,textvariable=sp5)
    spinpd5.grid(row=6,column=1)

    Label(shopframe,bg="#F6F6F6",image=pd6).grid(row=4,column=2)
    Label(shopframe,bg="#F6F6F6",text="ชื่อสินค้า: มาม่าถ้วย\nราคา 20 บาท").grid(row=5,column=2)
    spinpd6 = Spinbox(shopframe,from_=0,to=result_s[5],justify=CENTER,width=10,textvariable=sp6)
    spinpd6.grid(row=6,column=2)

    Button(shopframe,bg="grey",text="ออก",command=clearp1,width=8).grid(row=7,column=2,sticky='w',padx=(20,0))
    Button(shopframe,bg="grey",text="หน้าต่อไป",command=page2,width=8).grid(row=7,column=2,pady=20)

    shopframe.grid(row=0,column=0,columnspan=4,sticky='news')
    return spinpd1,spinpd2,spinpd3,spinpd4,spinpd5,spinpd6

def clearp1():
    sp1.set(0)
    sp2.set(0)
    sp3.set(0)
    sp4.set(0)
    sp5.set(0)
    sp6.set(0)
    sp7.set(0)
    sp8.set(0)
    sp9.set(0)
    sp10.set(0)
    shopframe.destroy()
    homepage()

def page2():
    global shopframe2
    bgframe = Frame(root,bg='#F6F6F6')
    bgframe.place(x=0,y=0,width=w,height=h)
    shopframe.destroy()
    homeframe.destroy()
    shopframe2 = Frame(root,bg='#F6F6F6')
    shopframe2.rowconfigure((0,1,2,3,4,5,6),weight=2)
    shopframe2.columnconfigure((0,1,2),weight=1)

    Label(shopframe2,bg="#F6F6F6",text="Kira Internet Cafe Shop",font="Times 24 bold").grid(row=0,column=0,columnspan=3,pady=20)
    Button(shopframe2,image=stockpic,bg="#F6F6F6",command=stock,border=0).grid(row=0,column=2,sticky='e',padx=30,pady=(20,0))
    Label(shopframe2,bg="#F6F6F6",image=pd7).grid(row=1,column=0)
    Label(shopframe2,bg="#F6F6F6",text="ชื่อสินค้า: นมเปรี้ยว\nราคา 6 บาท").grid(row=2,column=0)
    spinpd7 = Spinbox(shopframe2,from_=0,to=result_s[6],justify=CENTER,width=10,textvariable=sp7)
    spinpd7.grid(row=3,column=0)

    Label(shopframe2,bg="#F6F6F6",image=pd8).grid(row=1,column=1)
    Label(shopframe2,bg="#F6F6F6",text="ชื่อสินค้า: นมจืด\nราคา 14 บาท").grid(row=2,column=1)
    spinpd8 = Spinbox(shopframe2,from_=0,to=result_s[7],justify=CENTER,width=10,textvariable=sp8)
    spinpd8.grid(row=3,column=1)

    Label(shopframe2,bg="#F6F6F6",image=pd9).grid(row=1,column=2)
    Label(shopframe2,bg="#F6F6F6",text="ชื่อสินค้า: น้ำเปล่าขวดเล็ก\nราคา 7 บาท").grid(row=2,column=2)
    spinpd9 = Spinbox(shopframe2,from_=0,to=result_s[8],justify=CENTER,width=10,textvariable=sp9)
    spinpd9.grid(row=3,column=2)

    Label(shopframe2,bg="#F6F6F6",image=pd10).grid(row=4,column=0)
    Label(shopframe2,bg="#F6F6F6",text="ชื่อสินค้า: น้ำเปล่าขวดใหญ่\nราคา 13 บาท").grid(row=5,column=0)
    spinpd10 = Spinbox(shopframe2,from_=0,to=result_s[9],justify=CENTER,width=10,textvariable=sp10)
    spinpd10.grid(row=6,column=0)

    Button(shopframe2,bg="grey",text="ออก",command=clearp2,width=8).grid(row=7,column=2,sticky='w',padx=(45,0),pady=20)
    Button(shopframe2,bg="grey",text="ย้อนกลับ",command=backshop,width=8).grid(row=7,column=2,pady=20,padx=(30,0))
    Button(shopframe2,bg="grey",text="ตะกร้า",command=checkout,width=8).grid(row=7,column=2,sticky='e',padx=20,pady=20) #รูปตะกร้า

    shopframe2.grid(row=0,column=0,columnspan=4,sticky='news')
    return spinpd7,spinpd8,spinpd9,spinpd10

def backshop():
    shopframe2.destroy()
    shop()

def clearp2():
    sp1.set(0)
    sp2.set(0)
    sp3.set(0)
    sp4.set(0)
    sp5.set(0)
    sp6.set(0)
    sp7.set(0)
    sp8.set(0)
    sp9.set(0)
    sp10.set(0)
    shopframe.destroy()
    shopframe2.destroy()
    homepage()

def checkout():
    global choframe,total_p
    bgframe = Frame(root,bg='#F6F6F6')
    bgframe.place(x=0,y=0,width=w,height=h)
    shopframe.destroy()
    shopframe2.destroy()
    homeframe.destroy()
    choframe = Frame(root,bg='#F6F6F6')
    choframe.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12),weight=1)
    choframe.columnconfigure((0,1,2,3),weight=1)

    Button(choframe,image=back,bg="#F6F6F6",command=backshopco,border=0).grid(row=0,column=3,sticky='e',padx=20)
    Label(choframe,text="รายการทั้งหมด",font="Times 24 bold",bg="#F6F6F6").grid(row=0,column=0,columnspan=4)
    Label(choframe,text="ชื่อสินค้า",bg="#F6F6F6").grid(row=1,column=0)
    Label(choframe,text="ราคาสินค้า",bg="#F6F6F6").grid(row=1,column=1)
    Label(choframe,text="จำนวน",bg="#F6F6F6").grid(row=1,column=2)
    Label(choframe,text="รวม",bg="#F6F6F6").grid(row=1,column=3)
    total1,total2,total3,total4,total5,total6,total7,total8,total9,total10 = 0,0,0,0,0,0,0,0,0,0
    if sp1.get() != "0" and sp1.get() != "":
        total1 = int(sp1.get()) * 7
        Label(choframe,image=pd01,text="ตะวัน",bg="#F6F6F6",compound=LEFT).grid(row=2,column=0,sticky='w',padx=(150,0),pady=(10,0))
        Label(choframe,text=7,bg="#F6F6F6").grid(row=2,column=1)
        Label(choframe,text=sp1.get(),bg="#F6F6F6").grid(row=2,column=2)
        Label(choframe,text=total1,bg="#F6F6F6").grid(row=2,column=3)
    if sp2.get() != "0" and sp2.get() != "":
        total2 = int(sp2.get()) * 20
        Label(choframe,image=pd02,text="เลย์",bg="#F6F6F6",compound=LEFT).grid(row=3,column=0,sticky='w',padx=(150,0),pady=(10,0))
        Label(choframe,text=20,bg="#F6F6F6").grid(row=3,column=1)
        Label(choframe,text=sp2.get(),bg="#F6F6F6").grid(row=3,column=2)
        Label(choframe,text=total2,bg="#F6F6F6").grid(row=3,column=3)
    if sp3.get() != "0" and sp3.get() != "":
        total3 = int(sp3.get()) * 10
        Label(choframe,image=pd03,text="โค้กกระป๋อง",bg="#F6F6F6",compound=LEFT).grid(row=4,column=0,sticky='w',padx=(150,0),pady=(10,0))
        Label(choframe,text=10,bg="#F6F6F6").grid(row=4,column=1)
        Label(choframe,text=sp3.get(),bg="#F6F6F6").grid(row=4,column=2)
        Label(choframe,text=total3,bg="#F6F6F6").grid(row=4,column=3)
    if sp4.get() != "0" and sp4.get() != "":
        total4 = int(sp4.get()) * 12
        Label(choframe,image=pd04,text="โค้กขวดเล็ก",bg="#F6F6F6",compound=LEFT).grid(row=5,column=0,sticky='w',padx=(150,0),pady=(10,0))
        Label(choframe,text=12,bg="#F6F6F6").grid(row=5,column=1)
        Label(choframe,text=sp4.get(),bg="#F6F6F6").grid(row=5,column=2)
        Label(choframe,text=total4,bg="#F6F6F6").grid(row=5,column=3)
    if sp5.get() != "0" and sp5.get() != "":
        total5 = int(sp5.get()) * 24
        Label(choframe,image=pd05,text="โค้กขวดใหญ่",bg="#F6F6F6",compound=LEFT).grid(row=6,column=0,sticky='w',padx=(150,0),pady=(10,0))
        Label(choframe,text=24,bg="#F6F6F6").grid(row=6,column=1)
        Label(choframe,text=sp5.get(),bg="#F6F6F6").grid(row=6,column=2)
        Label(choframe,text=total5,bg="#F6F6F6").grid(row=6,column=3)
    if sp6.get() != "0" and sp6.get() != "":
        total6 = int(sp6.get()) * 20
        Label(choframe,image=pd06,text="มาม่าถ้วย",bg="#F6F6F6",compound=LEFT).grid(row=7,column=0,sticky='w',padx=(150,0),pady=(10,0))
        Label(choframe,text=20,bg="#F6F6F6").grid(row=7,column=1)
        Label(choframe,text=sp6.get(),bg="#F6F6F6").grid(row=7,column=2)
        Label(choframe,text=total6,bg="#F6F6F6").grid(row=7,column=3)
    if sp7.get() != "0" and sp7.get() != "":
        total7 = int(sp7.get()) * 6
        Label(choframe,image=pd07,text="นมเปรี้ยว",bg="#F6F6F6",compound=LEFT).grid(row=8,column=0,sticky='w',padx=(150,0),pady=(10,0))
        Label(choframe,text=6,bg="#F6F6F6").grid(row=8,column=1)
        Label(choframe,text=sp7.get(),bg="#F6F6F6").grid(row=8,column=2)
        Label(choframe,text=total7,bg="#F6F6F6").grid(row=8,column=3)
    if sp8.get() != "0" and sp8.get() != "":
        total8 = int(sp8.get()) * 14
        Label(choframe,image=pd08,text="นมจืด",bg="#F6F6F6",compound=LEFT).grid(row=9,column=0,sticky='w',padx=(150,0),pady=(10,0))
        Label(choframe,text=14,bg="#F6F6F6").grid(row=9,column=1)
        Label(choframe,text=sp8.get(),bg="#F6F6F6").grid(row=9,column=2)
        Label(choframe,text=total8,bg="#F6F6F6").grid(row=9,column=3)
    if sp9.get() != "0" and sp9.get() != "":
        total9 = int(sp9.get()) * 7
        Label(choframe,image=pd09,text="น้ำเปล่าขวดเล็ก",bg="#F6F6F6",compound=LEFT).grid(row=10,column=0,sticky='w',padx=(150,0),pady=(10,0))
        Label(choframe,text=7,bg="#F6F6F6").grid(row=10,column=1)
        Label(choframe,text=sp9.get(),bg="#F6F6F6").grid(row=10,column=2)
        Label(choframe,text=total9,bg="#F6F6F6").grid(row=10,column=3)
    if sp10.get() != "0" and sp10.get() != "":
        total10 = int(sp10.get()) * 13
        Label(choframe,image=pd010,text="น้ำเปล่าขวดใหญ่",bg="#F6F6F6",compound=LEFT).grid(row=11,column=0,sticky='w',padx=(150,0),pady=(10,0))
        Label(choframe,text=13,bg="#F6F6F6").grid(row=11,column=1)
        Label(choframe,text=sp10.get(),bg="#F6F6F6").grid(row=11,column=2)
        Label(choframe,text=total10,bg="#F6F6F6").grid(row=11,column=3)
    total_p = total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10
    Label(choframe,text=("รวมทั้งหมด",total_p,"บาท"),bg="#F6F6F6").grid(column=3,sticky='w',pady=15,padx=20)
    Button(choframe,text="ยืนยัน",bg="grey",width=8,command=pay).grid(column=3,sticky='w',pady=10,padx=20)
    choframe.grid(row=0,column=0,columnspan=4,sticky='news')

def pay():
    askp = messagebox.askquestion("Admin","ต้องการชำระเงินหรือไม่")
    if askp == "yes":
        sql1 = "select * from product"
        cursor.execute(sql1)
        result = cursor.fetchall()
        for data in result:
            namepdlst.append(data[0])
            pdlst.append(data[2])
        sql2 = "update product set stock=? where name=?"
        sql_r1 = "insert into report1 values(?,?,?,?,?,?)"
        cursor.execute(sql_r1,[retimed,retimem,retimey,"รายรับ","ขายสินค้า",total_p])
        conn.commit()
        if sp1.get() != "0" and sp1.get() != "" :
            total = int(pdlst[0]) - int(sp1.get())
            cursor.execute(sql2,[total,namepdlst[0]])
            conn.commit()
        if sp2.get() != "0" and sp2.get() != "" :
            total = int(pdlst[1]) - int(sp2.get())
            cursor.execute(sql2,[total,namepdlst[1]])
            conn.commit()
        if sp3.get() != "0" and sp3.get() != "" :
            total = int(pdlst[2]) - int(sp3.get())
            cursor.execute(sql2,[total,namepdlst[2]])
            conn.commit()
        if sp4.get() != "0" and sp4.get() != "" :
            total = int(pdlst[3]) - int(sp4.get())
            cursor.execute(sql2,[total,namepdlst[3]])
            conn.commit()
        if sp5.get() != "0" and sp5.get() != "" :
            total = int(pdlst[4]) - int(sp5.get())
            cursor.execute(sql2,[total,namepdlst[4]])
            conn.commit()
        if sp6.get() != "0" and sp6.get() != "" :
            total = int(pdlst[5]) - int(sp6.get())
            cursor.execute(sql2,[total,namepdlst[5]])
            conn.commit()
        if sp7.get() != "0" and sp7.get() != "" :
            total = int(pdlst[6]) - int(sp7.get())
            cursor.execute(sql2,[total,namepdlst[6]])
            conn.commit()
        if sp8.get() != "0" and sp8.get() != "" :
            total = int(pdlst[7]) - int(sp8.get())
            cursor.execute(sql2,[total,namepdlst[7]])
            conn.commit()
        if sp9.get() != "0" and sp9.get() != "" :
            total = int(pdlst[8]) - int(sp9.get())
            cursor.execute(sql2,[total,namepdlst[8]])
            conn.commit()
        if sp10.get() != "0" and sp10.get() != "" :
            total = int(pdlst[9]) - int(sp10.get())
            cursor.execute(sql2,[total,namepdlst[9]])
            conn.commit()
        sp1.set(0)
        sp2.set(0)
        sp3.set(0)
        sp4.set(0)
        sp5.set(0)
        sp6.set(0)
        sp7.set(0)
        sp8.set(0)
        sp9.set(0)
        sp10.set(0)
        messagebox.showinfo("Admin","ชำระเงินสำเร็จ")
        backshopco()

def backshopco():
    choframe.destroy()
    shopframe.destroy()
    shop()

def stock():
    global stockframe,stock1,stock2,stock3,stock4,stock5,stock6,stock7,stock8,stock9,stock10
    bgframe = Frame(root,bg='#F6F6F6')
    bgframe.place(x=0,y=0,width=w,height=h)
    shopframe.destroy()
    homeframe.destroy()
    stockframe = Frame(root,bg='#F6F6F6')
    stockframe.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12),weight=1)
    stockframe.columnconfigure((0,1,2,3,4),weight=1)
        
    sql = "select * from product"
    cursor.execute(sql)
    result = cursor.fetchall()
    Button(stockframe,image=back,bg="#F6F6F6",command=backshopst,border=0).grid(row=0,column=4,sticky='e',padx=20)
    Label(stockframe,text="คลังสินค้า",font="Times 24 bold",bg="#F6F6F6").grid(row=0,column=0,columnspan=5)
    Label(stockframe,text="ชื่อสินค้า",bg="#F6F6F6").grid(row=1,column=0,columnspan=2)
    Label(stockframe,text="ราคาสินค้า",bg="#F6F6F6").grid(row=1,column=2,sticky='w')
    Label(stockframe,text="จำนวนคงเหลือ",bg="#F6F6F6").grid(row=1,column=3,sticky='w')
    Label(stockframe,text="จำนวนที่ต้องการเพิ่ม",bg="#F6F6F6").grid(row=1,column=4,sticky='w')
    Label(stockframe,image=pd01,bg="#F6F6F6").grid(row=2,column=0)
    Label(stockframe,image=pd02,bg="#F6F6F6").grid(row=3,column=0)
    Label(stockframe,image=pd03,bg="#F6F6F6").grid(row=4,column=0)
    Label(stockframe,image=pd04,bg="#F6F6F6").grid(row=5,column=0)
    Label(stockframe,image=pd05,bg="#F6F6F6").grid(row=6,column=0)
    Label(stockframe,image=pd06,bg="#F6F6F6").grid(row=7,column=0)
    Label(stockframe,image=pd07,bg="#F6F6F6").grid(row=8,column=0)
    Label(stockframe,image=pd08,bg="#F6F6F6").grid(row=9,column=0)
    Label(stockframe,image=pd09,bg="#F6F6F6").grid(row=10,column=0)
    Label(stockframe,image=pd010,bg="#F6F6F6").grid(row=11,column=0)
    for i,data in zip(range(1,11),result):
        Label(stockframe,text=data[0],bg="#F6F6F6").grid(row=i+1,column=1,sticky='w')
        Label(stockframe,text=data[1],bg="#F6F6F6").grid(row=i+1,column=2,sticky='w')
        Label(stockframe,text=data[2],bg="#F6F6F6").grid(row=i+1,column=3,sticky='w')
        namestocklst.append(data[0])
        stocklst.append(data[2])
    stock1 = Spinbox(stockframe,from_=0,to=1000,justify=CENTER,width=10,textvariable=sps1)
    stock1.grid(row=2,column=4,sticky='w')
    stock2 = Spinbox(stockframe,from_=0,to=1000,justify=CENTER,width=10,textvariable=sps2)
    stock2.grid(row=3,column=4,sticky='w')
    stock3 = Spinbox(stockframe,from_=0,to=1000,justify=CENTER,width=10,textvariable=sps3)
    stock3.grid(row=4,column=4,sticky='w')
    stock4 = Spinbox(stockframe,from_=0,to=1000,justify=CENTER,width=10,textvariable=sps4)
    stock4.grid(row=5,column=4,sticky='w')
    stock5 = Spinbox(stockframe,from_=0,to=1000,justify=CENTER,width=10,textvariable=sps5)
    stock5.grid(row=6,column=4,sticky='w')
    stock6 = Spinbox(stockframe,from_=0,to=1000,justify=CENTER,width=10,textvariable=sps6)
    stock6.grid(row=7,column=4,sticky='w')
    stock7 = Spinbox(stockframe,from_=0,to=1000,justify=CENTER,width=10,textvariable=sps7)
    stock7.grid(row=8,column=4,sticky='w')
    stock8 = Spinbox(stockframe,from_=0,to=1000,justify=CENTER,width=10,textvariable=sps8)
    stock8.grid(row=9,column=4,sticky='w')
    stock9 = Spinbox(stockframe,from_=0,to=1000,justify=CENTER,width=10,textvariable=sps9)
    stock9.grid(row=10,column=4,sticky='w')
    stock10 = Spinbox(stockframe,from_=0,to=1000,justify=CENTER,width=10,textvariable=sps10)
    stock10.grid(row=11,column=4,sticky='w')
    Button(stockframe,text="ยืนยัน",bg='grey',width=8,command=updatestock).grid(row=12,column=4,sticky='w',padx=10,pady=10) # db
    Button(stockframe,text="ออก",bg='grey',width=8,command=backstock).grid(row=12,column=3,sticky='e')
    stockframe.grid(row=0,column=0,columnspan=5,sticky='news')
    return stock1,stock2,stock3,stock4,stock5,stock6,stock7,stock8,stock9,stock10

def backshopst():
    stockframe.destroy()
    shopframe2.destroy()
    shop()

def updatestock():
    ask = messagebox.askquestion("Admin","ต้องการเพิ่มสินค้าในคลังหรือไม่")
    price1,price2,price3,price4,price5,price6,price7,price8,price9,price10 = 0,0,0,0,0,0,0,0,0,0
    if ask == "yes":
        sql_r = "select name,price from product"
        cursor.execute(sql_r)
        result = cursor.fetchall()
        for i in result:
            pricelst.append(i[1])
        sql = "update product set stock=? where name=?"
        if sps1.get() != "0" and sps1.get() != "" :
            total = int(stocklst[0]) + int(sps1.get())
            price1 = int(pricelst[0]) * int(sps1.get())
            cursor.execute(sql,[total,namestocklst[0]])
            conn.commit()
        if sps2.get() != "0" and sps2.get() != "" :
            total = int(stocklst[1]) + int(sps2.get())
            price2 = int(pricelst[1]) * int(sps2.get())
            cursor.execute(sql,[total,namestocklst[1]])
            conn.commit()
        if sps3.get() != "0" and sps3.get() != "" :
            total = int(stocklst[2]) + int(sps3.get())
            price3 = int(pricelst[2]) * int(sps3.get())
            cursor.execute(sql,[total,namestocklst[2]])
            conn.commit()
        if sps4.get() != "0" and sps4.get() != "" :
            total = int(stocklst[3]) + int(sps4.get())
            price4 = int(pricelst[3]) * int(sps4.get())
            cursor.execute(sql,[total,namestocklst[3]])
            conn.commit()
        if sps5.get() != "0" and sps5.get() != "" :
            total = int(stocklst[4]) + int(sps5.get())
            price5 = int(pricelst[4]) * int(sps5.get())
            cursor.execute(sql,[total,namestocklst[4]])
            conn.commit()
        if sps6.get() != "0" and sps6.get() != "" :
            total = int(stocklst[5]) + int(sps6.get())
            price6 = int(pricelst[5]) * int(sps6.get())
            cursor.execute(sql,[total,namestocklst[5]])
            conn.commit()
        if sps7.get() != "0" and sps7.get() != "" :
            total = int(stocklst[6]) + int(sps7.get())
            price7 = int(pricelst[6]) * int(sps7.get())
            cursor.execute(sql,[total,namestocklst[6]])
            conn.commit()
        if sps8.get() != "0" and sps8.get() != "" :
            total = int(stocklst[7]) + int(sps8.get())
            price8 = int(pricelst[7]) * int(sps8.get())
            cursor.execute(sql,[total,namestocklst[7]])
            conn.commit()
        if sps9.get() != "0" and sps9.get() != "" :
            total = int(stocklst[8]) + int(sps9.get())
            price9 = int(pricelst[8]) * int(sps9.get())
            cursor.execute(sql,[total,namestocklst[8]])
            conn.commit()
        if sps10.get() != "0" and sps10.get() != "" :
            total = int(stocklst[9]) + int(sps10.get())
            price10 = int(pricelst[9]) * int(sps10.get())
            cursor.execute(sql,[total,namestocklst[9]])
            conn.commit()
        total_price =  price1 + price2 + price3 + price4 + price5 + price6 + price7 + price8 + price9 + price10
        sql_r1 = "insert into report1 values(?,?,?,?,?,?)"
        cursor.execute(sql_r1,[retimed,retimem,retimey,"รายจ่าย","เพิ่มสินค้า",total_price])
        conn.commit()
        sps1.set(0)
        sps2.set(0)
        sps3.set(0)
        sps4.set(0)
        sps5.set(0)
        sps6.set(0)
        sps7.set(0)
        sps8.set(0)
        sps9.set(0)
        sps10.set(0)
        messagebox.showinfo("Admin","เพิ่มสินค้าในคลังสำเร็จ")
        
def backstock():
    ask = messagebox.askquestion("Admin","ต้องการออกหรือไม่")
    if ask == "yes":
        sps1.set(0)
        sps2.set(0)
        sps3.set(0)
        sps4.set(0)
        sps5.set(0)
        sps6.set(0)
        sps7.set(0)
        sps8.set(0)
        sps9.set(0)
        sps10.set(0)
        stockframe.destroy()
        shopframe2.destroy()
        shop()

######################################################## รายงาน ########################################################

def report(): 
    global repframe
    sql = "select * from manager where username=?"
    cursor.execute(sql,[muserinfo.get()])
    result = cursor.fetchall()
    if result: 
        bgframe = Frame(root,bg='#F6F6F6')
        bgframe.place(x=0,y=0,width=w,height=h)
        repframe = Frame(root,bg='#F6F6F6')
        repframe.columnconfigure((0,1,2),weight=1)

        Label(repframe,text="รายงาน",font="Times 24 bold",bg="#F6F6F6").grid(row=0,column=0,columnspan=4,pady=20)
        Button(repframe,image=home,bg='#F6F6F6',border=0,command=rbackhome).grid(row=0,column=0,columnspan=4,sticky='e',padx=30,pady=10)
        Label(repframe,text="รายงาน: ",bg="#F6F6F6").grid(row=1,column=1,sticky='e',padx=(0,550),pady=10)
        Label(repframe,text="วัน/เดือน/ปี: ",bg="#F6F6F6").grid(row=2,column=1,sticky='e',padx=(0,550),pady=10)
        reportname = Combobox(repframe,values=["สรุปรายรับรายจ่ายภายในร้าน","สรุปชั่วโมงการเข้าใช้งาน"],width=30,textvariable=rnamespy)
        reportname.grid(row=1,column=1,columnspan=3,padx=(100,0),pady=10)
        day = Combobox(repframe,values=list(range(1,32)),width=5,textvariable=rdayspy)
        day.grid(row=2,column=1,columnspan=3,padx=(0,250),pady=10)
        month = Combobox(repframe,values=['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม'],width=11,textvariable=rmonthspy)
        month.grid(row=2,column=1,columnspan=3,padx=(30,0),pady=10)
        year = Combobox(repframe,values=list(range(2018,2023)),width=10,textvariable=ryearspy)
        year.grid(row=2,column=1,columnspan=3,padx=(380,0),pady=10)
        Button(repframe,text="แสดงข้อมูล",bg="grey",command=showreport).grid(row=3,column=0,columnspan=4)
        repframe.grid(row=0,column=0,columnspan=4,sticky='news')
    else:
        messagebox.showwarning("Admin","หน้านี้สามารถเข้าได้เฉพาะผู้จัดการเท่านั้น")

def rbackhome():
    rnamespy.set("")
    rdayspy.set("")
    rmonthspy.set("")
    ryearspy.set("")
    repframe.destroy()
    homeframe.destroy()
    homepage()

def showreport():
    month = 0
    if rnamespy.get() == "":
        messagebox.showwarning("Admin","กรุณาเลือกประเภทรายงาน")
    elif rdayspy.get() == "" or rmonthspy.get() == "" or ryearspy.get() == "":
        messagebox.showwarning("Admin","กรุณาเลือก วัน/เดือน/ปี")
    else:
        if rmonthspy.get() == "มกราคม":
            month = 1
        elif rmonthspy.get() == "กุมภาพันธ์":
            month = 2
        elif rmonthspy.get() == "มีนาคม":
            month = 3
        elif rmonthspy.get() == "เมษายน":
            month = 4
        elif rmonthspy.get() == "พฤษภาคม":
            month = 5
        elif rmonthspy.get() == "มิถุนายน":
            month = 6
        elif rmonthspy.get() == "กรกฎาคม":
            month = 7
        elif rmonthspy.get() == "สิงหาคม":
            month = 8
        elif rmonthspy.get() == "กันยายน":
            month = 9
        elif rmonthspy.get() == "ตุลาคม":
            month = 10
        elif rmonthspy.get() == "พฤศจิกายน":
            month = 11
        elif rmonthspy.get() == "ธันวาคม":
            month = 12
        if rnamespy.get() == "สรุปรายรับรายจ่ายภายในร้าน":
            sql = "select * from report1"
            cursor.execute(sql)
            result = cursor.fetchall()
            for i,data in enumerate(result):
                if int(rdayspy.get()) == data[0] and int(month) == data[1] and int(ryearspy.get()) == data[2]:
                    rp1_d.append(data[0])
                    rp1_m.append(data[1])
                    rp1_y.append(data[2])
                    rp1_t.append(data[3])
                    rp1_n.append(data[4])
                    rp1_p.append(data[5])
            if rp1_d != []:
                Label(repframe,text="สรุปรายรับรายจ่ายภายในร้าน",font="Times 20 bold",bg="#F6F6F6").grid(row=4,column=0,columnspan=4)
                Label(repframe,text="วัน  เดือน  ปี",bg="#F6F6F6").grid(row=5,column=0,padx=20)
                Label(repframe,text="ประเภท",bg="#F6F6F6").grid(row=5,column=1,sticky='w',padx=(80,0))
                Label(repframe,text="ช่องทางรายรับรายจ่าย",bg="#F6F6F6").grid(row=5,column=1,sticky='e',padx=(0,260))
                Label(repframe,text="ราคา",bg="#F6F6F6").grid(row=5,column=1,sticky='e',padx=(0,10),pady=10)
                Label(repframe,bg="#F6F6F6").grid(row=6,column=0,columnspan=4,rowspan=10,sticky='news')
                Button(repframe,text="แสดงข้อมูล",bg="grey",command=backre1).grid(row=3,column=0,columnspan=4)
                for i in range(len(rp1_d)):
                    Label(repframe,text=(rp1_d[i]),bg="#F6F6F6").grid(row=i+6,column=0,sticky='w',padx=(100,0))
                    Label(repframe,text=(rp1_m[i]),bg="#F6F6F6").grid(row=i+6,column=0,sticky='w',padx=(160,0))
                    Label(repframe,text=(rp1_y[i]),bg="#F6F6F6").grid(row=i+6,column=0,sticky='e',padx=(0,80))
                    Label(repframe,text=(rp1_t[i]),bg="#F6F6F6").grid(row=i+6,column=1,sticky='w',padx=(80,0))
                    Label(repframe,text=(rp1_n[i]),bg="#F6F6F6").grid(row=i+6,column=1,padx=(100,0))
                    Label(repframe,text=(rp1_p[i]),bg="#F6F6F6").grid(row=i+6,column=1,sticky='e',padx=25)
                    cnt.append(i)
                Button(repframe,bg="grey",text="แปลงเป็น PDF",command=convertpdf1).grid(row=20,column=0,columnspan=4,sticky='e',padx=20,pady=10)
            else:
                messagebox.showwarning("Admin","ไม่พบข้อมูล")
        elif rnamespy.get() == "สรุปชั่วโมงการเข้าใช้งาน":
            sql = "select * from report2"
            cursor.execute(sql)
            result = cursor.fetchall()
            for i,data in enumerate(result):
                if int(rdayspy.get()) == data[0] and int(month) == data[1] and int(ryearspy.get()) == data[2]:
                    rp2_d.append(data[0])
                    rp2_m.append(data[1])
                    rp2_y.append(data[2])
                    rp2_mem.append(data[3])
                    rp2_h.append(data[4])
                    rp2_p.append(data[5])
                    cnt2.append(i)
            if rp2_d != []:
                Label(repframe,text="สรุปชั่วโมงการเข้าใช้งาน",font="Times 20 bold",bg="#F6F6F6").grid(row=4,column=0,columnspan=4,sticky='news')
                Label(repframe,text="วัน  เดือน  ปี",bg="#F6F6F6").grid(row=5,column=0,padx=20)
                Label(repframe,text="สมาชิก",bg="#F6F6F6").grid(row=5,column=1,sticky='w',padx=(80,0))
                Label(repframe,text=" จำนวนชั่วโมงที่ใช้งาน",bg="#F6F6F6").grid(row=5,column=1,sticky='e',padx=(0,260))
                Label(repframe,text="คะแนน",bg="#F6F6F6").grid(row=5,column=1,sticky='e',padx=(0,10),pady=10)
                Label(repframe,bg="#F6F6F6").grid(row=6,column=0,columnspan=4,rowspan=10,sticky='news')
                Button(repframe,text="แสดงข้อมูล",bg="grey",command=backre2).grid(row=3,column=0,columnspan=4)
                for i in range(len(rp2_d)):
                    Label(repframe,text=(rp2_d[i]),bg="#F6F6F6").grid(row=i+6,column=0,sticky='w',padx=(100,0))
                    Label(repframe,text=(rp2_m[i]),bg="#F6F6F6").grid(row=i+6,column=0,sticky='w',padx=(160,0))
                    Label(repframe,text=(rp2_y[i]),bg="#F6F6F6").grid(row=i+6,column=0,sticky='e',padx=(0,80))
                    Label(repframe,text=(rp2_mem[i]),bg="#F6F6F6").grid(row=i+6,column=1,sticky='w',padx=(100,0))
                    Label(repframe,text=(rp2_h[i]),bg="#F6F6F6").grid(row=i+6,column=1,padx=(80,0))
                    Label(repframe,text=(rp2_p[i]),bg="#F6F6F6").grid(row=i+6,column=1,sticky='e',padx=30)
                Button(repframe,bg="grey",text="แปลงเป็น PDF",command=convertpdf2).grid(row=20,column=0,columnspan=4,sticky='e',padx=20,pady=10)
            else:
                messagebox.showwarning("Admin","ไม่พบข้อมูล")
        else:
            messagebox.showwarning("Admin","ไม่พบข้อมูล")

def backre1():
    rp1_d.clear()
    rp1_m.clear()
    rp1_y.clear()
    rp1_t.clear()
    rp1_n.clear()
    rp1_p.clear()
    cnt.clear()
    showreport()

def backre2():
    rp2_d.clear()
    rp2_m.clear()
    rp2_y.clear()
    rp2_mem.clear()
    rp2_h.clear()
    rp2_p.clear()
    cnt2.clear()
    showreport()

def convertpdf1():
    pdf1 = canvas.Canvas("report1_%s-%s-%s.pdf"%(retimed,retimem,retimey))
    pdf1.setFont('angsana',18)
    pdf1.drawString(250,800,"สรุปรายรับรายจ่ายภายในร้าน")
    pdf1.drawString(100,750,"  วัน เดือน ปี")
    pdf1.drawString(200,750,"ประเภท")
    pdf1.drawString(325,750,"ช่องทางรายรับรายจ่าย")
    pdf1.drawString(500,750,"ราคา")
    cnty = 0
    for i in range(len(cnt)):
        pdf1.drawString(100,(700-cnty),str(rp1_d[i]))
        pdf1.drawString(120,(700-cnty),str(rp1_m[i]))
        pdf1.drawString(140,(700-cnty),str(rp1_y[i]))
        pdf1.drawString(200,(700-cnty),str(rp1_t[i]))
        pdf1.drawString(320,(700-cnty),str(rp1_n[i]))
        pdf1.drawString(500,(700-cnty),str(rp1_p[i]))
        cnty += 30
    pdf1.save()
    Popen("report1_%s-%s-%s.pdf"%(retimed,retimem,retimey),shell=True)
    
def convertpdf2():
    pdf2 = canvas.Canvas("report2_%s-%s-%s.pdf"%(retimed,retimem,retimey))
    pdf2.setFont('angsana',18)
    pdf2.drawString(250,800,"สรุปรายรับรายจ่ายภายในร้าน")
    pdf2.drawString(100,750,"  วัน เดือน ปี")
    pdf2.drawString(200,750,"สมาชิก")
    pdf2.drawString(325,750,"จำนวนชั่วโมงที่ใช้งาน")
    pdf2.drawString(500,750,"คะแนน")
    cntx = 0
    for i in range(len(cnt2)):
        pdf2.drawString(100,(700-cntx),str(rp2_d[i]))
        pdf2.drawString(120,(700-cntx),str(rp2_m[i]))
        pdf2.drawString(140,(700-cntx),str(rp2_y[i]))
        pdf2.drawString(200,(700-cntx),str(rp2_mem[i]))
        pdf2.drawString(320,(700-cntx),str(rp2_h[i]))
        pdf2.drawString(500,(700-cntx),str(rp2_p[i]))
        cntx += 30
    pdf2.save()
    Popen("report2_%s-%s-%s.pdf"%(retimed,retimem,retimey),shell=True)

def logouthome(): 
    logo = messagebox.askquestion("Admin","คุณแน่ใจหรือว่าต้องการออกจากระบบ")
    if logo == 'yes':
        muserinfo.set("")
        mpwdinfo.set("")
        userinfo.set("")
        epwdinfo.set("")
        chhrspy.set(0)
        daytime.set(0)
        homeframe.destroy()
        loginlayout()
        cntdownhourtime()

w = 1400
h = 920

createconnection()
root = mainWindow()

arrPc = [0,0,0,0,0,0,0,0,0,0]

ulk = IntVar()
daytime = IntVar()
daytime.set(24)
hrspy1 = StringVar()
hrspy2 = StringVar()
hrspy3 = StringVar()
hrspy4 = StringVar()
hrspy5 = StringVar()
hrspy6 = StringVar()
hrspy7 = StringVar()
hrspy8 = StringVar()
hrspy9 = StringVar()
hrspy10 = StringVar()
hrspy1.set("0")
hrspy2.set("0")
hrspy3.set("0")
hrspy4.set("0")
hrspy5.set("0")
hrspy6.set("0")
hrspy7.set("0")
hrspy8.set("0")
hrspy9.set("0")
hrspy10.set("0")
mnspy1 = StringVar()
mnspy2 = StringVar()
mnspy3 = StringVar()
mnspy4 = StringVar()
mnspy5 = StringVar()
mnspy6 = StringVar()
mnspy7 = StringVar()
mnspy8 = StringVar()
mnspy9 = StringVar()
mnspy10 = StringVar()
mnspy1.set("0")
mnspy2.set("0")
mnspy3.set("0")
mnspy4.set("0")
mnspy5.set("0")
mnspy6.set("0")
mnspy7.set("0")
mnspy8.set("0")
mnspy9.set("0")
mnspy10.set("0")
scspy1 = StringVar()
scspy2 = StringVar()
scspy3 = StringVar()
scspy4 = StringVar()
scspy5 = StringVar()
scspy6 = StringVar()
scspy7 = StringVar()
scspy8 = StringVar()
scspy9 = StringVar()
scspy10 = StringVar()
scspy1.set("0")
scspy2.set("0")
scspy3.set("0")
scspy4.set("0")
scspy5.set("0")
scspy6.set("0")
scspy7.set("0")
scspy8.set("0")
scspy9.set("0")
scspy10.set("0")
usepspy = StringVar()
chhrspy = StringVar()
chhrspy.set(1)

userinfo = StringVar()
muserinfo = StringVar()
mpwdinfo = StringVar()
epwdinfo = StringVar()
fname = StringVar()
lname = StringVar()
bday = StringVar()
ads = StringVar()
phnum = StringVar()
em = StringVar()
newuserinfo = StringVar()
newpwdinfo = StringVar()
cfpwdinfo = StringVar()

fname2 = StringVar()
lname2 = StringVar()
bday2 = StringVar()
ads2 = StringVar()
phnum2 = StringVar()
em2 = StringVar()
newuserinfo2 = StringVar()

fname_espy = StringVar()
lname_espy = StringVar()
bd_espy = StringVar()
ads_espy = StringVar()
phone_espy = StringVar()
email_espy = StringVar()
user_espy = StringVar()
searchspy = StringVar()

pwd = StringVar()
newpwd = StringVar()
cfpwd = StringVar()

fname_uspy = StringVar()
lname_uspy = StringVar()
bd_uspy = StringVar()
ads_uspy = StringVar()
phone_uspy = StringVar()
email_uspy = StringVar()
user_uspy = StringVar()
searchuspy = StringVar()
unamespy = StringVar()
upointspy = StringVar()

sps1 = StringVar()
sps2 = StringVar()
sps3 = StringVar()
sps4 = StringVar()
sps5 = StringVar()
sps6 = StringVar()
sps7 = StringVar()
sps8 = StringVar()
sps9 = StringVar()
sps10 = StringVar()

sp1 = StringVar()
sp2 = StringVar()
sp3 = StringVar()
sp4 = StringVar()
sp5 = StringVar()
sp6 = StringVar()
sp7 = StringVar()
sp8 = StringVar()
sp9 = StringVar()
sp10 = StringVar()

rnamespy = StringVar()
rdayspy = StringVar()
rmonthspy = StringVar()
ryearspy = StringVar()

namepdlst = []
pdlst = []
namestocklst = []
stocklst = []
pricelst = []

userpic = PhotoImage(file="img/user.png").subsample(3,3)
logout = PhotoImage(file="img/logout.png").subsample(9,9)
home = PhotoImage(file="img/home.png").subsample(9,9)
computer = PhotoImage(file="img/computer.png").subsample(2,2)
lock = PhotoImage(file="img/lock.png").subsample(6,6)
unlock = PhotoImage(file="img/unlock.png").subsample(6,6)
back = PhotoImage(file="img/back.png").subsample(4,4)
search = PhotoImage(file="img/search.png").subsample(6,6)
stockpic = PhotoImage(file="img/stock.png").subsample(4,4)

voucher1 = PhotoImage(file="img/voucher1.png")
voucher2 = PhotoImage(file="img/voucher2.png")
voucher3 = PhotoImage(file="img/voucher3.png")
voucher4 = PhotoImage(file="img/voucher4.png")
voucher5 = PhotoImage(file="img/voucher5.png")

pd1 = PhotoImage(file="img/pd1.png").subsample(2,2)
pd2 = PhotoImage(file="img/pd2.png").subsample(2,2)
pd3 = PhotoImage(file="img/pd3.png").subsample(2,2)
pd4 = PhotoImage(file="img/pd4.png").subsample(2,2)
pd5 = PhotoImage(file="img/pd5.png").subsample(2,2)
pd6 = PhotoImage(file="img/pd6.png").subsample(2,2)
pd7 = PhotoImage(file="img/pd7.png").subsample(2,2)
pd8 = PhotoImage(file="img/pd8.png").subsample(2,2)
pd9 = PhotoImage(file="img/pd9.png").subsample(2,2)
pd10 = PhotoImage(file="img/pd10.png").subsample(2,2)

pd01 = PhotoImage(file="img/pd1.png").subsample(6,6)
pd02 = PhotoImage(file="img/pd2.png").subsample(6,6)
pd03 = PhotoImage(file="img/pd3.png").subsample(6,6)
pd04 = PhotoImage(file="img/pd4.png").subsample(6,6)
pd05 = PhotoImage(file="img/pd5.png").subsample(6,6)
pd06 = PhotoImage(file="img/pd6.png").subsample(6,6)
pd07 = PhotoImage(file="img/pd7.png").subsample(6,6)
pd08 = PhotoImage(file="img/pd8.png").subsample(6,6)
pd09 = PhotoImage(file="img/pd9.png").subsample(6,6)
pd010 = PhotoImage(file="img/pd10.png").subsample(6,6)

retimey = date.today().year
retimem = date.today().month
retimed = date.today().day
pdflst = []
cnt = []
cnt2 = []
rp1_d = []
rp1_m = []
rp1_y = []
rp1_t = []
rp1_n = []
rp1_p = []
rp2_d = []
rp2_m = []
rp2_y = []
rp2_mem = []
rp2_h = []
rp2_p = []

balance = array.array('i', [300,200,100])

loginlayout()
root.mainloop()
cursor.close()
conn.close()