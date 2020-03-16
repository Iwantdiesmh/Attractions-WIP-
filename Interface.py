from tkinter import *

def vi_int(int_var):
    try:
        int(int_var.get())
        return True
    except ValueError:
        return False

def handle_ok_button1():
    """ok button handler"""
    okButton1()

def okButton1(): #fix
    print("well it works for now")
    pass

def handle_ok_button2():
    """ok button handler"""
    okButton2()

def okButton2(): #fix
    print("well it doesn't work for now")
    pass

def handle_ok_button3():
    """ok button handler"""
    okButton3()

def okButton3(): #fix
    print("this dont work")
    pass #crash the program?

def handle_ok_button4():
    """ok button handler"""
    okButton4()

def okButton4(): #fix
    print("this dont work")
    pass #crash the program?

def handle_ok_button5():
    """ok button handler"""
    okButton5()

def okButton5(): #fix
    print("this dont work")
    pass #crash the program?

root = Tk()
root.title("Ride Page")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
#frame1.geometry('1080x720')

#Frame 1---------------------------------------------------------------------------------------------------------
frame1 = Frame(root)
frame1.grid(row=0,column=0)

Label(frame1,text="Rides").grid(row=0,column=0,sticky="N") #copy and paste for lame use

#Frame 2--------------------------------------------------------------------------------------------------------
frame2 = Frame(root) #I need to figure out how to give them variable -> also this is bugged
frame2.grid(row=0,column=1)

string_entry_var1 = StringVar()
string_entry_var1.set(int(0))
string_entry_value = Entry(frame2,textvariable=string_entry_var1)
string_entry_value.grid(row=1,column=0,sticky=W)

string_entry_var2 = StringVar()
string_entry_var2.set(int(0))
string_entry_value = Entry(frame2,textvariable=string_entry_var2)
string_entry_value.grid(row=4,column=0,sticky=W)

string_entry_var3 = StringVar()
string_entry_var3.set(int(0))
string_entry_value = Entry(frame2,textvariable=string_entry_var3)
string_entry_value.grid(row=7,column=0,sticky=W)

string_entry_var4 = StringVar()
string_entry_var4.set(int(0))
string_entry_value = Entry(frame2,textvariable=string_entry_var4)
string_entry_value.grid(row=10,column=0,sticky=W)

string_entry_var5 = StringVar()
string_entry_var5.set(int(0))
string_entry_value = Entry(frame2,textvariable=string_entry_var5)
string_entry_value.grid(row=13,column=0,sticky=W)

Label(frame2,text='Number Of People on the Ride').grid(row=0,column=0,sticky=W)
Label(frame2,text='State of Ride').grid(row=3, column=0,sticky=W)
Label(frame2,text='People Getting on the Ride').grid(row=6,column=0,sticky=W)
Label(frame2,text='People on the Ride').grid(row=9,column=0,sticky=W)
Label(frame2,text='Most People in line').grid(row=12,column=0,sticky=W)

#Frame 3--------------------------------------------------------------------------------------------------------
frame3 = Frame(root)
frame3.grid(row=1,column=0)
ok_button1 = Button(frame3,text="Create",width=10,height=1,command=handle_ok_button1)
ok_button1.pack(side=LEFT)
ok_button2 = Button(frame3,text="Edit",width=10,height=1,command=handle_ok_button2)
ok_button2.pack(side=LEFT)
ok_button3 = Button(frame3,text="Delete",width=10,height=1,command=handle_ok_button3)
ok_button3.pack(side=LEFT)

#Frame 4--------------------------------------------------------------------------------------------------------
frame4 = Frame(root)
frame4.grid(row=1,column=1)

ok_button4 = Button(frame4,text="Update",width=15,height=1,command=handle_ok_button4)
ok_button4.pack(side=LEFT)
ok_button5 = Button(frame4,text="Reset",width=15,height=1,command=handle_ok_button5)
ok_button5.pack(side=LEFT)

#Menu-----------------------------------------------------------------------------------------------------------
filemenu.add_command(label="Save",command=menu_save)
filemenu.add_command(label="Save As",command=menu_save)
filemenu.add_command(label="Import",command=menu_save
filemenu.add_command(label="Exit",command=menu_save)

#----------------------------------------------------------------------------------------------------------------
root.validate=ALL
vcmd=lambda: vi_int(int(string_entry_var1))
vcmd=lambda: vi_int(int(string_entry_var2))
vcmd=lambda: vi_int(int(string_entry_var3))
vcmd=lambda: vi_int(int(string_entry_var4))
vcmd=lambda: vi_int(int(string_entry_var5))
