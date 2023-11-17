import os
from tkinter import Tk, PhotoImage, Label, Frame, StringVar, Entry, Button, Listbox, Scrollbar, LEFT,BOTH,RIGHT,BOTTOM,END,ANCHOR 

root = Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

def AddTask():
    task = task_entry.get()
    task_entry.delete(0, END)
    
    if task:
        with open("To Do List/taskfiles.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert( END, task)
        
def DeleteTask():
    task =str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("To Do List/taskfiles.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
                
        listbox.delete( ANCHOR)

def OpenTaskFile():
    try:
        with open("To Do List/taskfiles.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task.strip():  
                task_list.append(task.strip())
                listbox.insert(END, task.strip())
    except:
        file=open("To Do List/taskfiles.txt", "w")
        file.close
            
# file.close Get the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the image
task_path =os.path.join(script_directory, "picture", "task.png")
topbar_path =os.path.join(script_directory, "picture", "topbar.png")
dock_path =os.path.join(script_directory, "picture", "dock.png")
delete_path =os.path.join(script_directory, "picture", "delete.png")

# Icon
try:
    Image_icon = PhotoImage(file=task_path)
    root.iconphoto(False, Image_icon)
except Exception as e_icon:
    print("Error loading icon image:", e_icon)

# Topbar
try:
    TopImage = PhotoImage(file=topbar_path)
    # Display the image using a Label
    label_top = Label(root, image=TopImage)
    label_top.pack()  # You can use .grid() if you want more control over the positioning
except Exception as e_top:
    print("Error loading topbar image:", e_top)
    
# Dock
try:
    DockImage = PhotoImage(file=dock_path)
    label_dock = Label(root, image=DockImage, bg="#32405b")
    label_dock.place(x=30, y=25)
except Exception as e_dock:
    print ("Eror Loading dock image:", e_dock)
    
# Note
try:
    NoteImage = PhotoImage(file=task_path)
    label_task = Label(root, image=NoteImage, bg="#32405b")
    label_task.place(x=340, y=25)
except Exception as e_task:
    print ("Eror Loading task image:", e_task)

# Delete
try:
    DeleteImage = PhotoImage(file=delete_path)
    Button(root,image=DeleteImage,bd=0,command=DeleteTask).pack(side=BOTTOM, pady=13)
except Exception as e_delete:
    print ("Eror Loading delete image:", e_delete)

heading=Label(root,text="ALL TASK", font="arial 20 bold", fg="white",bg="#32405b")
heading.place(x=130,y=20)

# Main
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry = Entry(frame, width=18,font="arial 20", bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=AddTask)
button.place(x=300, y=0)
button.bind('<Return>', lambda event=None: AddTask())

# List Box
frame1= Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(160,0))

listbox= Listbox(frame1,font=('arial',12),width=40,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

OpenTaskFile()

root.mainloop()