import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
def mainWindow():
    root = Tk()
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#F6F6F6')
    icon = PhotoImage(file="img/icon.png")  
    root.iconphoto(TRUE,icon)                 
    root.title("Kira Internet Cafe")
    root.option_add('*font',"Times 20")
    root.rowconfigure((0,1,2,3),weight=1)
    root.columnconfigure((0,1,2,3),weight=1)
    return root
def createconnection():
    global conn,cursor
    conn = sqlite3.connect('kirainternet.db')
    cursor = conn.cursor()

def stock():
    global stockframe,searchspin
    bgframe = Frame(root,bg='#F6F6F6')
    bgframe.place(x=0,y=0,width=w,height=h)
    #shopframe.destroy()
    #homeframe.destroy()
    stockframe = Frame(root,bg='#F6F6F6')
    stockframe.rowconfigure((0,1,2,3,4,5,6,7,8),weight=1)
    stockframe.columnconfigure((0,1,2,3),weight=1)

    sqlname = "select name from product"
    cursor.execute(sqlname)
    result_name = cursor.fetchall()
    Label(stockframe,text="จัดการสินค้า",font="Times 24 bold",bg="#F6F6F6").grid(row=0,column=0,columnspan=4,pady=30)
    Label(stockframe,text="กรุณาเลือกชื่อสินค้า: ",bg="#F6F6F6").grid(row=1,column=1,sticky='e')
    Button(stockframe,text="เพิ่มข้อมูล",bg="grey",width=10,command=add).grid(row=2,column=2,sticky='w',padx=(216,0))
    Button(stockframe,text="ลบข้อมูล",bg="grey",width=10,command=delete).grid(row=2,column=3,sticky='w')
    Button(stockframe,text="แก้ไขข้อมูล",bg="grey",width=10,command=editstock).grid(row=2,column=2,sticky='e')
    Button(stockframe,text="ออก",bg="grey",width=10,command=backtoshop).grid(row=3,column=3,sticky='w')
    searchspin = Combobox(stockframe,justify=CENTER,textvariable=namepdspy)
    mylst = [i for i, in result_name]
    searchspin['values'] = mylst
    searchspin.current(0)
    searchspin.grid(row=1,column=2,columnspan=2,sticky='w',padx=20)
    stockframe.grid(row=0,column=0,columnspan=4,sticky='news')

def add():
    global pdname,pdpicture,pdprice,pdamount
    searchspin.current(0)
    Label(stockframe,bg="#F6F6F6").grid(row=4,column=0,sticky='news',rowspan=10,columnspan=4)
    Label(stockframe,text="ชื่อสินค้า: ",bg="#F6F6F6").grid(row=4,column=1,sticky='e',pady=(30,0))
    Label(stockframe,text="ราคาสินค้า: ",bg="#F6F6F6").grid(row=5,column=1,sticky='e')
    Label(stockframe,text="จำนวนสินค้า: ",bg="#F6F6F6").grid(row=6,column=1,sticky='e')
    Label(stockframe,text="ประเภทสินค้า: ",bg="#F6F6F6").grid(row=7,column=1,sticky='e')
    pdname = Entry(stockframe,bg="#F6F6F6",textvariable=newnpr)
    pdname.grid(row=4,column=2,sticky='w',pady=(30,0),padx=10)
    pdprice = Entry(stockframe,bg="#F6F6F6",textvariable=newppr)
    pdprice.grid(row=5,column=2,sticky='w',padx=10)
    pdamount = Entry(stockframe,bg="#F6F6F6",textvariable=newapr)
    pdamount.grid(row=6,column=2,sticky='w',padx=10)
    Radiobutton(stockframe,text="อาหาร",bg="#F6F6F6",variable=typefnd,value=1).grid(row=7,column=2,sticky='w',padx=10)
    Radiobutton(stockframe,text="เครื่องดื่ม",bg="#F6F6F6",variable=typefnd,value=2).grid(row=7,column=2,sticky='w',padx=(150,0))
    Button(stockframe,text="ยืนยัน",bg="grey",command=confirmadd,width=10).grid(row=8,column=3,sticky='w',padx=10)
    pdname.delete(0,END)
    pdprice.delete(0,END)
    pdamount.delete(0,END)
    pdname.insert(0,"ชื่อสินค้า")
    pdname.config(state=DISABLED)
    pdname.bind("<Button-1>",pdtname)
    pdprice.insert(0,"00")
    pdprice.config(state=DISABLED)
    pdprice.bind("<Button-1>",pdtprice)
    pdamount.insert(0,"000")
    pdamount.config(state=DISABLED)
    pdamount.bind("<Button-1>",pdtamount)

def pdtname(event):
    pdname.config(state=NORMAL)
    pdname.delete(0,END)
def pdtprice(event):
    pdprice.config(state=NORMAL)
    pdprice.delete(0,END)
def pdtamount(event):
    pdamount.config(state=NORMAL)
    pdamount.delete(0,END)

def confirmadd():
    ch_price = newppr.get()
    ch_amt = newapr.get()
    if newnpr.get() == "" or newnpr.get() == "ชื่อสินค้า":
        messagebox.showwarning("Admin","กรุณากรอกชื่อสินค้า")
    elif newppr.get() == "" or newppr.get() == "00" or int(newppr.get()) == 0:
        messagebox.showwarning("Admin","กรุณากรอกราคาสินค้า")
    elif ch_price.isdigit() != True:
        messagebox.showwarning("Admin","กรุณากรอกราคาสินค้าเป็นตัวเลขเท่านั้น")
    elif ch_amt.isdigit() != True:
        messagebox.showwarning("Admin","กรุณากรอกจำนวนสินค้าเป็นตัวเลขเท่านั้น")
    elif newapr.get() == "" or newapr.get() == "000" or int(newapr.get()) == 0:
        messagebox.showwarning("Admin","กรุณากรอกจำนวนสินค้า")
    elif typefnd.get() == 0:
        messagebox.showwarning("Admin","กรุณาเลือกประเภทสินค้า")
    else:
        sql = "select * from product where name=?"
        cursor.execute(sql,[newnpr.get()])
        result = cursor.fetchall()
        if result:
            messagebox.showwarning("Admin","สินค้าชิ้นนี้มีชื่อในระบบแล้ว กรุณาลองใหม่")
        else:
            confirm = messagebox.askquestion("Admin","คุณแน่ใจหรือว่าต้องการเพิ่มข้อมูลสินค้า")
            if confirm == "yes" :
                if typefnd.get() == 1:
                    sql="insert into product values(?,?,?,?,?)"
                    cursor.execute(sql,[newnpr.get(),newppr.get(),newapr.get(),0,"อาหาร"])
                    conn.commit()
                else:
                    sql="insert into product values(?,?,?,?,?)"
                    cursor.execute(sql,[newnpr.get(),newppr.get(),newapr.get(),0,"เครื่องดื่ม"])
                    conn.commit()
                pdname.delete(0,END)
                pdprice.delete(0,END)
                pdamount.delete(0,END)
                messagebox.showinfo("Admin","บันทึกข้อมูลเรียบร้อย")
                #stockframe.destroy()
                #shop()

def delete():
    sql = "select * from product where name=?"
    cursor.execute(sql,[namepdspy.get()])
    result = cursor.fetchall()
    if result:
        Label(stockframe,bg="#F6F6F6").grid(row=4,column=0,sticky='news',rowspan=10,columnspan=4)
        askdel = messagebox.askquestion("Admin","คุณแน่ใจหรือว่าต้องการลบข้อมูลสินค้า")
        if askdel == "yes":
            sql="delete from product where name=?"
            cursor.execute(sql,[namepdspy.get()])
            conn.commit()
            messagebox.showinfo("Admin","ลบข้อมูลสินค้าเรียบร้อย")
            searchspin.current(0)
            #stockframe.destroy()
            #shop()
    else:
        messagebox.showwarning("Admin","ไม่พบชื่อสินค้านี้ในระบบ กรุณาลองใหม่")

def editstock():
    global pdn,pdp,pda
    sql = "select * from product where name=?"
    cursor.execute(sql,[namepdspy.get()])
    result = cursor.fetchall()
    if result:
        Label(stockframe,bg="#F6F6F6").grid(row=4,column=0,sticky='news',rowspan=10,columnspan=4)
        Label(stockframe,text="ชื่อสินค้า: ",bg="#F6F6F6").grid(row=4,column=1,sticky='e',pady=(30,0))
        Label(stockframe,text="ราคาสินค้า: ",bg="#F6F6F6").grid(row=5,column=1,sticky='e')
        Label(stockframe,text="จำนวนสินค้า: ",bg="#F6F6F6").grid(row=6,column=1,sticky='e')
        Label(stockframe,text="ประเภทสินค้า: ",bg="#F6F6F6").grid(row=7,column=1,sticky='e')
        pdn = Entry(stockframe,bg="#F6F6F6",textvariable=npr)
        pdn.grid(row=4,column=2,sticky='w',pady=(30,0),padx=10)
        pdp = Entry(stockframe,bg="#F6F6F6",textvariable=ppr)
        pdp.grid(row=5,column=2,sticky='w',padx=10)
        pda = Entry(stockframe,bg="#F6F6F6",textvariable=apr)
        pda.grid(row=6,column=2,sticky='w',padx=10)
        pdt = Entry(stockframe,bg="#F6F6F6")
        pdt.grid(row=7,column=2,sticky='w',padx=10)
        Button(stockframe,text="ยืนยัน",bg="grey",command=confirmedit,width=10).grid(row=8,column=3,sticky='w',padx=10)
        pdn.delete(0,END)
        pdp.delete(0,END)
        pda.delete(0,END)
        for i in result:
            pdn.insert(0,i[0])
            pdp.insert(0,i[1])
            pda.insert(0,i[2])
            pdt.insert(0,i[4])
        pdn.config(state=DISABLED)
        pdn.bind("<Button-1>",pdtn)
        pdp.config(state=DISABLED)
        pdp.bind("<Button-1>",pdtp)
        pda.config(state=DISABLED)
        pda.bind("<Button-1>",pdta)
        pdt.config(state=DISABLED)
    else:
        messagebox.showwarning("Admin","ไม่พบชื่อสินค้านี้ในระบบ กรุณาลองใหม่")

def pdtn(event):
    pdn.config(state=NORMAL)
    pdn.delete(0,END)
def pdtp(event):
    pdp.config(state=NORMAL)
    pdp.delete(0,END)
def pdta(event):
    pda.config(state=NORMAL)
    pda.delete(0,END)

def confirmedit():
    ch_price = ppr.get()
    ch_amt = apr.get()
    if npr.get() == "":
        messagebox.showwarning("Admin","กรุณากรอกชื่อสินค้า")
    elif ppr.get() == "" or int(ppr.get()) == 0:
        messagebox.showwarning("Admin","กรุณากรอกราคาสินค้า")
    elif ch_price.isdigit() != True:
        messagebox.showwarning("Admin","กรุณากรอกราคาสินค้าเป็นตัวเลขเท่านั้น")
    elif ch_amt.isdigit() != True:
        messagebox.showwarning("Admin","กรุณากรอกจำนวนสินค้าเป็นตัวเลขเท่านั้น")
    elif apr.get() == "" or int(apr.get()) == 0:
        messagebox.showwarning("Admin","กรุณากรอกจำนวนสินค้า")
    else:
        sql = "select * from product where name=?"
        cursor.execute(sql,[npr.get()])
        result = cursor.fetchall()
        if result:
            confirm = messagebox.askquestion("Admin","คุณแน่ใจหรือว่าต้องการแก้ไขข้อมูลสินค้า")
            if confirm == "yes" :
                sql="insert into product values(name=?,price=?,stock=?)"
                cursor.execute(sql,[npr.get(),ppr.get(),apr.get()])
                conn.commit()
                pdn.delete(0,END)
                pdp.delete(0,END)
                pda.delete(0,END)
                messagebox.showinfo("Admin","บันทึกข้อมูลเรียบร้อย")
                #stockframe.destroy()
                #shop()
def backtoshop():
    pdn.delete(0,END)
    pdp.delete(0,END)
    pda.delete(0,END)
    pdname.delete(0,END)
    pdprice.delete(0,END)
    pdamount.delete(0,END)
    pdpicture.delete(0,END)
    stockframe.destroy()
    stock()

w = 1400
h = 920

createconnection()
root = mainWindow()

sql = "select * from product"
cursor.execute(sql)
result_s = cursor.fetchall()
newnpr = StringVar()
newppr = StringVar()
newapr = StringVar()
typefnd = IntVar()
typefnd.set(0)
namepdspy = StringVar()
npr = StringVar()
ppr = StringVar()
apr = StringVar()

stock()
root.mainloop()
cursor.close()
conn.close()