# from tkinter import *

# langas = Tk()

# uzrasas1 = Label(langas, text="Vardas")
# laukas1 = Entry(langas)
# uzrasas2 = Label(langas, text="Pavardė")
# laukas2 = Entry(langas)
# varnele = Checkbutton(langas, text="Pažymėk varnelę")

# uzrasas1.grid(row=0, column=0, sticky=E)
# laukas1.grid(row=0, column=1)
# uzrasas2.grid(row=1, column=0, sticky=E)
# laukas2.grid(row=1, column=1)
# varnele.grid(row=2, columnspan=2)

# langas.mainloop()

# from tkinter import *
# langas = Tk()

# def spausdinti():
#     print("Spausdina!")

# mygtukas = Button(langas, text="Spausdinti", command=spausdinti)
# mygtukas.pack()
# langas.mainloop()

# from tkinter import *
# langas = Tk()

# def spausdinti(event):
#     print("Paspaustas kairys pelės mygtukas!")

# def spausdinti2(event):
#     print("Paspaustas dešinys pelės mygtukas!")

# def spausdinti3(event):
#     print("Paspaustas ENTER!")

# mygtukas = Button(langas, text="Spausdinti")
# mygtukas.bind("<Button-1>", spausdinti)
# mygtukas.bind("<Button-3>", spausdinti2)
# langas.bind("<Return>", spausdinti3)
# mygtukas.pack()

# langas.mainloop()

# # Paspaustas kairys pelės mygtukas!
# # Paspaustas dešinys pelės mygtukas!
# # Paspaustas ENTER!

# from tkinter import *

# langas = Tk()

# def spausdinti():
#     ivesta = laukas1.get()
#     rezultatas["text"] = ivesta

# uzrasas1 = Label(langas, text="Įrašykite žodį")
# laukas1 = Entry(langas)
# mygtukas = Button(langas, text="Įvesti", command=spausdinti)
# rezultatas = Label(langas, text="")

# uzrasas1.grid(row=0, column=0)
# laukas1.grid(row=0, column=1)
# mygtukas.grid(row=0, column=2)
# rezultatas.grid(row=1, columnspan=3)

# langas.mainloop()

# from tkinter import *
# langas = Tk()

# meniu = Menu(langas)
# langas.config(menu=meniu)
# submeniu = Menu(meniu, tearoff = 0)

# meniu.add_cascade(label="Meniu", menu=submeniu)
# submeniu.add_command(label="Pirmas")
# submeniu.add_command(label="Antras")
# langas.mainloop()

# from tkinter import *

# root = Tk()
# var = StringVar()
# label = Label( root, textvariable=var, relief=RAISED )

# var.set("Hey!? How are you doing?")
# label.pack()
# root.mainloop()

# from tkinter import *   
# gui = Tk()  
# gui.geometry('200x200')  
# gui.configure(bg='alice blue') 
  
# gui.mainloop()

# from tkinter import *   
# gui = Tk()  
# gui.geometry('200x200')  
# #set the window color
# gui.configure(bg='yellow') 
  
# gui.mainloop()

from tkinter import *   
gui = Tk()  
gui.geometry('200x200')  
#set the window color
gui['bg']='green3'
  
gui.mainloop()

b1 = tk.Button(my_w, text='Hi  Welcome', 
   width=20,bg='yellow',font=my_font,fg='green', bg='AntiqueWhite2')
