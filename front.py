from tkinter import *
import back

def get_selected_row(event):
    global selected_row
    index=list.curselection()[0]
    selected_row=list.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_row[1])
    e2.delete(0,END)
    e2.insert(END,selected_row[2])
    e3.delete(0,END)
    e3.insert(END,selected_row[3])
    e4.delete(0,END)
    e4.insert(END,selected_row[4])
    e5.delete(0,END)
    e5.insert(END,selected_row[5])
    e6.delete(0,END)
    e6.insert(END,selected_row[6])

def clear_values():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)

def delete_command():
    back.delete(selected_row[0]) 

def view_command():
    list.delete(0,END)
    for row in back.view():
        list.insert(END,row)

def search_command():
    list.delete(0,END)
    for row in back.search(date_text.get(),expend_text.get(),exercise_text.get(),study_text.get(),diet_text.get(),py_text.get()):
        list.insert(END,row)

def add_command():
    back.insert(date_text.get(),expend_text.get(),exercise_text.get(),study_text.get(),diet_text.get(),py_text.get())
    list.delete(0,END)
    list.insert(END,(date_text.get(),expend_text.get(),exercise_text.get(),study_text.get(),diet_text.get(),py_text.get()))

win=Tk() #creates a window win

win.wm_title("MY ROUTINE DATABASE")
 #labels
l1=Label(win, text='Date')
l1.grid(row=0,column=0)
l2=Label(win, text='Expenditure')
l2.grid(row=0,column=2)
l3=Label(win, text='Exercise')
l3.grid(row=1,column=0)
l4=Label(win, text='Study')
l4.grid(row=1,column=2)
l5=Label(win, text='Diet')
l5.grid(row=2,column=0)
l6=Label(win, text='Python')
l6.grid(row=2,column=2)

#entries
date_text=StringVar()
e1=Entry(win,textvariable=date_text)
e1.grid(row=0,column=1)

expend_text=StringVar()
e2=Entry(win,textvariable=expend_text)
e2.grid(row=0,column=3)

exercise_text=StringVar()
e3=Entry(win,textvariable=exercise_text)
e3.grid(row=1,column=1)

study_text=StringVar()
e4=Entry(win,textvariable=study_text)
e4.grid(row=1,column=3)

diet_text=StringVar()
e5=Entry(win,textvariable=diet_text)
e5.grid(row=2,column=1)

py_text=StringVar()
e6=Entry(win,textvariable=py_text)
e6.grid(row=2,column=3)

#listbox
list=Listbox(win,height=8,width=50)
list.grid(row=3,column=0,rowspan=9,columnspan=2)

#scrollbar
sb=Scrollbar(win)
sb.grid(row=3,column=2,rowspan=9)

list.bind('<<ListboxSelect>>',get_selected_row) #1st param is an action like a click on the listbox,2nd is the function


#buttons
b1=Button(win,text="ADD",width=12,pady=5,command=add_command)
b1.grid(row=3,column=3)

b2=Button(win,text="Search",width=12,pady=5,command=search_command)
b2.grid(row=4,column=3)

b3=Button(win,text="Delete date",width=12,pady=5,command=delete_command)
b3.grid(row=5,column=3)

b4=Button(win,text="View all",width=12,pady=5,command=view_command)
b4.grid(row=6,column=3)

b5=Button(win,text="Close",width=12,pady=5,command=win.destroy)#window is closed
b5.grid(row=7,column=3)

b6=Button(win,text="Clear",width=12,pady=5,command=clear_values)#window is closed
b6.grid(row=8,column=3)

win.mainloop()
