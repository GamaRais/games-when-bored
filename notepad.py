from tkinter import *
from tkinter import filedialog

window = Tk()
window.geometry("400x900") 
window['background'] = '#142345'

icon = PhotoImage(file= 'headphone.png')
window.iconphoto(True, icon)

def excite():
    exit()

def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Text File", ".txt"), ("HTML File", ".html"), ("All Files", ".*")])
    filetext = str(listbox.get(0, END))
    file.write(filetext)
    file.close()

def deleter(event):
    listbox.delete(listbox.curselection())

def delete():
    listbox.delete(listbox.curselection())

window.bind("<Return>", deleter)

def submissions():
    listbox.insert(listbox.size(), entry.get())

menubar = Menu(window)
window.config(menu=menubar)
menubar['background'] = '#142345'

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Exit", command= excite)

todo_name = Label(window, text="To-Do List", font=("Calibri", 25), bg = '#617fc2')
todo_name.pack(side=TOP)

listbox = Listbox(window, bg="#617fc2", font=("Constantia", 35), width= 30 )
listbox.pack()

frame = Frame(window)
frame.pack(side=BOTTOM)

title = window.title("To-Do List")
window.title()
entry = Entry(frame, font=("consolas", 25), bg = '#617fc2', width=30)
entry.pack(side=LEFT)
delete_button = Button(frame, text='Delete', font=("consolas", 15), bg = '#617fc2', command=delete, width= 7)
delete_button.pack(side=RIGHT)
submit = Button(frame, text='Enter', font=("consolas", 15), bg = '#617fc2', command=submissions, width= 5)
submit.pack(side=RIGHT)


listbox.config(height=listbox.size())


window.mainloop()