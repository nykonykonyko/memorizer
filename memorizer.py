from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
screen = Tk()
screen.geometry("600x800")
screen.title("Memorizer")
def add_item():
    item = e.get().strip()
    if item:
        listbox.insert(0, item)
        e.delete(0, END)
    else:
        showwarning("Input Error", "Please enter a valid item.")        

def delete_item():
    i = listbox.curselection()
    if i:
        listbox.delete(i)
    else:
        showwarning("Selection Error", "Please select an item to delete.")

Button(screen,text="Open File",command=None).pack(pady=10,side=LEFT,padx=10)
Button(screen,text="Delete",command=delete_item).pack(pady=10,side=RIGHT,padx=10)
Button(screen,text="Save File",command=None).pack(pady=10,padx=10)

e = Entry(screen,font="Arial 15 bold")
e.pack(pady=10,padx=10)
Button(screen,text="Add",command=add_item).pack(pady=10,padx=10)

frame = Frame(screen)
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT,fill=Y)
listbox = Listbox(frame,font="Arial 15 bold",yscrollcommand=scrollbar.set,bg="lightgreen",selectbackground="green",selectforeground="white")
for i in range(10):
    listbox.insert(END,f"Item {i+1}")
listbox.pack(side=LEFT,fill=BOTH,expand=True)
scrollbar.config(command=listbox.yview)
frame.pack(pady=10,padx=10,fill=BOTH,expand=True)

screen.mainloop()
