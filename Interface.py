from tkinter import *
from tkinter import filedialog
from Attributes import Attraction
import Pmw
import pickle
import sys
running = False
time_passed = 0
globalride = None
updated = False
new = False
ride_variables_saved = True
update_stats_ride = None
importfile = None
save_changes = True #true whenever you successfully changed the data
edit_page = False


def vi_int(int_var):
    try:
        int(int_var.get())
        return True
    except ValueError:
        return False

#Turn off the #@($*#)$#@ rides please---------------------------------------------------------------------
def turn_off_rides():
    dialog = Pmw.MessageDialog(title="Amusement Park-ish",buttons=("Ok",),message_text="Please turn off the rides")
    
#Buttons[create]------------------------------------------------------------------------------------------------
def button_create():
    global new
    global baypass
    new = True
    ride_variables_saved = False
    save_changes = False

    global globalride
    if running == False:
        globalride = Attraction(1,1,1,'None') #put something in the params
        update_frame5(globalride)

    else:
        turn_off_rides()

#edit-------------------------------------------------------
def button_edit():
    global new
    global ride_variables_saved
    global edit_page
    new = False
    save_changes = False
    edit_page = True
    
    global running
    if running == False:
        sels = box.getcurselection()
        if len(sels) == 0:
             dialog = Pmw.MessageDialog(title="Amusement Park-ish",buttons=("Ok",),message_text="Please select a ride")

        else:
            selection = sels[0]
            ride = determineRide(selection)
            update_frame5(ride)
            ride_variables_saved = False

    else:
        turn_off_rides()

def update_frame5(ride):
    global globalride
    globalride = ride
    string_entry_name.set(str(ride.name))
    string_entry_capacity.set(int(ride.capacity))
    string_entry_loadtime.set(int(ride.loadtime))
    string_entry_duration.set(int(ride.duration))
    frame5.tkraise()

#delete----------------------------------------------------
def button_delete():
    global running
    save_changes = False
    if running == False:
        sels = box.getcurselection()
        if len(sels) == 0:
             dialog = Pmw.MessageDialog(title="Amusement Park-ish",buttons=("Ok",),message_text="Please select a ride")

        else:
            selection = sels[0]
            selected_ride = determineRide(selection)
            print(ride_variables_saved, selected_ride, globalride)
            if ride_variables_saved == False and selected_ride == globalride:
                dialog = Pmw.MessageDialog(title="Amusement Park-ish",buttons=("Ok",),message_text="Deleting without saving update")

            else:
                for (i, ride) in enumerate(rides):
                    if selected_ride == ride:
                        del rides[i]
                        update_rides()
                        break

    else:
        turn_off_rides()

#update----------------------------------------------------
def button_update():
    global updated
    global new
    global ride_variables_saved
    global edit_page
    save_changes = True
    ride_entry_name = string_entry_name.get()
    negative_number = False
    
    if edit_page == True:
        for ride in rides:
            if ride == globalride:
                continue

            if ride.name == ride_entry_name:
                dialog = Pmw.MessageDialog(title="Amusement Park-ish",buttons=("ok",),
                    message_text="ridename [%s] already exists" % ride_entry_name)
                return False

        if int(string_entry_capacity.get()) <= 0:
            dialog = Pmw.MessageDialog(title="Amusement Park-ish",buttons=("ok",),
                message_text="don't put in a zero or negative number")
            negative_number = True
            return False

        if int(string_entry_loadtime.get()) <= 0:
            dialog = Pmw.MessageDialog(title="Amusement Park-ish",buttons=("ok",),
                message_text="don't put in a zero or negative number")
            negative_number = True
            return False

        if int(string_entry_duration.get()) <= 0:
            dialog = Pmw.MessageDialog(title="Amusement Park-ish",buttons=("ok",),
                message_text="don't put in a zero or negative number")
            negative_number = True
            return False

        try:
            globalride.name = str(string_entry_name.get())
            globalride.capacity = int(string_entry_capacity.get())
            globalride.loadtime = int(string_entry_loadtime.get())
            globalride.duration = int(string_entry_duration.get())

        except TclError as error:
            dialog = Pmw.MessageDialog(title="Amusement Park-ish",buttons=("ok",),
                message_text=str(error))
            negative_number = True
            return False

        updated = True
        if new == True:
            rides.append(globalride)
            new = False

        if negative_number == False:
            update_rides()
            ride_variables_saved = True

        edit_page = False
        return True

        
    else:
            dialog = Pmw.MessageDialog(title="Amusement Park-ish",buttons=("ok",),
                message_text=str("Please hit the edit button first"))
            
#reset------------------------------------------------------
def button_reset():
    global ride_variables_saved
    update_frame5(globalride)
    ride_variables_saved = True
    save_changes = True

#menu[file]-------------------------------------------------------------------------------------------------------
def file_save():
    button_update()
    
    if running:
        turn_off_rides()

    else:    
        if not importfile:
            file_saveas()
            return
        
    with open(importfile, "wb") as picklefile:
        pickle.dump(rides, picklefile)
        pickle.dump(rides, picklefile)

def file_saveas():
    if check_before_continuing():
        if running:
            turn_off_rides()

        else:
            filename = filedialog.asksaveasfilename(
                    initialdir ="/",
                    title = "h.",
                    filetypes = (("rides","*.pickle"),("all files","*.*")))

            if filename == "":
                return

            if "." not in filename:
                filename += ".pickle"

            global importfile
            importfile = filename
            file_save()

def file_load():
    global rides
    global time_passed
    global importfile
    
    print("fileload")
    
    filename = filedialog.askopenfilename(
            initialdir ="/",
            title = "h.",
            filetypes = (("rides","*.pickle"),("all files","*.*")))

    if filename == "":
        return
        
    try:
        with open(filename, "rb") as picklefile:
            rides = pickle.load(picklefile)
            time_passed = pickle.load(picklefile)
            print(time_passed)
            update_rides()

    except:
        dialog = Pmw.MessageDialog(title="Amusement Park-ish",buttons=("ok",),
            message_text="invalid file")

    importfile = filename

def file_exit():
    if check_before_exiting():
        # save the data
        #  TODO:  Exit the program instdad of sys.exit()
        root.destroy()
        sys.exit()

#control----------------------------------------------------
def control_start():
    global running
    running = True
    run_all_rides()

def control_stop():
    global running
    running = False

#help-------------------------------------------------------
def help_about():
    dialog = Pmw.MessageDialog(title="About Page",buttons=("Close",),message_text='''By: Angus Chen
A professional coder who understands about as much as
the random kid on the block

Amusement Park is simple code made to simulate an actual
park in basically no areas whatsoever
''')

#find state--------------------------------------------------------------------------------------------------------
def find_state(ride):
    if ride.loading:
        return str('Loading')

    elif ride.running:
        return str('Running')

    else:
        return str('Off')

#update----------------------------------------------------------------------------------------------------------
def update_message():
    message = str('Running = %s | Minutes Passed = %s' %(running, time_passed))
    string_entry_status.set(message)

def update_statistics(ride):
    global update_stats_ride
    update_stats_ride = ride
    int_entry_line.set(ride.line)
    string_entry_state.set(find_state(ride))
    int_entry_in_load.set(ride.in_load)
    int_entry_in_action.set(ride.in_action)
    int_entry_max.set(ride.maxLine)
    root.after(1000, auto_update)

def auto_update():
    update_statistics(update_stats_ride)
    
#running rides----------------------------------------------------------------------------------------------------
def run_the_ride(ride):
    ride.put_someone_in_line()
    ride.step()

#run_all_rides------------------------------------------------
def run_all_rides():
    '''calls run_the_ride for every value in the list then sleeps for a in-game minute'''
    global time_passed
    if not running:
        update_message()
        return

    for ride in rides:
        run_the_ride(ride)
        update_message()

    time_passed += 1
    root.after(1000, run_all_rides)

#yes/no/cancel----------------------------------------------------------------------------------------------------
def check_before_continuing():
    global ride_variables_saved
    if ride_variables_saved or identical_ride_variables():
        return True

    dialog = Pmw.MessageDialog(title="Amusement Park-ish",buttons=("Yes","No","Cancel"),
        message_text="Do you want to save the updated data before continuing?")

    answer1 = dialog.activate()

    if answer1 == "Yes":
        if not button_update():
            return False
        
        ride_variables_saved = True
        dialog.deactivate()
        return True

    if answer1 == "No":
        ride_variables_saved = True
        dialog.deactivate()
        return False

#check_before_continuing but its for exit button------------------------
def check_before_exiting():
    """Returns True if OK to exit; False otherwise"""
    #  TODO:  Make the above actually be correct
    global ride_variables_saved
    if ride_variables_saved or identical_ride_variables():
        return True

    dialog = Pmw.MessageDialog(title="Amusement Park-ish",buttons=("Yes","No","Cancel"),
        message_text="Do you want to save the updated data before exiting?")

    answer = dialog.activate()

    if answer == "Yes":
        #  TODO:  Save the data and return True
        button_update()
        file_save()
        dialog.deactivate()
        return True

    if answer == "No":
        #  TODO:  Only destroy in file_exit; return True
        dialog.deactivate()
        return True

    if answer == "Cancel":
        return False

        #   TODO:  If answer == "Cancel" return False 

    #  TODO:  Call deactivate before each of the return's above   

#verify_if_string_is_changed-------------------------------------------
def identical_ride_variables():
    if string_entry_name.get() == globalride.name:
        try:
            if string_entry_capacity.get() == globalride.capacity:
                if string_entry_loadtime.get() == globalride.loadtime:
                    if string_entry_duration.get() == globalride.duration:
                        return True

        except TclError as error:
            dialog = Pmw.MessageDialog(title="Amusement Park-ish",buttons=("ok",),
                message_text=str(error))

    return False

#finding rides----------------------------------------------------------------------------------------------------
def switch_to_different_ride():
    """Callback when an item is selected"""
    if check_before_continuing():
        sels = box.getcurselection()
        if len(sels) == 1:
            selection = sels[0]
            ride = determineRide(selection)
            frame2.tkraise()
            update_statistics(ride)

def determineRide(selection):
    for ride in rides:
        if selection == ride.name:
            return ride

    raise RuntimeError('%s not found' %selection)

#finding rides----------------------------------------------------------------------------------------------------
def update_rides():
    box.setlist(rides)

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
root.protocol("WM_DELETE_WINDOW", file_exit)
root.title("Amusement Park-ish")
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
            selectioncommand=switch_to_different_ride,usehullsize = 1,
            hull_width = 200,hull_height = 250)

box.pack(fill="both", expand=1, padx=5, pady=5)

#Frame 2--------------------------------------------------------------------------------------------------------
frame2 = Frame(root)
frame2.grid(row=0,column=1,sticky='NSEW')

Label(frame2,text='People in Line').grid(row=0,column=0,sticky=W)
int_entry_line = IntVar()
Label(frame2,textvariable=int_entry_line).grid(row=1,column=0,sticky=W)

Label(frame2,text='State of Ride').grid(row=2,column=0,sticky=W)
string_entry_state = StringVar()
Label(frame2,textvariable=string_entry_state).grid(row=3,column=0,sticky=W)

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
frame3.grid(row=2,column=0)
ok_button1 = Button(frame3,text="Create",width=9,height=1,command=button_create)
ok_button1.pack(side=LEFT)
ok_button2 = Button(frame3,text="Edit",width=9,height=1,command=button_edit)
ok_button2.pack(side=LEFT)
ok_button3 = Button(frame3,text="Delete",width=9,height=1,command=button_delete)
ok_button3.pack(side=LEFT)

#Frame 4--------------------------------------------------------------------------------------------------------
frame4 = Frame(root)
frame4.grid(row=2,column=1)

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

string_entry_capacity = IntVar()
string_entry_value = Entry(frame5,textvariable=string_entry_capacity,width=30)
string_entry_value.grid(row=3,column=0,sticky=W)

string_entry_loadtime = IntVar()
string_entry_value = Entry(frame5,textvariable=string_entry_loadtime,width=30)
string_entry_value.grid(row=5,column=0,sticky=W)

string_entry_duration = IntVar()
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

#Frame Middle-----------------------------------------------------------------------------------------------------------
frame_middle = Frame(root)
frame_middle.grid(row=1,column=0,sticky='NSEW')

string_entry_status = StringVar()
Label(frame_middle,textvariable=string_entry_status).grid(row=0,column=0,sticky=W)

#Menu-----------------------------------------------------------------------------------------------------------
filemenu.add_command(label="Open...",command=file_load)
filemenu.add_command(label="Save",command=file_save)
filemenu.add_command(label="Save As...",command=file_saveas)
filemenu.add_command(label="Exit",command=file_exit)
menubar.add_cascade(label="File",menu=filemenu)

controlmenu.add_command(label="Start",command=control_start)
controlmenu.add_command(label="Stop",command=control_stop)
menubar.add_cascade(label="Control",menu=controlmenu)

helpmenu.add_command(label="About...",command=help_about)
menubar.add_cascade(label="Help",menu=helpmenu)

#----------------------------------------------------------------------------------------------------------------
root.config(menu=menubar)
root.validate=ALL
frame2.tkraise()
root.mainloop()
