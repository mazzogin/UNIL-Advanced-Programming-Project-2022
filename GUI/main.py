from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pandas as pd





def main():
    global tree
    main_f.pack(fill="both", expand=1)
    Label(main_f,text="Price from").place(relx=0,rely=0,anchor="nw")
    entry1 = Entry(main_f)
    entry1.insert(END,"0")
    entry1.place(relx=0.1,rely=0,anchor="nw",relwidth=0.15)
    Label(main_f,text="to").place(relx=0.25,rely=0,anchor="nw",relwidth=0.05)
    entry2 = Entry(main_f)
    entry2.place(relx=0.3,rely=0,anchor="nw",relwidth=0.15) 

    Label(main_f,text="Rooms: ").place(relx=0.5,rely=0,anchor="nw")
    entry3 = Entry(main_f)
    entry3.place(relx=0.57,rely=0,anchor="nw",relwidth=0.1)

    Label(main_f,text="to").place(relx=0.65,rely=0,anchor="nw",relwidth=0.05)
    entry4 = Entry(main_f)
    entry4.place(relx=0.7,rely=0,anchor="nw",relwidth=0.1) 
    

    Button(main_f,text="Search",command=lambda:search_info(int(entry1.get()),int(entry2.get()),float(entry3.get()),float(entry4.get()))).place(relx=0.9,rely=0,anchor="nw")
    scrollbar = Scrollbar(main_f)
    scrollbar.place(relx=0.975,rely=0.525,anchor="center",relheight=0.9)
    tree = ttk.Treeview(main_f, show='headings',yscrollcommand=scrollbar.set)
    tree['columns']=new
    tree.column("#0",anchor="center",width=0)
    for i in new:
        tree.column(i,anchor="center",width=20)
    for i in new:
        tree.heading(i,text=i)
    tree.place(relx=0.48,rely=0.525,anchor="center",relheight=0.9,relwidth=0.95)
    scrollbar.config(command=tree.yview)
    
def search_info(price1,price2, room1,room2):
    global tree
    tree.delete(*tree.get_children())
    new_list = []
    new_list2 = []
    new_list3 = []
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

            

if __name__ == "__main__":
    #config
    width = 700
    height = 500
    title = ""
    f1 = ("Arial",14)
    #tkinter
    root = Tk()
    root.geometry("{}x{}".format(width,height))
    root.title(title)
    #Frames
    main_f = Frame()
    #open xlm
    xl_file = pd.read_excel("comparis-data-sample.xlsx",index_col=None,engine="openpyxl",dtype="string")
    new = list(xl_file)
    #print(xl_file[new].loc[[2,3]])
    #print(xl_file["Price"].loc[3])
    
    #functions
    main()
    root.mainloop()
