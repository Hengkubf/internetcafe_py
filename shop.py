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

def shop():
    global amt_list,shopframe
    bgframe = Frame(root,bg='#F6F6F6')
    bgframe.place(x=0,y=0,width=w,height=h)
    #homeframe.destroy()
    shopframe = Frame(root,bg='#F6F6F6')
    shopframe.pack(fill=BOTH,expand=True)
    root.config(bg='#F6F6F6')

    canvas = Canvas(shopframe,bg='#F6F6F6')
    canvas.pack(side=LEFT, fill=BOTH,expand=True)
    scrollbar = Scrollbar(shopframe, orient=VERTICAL,command=canvas.yview)
    scrollbar.pack(side=RIGHT,fill=Y)
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>',lambda e: canvas.configure(scrollregion = canvas.bbox("all")))
    secondframe = Frame(canvas,bg='#F6F6F6')
    secondframe.grid(row=0,column=0,sticky='news')
    canvas.create_window((0,0), window=secondframe, anchor="nw")
    Label(secondframe,bg="#F6F6F6",text="Kira Internet Cafe Shop",font="Times 24 bold").grid(row=0,column=0,columnspan=4,padx=520,pady=30)
    #Button(choframe,image=back,bg="#F6F6F6",command=backshopco,border=0).grid(row=0,column=3,sticky='e',padx=20) #กลับหน้าหลัก
    Label(secondframe,bg="#F6F6F6",text="ชื่อสินค้า",font="Times 20 bold").grid(row=1,column=0,pady=10)
    Label(secondframe,bg="#F6F6F6",text="ราคาสินค้า",font="Times 20 bold").grid(row=1,column=1,pady=10)
    Label(secondframe,bg="#F6F6F6",text="จำนวนสินค้า",font="Times 20 bold").grid(row=1,column=2,pady=10)
    for i,data in enumerate(result_s) :
        img_list[data[0]] = PhotoImage(file=data[3]).subsample(3,3)
        Label(secondframe,text=data[0],image=img_list[data[0]],compound=LEFT,bg="#F6F6F6").grid(row=i+2,column=0,sticky='w',padx=(120,0),pady=10)
        Label(secondframe,text=(data[1],"บาท"),bg="#F6F6F6").grid(row=i+2,column=1,sticky='w',padx=(120,0),pady=10)
        Spinbox(secondframe,from_=0,to=data[2],bg="white",width=10,justify=CENTER,textvariable=amt_list[i]).grid(row=i+2,column=2,padx=20)
    Button(secondframe,bg="grey",text="ยืนยัน",width=10,command=checkout).grid(column=2,pady=20)

def checkout():
    global total,namelst,pricelst,amountlst
    amt_amt = []
    mst_ch = []
    zst_ch = []
    st_ch = []
    for i,data in enumerate(result_s):
        if int(amt_list[i].get()) > int(data[2]):
            messagebox.showwarning("Admin","สินค้า%sมีจำนวนน้อยกว่าที่ต้องการ กรุณาลองใหม่อีกครั้ง"%data[0])
            mst_ch.append("A") 
        if int(amt_list[i].get()) < 0 :
            zst_ch.append("A")
        amt_amt.append(amt_list[i].get()) 
        if int(amt_list[i].get()) == 0:
            st_ch.append(0)
    if len(st_ch) == len(amt_amt):
        messagebox.showwarning("Admin","กรุณาเลือกสินค้า")
        shopframe.destroy()
        shop()
    if "A" in mst_ch:
        shopframe.destroy()
        shop()
    if "A" in zst_ch:
        messagebox.showwarning("Admin","กรุณากรอกเลขที่มีค่ามากกว่า 0")
        shopframe.destroy()
        shop()
    if len(st_ch) != len(amt_amt) and "A" not in mst_ch and "A" not in zst_ch:
        bgframe = Frame(root,bg='#F6F6F6')
        bgframe.place(x=0,y=0,width=w,height=h)
        shopframe.destroy()
        #homeframe.destroy()
        choframe = Frame(root,bg='#F6F6F6')
        choframe.pack(fill=BOTH,expand=True)

        canvas = Canvas(choframe,bg='#F6F6F6')
        canvas.pack(side=LEFT, fill=BOTH,expand=True)
        scrollbar = Scrollbar(choframe, orient=VERTICAL,command=canvas.yview)
        scrollbar.pack(side=RIGHT,fill=Y)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>',lambda e: canvas.configure(scrollregion = canvas.bbox("all")))
        secondframe = Frame(canvas,bg='#F6F6F6')
        secondframe.grid(row=0,column=0,sticky='news')
        canvas.create_window((0,0), window=secondframe, anchor="nw")
        #Button(choframe,image=back,bg="#F6F6F6",command=backshopco,border=0).grid(row=0,column=3,sticky='e',padx=20) #กลับหน้าร้านค้า
        Label(secondframe,text="รายการทั้งหมด",font="Times 24 bold",bg="#F6F6F6").grid(row=0,column=0,columnspan=4,padx=600,pady=30)
        Label(secondframe,text="ชื่อสินค้า",bg="#F6F6F6",font="Times 20 bold").grid(row=1,column=0,pady=10)
        Label(secondframe,text="ราคาสินค้า",bg="#F6F6F6",font="Times 20 bold").grid(row=1,column=1,pady=10)
        Label(secondframe,text="จำนวน",bg="#F6F6F6",font="Times 20 bold").grid(row=1,column=2,pady=10)
        Label(secondframe,text="รวม",bg="#F6F6F6",font="Times 20 bold").grid(row=1,column=3,pady=10)
        total = 0
        namelst = []
        amountlst = []
        for i,data in enumerate(result_s) :
            if len(st_ch) != len(amt_amt) and "A" not in mst_ch and "A" not in zst_ch and int(amt_list[i].get()) != 0:
                Label(secondframe,text=data[0],image=img_list[data[0]],compound=LEFT,bg="#F6F6F6").grid(row=i+2,column=0,sticky='w',padx=(120,0),pady=10)
                Label(secondframe,text=(data[1],"บาท"),bg="#F6F6F6").grid(row=i+2,column=1,sticky='w',padx=(120,0),pady=10)
                Label(secondframe,text=amt_list[i].get(),bg="#F6F6F6").grid(row=i+2,column=2,sticky='w',padx=(120,0),pady=10)
                Label(secondframe,text=(int(data[1])*int(amt_list[i].get())),compound=LEFT,bg="#F6F6F6").grid(row=i+2,column=3,sticky='w',padx=(120,0),pady=10)
                namelst.append(data[0])
                amountlst.append(amt_list[i].get())
                total += int(data[1])*int(amt_list[i].get())
        Label(secondframe,text=("รวมทั้งหมด %0.2f บาท"%total),compound=LEFT,bg="#F6F6F6",font="Times 20 bold").grid(column=2,columnspan=3,sticky='w',padx=(120,0),pady=10)
        Button(secondframe,bg="grey",text="ยืนยัน",width=10,command=pay).grid(column=3,pady=30)

def pay():
    askpay = messagebox.askquestion("Admin","ต้องการชำระสินค้าหรือไม่")
    if askpay == "yes":
        pdlst = []
        '''sql_r1 = "insert into report1 values(?,?,?,?,?,?)"
        cursor.execute(sql_r1,[retimed,retimem,retimey,"รายรับ","ขายสินค้า",total])
        conn.commit()'''
        sql2 = "update product set stock=? where name=?"
        for data in result_s:
            pdlst.append(data[2])
        for i in range(len(namelst)):
            totalst = (pdlst[i]) - amountlst[i]
            cursor.execute(sql2,[totalst,namelst[i]])
            conn.commit()
        messagebox.showinfo("Admin","ชำระเงินสำเร็จ")
        #backshopco()

w = 1400
h = 920

createconnection()
root = mainWindow()
sql = "select * from product"
cursor.execute(sql)
result_s = cursor.fetchall()
amt_list = [IntVar() for i in result_s]
img_list = {}
shop()
root.mainloop()
cursor.close()
conn.close()