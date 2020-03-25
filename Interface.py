from tkinter import *
        
def vi_int(int_var):
    try:
        int(int_var.get())
        return True
    except ValueError:
        return False

def handle_ok_button1():
    okButton1()

def okButton1(): #fix
    print("")
    pass

def handle_ok_button2():
    okButton2()

def okButton2(): #fix
    print("")
    pass

def handle_ok_button3():
    okButton3()

def okButton3(): #fix
    print("")
    pass #crash the program?

def handle_ok_button4():
    okButton4()

def okButton4(): #fix
    print("")

    pass

def handle_ok_button5():
    okButton5()

def okButton5(): #fix
    print("")
    pass

def handle_ok_button6():
    okButton6()

def okButton6(): #fix
    print("")
    pass

def file_save():
    pass

def file_saveas():
    pass

def file_import():
    pass

def file_exit():
    pass

def control_start():
    pass

def control_pause():
    pass

def control_stop():
    pass

def help_about():
    pass

root = Tk()
root.title("Ride Page")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
controlmenu = Menu(menubar, tearoff=0)
helpmenu = Menu(menubar, tearoff=0)
#scrollbar = Scrollbar(root)
#scrollbar.pack(side=RIGHT, fill=Y)

#Frame 1---------------------------------------------------------------------------------------------------------
frame1 = Frame(root,highlightcolor="black", highlightthickness=1)
frame1.grid(row=0,column=0)

Label(frame1,text="Rides").grid(row=0,column=0,sticky=N) #copy and paste for lame use
Label(frame1,text=" ").grid(row=1,column=0,sticky="N")
Label(frame1,text=" ").grid(row=2,column=0,sticky="N")
Label(frame1,text=" ").grid(row=3,column=0,sticky="N")
Label(frame1,text=" ").grid(row=4,column=0,sticky="N")
Label(frame1,text=" ").grid(row=5,column=0,sticky="N")
Label(frame1,text=" ").grid(row=6,column=0,sticky="N")
Label(frame1,text=" ").grid(row=7,column=0,sticky="N")
Label(frame1,text=" ").grid(row=8,column=0,sticky="N")
Label(frame1,text=" ").grid(row=9,column=0,sticky="N")
Label(frame1,text=" ").grid(row=10,column=0,sticky="N")

#Frame 2--------------------------------------------------------------------------------------------------------
frame2 = Frame(root) 
frame2.grid(row=0,column=1)
string_entry_var1 = StringVar()
string_entry_var1.set(int(0))
string_entry_value = Entry(frame2,textvariable=string_entry_var1,width=30)
string_entry_value.grid(row=1,column=0,sticky=W)

string_entry_var2 = StringVar()
string_entry_var2.set(int(0))
string_entry_value = Entry(frame2,textvariable=string_entry_var2,width=30)
string_entry_value.grid(row=3,column=0,sticky=W)

string_entry_var3 = StringVar()
string_entry_var3.set(int(0))
string_entry_value = Entry(frame2,textvariable=string_entry_var3,width=30)
string_entry_value.grid(row=5,column=0,sticky=W)

string_entry_var4 = StringVar()
string_entry_var4.set(int(0))
string_entry_value = Entry(frame2,textvariable=string_entry_var4,width=30)
string_entry_value.grid(row=7,column=0,sticky=W)

string_entry_var5 = StringVar()
string_entry_var5.set(int(0))
string_entry_value = Entry(frame2,textvariable=string_entry_var5,width=30)
string_entry_value.grid(row=9,column=0,sticky=W)

string_entry_var6 = StringVar()
string_entry_var6.set(int(0))
string_entry_value = Entry(frame2,textvariable=string_entry_var6,width=30)
string_entry_value.grid(row=11,column=0,sticky=W)

Label(frame2,text='Number Of People on the Ride').grid(row=0,column=0,sticky=W)
Label(frame2,text='People in Line').grid(row=2,column=0,sticky=W)
Label(frame2,text='State of Ride').grid(row=4, column=0,sticky=W)
Label(frame2,text='People Getting on the Ride').grid(row=6,column=0,sticky=W)
Label(frame2,text='People on the Ride').grid(row=8,column=0,sticky=W)
Label(frame2,text='Most People in Line').grid(row=10,column=0,sticky=W)

#Frame 3--------------------------------------------------------------------------------------------------------
frame3 = Frame(root)
frame3.grid(row=1,column=0)
ok_button1 = Button(frame3,text="Create",width=7,height=1,command=handle_ok_button1)
ok_button1.pack(side=LEFT)
ok_button2 = Button(frame3,text="Edit",width=7,height=1,command=handle_ok_button2)
ok_button2.pack(side=LEFT)
ok_button3 = Button(frame3,text="Delete",width=7,height=1,command=handle_ok_button3)
ok_button3.pack(side=LEFT)

#Frame 4--------------------------------------------------------------------------------------------------------
frame4 = Frame(root)
frame4.grid(row=1,column=1)

ok_button4 = Button(frame4,text="Update",width=13,height=1,command=handle_ok_button4)
ok_button4.pack(side=LEFT)
ok_button5 = Button(frame4,text="Reset",width=13,height=1,command=handle_ok_button5)
ok_button5.pack(side=LEFT)

#Frame 5--------------------------------------------------------------------------------------------------------
frame5 = Frame(root)
frame5.grid(row=0,column=2)

string_entry_var7 = StringVar()
string_entry_var7.set(int(0))
string_entry_value = Entry(frame5,textvariable=string_entry_var7,width=30)
string_entry_value.grid(row=1,column=0,sticky=W)

string_entry_var8 = StringVar()
string_entry_var8.set(int(0))
string_entry_value = Entry(frame5,textvariable=string_entry_var8,width=30)
string_entry_value.grid(row=3,column=0,sticky=W)

string_entry_var9 = StringVar()
string_entry_var9.set(int(0))
string_entry_value = Entry(frame5,textvariable=string_entry_var9,width=30)
string_entry_value.grid(row=5,column=0,sticky=W)

string_entry_var10 = StringVar()
string_entry_var10.set(int(0))
string_entry_value = Entry(frame5,textvariable=string_entry_var10,width=30)
string_entry_value.grid(row=7,column=0,sticky=W)

Label(frame5,text='Name').grid(row=0,column=0,sticky=W)
Label(frame5,text='Capacity').grid(row=2,column=0,sticky=W)
Label(frame5,text='Loadtime').grid(row=4, column=0,sticky=W)
Label(frame5,text='Duration').grid(row=6,column=0,sticky=W)

Label(frame5,text=' ').grid(row=8,column=0,sticky=W)
Label(frame5,text=' ').grid(row=9,column=0,sticky=W)
Label(frame5,text=' ').grid(row=10,column=0,sticky=W)
Label(frame5,text=' ').grid(row=11,column=0,sticky=W)

#Frame 6--------------------------------------------------------------------------------------------------------
frame6 = Frame(root)
frame6.grid(row=1,column=2)

ok_button6 = Button(frame6,text="Clear",width=30,height=1,command=handle_ok_button6)
ok_button6.pack(side=LEFT)

#Menu-----------------------------------------------------------------------------------------------------------
filemenu.add_command(label="Save",command=file_save)
filemenu.add_command(label="Save As...",command=file_saveas)
filemenu.add_command(label="Import",command=file_import)
filemenu.add_command(label="Exit",command=file_exit)
menubar.add_cascade(label="File",menu=filemenu)

controlmenu.add_command(label="Start",command=control_start)
controlmenu.add_command(label="Pause",command=control_pause)
controlmenu.add_command(label="Stop",command=control_stop)
menubar.add_cascade(label="Control",menu=controlmenu)

helpmenu.add_command(label="About...",command=help_about)
menubar.add_cascade(label="Help",menu=helpmenu)

#----------------------------------------------------------------------------------------------------------------
root.config(menu=menubar)
root.validate=ALL
root.mainloop()

vcmd=lambda: vi_int(int(string_entry_var1))
vcmd=lambda: vi_int(int(string_entry_var2))
vcmd=lambda: vi_int(int(string_entry_var3))
vcmd=lambda: vi_int(int(string_entry_var4))
vcmd=lambda: vi_int(int(string_entry_var5))
vcmd=lambda: vi_int(int(string_entry_var6))
vcmd=lambda: vi_int(int(string_entry_var7))
vcmd=lambda: vi_int(int(string_entry_var8))
vcmd=lambda: vi_int(int(string_entry_var9))
vcmd=lambda: vi_int(int(string_entry_var10))
