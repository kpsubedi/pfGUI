import Tkinter as tk
import tkMessageBox
from Tkinter import Tk, Frame, Menu
from Tkinter import *
import pf
import utils.passrule


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
	self.initUI()
	self.buttomPanel()
	self.leftPanel()
	#self.rightPanel()
	self.centerWindow()
    def buttomPanel(self):
        group = tk.LabelFrame(text="Firewall Status")
	group.pack(side=BOTTOM,fill="x",padx=5, pady=5)
	bp = tk.Label(group,text="The firewall is disabled.",fg="red")
	bp.pack(anchor=W)
    def leftPanel(self):
        lb = tk.Listbox(self,width=25)
        lb.insert("1","Network Address Translation")
        lb.insert("2","Create Tables")
        lb.insert("3","Port Forwarding")
	lb.insert("end","Custom Rules")
	lb.selection_set(first=0)
        lb.bind("<Double-Button-1>",self.OnDouble)
        lb.pack(side="left", fill="y",padx=5, pady=5)
        #lb.grid(row=0, column=0, rowspan=1, columnspan=16, sticky=tk.N+tk.S)
	#retValue = self.OnDouble(self)
	#print retValue
    #def rightPanel(self):
	#entry = tk.Entry(self)
	#entry.pack(side='right')
	#labelFrame = tk.LabelFrame()
	#labelFrame.pack(side=RIGHT,fill="both",expand="YES",padx=5, pady=5)
        #test = tk.Label(labelFrame, text="Ths")
	#test.pack(anchor=W)	
    def initUI(self):
        self.title("Firewall Configuration")
        menubar = Menu(self)
        self.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Apply")
        fileMenu.add_command(label="Reload")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit",command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)
	optionsMenu = Menu(menubar)
	optionsMenu.add_command(label="Start Configuration Wizard", state=DISABLED)
	optionsMenu.add_separator()
	optionsMenu.add_command(label="Enable Firewall", command=self.onEnable)
	optionsMenu.add_command(label="Disable Firewall", command=self.onDisable, state=DISABLED)
	menubar.add_cascade(label="Options", menu=optionsMenu)

	helpMenu = Menu(menubar)
	helpMenu.add_command(label="About", command=self.onAbout)
	menubar.add_cascade(label="Help", menu=helpMenu)
    def onAbout(self):
	tkMessageBox.showinfo("Firewall","OpenBSD Firewall Configuration")
    def onEnable(self):
	tkMessageBox.showinfo("Enable","Enable SEction")
    def onDisable(self):
        tkMessageBox.showinfo("Disabe","Disable SEction")
    def onExit(self):
        self.quit() 
    def centerWindow(self):
        w = 490
        h = 450
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('%dx%d+%d+%d' %(w,h,x,y))

    def OnDouble(self, event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
	if selection[0] == "0":
	    tkMessageBox.showinfo("selection:"+selection[0],"Zero:"+selection[0])
	    labelFrame = LabelFrame(self,text="Network Address Translation")
	    labelFrame.pack(side=RIGHT,fill="both",expand="YES",padx=5, pady=5)
            test = tk.Label(labelFrame, text="Ths")
	    test.pack(anchor=W)	
	    #labelFrame0 = LabelFrame(self, text="Zero")
	    #labelFrame0.pack(side=RIGHT)
	    #self.initInterfaceone()
        elif selection[0] == "1":
	    tkMessageBox.showinfo("selection:"+selection[0],"One:"+selection[0])
	    labelFrame1 = LabelFrame(self,text="One Configuration")
	    labelFrame1.pack(side=RIGHT,fill="both",expand="YES",padx=5, pady=5)
            test1 = tk.Label(labelFrame1, text="One config")
	    test1.pack(anchor=W)	
	elif selection[0] == "2":
	    tkMessageBox.showinfo("Selection:"+selection[0],"Two:"+selection[0])
	    labelFrame2 = LabelFrame(self,text="Two Configuration")
	    labelFrame2.pack(side=RIGHT,fill="both",expand="YES",padx=5, pady=5)
            test2 = tk.Label(labelFrame2, text="Two config")
	    test2.pack(anchor=W)	
	elif selection[0] == "3":
	    #drawRightBox(self)
	    tkMessageBox.showinfo("Selection:"+selection[0],"Three:"+selection[0])	
	    labelFrame2 = LabelFrame(self,text="Three Configuration")
	    labelFrame2.pack(side=RIGHT,fill="both",expand="YES",padx=5, pady=5)
            test2 = tk.Label(labelFrame2, text="Three config")
	    test2.pack(anchor=W)	
	    labelFrame3 = LabelFrame(self, text="Three")
	    labelFrame3.pack(side=RIGHT)
        #print "Selection:", selection, ": '%s'" %value
        #tkMessageBox.showinfo("Test","Test")
	return value
    def drawRightBox(self):
        tkMessageBox.showinfo("Hi","How")
    def initInterfaceone(self):
	tkMessageBox.showinfo("90","90")	
	box = Frame(self)
	box.pack()

if __name__=="__main__":
    app = SampleApp()
    app.mainloop()

