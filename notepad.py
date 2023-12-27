from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

window = Tk()
window.geometry("1280x720") 
window['background'] = '#142345'

icon = PhotoImage(file= 'headphone.png')
window.iconphoto(True, icon)
title = window.title("To-Do List")
window.title()

#Button Functions
def delete():
    listbox.delete(listbox.curselection())

def excite():
    exit()

def clear():
    listbox.delete(0, END)

def submissions():
    entrycontent = entry.get()
    if entrycontent == '' or entrycontent == ' ':
        messagebox.showerror(title= 'Empty Space', message= "You can't enter an empty entry")
    else:    
        listbox.insert(listbox.size(), entry.get())
        entry.delete(0, END)

def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Text File", ".txt"), ("HTML File", ".html"), ("All Files", ".*")])
    filetext = str(listbox.get(0, END))
    file.write(filetext)
    file.close()

#Keybind Functions
def enterer(event):
    entrycontent = entry.get()
    if entrycontent == '' or entrycontent == ' ':
        messagebox.showerror(title= 'Empty Space', message= "You can't enter an empty entry")
    else:    
        listbox.insert(listbox.size(), entry.get())
        entry.delete(0, END)

def deleter(event):
    listbox.delete(listbox.curselection())


def clearer(event):
    listbox.delete(0, END)

#Keybinds
window.bind("<BackSpace>", deleter)
window.bind("<Return>", enterer)
window.bind("<Escape>", clearer)

#Menu Bar
menubar = Menu(window, bg='#617fc2')
window.config(menu=menubar)
fileMenu = Menu(menubar, tearoff=0, bg='#617fc2')
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Exit", command= excite)

#Label
todo_name = Label(window, text="To-Do List", font=("Calibri", 25), bg = '#617fc2')
todo_name.pack(side=TOP)

#Listbox
listbox = Listbox(window, bg="#617fc2", font=("Constantia", 25), width= 40 )
listbox.pack()

#Bottom Frame
frame = Frame(window)
frame.pack(side=BOTTOM)

#Entry and Buttons
entry = Entry(frame, font=("consolas", 25), bg = '#617fc2', width=30, bd=0)
entry.pack(side=LEFT)
clear_button = Button(frame, text='Clear', font=("consolas", 15), bg = '#617fc2', command=clear, width= 7, borderwidth=2)
clear_button.pack(side=RIGHT)
delete_button = Button(frame, text='Delete', font=("consolas", 15), bg = '#617fc2', command=delete, width= 7, borderwidth=2)
delete_button.pack(side=RIGHT)
submit = Button(frame, text='Enter', font=("consolas", 15), bg = '#617fc2', command=submissions, width= 7, borderwidth=2)
submit.pack(side=RIGHT)

#instruction
instruction_frame = Frame(window, bg='#879fd4', )
instruction_frame.place(x=10, y=400)
clear_instruct = Label(instruction_frame, text='Press Esc or clear to clear the listbox', font=("Times New Roman", 10), bg='#879fd4' )
clear_instruct.pack()
enter_instruct = Label(instruction_frame, text='Press Enter or the Enter button to submit the entry', font=("Times New Roman", 10), bg='#879fd4' )
enter_instruct.pack()
delete_instruct = Label(instruction_frame, text='Press backspace or the Delete button to Delete the currently selected', font=("Times New Roman", 10), bg='#879fd4' )
delete_instruct.pack()

listbox.config(height=listbox.size())


window.mainloop()
