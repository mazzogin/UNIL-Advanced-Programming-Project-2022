from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import openpyxl
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
            
#define clear box
def clear_fields():
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        tree1.delete(*tree1.get_children())
        
#define graph
def graph_it1():
    #Style and look of my plot
    sns.set(style="whitegrid")
    f, ax = plt.subplots(figsize=(18, 6),)
    sns.set_color_codes("pastel")
    #generate the bar plot
    sns.barplot(x='zip_code', y='price', ci = False, data=data, palette="Blues_d");
    #rotate the x-labels so the zipcodes are easier to read
    plt.xticks(rotation = 90);
    plt.title("Average price by zip code")
    plt.savefig(r'GUI/PricebyZip.png')
    plt.show()   

def graph_it2():
    #Style and look of my plot
    sns.set(style="whitegrid")
    f, ax = plt.subplots(figsize=(18, 6),)
    sns.set_color_codes("pastel")
    #generate the bar plot
    sns.barplot(x='rooms', y='price', ci = False, data=dataR, palette="Blues_d");
    #rotate the x-labels so the zipcodes are easier to read
    plt.xticks(rotation = 90);
    plt.title("Average price by number of rooms")
    plt.savefig(r'GUI/PricebyRooms.png')   
    plt.show()   
     
#config
width = 1100
height = 700
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
frame1 = ttk.Frame(tab_control, width=1100, height=700)
frame2 = ttk.Frame(tab_control, width=1100, height=700)
frame3 = ttk.Frame(tab_control, width=1100, height=700)
frame4 = ttk.Frame(tab_control, width=1100, height=700)

frame1.pack(expand=TRUE, fill='both')
frame2.pack(expand=TRUE, fill='both')
frame3.pack(expand=TRUE, fill='both')
frame4.pack(expand=TRUE, fill='both')

#Define tabs
tab_control.add(frame1, text='Price Range')
tab_control.add(frame2, text='Number of Rooms')
tab_control.add(frame3, text='Zip Code')
tab_control.add(frame4, text='Graphs') 
    
#open xlm
xl_file = pd.read_excel("GUI/gui_data/data.xlsx",index_col=None,engine="openpyxl",dtype="string")
new = list(xl_file)

#graph file
data = df = pd.read_excel('GUI/gui_data/MeanPriceZIP.xlsx',
                   sheet_name='Sheet1', engine="openpyxl",index_col=0)
data['price'] = data['price'].astype(float)
data['zip_code'] = data['zip_code'].astype(int)

dataR = df = pd.read_excel('GUI/gui_data/MeanPriceRooms.xlsx',
                   sheet_name='Sheet1', engine="openpyxl",index_col=0)
dataR['price'] = dataR['price'].astype(float)
dataR['rooms'] = dataR['rooms'].astype(float)

### format tab1
Label1 = Label(frame1,text="Enter your price range:").grid(row=1, column=0, sticky=W, padx=10)
entry1 = Entry(frame1)
entry1.grid(row=1, column=1)
 
Label2 = Label(frame1,text="to").grid(row=1, column=2)
entry2 = Entry(frame1)
entry2.grid(row=1, column=3)

B1= Button(frame1, text="Search",command=lambda:search_info1(int(entry1.get()),int(entry2.get()))).grid(row=1, column=5, padx=5)
B2 = Button(frame1, text="Clear", command=clear_fields)
B2.grid(row=4, column=4)

#Scrollbar format
scrollbar1 = Scrollbar(root)
scrollbar1.place(relx=0.975,rely=0.6,anchor="center",relheight=0.9)

#treeview format
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

B3= Button(frame2, text="Search",command=lambda:search_info2(float(entry3.get()),float(entry4.get()))).grid(row=1, column=5, padx=5)
B4 = Button(frame2, text="Clear", command=clear_fields)
B4.grid(row=4, column=5)            
### Format tab 3
Label3 = Label(frame3,text="ZIP CODE").grid(row=1, column=0, sticky=W, padx=10)
entry5 = Entry(frame3)
entry5.grid(row=1, column=1)

B5= Button(frame3, text="Search",command=lambda:search_info3(int(entry5.get()))).grid(row=1, column=5, padx=5)
B6 = Button(frame3, text="Clear", command=clear_fields)
B6.grid(row=4, column=5)            

### Format tab 4
Label4 = Label(frame4,text="Average price by Zip Code").grid(row=1, column=0, sticky=W, padx=10)
B5= Button(frame4, text="See graph",command=lambda:graph_it1()).grid(row=1, column=3, padx=5)

Label5 = Label(frame4,text="Average price by number of rooms").grid(row=2, column=0, sticky=W, padx=10)
B6= Button(frame4, text="See graph",command=lambda:graph_it2()).grid(row=2, column=3, padx=5)

#functions
root.mainloop()