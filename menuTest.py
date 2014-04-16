from Tkinter import Tk, Frame, Menu
import tkMessageBox
from Tkinter import *
import pf
import Tkinter as tk


class MainGUI(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.master = master 
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.initUI()
        optionList = tk.Listbox(self)
        #optionList.grid(sticky=tk.N+tk.S)
        #optionList.pack(side=LEFT, fill=Y)
        optionList.insert("end","Firewall Status")
        optionList.insert("end","Port Forwarding")
        optionList.insert("end","Custom Rules")
        #optionList.config(selectmode=EXTENDED)
        optionList.bind("<Double-Button-1>>", self.OnDouble)
        optionList.pack(side=LEFT, fill=Y,expand=True)
        self.centerWindow()
    def initUI(self):
        self.master.title("Firewall Configuration")
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        
	fileMenu = Menu(menubar)
        fileMenu.add_command(label="Apply")
        fileMenu.add_command(label="Reload")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)

        optionsMenu = Menu(menubar)
        optionsMenu.add_command(label="Start Configuration Wizard",state=DISABLED)
        optionsMenu.add_separator()
        optionsMenu.add_command(label="Enable Firewall", command=self.onEnable,state=DISABLED)
        optionsMenu.add_command(label="Disable Firewall", command=self.onDisable)
        menubar.add_cascade(label="Options", menu=optionsMenu)

        helpMenu = Menu(menubar)
        helpMenu.add_command(label="About", command=self.onAbout)
        menubar.add_cascade(label="Help", menu=helpMenu)

        #optionList = Listbox(self.master,name='optionList')
        #optionList.grid(sticky=tk.N+tk.S)
        #optionList.pack(side=LEFT, fill=Y)
        #optionList.insert("end","Firewall Status")
        #optionList.insert("end","Port Forwarding")
        #optionList.insert("end","Custom Rules")
        #optionList.config(selectmode=EXTENDED)
        #optionList.bind("<Double-Button-1>>", self.OnDouble)
        #optionList.pack(side=LEFT, fill=Y)
    
    def OnDouble(self, event):
        widget = event.widget
        selection = wodget.curselection()
        value = widget.get(selection[0])
        tkMessageBox.showinfo("Test","Test")  
        print "selection:", selection, ": '%s'" % value 
    def getSelectedItem(self):
        return self.curselection() 
    def onEnable(self):
        tkMessageBox.showinfo("Enable","Firewall")
    def onDisable(self):
        
        tkMessageBox.showinfo("Disable","Disable")
    def onExit(self):
        self.quit()
    def onAbout(self):
        tkMessageBox.showinfo("Firewall","OpenBSD Firewall Configuration")
    def centerWindow(self):
        w = 490
        h = 450
        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()
        x = (sw-w)/2
        y = (sh - h)/2
        self.master.geometry('%dx%d+%d+%d' %(w,h,x,y))

def main():
    root = Tk()
    rwidth = root.winfo_screenwidth()
    rheight = root.winfo_screenheight()
    root.geometry(("%dx%d")%(rwidth,rheight))
    app = MainGUI(root)
    root.mainloop()

if __name__=='__main__':
    main()

