from tkinter import *

main_page = Tk() 

def color():
    input = input1.get()
    label2["text"] = (f"It is your collar for today - {input}!")
    main_page.configure(bg=input)
    button1.configure(bg=input)
    label1.configure(bg=input)
    label2.configure(bg=input)

def clean():
    label2["text"] = ""

def exit():
    main_page.destroy()

label1 = Label(main_page, text="Input color")
input1 = Entry(main_page)
button1 = Button(main_page, text="Enter", command=color)
input1.bind("<Return>", lambda event: color())
label2 = Label(main_page, text="")

meniu = Menu(main_page)
main_page.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)
meniu.add_cascade(label="Meniu", menu=submeniu)

submeniu.add_command(label="Clean", command = clean)
submeniu.add_separator()
submeniu.add_command(label="Exit", command = exit)

label1.grid(row=0, column=0)
input1.grid(row=0, column=1)
button1.grid(row=0, column=2)
label2.grid(row=1, columnspan=3)
main_page.mainloop()