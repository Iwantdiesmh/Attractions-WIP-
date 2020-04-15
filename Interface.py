from tkinter import *
from Attributes import Attraction
import Pmw

def vi_int(int_var):
    try:
        int(int_var.get())
        return True
    except ValueError:
        return False
    
#Buttons[create]-------------------------------------------------------------------------------------------------
def button_create():
    ride = Attraction(0,0,0,'~~~') #put something in the params
    update_frame5(ride)

#edit-------------------------------------------------------
def button_edit():
    sels = box.getcurselection()
    selection = sels[0]
    ride = determineRide(selection)
    update_frame5(ride)

def update_frame5(ride):
    string_entry_name.set(ride.name)
    string_entry_capacity.set(ride.capacity)
    string_entry_loadtime.set(ride.loadtime)
    string_entry_duration.set(ride.duration)
    frame5.tkraise()

#delete----------------------------------------------------
def button_delete():
    pass

#update----------------------------------------------------
def button_update():
    pass

#reset------------------------------------------------------
def button_reset():
    pass

#menu[file]-------------------------------------------------------------------------------------------------------
def file_save():
    pass

def file_saveas():
    pass

def file_import():
    pass

def file_exit():
    pass

#control----------------------------------------------------
def control_start():
    pass

def control_pause():
    pass

def control_stop():
    pass

#help-------------------------------------------------------
def help_about():
    pass

#finding rides----------------------------------------------------------------------------------------------------
def selectionCommand():
    """Callback when an item is selected"""
    sels = box.getcurselection()
    selection = sels[0]
    ride = determineRide(selection)
    print(ride.name)
    #TODO: check for incomplete edit
    frame2.tkraise()
    int_entry_line.set(ride.line)
    #int_entry_state.set(ride.state)
    int_entry_in_load.set(ride.in_load)
    int_entry_in_action.set(ride.in_action)
    int_entry_max.set(ride.maxLine)
    
def determineRide(selection):
    for ride in rides:
        if selection == ride.name:
            return ride
            
    raise RuntimeError('%s not found' %selection)

#displaying rides-------------------------------------------------------------------------------------------------
rides = []

def create_the_rides():
    '''creates the ride (hardcoded currently) by calling create_the_ride and putting in the parameters'''
    create_the_ride(loadtime=2,duration=5,capacity=12,name="Rollercoaster") #1
    create_the_ride(loadtime=2,duration=5,capacity=25,name="Rollercoaster number 2") #2
    create_the_ride(loadtime=1,duration=5,capacity=30,name="Carousel") #3
    create_the_ride(loadtime=15,duration=10,capacity=60,name="Peter the Pan") #4
    create_the_ride(loadtime=1,duration=2,capacity=10,name="Drop Tower") #5
    create_the_ride(loadtime=1,duration=1,capacity=1,name="Bizza Hut") #6
    create_the_ride(loadtime=3,duration=55,capacity=40,name="Gravity Swing") #7
    create_the_ride(loadtime=1,duration=3,capacity=4,name="Buzz Light Second") #8
    create_the_ride(loadtime=5,duration=6,capacity=20,name="Smaller Than Average Mermaid") #9
    create_the_ride(loadtime=1,duration=1,capacity=1,name="Hot Dogs") #10


def create_the_ride(loadtime, duration, capacity, name):
    '''checks if any of the values equal zero (because it wont work then) and adds it to the 'rides' list'''
    if loadtime==0 or duration==0 or capacity==0: #need to check for name. Dont know to do it
        raise Exception('no 0 values for input')

    ride = Attraction(loadtime, duration, capacity, name)
    rides.append(ride)

#stuff------------------------------------------------------------------------------------------------------------
create_the_rides()
root = Tk()
root.title("Ride Page")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
controlmenu = Menu(menubar, tearoff=0)
helpmenu = Menu(menubar, tearoff=0)

#Frame 1---------------------------------------------------------------------------------------------------------
frame1 = Frame(root,highlightcolor="black", highlightthickness=1)
frame1.grid(row=0,column=0)

# Create the ScrolledListBox.
selection = None
box = Pmw.ScrolledListBox(frame1,items=rides,labelpos="nw",
            label_text="Rides",listbox_height = 6,
            selectioncommand=selectionCommand,usehullsize = 1,
            hull_width = 200,hull_height = 250)

box.pack(fill = "both", expand = 1, padx = 5, pady = 5)

#Frame 2--------------------------------------------------------------------------------------------------------
frame2 = Frame(root)
frame2.grid(row=0,column=1,sticky='NSEW')

Label(frame2,text='People in Line').grid(row=0,column=0,sticky=W)
int_entry_line = IntVar()
Label(frame2,textvariable=int_entry_line).grid(row=1,column=0,sticky=W)

Label(frame2,text='State of Ride').grid(row=2,column=0,sticky=W)
int_entry_state = IntVar()
Label(frame2,textvariable=int_entry_state).grid(row=3,column=0,sticky=W)

Label(frame2,text='People Getting on the Ride').grid(row=4, column=0,sticky=W)
int_entry_in_load = IntVar()
Label(frame2,textvariable=int_entry_in_load).grid(row=5,column=0,sticky=W)

Label(frame2,text='People on the Ride').grid(row=6,column=0,sticky=W)
int_entry_in_action = IntVar()
Label(frame2,textvariable=int_entry_in_action).grid(row=7,column=0,sticky=W)

Label(frame2,text='Most People in Line').grid(row=8,column=0,sticky=W)
int_entry_max = IntVar()
Label(frame2,textvariable=int_entry_max).grid(row=9,column=0,sticky=W)

#Frame 3--------------------------------------------------------------------------------------------------------
frame3 = Frame(root)
frame3.grid(row=1,column=0)
ok_button1 = Button(frame3,text="Create",width=9,height=1,command=button_create)
ok_button1.pack(side=LEFT)
ok_button2 = Button(frame3,text="Edit",width=9,height=1,command=button_edit)
ok_button2.pack(side=LEFT)
ok_button3 = Button(frame3,text="Delete",width=9,height=1,command=button_delete)
ok_button3.pack(side=LEFT)

#Frame 4--------------------------------------------------------------------------------------------------------
frame4 = Frame(root)
frame4.grid(row=1,column=1)

ok_button4 = Button(frame4,text="Update",width=13,height=1,command=button_update)
ok_button4.pack(side=LEFT)
ok_button5 = Button(frame4,text="Reset",width=13,height=1,command=button_reset)
ok_button5.pack(side=LEFT)

#Frame 5--------------------------------------------------------------------------------------------------------
frame5 = Frame(root)
frame5.grid(row=0,column=1,sticky='NSEW')

string_entry_name = StringVar()
string_entry_value = Entry(frame5,textvariable=string_entry_name,width=30)
string_entry_value.grid(row=1,column=0,sticky=W)

string_entry_capacity = StringVar()
string_entry_value = Entry(frame5,textvariable=string_entry_capacity,width=30)
string_entry_value.grid(row=3,column=0,sticky=W)

string_entry_loadtime = StringVar()
string_entry_value = Entry(frame5,textvariable=string_entry_loadtime,width=30)
string_entry_value.grid(row=5,column=0,sticky=W)

string_entry_duration = StringVar()
string_entry_value = Entry(frame5,textvariable=string_entry_duration,width=30)
string_entry_value.grid(row=7,column=0,sticky=W)

Label(frame5,text='Name').grid(row=0,column=0,sticky=W)
Label(frame5,text='Capacity').grid(row=2,column=0,sticky=W)
Label(frame5,text='Loadtime').grid(row=4, column=0,sticky=W)
Label(frame5,text='Duration').grid(row=6,column=0,sticky=W)

Label(frame5,text=' ').grid(row=8,column=0,sticky=W)
Label(frame5,text=' ').grid(row=9,column=0,sticky=W)
Label(frame5,text=' ').grid(row=10,column=0,sticky=W)
Label(frame5,text=' ').grid(row=11,column=0,sticky=W)

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
frame2.tkraise()
root.mainloop()
