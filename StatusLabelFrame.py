from Tkinter import *

master = Tk()
group = LabelFrame(master, text="Firewall Status",padx=5, pady=5)
group.pack(padx=10,pady=10)

w = Entry(group)
w.pack()

mainloop()

