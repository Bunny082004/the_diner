from tkinter import *
#from tkinter import messagebox as msg
import pymysql as p
from tkinter import ttk
from datetime import date
mydb=p.connect(host='localhost',user='root',password='root',port=3306,database='hotel')
cursor=mydb.cursor()
class Diner:
    def __init__(self):
        r=Tk()
        r.geometry('600x600')
        r.config(bg='#85929E')
        r.resizable(False,False)
        img=PhotoImage(file="hotelnext.png")
        Label(r,image=img,bg='#85929E',).place(x=-900,y=0)
        Button(r,text='Menu Display',bg='#CED7D7',fg='#17202A',font=('bold',30),command=self.menudisplay).place(x=0,y=60)
        Button(r,text='Menu update',bg='#CED7D7',fg='#17202A',font=('bold',30),command=self.menuUpdate).place(x=0,y=150)
        Button(r,text='Purchase',bg='#CED7D7',fg='#17202A',font=('bold',30),command=self.purchase).place(x=0,y=240)
        Button(r,text="Sell",bg="#CED7D7",fg="#17202A",font=('bold',30),command=self.sell).place(x=0,y=330)
        Button(r,text="Net Total",bg="#CED7D7",fg="#17202A",font=('bold',30),command=self.cdisplay).place(x=0,y=420)
        Button(r,text="ClockOff",bg="#CED7D7",fg="#17202A",font=('bold',30),command=self.colockOff).place(x=260,y=510)
        r.mainloop()
    def cdisplay(self):
        y=Tk()
        cursor.execute('select * from Total')
        t=1
        for i in cursor:
            t+=1
        tv=ttk.Treeview(y,columns=(1,2,3,4),show="headings",height=t)
        tv.pack()
        tv.heading(1,text="Date")
        tv.heading(2,text="Income")
        tv.heading(3,text="Expenditure")
        tv.heading(4,text="Net")
        cursor.execute('select * from Total')
        for i in cursor:
            tv.insert('','end',values=i)
        y.mainloop()
    def colockOff(self):
        currentDate=date.today()
        income=0
        expenditure=0
        cursor.execute('select * from Sell')
        for i in cursor:
            if i[0]==currentDate:
                income+=i[3]
        cursor.execute('select * from Purchase')
        for i in cursor:
            if i[0]==currentDate:
                expenditure+=i[3]
        cursor.execute("insert into Total values(%s,%s,%s,%s)",(currentDate,income,expenditure,income-expenditure))
        mydb.commit()
    def sell(self):
        y=Toplevel()
        y.geometry('600x600')
        y.config(bg='#85929E')
        y.resizable(False,False)
        img=PhotoImage(file="hotelnext.png")
        Label(y,image=img,bg='#85929E',).place(x=-900,y=0)
        Label(y,text='Item',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=80)
        Label(y,text='Quantity',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=150)
        Label(y,text='Total',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=220)
        self.sItem=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.sItem.place(x=200,y=80)
        self.sQuantity=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.sQuantity.place(x=200,y=150)
        self.sPrice=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.sPrice.place(x=200,y=220)
        Button(y,text='Add',bg='#CED7D7',fg='#17202A',font=('bold',30),command=self.sadd).place(x=250,y=300)
        Button(y,text='Display',bg='#CED7D7',fg='#17202A',font=('bold',30),command=self.sdisplay).place(x=220,y=500)
        y.mainloop()
    def sdisplay(self):
        y=Tk()
        cursor.execute('select * from Sell')
        t=1
        for i in cursor:
            t+=1
        tv=ttk.Treeview(y,columns=(1,2,3,4),show="headings",height=t)
        tv.pack()
        tv.heading(1,text="Date")
        tv.heading(2,text="Item")
        tv.heading(3,text="Quantity")
        tv.heading(4,text="Total amt ")
        cursor.execute('select * from Sell')
        for i in cursor:
            tv.insert('','end',values=i)
        y.mainloop()
    def sadd(self):
        currentDate=date.today()
        item =self.sItem.get()
        quantity=int(self.sQuantity.get())
        price=int(self.sPrice.get())
        cursor.execute("insert into Sell values(%s,%s,%s,%s)",(currentDate,item,quantity,price*quantity))
        mydb.commit()
    def purchase(self):
        y=Toplevel()
        y.geometry('600x600')
        y.config(bg='#85929E')
        y.resizable(False,False)
        img=PhotoImage(file="hotelnext.png")
        Label(y,image=img,bg='#85929E',).place(x=-900,y=0)
        Label(y,text='Item',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=80)
        Label(y,text='Quantity',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=150)
        Label(y,text='Total',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=220)
        self.pItem=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.pItem.place(x=200,y=80)
        self.pQuantity=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.pQuantity.place(x=200,y=150)
        self.pPrice=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.pPrice.place(x=200,y=220)
        Button(y,text='Add',bg='#CED7D7',fg='#17202A',font=('bold',30),command=self.padd).place(x=250,y=300)
        Button(y,text='Display',bg='#CED7D7',fg='#17202A',font=('bold',30),command=self.pdisplay).place(x=220,y=500)
        y.mainloop()
    def padd(self):
        currentDate=date.today()
        item =self.pItem.get()
        quantity=self.pQuantity.get()
        price=self.pPrice.get()
        cursor.execute("insert into Purchase values(%s,%s,%s,%s)",(currentDate,item,quantity,price))
        mydb.commit()
    def pdisplay(self):
        y=Tk()
        cursor.execute('select * from Purchase')
        t=1
        for i in cursor:
            t+=1
        tv=ttk.Treeview(y,columns=(1,2,3,4),show="headings",height=t)
        tv.pack()
        tv.heading(1,text="Date")
        tv.heading(2,text="Item")
        tv.heading(3,text="Price")
        tv.heading(4,text="Total amt ")
        cursor.execute('select * from Purchase')
        for i in cursor:
            tv.insert('','end',values=i)
        y.mainloop()
    def menudisplay(self):
        y=Tk()
        cursor.execute('select * from Menu')
        t=1
        for i in cursor:
            t+=1
        tv=ttk.Treeview(y,columns=(1,2),show="headings",height=t)
        tv.pack()
        tv.heading(1,text="Item")
        tv.heading(2,text="Price")
        cursor.execute('select * from Menu')
        for i in cursor:
            tv.insert('','end',values=i)
        y.mainloop()
    def menuUpdate(self):
        y=Toplevel()
        y.geometry('600x600')
        y.config(bg='#85929E')
        y.resizable(False,False)
        img=PhotoImage(file="hotelnext.png")
        Label(y,image=img,bg='#85929E',).place(x=-900,y=0)
        Label(y,text='Item',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=80)
        Label(y,text='Price',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=150)
        self.Item=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.Item.place(x=200,y=80)
        self.Price=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.Price.place(x=200,y=150)
        Button(y,text='Add',bg='#CED7D7',fg='#17202A',font=('bold',30),command=self.madd).place(x=250,y=300)
        Button(y,text='Update',bg='#CED7D7',fg='#17202A',font=('bold',30),command=self.mupdate).place(x=220,y=400)
        y.mainloop()
    def madd(self):
        item =self.Item.get()
        price=self.Price.get()
        cursor.execute("insert into Menu values(%s,%s)",(item,price))
        mydb.commit()
    def mupdate(self):
        item=self.Item.get()
        price=self.Price.get()
        cursor.execute("update Menu set Price=%s where Item=%s",(price,item))
        mydb.commit()

r=Diner()