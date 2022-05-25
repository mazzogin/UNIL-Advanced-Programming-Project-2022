from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
import tkinter
import pandas as pd
import openpyxl



ent1t1= Tk.Entry(frame1)
ent1t1.pack(fill="both", expand=1)
    label1=Tk.Label(frame1,text="Enter your price range:").grid(row=1, column=0, sticky=W, padx=10)
    entry1 = tk.Entry(frame1)
    entry1.grid(row=1, column=1)
 
    Label(frame1,text="to").grid(row=1, column=2)
    entry2 = Entry(frame1)
    entry2.grid(row=1, column=3)
    Label(frame1,text="Number of rooms: ").grid(row=2, column=0, sticky=W, padx=10)
    entry3 = Entry(frame1)
    entry3.grid(row=2, column=1, pady=5)

    Label(frame1,text="to").grid(row=2, column=2)
    entry4 = Entry(frame1)
    entry4.grid(row=2, column=3, pady=5)
    
    Label(frame1,text="Zip Code").grid(row=3, column=0, sticky=W, padx=10)
    entry5 = Entry(frame1)
    entry5.grid(row=3, column=1, pady=5)
    
    #define clear box
    def clear_fields():
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
    
    #search button
    Button(frame1,text="Search",command=lambda:search_info(int(entry1.get()),int(entry2.get()),
                                                           int(entry3.get()),int(entry4.get()),
                                                           int(entry5.get()))).grid(row=4, column=3, pady=5)
    
    #clear button
    Clear_Button = Button(frame1, text="Clear", command=clear_fields)
    Clear_Button.grid(row=4, column=4)
           

    
    scrollbar = Scrollbar(frame1)
    scrollbar.place(relx=0.975,rely=1,anchor="center",relheight=0.9)
    tree = ttk.Treeview(frame1, show='headings',yscrollcommand=scrollbar.set)
    tree['columns']=new
    tree.column("#0",anchor="center",width=0)
    for i in new:
        tree.column(i,anchor="center",width=20)
    for i in new:
        tree.heading(i,text=i)
    tree.place(relx=0.48,rely=1,anchor="center",relheight=0.9,relwidth=0.95)
    scrollbar.config(command=tree.yview)

    
   
def search_info(price1, price2, room1,room2, zipcode):
    global tree
    tree.delete(*tree.get_children())
    new_list = []
    new_list2 = []
    numbers = []
    for i in range(0,len(xl_file)):
        a = int(xl_file["Price"].loc[[i]])
        if a > price1 and a <= price2:
            numbers.append(i)
    
    if len(numbers) == 0:
        messagebox.showinfo(message="None found")
    else:
        for n in numbers:
            for m in new:
                new_list.append(xl_file[m].loc[n])
                try:
                    if type(new_list[3]) != type("str"):
                        new_list.clear()
                        break
                except IndexError:
                    pass
            if len(new_list) != 0:
                new_list2.append(list(new_list))
                new_list.clear()
        count = 0
        for k in range(len(new_list2)):
            
            try:
                if float(new_list2[k][3]) > float(room1) and float(new_list2[k][3]) <= float(room2):
                    count += 8
                else:
                    for j in range(0,8):
                        try:
                            new_list2.pop(count)
                        except:
                            pass
            except TypeError:
                    for j in range(0,8):
                        try:
                            new_list2.pop(count)
                        except:
                            pass
            except IndexError:
                pass
        for j in new_list2:
            tree.insert("",END,values=j)
        
        for h in range(0,len(new_list2)):
            b = int(xl_file["Zip_Code"].loc[[h]])
        if b ==zipcode:
            new_list2.append(h)
                                         
            

if __name__ == "__main__":
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
    frame1 = Frame(tab_control, width=700, height=500, bg= 'yellow')
    frame2 = Frame(tab_control, width=700, height=500, bg= 'orange')
    frame3 = Frame(tab_control, width=700, height=500, bg= 'red')
    frame4 = Frame(tab_control, width=700, height=500, bg= 'pink')
    frame5 = Frame(tab_control, width=700, height=500, bg= 'purple')
    
    frame1.pack(fill='both', expand=1)
    frame2.pack(fill='both', expand=1)
    frame3.pack(fill='both', expand=1)
    frame4.pack(fill='both', expand=1)
    frame5.pack(fill='both', expand=1)
    
    #Define tabs
    tab_control.add(frame1, text='Price Range')
    tab_control.add(frame2, text='Number of Rooms')
    tab_control.add(frame3, text='Zip Code')
    tab_control.add(frame4, text='TBD')
    tab_control.add(frame5, text='TBD')
    
    #open xlm
    xl_file = pd.read_excel("data.xlsx",index_col=None,engine="openpyxl",dtype="string")
    new = list(xl_file)
    #print(xl_file[new].loc[[2,3]])
    #print(xl_file["Price"].loc[3])
    
    #functions
    #frame1()
    #frame2()
    #frame3()
    #frame4()
    #frame5()
    root.mainloop()