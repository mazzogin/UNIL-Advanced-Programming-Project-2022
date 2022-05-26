from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
import tkinter
import pandas as pd
import openpyxl

#functions
def search_info1(price1,price2):
    global tree1
    tree1.delete(*tree1.get_children())
    new_list = []
    new_list2 = []
    numbers = []
    for i in range(0,len(xl_file)):
        a = int(xl_file["price"].loc[[i]])
        if a > price1 and a < price2:
            numbers.append(i)
    
    if len(numbers) == 0:
        messagebox.showinfo(message="None found")
    else:
        for n in numbers:
            for m in new:
                new_list.append(xl_file[m].loc[n])
            new_list2.append(list(new_list))
            new_list.clear()
        for k in new_list2:
            tree1.insert("",END,values=k)

def search_info2(rooms1,rooms2):
    global tree1
    tree1.delete(*tree1.get_children())
    new_list = []
    new_list2 = []
    numbers = []
    for i in range(0,len(xl_file)):
        a = float(xl_file["rooms"].loc[[i]])
        if a > rooms1 and a < rooms2:
            numbers.append(i)
    
    if len(numbers) == 0:
        messagebox.showinfo(message="None found")
    else:
        for n in numbers:
            for m in new:
                new_list.append(xl_file[m].loc[n])
            new_list2.append(list(new_list))
            new_list.clear()
        for k in new_list2:
            tree1.insert("",END,values=k)

def search_info3(zipcode):
    global tree1
    tree1.delete(*tree1.get_children())
    new_list = []
    new_list2 = []
    numbers = []
    for i in range(0,len(xl_file)):
        a = int(xl_file["zip_code"].loc[[i]])
        if a == zipcode:
            numbers.append(i)
    
    if len(numbers) == 0:
        messagebox.showinfo(message="None found")
    else:
        for n in numbers:
            for m in new:
                new_list.append(xl_file[m].loc[n])
            new_list2.append(list(new_list))
            new_list.clear()
        for k in new_list2:
            tree1.insert("",END,values=k)
            

#config
width = 700
height = 500
title = "Search properties"
f1 = ("Arial",14)
#tkinter
root = Tk()
root.geometry("{}x{}".format(width,height))
root.title(title)
#Create tab control
#main_f = Frame()
tab_control = ttk.Notebook(root)
tab_control.pack()
#Create Frames
frame1 = ttk.Frame(tab_control, width=700, height=500)
frame2 = ttk.Frame(tab_control, width=700, height=500)
frame3 = ttk.Frame(tab_control, width=700, height=500)

frame1.pack(expand=TRUE, fill='both')
frame2.pack(expand=TRUE, fill='both')
frame3.pack(expand=TRUE, fill='both')

#Define tabs
tab_control.add(frame1, text='Price Range')
tab_control.add(frame2, text='Number of Rooms')
tab_control.add(frame3, text='Zip Code')
   
    
#open xlm
xl_file = pd.read_excel("dataset.xlsx",index_col=None,engine="openpyxl",dtype="string")
new = list(xl_file)


### format tab1
Label1 = Label(frame1,text="Enter your price range:").grid(row=1, column=0, sticky=W, padx=10)
entry1 = Entry(frame1)
entry1.grid(row=1, column=1)
 
Label2 = Label(frame1,text="to").grid(row=1, column=2)
entry2 = Entry(frame1)
entry2.grid(row=1, column=3)

B1= Button(frame1, text="Search",command=lambda:search_info1(int(entry1.get()),int(entry2.get()))).place(relx=0.9,rely=0,anchor="nw")

scrollbar1 = Scrollbar(root)
scrollbar1.place(relx=0.975,rely=0.6,anchor="center",relheight=0.9)
tree1 = ttk.Treeview(root, show='headings',yscrollcommand=scrollbar1.set)
tree1['columns']=new
tree1.column("#0",anchor="center",width=0)
for i in new:
    tree1.column(i,anchor="center",width=20)
for i in new:
    tree1.heading(i,text=i)
tree1.place(relx=0.48,rely=0.6,anchor="center",relheight=0.9,relwidth=0.95)
scrollbar1.config(command=tree1.yview)


### format tab2
Label2 = Label(frame2,text="Number Of Rooms").grid(row=1, column=0, sticky=W, padx=10)
entry3 = Entry(frame2)
entry3.grid(row=1, column=1)
 
Label2 = Label(frame2,text="to").grid(row=1, column=2)
entry4 = Entry(frame2)
entry4.grid(row=1, column=3)

B2= Button(frame2, text="Search",command=lambda:search_info2(float(entry3.get()),int(entry4.get()))).place(relx=0.9,rely=0,anchor="nw")

'''scrollbar2 = Scrollbar(frame2)
scrollbar2.place(relx=0.975,rely=1.2,anchor="center",relheight=0.9)
tree2 = ttk.Treeview(frame1, show='headings',yscrollcommand=scrollbar2.set)
tree2['columns']=new
tree2.column("#0",anchor="center",width=0)
for i in new:
    tree2.column(i,anchor="center",width=20)
for i in new:
    tree2.heading(i,text=i)
tree2.place(relx=0.48,rely=1.2,anchor="center",relheight=0.9,relwidth=0.95)
scrollbar2.config(command=tree2.yview)'''

            
### Format tab 3
Label3 = Label(frame3,text="ZIP CODE").grid(row=1, column=0, sticky=W, padx=10)
entry5 = Entry(frame3)
entry5.grid(row=1, column=1)
 

B2= Button(frame3, text="Search",command=lambda:search_info3(int(entry5.get()))).place(relx=0.9,rely=0,anchor="nw")

'''scrollbar3 = Scrollbar(frame3)
scrollbar3.place(relx=0.975,rely=1.2,anchor="center",relheight=0.9)
tree3 = ttk.Treeview(frame1, show='headings',yscrollcommand=scrollbar3.set)
tree3['columns']=new
tree3.column("#0",anchor="center",width=0)
for i in new:
    tree3.column(i,anchor="center",width=20)
for i in new:
    tree3.heading(i,text=i)
tree3.place(relx=0.48,rely=1.2,anchor="center",relheight=0.9,relwidth=0.95)
scrollbar3.config(command=tree3.yview)'''


#functions
root.mainloop()

